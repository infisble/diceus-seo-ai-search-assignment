"""
Legacy-URL equity check: historical URLs (Wayback CDX, once 200) that are NOT in today's sitemap.
For each, follow redirects hop-by-hop and record the chain + final status, so we can see whether
past migrations (e.g. /industry/insurance/* -> /insurance/*, 'vitaminise' product rename) preserved equity.

Scope: all insurance-related legacy paths + all legacy section paths (/solutions/, /services/, /industry/,
/case-studies/, /blog/) + a deterministic sample of root-level legacy posts. ~1 req/s.
Output: data/legacy_redirects.csv
"""
import json, re, time, random
from pathlib import Path
from urllib.parse import urlparse, urljoin
import requests, pandas as pd

ROOT = Path(__file__).resolve().parents[1]
D = ROOT / "data"
UA = "Mozilla/5.0 (compatible; SEO-assignment-research-bot/1.0; low-rate)"


def legacy_paths():
    rows = json.load(open(D / "wayback_urls.json"))[1:]
    sm = {urlparse(x["url"]).path for x in json.load(open(D / "sitemap_urls.json", encoding="utf-8"))}
    paths = {}
    for o, ts, st, mt in rows:
        p = urlparse(o if "://" in o else "http://" + o)
        if p.query or re.search(r"\.(jpg|png|css|js|xml|pdf|txt|php)$", p.path) or "/wp-" in p.path or "/feed" in p.path \
                or "/cdn-cgi/" in p.path or "/amp" in p.path or "/page/" in p.path or "/user/" in p.path or "/search/" in p.path:
            continue
        path = (p.path if p.path.endswith("/") else p.path + "/").lower()
        if path not in sm:
            paths.setdefault(path, ts)
    return paths


def main():
    paths = legacy_paths()
    ins = [p for p in paths if re.search(r"insur|captive|claim|underwrit|polic|reinsur|broker|vitaminise", p)]
    sect = [p for p in paths if p not in ins and re.match(r"/(solutions|services|industry|expertise|company|blog|media)/", p)]
    cases = [p for p in paths if p not in ins and p.startswith("/case-studies/")]
    root = [p for p in paths if p not in ins and p.count("/") == 2 and p not in sect]
    random.seed(42)
    sample = ins + sect + random.sample(cases, min(30, len(cases))) + random.sample(root, min(90, len(root)))
    s = requests.Session(); s.headers["User-Agent"] = UA
    out = []
    for i, path in enumerate(sample):
        url = "https://diceus.com" + path
        chain, cur, final = [], url, None
        for _ in range(6):
            try:
                r = s.get(cur, allow_redirects=False, timeout=30)
            except Exception as e:
                final = f"ERR {e.__class__.__name__}"; break
            chain.append(f"{r.status_code}")
            time.sleep(1.0)
            if 300 <= r.status_code < 400 and r.headers.get("Location"):
                cur = urljoin(cur, r.headers["Location"])
            else:
                final = r.status_code; break
        out.append({"legacy_path": path, "wayback_first_seen": paths[path][:8],
                    "group": "insurance" if path in ins else "section" if path in sect else "case" if path in cases else "root_post",
                    "chain": ">".join(chain), "hops": len(chain) - 1, "final_status": final,
                    "final_url": cur if cur != url else None})
        if i % 20 == 0:
            print(i, path, out[-1]["chain"], flush=True)
    pd.DataFrame(out).to_csv(D / "legacy_redirects.csv", index=False)
    df = pd.DataFrame(out)
    print(df.groupby(["group", "final_status"]).size())


if __name__ == "__main__":
    main()
