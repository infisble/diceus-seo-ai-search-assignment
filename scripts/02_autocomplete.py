"""
Keyword universe discovery without paid tools: Google Autocomplete (US, en).

Seeds come from the business territories in the brief (products > solutions > alt-risk > services).
Each seed is expanded with question/commercial modifiers. Autocomplete returns queries that real
users type often enough to be suggested -> evidence of EXISTENCE of demand, NOT volume.
Volume is therefore marked DATA UNAVAILABLE downstream; we only use a relative "suggest depth" signal.

Rate: 1 request / 1.2 s. Output: data/autocomplete.json  {seed: {modifier: [suggestions]}}
"""
import json, time
from pathlib import Path
import requests

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data" / "autocomplete.json"

SEEDS = {
    "policy_admin": ["policy administration system", "policy administration software", "insurance policy management software", "pas insurance"],
    "claims": ["claims management software", "insurance claims software", "claims administration software", "health claims management"],
    "underwriting": ["underwriting workbench", "underwriting software", "insurance underwriting platform"],
    "reinsurance": ["reinsurance software", "reinsurance management system", "reinsurance accounting"],
    "group": ["group insurance software", "group benefits administration software", "group life insurance software"],
    "distribution": ["broker portal", "insurance agent portal", "insurance customer portal", "mga software"],
    "finance": ["insurance general ledger", "insurance accounting software", "statutory accounting software"],
    "data": ["insurance data warehouse", "insurance data analytics", "insurance data platform"],
    "alt_risk": ["captive insurance software", "captive management software", "captive insurance management",
                  "risk retention group software", "alternative risk software", "self insurance software",
                  "captive manager", "loss run software", "fronting carrier software", "program administrator software"],
    "core": ["insurance core system", "insurance software", "insurtech platform", "p&c insurance software"],
    "services": ["insurance software development", "insurance app development", "legacy insurance system modernization",
                 "insurance software testing"],
}
MODIFIERS = ["", " for", " vs", " best", " companies", " vendors", " what is", " features", " cost", " open source"]


def suggest(session, q):
    r = session.get("https://suggestqueries.google.com/complete/search",
                    params={"client": "firefox", "hl": "en", "gl": "us", "q": q}, timeout=15)
    r.raise_for_status()
    return r.json()[1]


def main():
    s = requests.Session()
    s.headers["User-Agent"] = "Mozilla/5.0 (research script, low rate)"
    out = json.loads(OUT.read_text()) if OUT.exists() else {}
    for terr, seeds in SEEDS.items():
        for seed in seeds:
            key = f"{terr}|{seed}"
            if key in out:
                continue
            out[key] = {}
            for m in MODIFIERS:
                q = (m.strip() + " " + seed) if m.strip() in ("best", "what is") else seed + m
                try:
                    out[key][q] = suggest(s, q)
                except Exception as e:
                    out[key][q] = {"error": str(e)[:100]}
                time.sleep(1.2)
            OUT.write_text(json.dumps(out, indent=1, ensure_ascii=False))
            print(key, sum(len(v) for v in out[key].values() if isinstance(v, list)), flush=True)


if __name__ == "__main__":
    main()
