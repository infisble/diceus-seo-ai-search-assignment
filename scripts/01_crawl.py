"""
Responsible crawler for diceus.com (assignment research).

- Seeds: every URL in the Yoast sitemap index + homepage; then BFS over internal links.
- Politeness: single thread, >=1.0 s between requests, robots.txt honoured (incl. wildcards),
  identifiable User-Agent, no query-string crawling (except recorded as found), hard cap.
- Redirects are NOT auto-followed: each hop is recorded so chains/loops are visible.
- Output: data/crawl.jsonl (one JSON object per fetched URL) + data/pages_text/*.txt (main text).

Usage:  python scripts/01_crawl.py [--max 2500] [--delay 1.0]
"""
import argparse, hashlib, json, re, time, sys
from collections import deque
from pathlib import Path
from urllib.parse import urljoin, urlparse, urldefrag

import requests
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
TEXT_DIR = DATA / "pages_text"
TEXT_DIR.mkdir(parents=True, exist_ok=True)
OUT = DATA / "crawl.jsonl"

HOST = "diceus.com"
BASE = "https://diceus.com/"
UA = "Mozilla/5.0 (compatible; SEO-assignment-research-bot/1.0; low-rate, 1 req/s, public pages only)"
SKIP_EXT = re.compile(r"\.(jpg|jpeg|png|gif|svg|webp|avif|pdf|zip|mp4|mp3|css|js|woff2?|ttf|ico|xml|docx?|xlsx?|pptx?)$", re.I)


# ---------- robots.txt with wildcard support (urllib.robotparser ignores '*' / '$') ----------
def load_robots(session):
    txt = session.get(BASE + "robots.txt", timeout=20).text
    rules, active = [], False
    for line in txt.splitlines():
        line = line.split("#")[0].strip()
        if not line or ":" not in line:
            continue
        k, v = [x.strip() for x in line.split(":", 1)]
        k = k.lower()
        if k == "user-agent":
            active = v == "*"
        elif active and k in ("allow", "disallow") and v:
            pat = re.escape(v).replace(r"\*", ".*")
            if pat.endswith(r"\$"):
                pat = pat[:-2] + "$"
            rules.append((k == "allow", len(v), re.compile("^" + pat)))
    return txt, rules


def robots_allowed(rules, url):
    p = urlparse(url)
    path = p.path + (("?" + p.query) if p.query else "")
    best = None
    for allow, length, rx in rules:
        if rx.match(path) and (best is None or length > best[1] or (length == best[1] and allow)):
            best = (allow, length)
    return True if best is None else best[0]


def norm(url):
    url, _ = urldefrag(url)
    p = urlparse(url)
    if p.scheme not in ("http", "https"):
        return None
    host = p.netloc.lower()
    if host not in (HOST, "www." + HOST):
        return None
    return url


def sitemap_urls(session):
    urls = []
    idx = session.get(BASE + "sitemap_index.xml", timeout=20).text
    for sm in re.findall(r"<loc>([^<]+)</loc>", idx):
        time.sleep(1)
        body = session.get(sm, timeout=30).text
        for loc, rest in re.findall(r"<loc>([^<]+)</loc>(.*?)</url>", body, re.S):
            lm = re.search(r"<lastmod>([^<]+)</lastmod>", rest)
            urls.append({"url": loc.strip(), "sitemap": sm.rsplit("/", 1)[-1], "lastmod": lm.group(1) if lm else None})
    return urls


def visible_text(soup):
    for t in soup(["script", "style", "noscript", "svg", "template", "iframe"]):
        t.decompose()
    main = soup.find("main") or soup.find("article") or soup.body or soup
    clone = BeautifulSoup(str(main), "lxml")
    for t in clone.find_all(["header", "footer", "nav", "form"]):
        t.decompose()
    for t in clone.select('[class*="cookie"], [id*="cookie"], [class*="footer"], [class*="header__"], [class*="menu"]'):
        t.decompose()
    txt = clone.get_text(" ", strip=True)
    return re.sub(r"\s+", " ", txt)


def schema_types(soup):
    types, raw_ok = [], True
    for s in soup.find_all("script", type="application/ld+json"):
        try:
            data = json.loads(s.string or "")
        except Exception:
            raw_ok = False
            continue
        stack = [data]
        while stack:
            d = stack.pop()
            if isinstance(d, list):
                stack.extend(d)
            elif isinstance(d, dict):
                t = d.get("@type")
                if t:
                    types.extend(t if isinstance(t, list) else [t])
                stack.extend(v for v in d.values() if isinstance(v, (dict, list)))
    return sorted(set(map(str, types))), raw_ok


