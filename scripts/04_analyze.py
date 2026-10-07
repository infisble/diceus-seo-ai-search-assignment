"""
Scalable current-state analysis over the full crawl dataset (no page-by-page manual review).

Inputs : data/crawl.jsonl, data/sitemap_urls.json, data/pages_text/*.txt, data/wayback_urls.json
Outputs: data/urls_analyzed.csv          one row per crawled URL, ~45 columns
         data/near_duplicates.csv        TF-IDF cosine pairs >= 0.80
         data/cannibalization.csv        URLs competing for the same insurance territory
         data/link_edges.csv             contextual internal link edges (nav/footer excluded)
         data/summary.json               aggregate counts used in the reports
Method notes are in 06_Methodology_AI_Workflow_and_Data_Gaps.md.
"""
import json, re
from collections import Counter, defaultdict
from pathlib import Path
from urllib.parse import urlparse

import networkx as nx
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

ROOT = Path(__file__).resolve().parents[1]
D = ROOT / "data"
HOME = "https://diceus.com/"

# ---------------------------------------------------------------- classification
def page_type(url, sitemap):
    p = urlparse(url).path
    if p in ("/", ""): return "homepage"
    if re.search(r"/page/\d+/?$", p): return "pagination"
    if re.match(r"/case-studies/(service|industry|expertise|country)/", p): return "case_filter_archive"
    if p.startswith("/da/"): return "localized_da"
    if p == "/insurance/": return "insurance_hub"
    if p == "/insurance/solutions/": return "insurance_products_hub"
    if p.startswith("/insurance/solutions/"): return "insurance_product"
    if p in ("/insurance/contact/", "/insurance/free-strategy-session/"): return "conversion"
    if p.startswith("/insurance/"): return "insurance_service"
    if p == "/services/": return "services_hub"
    if p.startswith("/services/"): return "generic_service"
    if p == "/industry/": return "industry_hub"
    if re.fullmatch(r"/industry/[^/]+/", p): return "industry_vertical_hub"
    if p.startswith("/industry/"): return "industry_service"
    if p == "/expertise/": return "expertise_hub"
    if p.startswith("/expertise/"): return "expertise_service"
    if p == "/case-studies/": return "case_hub"
    if p.startswith("/case-studies/"): return "case_study"
    if p == "/media/": return "media_hub"
    if p.startswith("/media/"): return "media_news"
    if p.startswith("/author/"): return "author"
    if p.startswith("/blog/") or p == "/blog/": return "blog_archive"
    if re.search(r"/page/\d+/?$", p): return "pagination"
    if p.strip("/") in ("privacy-policy", "cookie-policy", "terms-of-use", "terms-and-conditions"): return "legal"
    if p.strip("/") in ("contact", "free-strategy-session", "discovery-phase"): return "conversion"
    if p.strip("/") in ("about", "careers", "partners", "achievements", "our-locations", "testimonials"): return "company"
    if sitemap == "post-sitemap.xml": return "blog_post"
    if sitemap == "page-sitemap.xml": return "page_other"
    if p.startswith("/category/") or p.startswith("/tag/"): return "taxonomy"
    return "unclassified"


BUSINESS_LAYER = {
    "homepage": "Brand/Entry", "insurance_hub": "L1 Products (hub)", "insurance_products_hub": "L1 Products (hub)",
    "insurance_product": "L1 Products", "insurance_service": "L2/L3 Insurance solutions & services",
    "generic_service": "L3 Generic services", "services_hub": "L3 Generic services",
    "industry_hub": "Non-insurance verticals", "industry_vertical_hub": "Non-insurance verticals",
    "industry_service": "Non-insurance verticals", "expertise_hub": "L3 Generic services",
    "expertise_service": "L3 Generic services", "blog_post": "L4 Content", "media_news": "Company news",
    "media_hub": "Company news", "case_study": "Proof", "case_hub": "Proof", "case_filter_archive": "Archive/thin",
    "author": "Archive/thin", "blog_archive": "Archive/thin", "pagination": "Archive/thin", "taxonomy": "Archive/thin",
    "company": "Corporate", "legal": "Utility", "conversion": "Conversion", "localized_da": "Localized (DA)",
    "page_other": "Other page", "unclassified": "Unclassified",
}

