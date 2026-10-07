"""
Head re-check pass (fix for crawler v1 bug: only the FIRST meta robots tag was read).
Streams each 200-HTML URL, reads only until </head>, and records ALL robots/googlebot metas,
ALL canonicals and title count. 1 request/s. Output: data/head_recheck.json {url: {...}}
"""
import json, re, time
from pathlib import Path
import requests

ROOT = Path(__file__).resolve().parents[1]
D = ROOT / "data"
UA = "Mozilla/5.0 (compatible; SEO-assignment-research-bot/1.0; low-rate)"
OUT = D / "head_recheck.json"

def main():
    urls = [json.loads(l) for l in (D / "crawl.jsonl").open(encoding="utf-8")]
    urls = [r["url"] for r in urls if r.get("status") == 200]
    res = json.loads(OUT.read_text()) if OUT.exists() else {}
    s = requests.Session(); s.headers["User-Agent"] = UA
    for i, u in enumerate(urls):
        if u in res:
            continue
        t0 = time.time()
        try:
            with s.get(u, stream=True, timeout=30) as r:
                buf = b""
                for chunk in r.iter_content(16384):
                    buf += chunk
                    if b"</head>" in buf or len(buf) > 400000:
                        break
            head = buf.decode("utf-8", "ignore").split("</head>")[0]
            res[u] = {
                "robots": re.findall(r'<meta[^>]+name=["\'](?:robots|googlebot)["\'][^>]*content=["\']([^"\']*)', head, re.I),
                "canonicals": re.findall(r'<link[^>]+rel=["\']canonical["\'][^>]*href=["\']([^"\']*)', head, re.I),
                "titles": len(re.findall(r"<title", head, re.I)),
            }
        except Exception as e:
            res[u] = {"error": str(e)[:120]}
        if i % 50 == 0:
            OUT.write_text(json.dumps(res, indent=0)); print(i, u, res[u], flush=True)
        time.sleep(max(0, 1.0 - (time.time() - t0)))
    OUT.write_text(json.dumps(res, indent=0))
    bad = {u: v for u, v in res.items() if any("noindex" in x.lower() for x in v.get("robots", []))}
    print("noindex pages:", len(bad)); [print(u, v["robots"]) for u, v in bad.items()]

if __name__ == "__main__":
    main()
