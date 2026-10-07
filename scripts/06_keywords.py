"""
Keyword universe -> clusters -> scoring.

Input : data/autocomplete.json (Google Autocomplete US), data/serp_observations.json (SERP sample),
        data/urls_analyzed.csv (to map existing DICEUS pages to clusters)
Output: data/keywords.csv (one row per discovered query, with cluster + intent)
        data/clusters.csv (one row per cluster, with scoring)

Important evidence rules (see 06_ methodology):
- Autocomplete proves a query is typed often enough to be suggested; it is NOT a volume metric.
  We expose 'suggest_evidence' (how many seed/modifier expansions surfaced the cluster) as a RELATIVE
  demand proxy and keep 'search_volume' = DATA UNAVAILABLE.
- Intent is rule-based on modifiers, then spot-checked against SERP page types from the SERP sample.
"""
import json, re
from collections import defaultdict
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
D = ROOT / "data"

# Cluster definitions: (cluster_id, territory, business_layer, regex on query). Order matters: first match wins.
CLUSTERS = [
    ("captive_mgmt_software", "Alternative Risk", "Product", r"captive.*(software|system|platform|management system|technology|portal)|captive management software"),
    ("captive_manager_ops", "Alternative Risk", "Solution/Content", r"captive manag|captive insurance (companies|management)|captive accounting|cell captive|captive feasibility"),
    ("captive_concepts", "Alternative Risk", "Content", r"captive"),
    ("rrg_software", "Alternative Risk", "Product", r"risk retention"),
    ("self_insurance_admin", "Alternative Risk", "Product/Solution", r"self[- ]?insur|tpa software|third party admin"),
    ("mga_software", "Alternative Risk / Distribution", "Product/Solution", r"\bmga\b|managing general|program admin"),
    ("loss_runs", "Alternative Risk", "Feature/Content", r"loss run"),
    ("alt_risk_generic", "Alternative Risk", "Product/Hub", r"alternative risk|fronting"),
    ("pas_vendors", "Policy Administration", "Product", r"(policy admin|policy management|\bpas\b).*(vendor|compan|best|list|top|provider|vs|comparison|gartner)"),
    ("pas_software", "Policy Administration", "Product", r"policy admin|policy management (software|system)|insurance policy (software|system|management)|\bpas\b"),
    ("claims_self_insured", "Claims", "Product/Solution", r"claims.*(self|tpa|administrat)"),
    ("health_claims", "Claims", "Product/Solution", r"health.*claim|medical claim|claim.*health"),
    ("claims_software", "Claims", "Product", r"claim"),
    ("uw_workbench", "Underwriting", "Product", r"underwriting workbench|workbench"),
    ("uw_software", "Underwriting", "Product", r"underwrit"),
    ("reinsurance_accounting", "Reinsurance", "Product", r"reinsurance.*(accounting|ledger|financ)"),
    ("reinsurance_software", "Reinsurance", "Product", r"reinsurance"),
    ("group_benefits_admin", "Group Insurance", "Product", r"group|benefit"),
    ("broker_portal", "Distribution", "Product", r"broker|agent portal|agency"),
    ("customer_portal", "Distribution / CX", "Product", r"customer portal|policyholder portal|self service"),
    ("insurance_gl", "Finance / GL", "Product", r"general ledger|statutory|accounting"),
    ("insurance_dwh", "Data & Analytics", "Product", r"data warehouse|data model|data platform|datalake|data lake"),
    ("insurance_analytics", "Data & Analytics", "Solution/Content", r"analytic|data"),
    ("insurance_sw_dev_services", "Services", "Service", r"development|developer|app|build|custom|outsourc|testing|qa\b"),
    ("legacy_modernization", "Services", "Service/Content", r"moderni|legacy|migration|transformation"),
    ("core_systems_generic", "Core / Platform", "Hub/Content", r"core|platform|insurtech|p&c|insurance software"),
]

INTENT_RULES = [
    ("BOFU-vendor", r"\b(vendor|vendors|companies|providers|best|top|vs|alternatives?|pricing|cost|price|demo|comparison|gartner|reviews?)\b"),
    ("MOFU-solution", r"\b(for|features|requirements|benefits|platform|system|software|solution|module)\b"),
    ("TOFU-informational", r"\b(what|how|why|definition|meaning|example|examples|guide|vs\.)\b"),
    ("Service", r"\b(development|developer|outsourc|consulting|services|build)\b"),
]


def intent(q):
    for name, rx in INTENT_RULES:
        if re.search(rx, q):
            return name
    return "Navigational/ambiguous" if len(q.split()) <= 2 else "MOFU-solution"


def cluster(q):
    for cid, terr, layer, rx in CLUSTERS:
        if re.search(rx, q):
            return cid, terr, layer
    return "off_topic", "Off-topic", "-"


def main():
    ac = json.loads((D / "autocomplete.json").read_text(encoding="utf-8"))
    hits = defaultdict(lambda: {"seeds": set(), "count": 0})
    for key, mods in ac.items():
        terr_seed = key.split("|")[0]
        for q, sugg in mods.items():
            if not isinstance(sugg, list):
                continue
            for s in sugg:
                s = s.lower().strip()
                hits[s]["seeds"].add(terr_seed); hits[s]["count"] += 1
    rows = []
    for q, h in hits.items():
        cid, terr, layer = cluster(q)
        # relevance gate: drop consumer-only / job / unrelated suggestions
        consumer = bool(re.search(r"\b(job|jobs|salary|salaries|course|certification|login|near me|reddit|resume|careers?|interview questions|exam|quizlet|pdf|ppt|indeed)\b", q))
        rows.append({"query": q, "cluster": cid, "territory": terr, "business_layer": layer, "intent": intent(q),
                     "suggest_hits": h["count"], "seed_territories": ";".join(sorted(h["seeds"])),
                     "noise_flag": "noise (jobs/edu/consumer)" if consumer else "",
                     "search_volume": "DATA UNAVAILABLE"})
    kw = pd.DataFrame(rows).sort_values(["territory", "cluster", "suggest_hits"], ascending=[True, True, False])
    kw.to_csv(D / "keywords.csv", index=False, encoding="utf-8")
    clean = kw[(kw.noise_flag == "") & (kw.cluster != "off_topic")]
    cl = clean.groupby(["cluster", "territory", "business_layer"]).agg(
        queries=("query", "count"), suggest_evidence=("suggest_hits", "sum"),
        bofu_share=("intent", lambda s: round((s == "BOFU-vendor").mean(), 2)),
        sample_queries=("query", lambda s: " | ".join(list(s)[:6]))).reset_index()
    cl.to_csv(D / "clusters.csv", index=False, encoding="utf-8")
    print(f"queries={len(kw)} clean={len(clean)} clusters={len(cl)}")
    print(cl.sort_values("suggest_evidence", ascending=False).to_string()[:6000])


if __name__ == "__main__":
    main()