def parse(url, resp):
    soup = BeautifulSoup(resp.text, "lxml")
    g = lambda sel, attr="content": (soup.select_one(sel) or {}).get(attr) if soup.select_one(sel) else None
    title = soup.title.get_text(strip=True) if soup.title else None
    h1 = [h.get_text(" ", strip=True) for h in soup.find_all("h1")]
    h2 = [h.get_text(" ", strip=True) for h in soup.find_all("h2")]
    stypes, schema_ok = schema_types(soup)
    links_int, links_ext, nav_links = [], 0, set()
    for nav in soup.find_all(["header", "nav", "footer"]):
        for a in nav.find_all("a", href=True):
            u = norm(urljoin(url, a["href"]))
            if u:
                nav_links.add(u)
    for a in soup.find_all("a", href=True):
        href = a["href"].strip()
        if href.startswith(("mailto:", "tel:", "javascript:", "#")):
            continue
        u = norm(urljoin(url, href))
        if u:
            links_int.append({"to": u, "anchor": a.get_text(" ", strip=True)[:120],
                              "nofollow": "nofollow" in (a.get("rel") or []), "nav": u in nav_links})
        else:
            links_ext += 1
    imgs = soup.find_all("img")
    text = visible_text(soup)
    return {
        "title": title,
        "meta_description": g('meta[name="description"]'),
        # ALL robots/googlebot tags: a page can carry several (e.g. Yoast + a hard-coded one);
        # search engines apply the most restrictive combination. (v1 read only the first tag - bug found
        # during AI-agent cross-check, see methodology section I.)
        "meta_robots": " | ".join(m.get("content", "") for m in soup.select('meta[name="robots" i], meta[name="googlebot" i]')) or None,
        "canonical": g('link[rel="canonical"]', "href"),
        "canonical_count": len(soup.select('link[rel="canonical"]')),
        "lang": (soup.html or {}).get("lang") if soup.html else None,
        "hreflang": [(l.get("hreflang"), l.get("href")) for l in soup.select('link[rel="alternate"][hreflang]')],
        "og_type": g('meta[property="og:type"]'),
        "published": g('meta[property="article:published_time"]'),
        "modified": g('meta[property="article:modified_time"]'),
        "h1": h1, "h2": h2[:40], "h2_count": len(h2), "h3_count": len(soup.find_all("h3")),
        "schema_types": stypes, "schema_parse_ok": schema_ok,
        "word_count": len(text.split()),
        "img_count": len(imgs), "img_no_alt": sum(1 for i in imgs if not (i.get("alt") or "").strip()),
        "links_internal": links_int, "links_external_count": links_ext,
        "breadcrumb": " > ".join(x.get_text(strip=True) for x in soup.select('[class*="breadcrumb"] a, [class*="breadcrumb"] span')[:8]) or None,
        "_text": text,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--max", type=int, default=2500)
    ap.add_argument("--delay", type=float, default=1.0)
    args = ap.parse_args()

    s = requests.Session()
    s.headers.update({"User-Agent": UA, "Accept-Language": "en-US,en;q=0.9"})
    robots_txt, rules = load_robots(s)
    (DATA / "robots.txt").write_text(robots_txt, encoding="utf-8")

    sm = sitemap_urls(s)
    json.dump(sm, open(DATA / "sitemap_urls.json", "w", encoding="utf-8"), indent=1)
    print(f"sitemap URLs: {len(sm)}", flush=True)

    done = set()
    if OUT.exists():  # resume support
        for line in OUT.open(encoding="utf-8"):
            done.add(json.loads(line)["url"])
    queue = deque([BASE] + [x["url"] for x in sm])
    seen = set(queue) | done
    found_from = {}  # url -> first source page (discovery provenance)
    blocked = []
    n = len(done)
    last = 0.0
    with OUT.open("a", encoding="utf-8") as fh:
        while queue and n < args.max:
            url = queue.popleft()
            if url in done:
                continue
            p = urlparse(url)
            if SKIP_EXT.search(p.path):
                continue
            if not robots_allowed(rules, url):
                blocked.append(url)
                continue
            wait = args.delay - (time.time() - last)
            if wait > 0:
                time.sleep(wait)
            last = time.time()
            rec = {"url": url, "found_from": found_from.get(url, "sitemap/seed"), "ts": time.strftime("%Y-%m-%dT%H:%M:%S")}
            try:
                t0 = time.time()
                r = s.get(url, allow_redirects=False, timeout=30)
                rec.update(status=r.status_code, ttfb_ms=int((time.time() - t0) * 1000),
                           content_type=r.headers.get("Content-Type", ""), bytes=len(r.content),
                           x_robots_tag=r.headers.get("X-Robots-Tag"), location=r.headers.get("Location"),
                           cache=r.headers.get("cf-cache-status"))
            except Exception as e:
                rec.update(status=None, error=str(e)[:200])
                fh.write(json.dumps(rec, ensure_ascii=False) + "\n"); done.add(url); n += 1
                continue

            if 300 <= r.status_code < 400 and rec["location"]:
                tgt = norm(urljoin(url, rec["location"]))
                if tgt and tgt not in seen:
                    seen.add(tgt); queue.append(tgt); found_from[tgt] = "redirect:" + url
            elif r.status_code == 200 and "text/html" in rec["content_type"]:
                info = parse(url, r)
                text = info.pop("_text")
                h = hashlib.md5(url.encode()).hexdigest()[:16]
                (TEXT_DIR / f"{h}.txt").write_text(text, encoding="utf-8")
                rec["text_file"] = f"{h}.txt"
                rec["content_hash"] = hashlib.md5(text.encode()).hexdigest()
                rec.update(info)
                for l in info["links_internal"]:
                    u = l["to"]
                    pu = urlparse(u)
                    if pu.query or SKIP_EXT.search(pu.path):
                        continue
                    if u not in seen:
                        seen.add(u); queue.append(u); found_from[u] = url
            fh.write(json.dumps(rec, ensure_ascii=False) + "\n"); fh.flush()
            done.add(url); n += 1
            if n % 25 == 0:
                print(f"[{n}] queue={len(queue)} last={url} {rec.get('status')}", flush=True)
    json.dump(blocked, open(DATA / "robots_blocked.json", "w"), indent=1)
    print(f"DONE fetched={n} robots_blocked={len(blocked)} queue_left={len(queue)}", flush=True)


if __name__ == "__main__":
    main()