# Insurance territories (from the brief) -> regex on URL+title+H1. Used for topic tagging + cannibalization.
TERRITORIES = {
    "policy_administration": r"policy[ -]?(administration|admin|management)|\bpas\b",
    "claims": r"claims?\b",
    "underwriting": r"underwrit",
    "reinsurance": r"reinsurance",
    "group_insurance": r"group[ -](insurance|benefit|life)|life[ -]and[ -]pensions",
    "broker_distribution": r"broker|agency[ -]management|agent portal|distribution|digital[ -]channels",
    "customer_portal_cx": r"customer[ -]portal|customer[ -]experience|self[- ]service|super[- ]app|\bportal\b",
    "general_ledger_finance": r"general[ -]ledger|insurance accounting|financial management",
    "data_analytics_dwh": r"data[ -]warehouse|analytics|\bdata\b",
    "alternative_risk": r"captive|risk[ -]retention|alternative[ -]risk|self[- ]insur|\bmga\b|\brrg\b",
    "fraud": r"fraud",
    "insurance_generic": r"insur|insurtech",
}
INS_TERMS = re.compile(r"\b(insur\w*|policyholder\w*|underwrit\w*|claims?|reinsur\w*|captive\w*|premium\w*|broker\w*|actuar\w*|mga|carrier\w*|risk retention)\b", re.I)


def territories(text):
    t = text.lower()
    return [k for k, rx in TERRITORIES.items() if re.search(rx, t)]


