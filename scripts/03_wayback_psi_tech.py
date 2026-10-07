"""
Three small public-data collectors (each a handful of requests):

1. Wayback CDX  -> historical URL inventory of diceus.com (URLs that once returned 200).
   Used to find legacy URLs that now 404 / redirect = potential lost equity. One API call.
2. PageSpeed Insights v5 (no key, low quota) -> Lighthouse lab metrics + CrUX FIELD data
   (loadingExperience / originLoadingExperience) for one representative URL per template.
3. Technical probes -> host/protocol canonicalisation, soft-404 behaviour, trailing slash,
   and whether AI crawler user-agents get the same response (no bypass attempts; 1 request each).

Outputs: data/wayback_urls.json, data/psi.json, data/tech_probes.json
"""
import json, time, sys
from pathlib import Path
import requests

ROOT = Path(__file__).resolve().parents[1]
D = ROOT / "data"
UA = "Mozilla/5.0 (compatible; SEO-assignment-research-bot/1.0; low-rate)"

TEMPLATES = {
    "homepage": "https://diceus.com/",
    "insurance_hub": "https://diceus.com/insurance/",
    "product_pas": "https://diceus.com/insurance/solutions/policy-administration-system/",
    "product_captive": "https://diceus.com/insurance/solutions/captive-insurance/captive-management-platform/",
    "insurance_service": "https://diceus.com/insurance/claims-management-development/",
    "generic_service": "https://diceus.com/services/custom-software-development/",
    "industry": "https://diceus.com/industry/banking/",
    "expertise": "https://diceus.com/expertise/ai-software-development/",
    "blog_post": "https://diceus.com/modernizing-policy-administration-system/",
    "case": "https://diceus.com/case-studies/",
}


def wayback():
    out = D / "wayback_urls.json"
    if out.exists():
        return
    r = requests.get("http://web.archive.org/cdx/search/cdx", params={
        "url": "diceus.com/*", "output": "json", "fl": "original,timestamp,statuscode,mimetype",
        "filter": ["statuscode:200", "mimetype:text/html"], "collapse": "urlkey", "limit": 20000,
    }, timeout=180, headers={"User-Agent": UA})
    rows = r.json()
    out.write_text(json.dumps(rows, indent=0))
    print("wayback rows", len(rows))


def psi():
    out = D / "psi.json"
    res = json.loads(out.read_text()) if out.exists() else {}
    for name, url in TEMPLATES.items():
        for strategy in ("mobile", "desktop"):
            k = f"{name}|{strategy}"
            if k in res and "error" not in res[k]:
                continue
            try:
                r = requests.get("https://www.googleapis.com/pagespeedonline/v5/runPagespeed",
                                 params={"url": url, "strategy": strategy, "category": "performance"}, timeout=120)
                j = r.json()
                if "error" in j:
                    res[k] = {"error": j["error"].get("message", "")[:200]}
                else:
                    lh = j["lighthouseResult"]; a = lh["audits"]
                    fe = j.get("loadingExperience", {})
                    oe = j.get("originLoadingExperience", {})
                    res[k] = {
                        "url": url, "perf_score": lh["categories"]["performance"]["score"],
                        "lcp_lab_ms": a["largest-contentful-paint"]["numericValue"],
                        "cls_lab": a["cumulative-layout-shift"]["numericValue"],
                        "tbt_lab_ms": a["total-blocking-time"]["numericValue"],
                        "fcp_lab_ms": a["first-contentful-paint"]["numericValue"],
                        "page_weight_kb": a["total-byte-weight"]["numericValue"] / 1024,
                        "dom_size": a.get("dom-size", {}).get("numericValue"),
                        "field_url_category": fe.get("overall_category"),
                        "field_url_metrics": {m: v.get("percentile") for m, v in fe.get("metrics", {}).items()},
                        "field_origin_category": oe.get("overall_category"),
                        "field_origin_metrics": {m: v.get("percentile") for m, v in oe.get("metrics", {}).items()},
                    }
            except Exception as e:
                res[k] = {"error": str(e)[:200]}
            print(k, res[k].get("perf_score", res[k].get("error")), flush=True)
            out.write_text(json.dumps(res, indent=1))
            time.sleep(3)


def probes():
    out = D / "tech_probes.json"
    res = []
    def probe(label, url, ua=UA):
        try:
            r = requests.get(url, allow_redirects=False, timeout=30, headers={"User-Agent": ua})
            res.append({"label": label, "url": url, "ua": ua[:40], "status": r.status_code,
                        "location": r.headers.get("Location"), "bytes": len(r.content),
                        "x_robots": r.headers.get("X-Robots-Tag"), "server": r.headers.get("Server")})
        except Exception as e:
            res.append({"label": label, "url": url, "error": str(e)[:150]})
        time.sleep(1.2)
    probe("http->https", "http://diceus.com/")
    probe("www->non-www", "https://www.diceus.com/")
    probe("http+www", "http://www.diceus.com/")
    probe("no trailing slash", "https://diceus.com/insurance")
    probe("uppercase path", "https://diceus.com/Insurance/")
    probe("random 404", "https://diceus.com/this-page-should-not-exist-xyz123/")
    probe("index.php", "https://diceus.com/index.php")
    probe("llms.txt", "https://diceus.com/llms.txt")
    probe("query param dup", "https://diceus.com/insurance/?ref=test")
    probe("ai-ua GPTBot", "https://diceus.com/insurance/solutions/", "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; GPTBot/1.2; +https://openai.com/gptbot)")
    probe("ai-ua ClaudeBot", "https://diceus.com/insurance/solutions/", "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; ClaudeBot/1.0; +claudebot@anthropic.com)")
    probe("ai-ua PerplexityBot", "https://diceus.com/insurance/solutions/", "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; PerplexityBot/1.0; +https://perplexity.ai/perplexitybot)")
    probe("baseline UA", "https://diceus.com/insurance/solutions/")
    out.write_text(json.dumps(res, indent=1))
    for r in res:
        print(r)


if __name__ == "__main__":
    which = sys.argv[1:] or ["wayback", "probes", "psi"]
    if "wayback" in which: wayback()
    if "probes" in which: probes()
    if "psi" in which: psi()