def main():
    rows = [json.loads(l) for l in (D / "crawl.jsonl").open(encoding="utf-8")]
    rows = list({r["url"]: r for r in rows if r["url"] != "https://diceus.com"}.values())  # no-slash homepage = same resource
    # merge head re-check (all robots metas / canonicals) - fixes crawler v1 first-tag-only bug
    hr_path = D / "head_recheck.json"
    if hr_path.exists():
        hr = json.loads(hr_path.read_text())
        for r in rows:
            h = hr.get(r["url"])
            if h and "robots" in h:
                r["meta_robots"] = " | ".join(h["robots"]) or None
                r["canonical_count"] = len(h["canonicals"])
    sm = json.load(open(D / "sitemap_urls.json", encoding="utf-8"))
    sm_map = {x["url"]: x for x in sm}

    # ------------------------------------------------ link graph (contextual vs nav/footer)
    G_all, G_ctx = nx.DiGraph(), nx.DiGraph()
    status = {r["url"]: r.get("status") for r in rows}
    redirect_to = {r["url"]: r.get("location") for r in rows if r.get("status") and 300 <= r["status"] < 400}
    edges, anchors = [], defaultdict(Counter)
    # Contextual-link heuristic (crawler v1 flagged 'nav' by URL, not by element, so any body link to a
    # mega-menu URL looked like nav). Fix: template links repeat with a stable count on every page.
    # baseline(X) = modal per-page occurrence count of target X across pages that link to X, when X is
    # linked from >=30% of HTML pages (i.e. it is in the sitewide template). Occurrences above baseline
    # are counted as contextual (in-body) links. Validated manually on sample pages (methodology §I).
    per_page = {r["url"]: Counter(l["to"] for l in (r.get("links_internal") or [])) for r in rows}
    n_html = sum(1 for r in rows if r.get("status") == 200)
    reach = Counter(t for c in per_page.values() for t in c)
    baseline = {}
    for t, n in reach.items():
        if n >= 0.3 * n_html:
            baseline[t] = Counter(c[t] for c in per_page.values() if t in c).most_common(1)[0][0]
    for r in rows:
        G_all.add_node(r["url"]); G_ctx.add_node(r["url"])
        cnt = per_page[r["url"]]
        seen_ctx = Counter()
        for l in (r.get("links_internal") or []):  # anchor attribution approximate (template vs body order not stored)
            to = l["to"]
            if to == r["url"]:
                continue
            G_all.add_edge(r["url"], to)
            base = baseline.get(to, 1 if l["nav"] else 0)
            extra = cnt[to] - base
            if extra > 0 and seen_ctx[to] < extra:
                seen_ctx[to] += 1
                if seen_ctx[to] == 1:
                    G_ctx.add_edge(r["url"], to)
                edges.append((r["url"], to, l["anchor"]))
                if l["anchor"]:
                    anchors[to][l["anchor"].lower()[:60]] += 1
    depth = nx.single_source_shortest_path_length(G_all, HOME) if HOME in G_all else {}
    pr = nx.pagerank(G_all, alpha=0.85)
    pr_ctx = nx.pagerank(G_ctx, alpha=0.85)

    # internal links pointing to redirects / errors
    links_to_redirect = Counter(); links_to_error = Counter()
    for r in rows:
        for l in r.get("links_internal") or []:
            st = status.get(l["to"])
            if st and 300 <= st < 400: links_to_redirect[r["url"]] += 1
            if st and st >= 400: links_to_error[r["url"]] += 1

    # ------------------------------------------------ text similarity (near duplicates)
    html_rows = [r for r in rows if r.get("status") == 200 and r.get("text_file")]
    texts = [(D / "pages_text" / r["text_file"]).read_text(encoding="utf-8") for r in html_rows]
    vec = TfidfVectorizer(stop_words="english", max_df=0.35, min_df=2, ngram_range=(1, 2), sublinear_tf=True)
    X = vec.fit_transform(texts)
    S = cosine_similarity(X)
    urls_h = [r["url"] for r in html_rows]
    near = []
    max_sim = {}
    for i in range(len(urls_h)):
        S[i, i] = 0
        j = S[i].argmax()
        max_sim[urls_h[i]] = (float(S[i, j]), urls_h[j])
        for j in range(i + 1, len(urls_h)):
            if S[i, j] >= 0.80:
                near.append({"url_a": urls_h[i], "url_b": urls_h[j], "cosine": round(float(S[i, j]), 3)})
    pd.DataFrame(near).sort_values("cosine", ascending=False).to_csv(D / "near_duplicates.csv", index=False) if near else None
    # money-page overlap: commercial/content pages only (archives excluded), lower threshold 0.50
    money_types = {"insurance_product", "insurance_service", "generic_service", "industry_service", "expertise_service",
                   "blog_post", "insurance_hub", "insurance_products_hub", "homepage", "industry_vertical_hub", "page_other"}
    ptypes = [page_type(u, (sm_map.get(u) or {}).get("sitemap")) for u in urls_h]
    money = []
    for i in range(len(urls_h)):
        if ptypes[i] not in money_types: continue
        for j in range(i + 1, len(urls_h)):
            if ptypes[j] in money_types and S[i, j] >= 0.50:
                money.append({"url_a": urls_h[i], "type_a": ptypes[i], "url_b": urls_h[j], "type_b": ptypes[j], "cosine": round(float(S[i, j]), 3)})
    pd.DataFrame(money).sort_values("cosine", ascending=False).to_csv(D / "money_page_overlap.csv", index=False)
    max_sim_money = {}
    for m in money:
        for a, b in ((m["url_a"], m["url_b"]), (m["url_b"], m["url_a"])):
            if m["cosine"] > max_sim_money.get(a, (0, None))[0]:
                max_sim_money[a] = (m["cosine"], b)

    # ------------------------------------------------ per-URL table
    out = []
    title_count = Counter(r.get("title") for r in html_rows)
    h1_count = Counter((r.get("h1") or [""])[0] for r in html_rows)
    md_count = Counter(r.get("meta_description") for r in html_rows)
    for r, txt in zip(html_rows, texts):
        pass
    text_by_url = dict(zip(urls_h, texts))
    for r in rows:
        u = r["url"]; st = r.get("status")
        smx = sm_map.get(u, {})
        ptype = page_type(u, smx.get("sitemap"))
        txt = text_by_url.get(u, "")
        h1 = (r.get("h1") or [None])
        canonical = r.get("canonical")
        canon_self = (canonical is None) or (canonical.rstrip("/") == u.rstrip("/"))
        noindex = "noindex" in ((r.get("meta_robots") or "") + (r.get("x_robots_tag") or "")).lower()
        indexable = st == 200 and not noindex and canon_self
        ins_hits = len(INS_TERMS.findall(txt))
        wc = r.get("word_count") or 0
        topic_src = f"{urlparse(u).path} {r.get('title') or ''} {' '.join(r.get('h1') or [])}"
        terr = territories(topic_src)
        ms, msu = max_sim.get(u, (None, None))
        inl_all = G_all.in_degree(u); inl_ctx = G_ctx.in_degree(u)
        top_anchor = ", ".join(a for a, _ in anchors[u].most_common(3))
        out.append({
            "url": u, "path": urlparse(u).path, "status": st, "redirect_to": r.get("location"),
            "in_sitemap": u in sm_map, "sitemap": smx.get("sitemap"), "sitemap_lastmod": smx.get("lastmod"),
            "found_from": r.get("found_from"),
            "page_type": ptype, "business_layer": BUSINESS_LAYER.get(ptype, "?"),
            "insurance_territories": ";".join(t for t in terr if t != "insurance_generic"),
            "insurance_relevant": bool(terr) or (wc > 0 and ins_hits / max(wc, 1) * 1000 >= 8),
            "insurance_term_density_per_1k": round(ins_hits / max(wc, 1) * 1000, 1) if wc else None,
            "indexable": indexable, "noindex": noindex, "canonical": canonical, "canonical_self": canon_self,
            "title": r.get("title"), "title_len": len(r.get("title") or ""), "title_dup_count": title_count.get(r.get("title"), 0) if st == 200 else None,
            "meta_description": r.get("meta_description"), "meta_desc_len": len(r.get("meta_description") or ""),
            "meta_desc_dup_count": md_count.get(r.get("meta_description"), 0) if st == 200 else None,
            "h1": h1[0], "h1_count": len(r.get("h1") or []), "h1_dup_count": h1_count.get(h1[0], 0) if st == 200 else None,
            "h2_count": r.get("h2_count"), "word_count": wc,
            "schema_types": ";".join(r.get("schema_types") or []),
            "has_product_schema": any(t in (r.get("schema_types") or []) for t in ("Product", "SoftwareApplication", "Service")),
            "published": r.get("published"), "modified": r.get("modified"),
            "crawl_depth": depth.get(u), "inlinks_all": inl_all, "inlinks_contextual": inl_ctx,
            "outlinks_internal": len(r.get("links_internal") or []),
            "links_to_redirects": links_to_redirect.get(u, 0), "links_to_errors": links_to_error.get(u, 0),
            "internal_pagerank": round(pr.get(u, 0) * 1000, 3), "contextual_pagerank": round(pr_ctx.get(u, 0) * 1000, 3),
            "top_inbound_anchors": top_anchor,
            "max_similarity": round(ms, 3) if ms is not None else None, "most_similar_url": msu,
            "ttfb_ms": r.get("ttfb_ms"), "html_kb": round((r.get("bytes") or 0) / 1024),
            "img_no_alt": r.get("img_no_alt"), "hreflang": ";".join(f"{a}" for a, b in (r.get("hreflang") or [])),
            "lang": r.get("lang"),
        })
    df = pd.DataFrame(out)

    # orphan logic: in sitemap, 200, but no contextual inlinks AND not linked from nav
    df["orphan_contextual"] = (df.status == 200) & (df.inlinks_contextual == 0)
    df["orphan_total"] = (df.status == 200) & (df.inlinks_all == 0)
    # sitemap hygiene
    df["sitemap_non_indexable"] = df.in_sitemap & ~df.indexable
    df.to_csv(D / "urls_analyzed.csv", index=False, encoding="utf-8")
    pd.DataFrame(edges, columns=["from", "to", "anchor"]).to_csv(D / "link_edges.csv", index=False)

    # ------------------------------------------------ cannibalization clusters (insurance territories)
    cann = []
    idx = df[(df.status == 200)]
    for terr in TERRITORIES:
        if terr in ("insurance_generic", "data_analytics_dwh", "customer_portal_cx"):
            continue
        m = idx[idx.insurance_territories.str.contains(terr, na=False)]
        if len(m) >= 2:
            for _, x in m.iterrows():
                cann.append({"territory": terr, "url": x.url, "page_type": x.page_type, "title": x.title, "h1": x.h1,
                             "word_count": x.word_count, "inlinks_contextual": x.inlinks_contextual,
                             "internal_pagerank": x.internal_pagerank, "cluster_size": len(m)})
    pd.DataFrame(cann).to_csv(D / "cannibalization.csv", index=False)

    # ------------------------------------------------ summary
    ok = df[df.status == 200]
    summ = {
        "crawled": len(df), "status_counts": df.status.value_counts(dropna=False).to_dict(),
        "sitemap_urls": len(sm_map), "sitemap_not_crawled_or_non200": int(sum(1 for u in sm_map if status.get(u) != 200)),
        "discovered_not_in_sitemap_200": int(((df.status == 200) & ~df.in_sitemap).sum()),
        "page_type_counts": ok.page_type.value_counts().to_dict(),
        "business_layer_counts": ok.business_layer.value_counts().to_dict(),
        "insurance_relevant_200": int(ok.insurance_relevant.sum()),
        "indexable": int(df.indexable.sum()), "noindex": int(df.noindex.sum()),
        "canonical_not_self": int((~df.canonical_self & (df.status == 200)).sum()),
        "dup_titles": int((ok.title_dup_count > 1).sum()), "dup_h1": int((ok.h1_dup_count > 1).sum()),
        "missing_h1": int((ok.h1_count == 0).sum()), "multi_h1": int((ok.h1_count > 1).sum()),
        "missing_meta_desc": int((ok.meta_desc_len == 0).sum()),
        "title_over_60": int((ok.title_len > 60).sum()),
        "thin_under_300w": int((ok.word_count < 300).sum()),
        "near_duplicate_pairs_080": len(near), "money_page_overlap_pairs_050": len(money),
        "near_dup_pairs_excl_archives": sum(1 for x in near if page_type(x["url_a"], None) not in ("pagination", "case_filter_archive", "media_hub", "case_hub")),
        "orphan_contextual": int(df.orphan_contextual.sum()), "orphan_total": int(df.orphan_total.sum()),
        "depth_dist": ok.crawl_depth.value_counts(dropna=False).sort_index().to_dict(),
        "pages_linking_to_redirects": int((df.links_to_redirects > 0).sum()),
        "pages_linking_to_errors": int((df.links_to_errors > 0).sum()),
        "schema_type_counts": Counter(t for s in ok.schema_types.fillna("") for t in s.split(";") if t).most_common(25),
        "product_schema_on_products": int(ok[ok.page_type == "insurance_product"].has_product_schema.sum()),
        "products_total": int((ok.page_type == "insurance_product").sum()),
        "median_ttfb_ms": float(ok.ttfb_ms.median()), "median_html_kb": float(ok.html_kb.median()),
    }
    (D / "summary.json").write_text(json.dumps(summ, indent=1, default=str))
    print(json.dumps(summ, indent=1, default=str))


if __name__ == "__main__":
    main()
