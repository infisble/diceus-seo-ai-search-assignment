"""
Builds the three Excel deliverables from data/ + strategy_data.py:
  02_Current_State_Audit.xlsx, 03_Search_Market_and_Opportunity.xlsx, 05_90_Day_Execution_Plan.xlsx
"""
import json, re, sys
from collections import Counter
from pathlib import Path
import pandas as pd
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill, Border, Side
from openpyxl.utils import get_column_letter

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import strategy_data as S

D = ROOT / "data"
OUT = ROOT / "deliverables"
OUT.mkdir(exist_ok=True)

HDR = PatternFill("solid", fgColor="1F3A5F")
HFONT = Font(bold=True, color="FFFFFF")
TFONT = Font(bold=True, size=14, color="1F3A5F")
FILLS = {"FIX": "FDE2D6", "REPOSITION": "FDEBD3", "CREATE": "DDF3EA", "GROW": "DDF3EA", "OPTIMIZE": "DCE9FA", "KEEP": "EFEFEA",
         "VALIDATE": "FFF5CC", "CONSOLIDATE": "FFF5CC", "DEINDEX": "F3E1F0", "REDIRECT": "F3E1F0", "MUST DO": "DCE9FA",
         "HIGH-VALUE NEXT": "DDF3EA", "LATER": "EFEFEA"}
thin = Side(style="thin", color="D9D8D3")


def write_df(wb, name, df, widths=None, note=None, wrap_cols=(), color_col=None):
    ws = wb.create_sheet(name[:31])
    r0 = 1
    if note:
        ws.cell(1, 1, note).font = Font(italic=True, color="52514E")
        ws.cell(1, 1).alignment = Alignment(wrap_text=True, vertical="top")
        ws.merge_cells(start_row=1, start_column=1, end_row=1, end_column=max(4, min(len(df.columns), 10)))
        ws.row_dimensions[1].height = 48
        r0 = 3
    for j, c in enumerate(df.columns, 1):
        cell = ws.cell(r0, j, str(c)); cell.fill = HDR; cell.font = HFONT
        cell.alignment = Alignment(wrap_text=True, vertical="center")
    for i, row in enumerate(df.itertuples(index=False), r0 + 1):
        for j, v in enumerate(row, 1):
            if isinstance(v, float) and pd.isna(v):
                v = None
            elif isinstance(v, (list, tuple, dict)):
                v = json.dumps(v, ensure_ascii=False)
            cell = ws.cell(i, j, v)
            cell.border = Border(bottom=thin)
            if df.columns[j - 1] in wrap_cols:
                cell.alignment = Alignment(wrap_text=True, vertical="top")
            else:
                cell.alignment = Alignment(vertical="top")
        if color_col and color_col in df.columns:
            val = str(row[list(df.columns).index(color_col)]).upper()
            for k, f in FILLS.items():
                if val.startswith(k) or k in val.split(" ")[0]:
                    ws.cell(i, list(df.columns).index(color_col) + 1).fill = PatternFill("solid", fgColor=f)
                    break
    ws.freeze_panes = ws.cell(r0 + 1, 2)
    ws.auto_filter.ref = f"A{r0}:{get_column_letter(len(df.columns))}{r0 + len(df)}"
    for j, c in enumerate(df.columns, 1):
        w = (widths or {}).get(c)
        if w is None:
            sample = [len(str(c))] + [len(str(x)) for x in df[c].head(200).tolist()]
            w = min(max(sample) + 2, 60)
        ws.column_dimensions[get_column_letter(j)].width = w
    return ws


def readme(wb, title, lines):
    ws = wb.active; ws.title = "README"
    ws.cell(1, 1, title).font = TFONT
    for i, l in enumerate(lines, 3):
        c = ws.cell(i, 1, l); c.alignment = Alignment(wrap_text=True, vertical="top")
        if l.isupper() or l.endswith(":"):
            c.font = Font(bold=True, color="1F3A5F")
    ws.column_dimensions["A"].width = 150


EVIDENCE_LINES = [
    "EVIDENCE LABELS:",
    "FACT / OBSERVED = measured in our own crawl, raw HTML, HTTP probe or recorded SERP/AI-panel output on 2026-10-06.",
    "INFERENCE = reasoned from facts. HYPOTHESIS = plausible, needs testing. RECOMMENDATION = proposed action.",
    "DATA UNAVAILABLE = no access (GSC, GA4, CRM, backlink tools, search volumes). Missing data is never treated as zero.",
    "VALIDATION REQUIRED = action is blocked until the named data is reviewed.",
]

# ======================================================================================== 02
def proposed(row, noindex_urls):
    t, p = row.page_type, row.path or ""
    for tr in S.TRANSITION:
        if tr[1].strip() == p:
            return tr[5], tr[4], tr[6]
    if row.url in noindex_urls: return "FIX (remove stray noindex)", "Product page - must be indexable", "P0"
    m = {
        "insurance_product": ("KEEP + OPTIMIZE", "L1 product page (one query cluster per URL)", "P1"),
        "insurance_service": ("KEEP + OPTIMIZE / VALIDATE overlaps", "L3 insurance services around products", "P2"),
        "generic_service": ("KEEP (demote) / VALIDATE BEFORE ACTION", "Secondary technology services", "P3"),
        "expertise_service": ("KEEP (demote) / VALIDATE BEFORE ACTION", "Secondary technology services", "P3"),
        "industry_service": ("KEEP (demote) / VALIDATE BEFORE ACTION", "Secondary non-insurance vertical", "P3"),
        "industry_vertical_hub": ("KEEP (demote) / VALIDATE BEFORE ACTION", "Secondary vertical hub", "P3"),
        "case_study": ("KEEP + OPTIMIZE (tag to product)", "Proof", "P2"),
        "case_filter_archive": ("DEINDEX noindex,follow - VALIDATE first", "Utility archive", "LATER"),
        "pagination": ("KEEP", "Pagination (crawl path)", "-"),
        "media_news": ("KEEP", "Entity / PR proof", "P3"),
        "author": ("KEEP + enrich (E-E-A-T)", "Author entity", "P3"),
        "localized_da": ("VALIDATE BEFORE ACTION", "Nordic localisation", "LATER"),
    }
    if t == "blog_post":
        if re.search(r"intern|senior-|business-development-manager|product-designer|hr-generalist|pr-intern", p):
            return "REPOSITION -> careers; 410/noindex when closed", "Vacancy", "P3"
        if row.insurance_relevant:
            return "KEEP + OPTIMIZE (add contextual links to owner product)", "L4 authority spoke of a product hub", "P1"
        return "KEEP / VALIDATE (prune only 0-click, 0-link after GSC)", "Generic content", "LATER"
    return m.get(t, ("KEEP", t, "-"))


def build_02():
    df = pd.read_csv(D / "urls_analyzed.csv")
    hr = json.loads((D / "head_recheck.json").read_text()) if (D / "head_recheck.json").exists() else {}
    noindex_urls = {u for u, v in hr.items() if any("noindex" in x.lower() for x in v.get("robots", []))}
    summ = json.loads((D / "summary.json").read_text())
    df["robots_all_tags"] = df.url.map(lambda u: " | ".join(hr.get(u, {}).get("robots", [])) if u in hr else "NOT CHECKED")
    df["noindex_effective"] = df.url.isin(noindex_urls)
    acts = df.apply(lambda r: proposed(r, noindex_urls), axis=1)
    df["proposed_action"] = [a[0] for a in acts]; df["future_role"] = [a[1] for a in acts]; df["priority"] = [a[2] for a in acts]
    df["gsc_clicks_12m"] = "DATA UNAVAILABLE"; df["referring_domains"] = "DATA UNAVAILABLE"

    wb = Workbook()
    readme(wb, "02 Current State Audit - diceus.com (crawl 2026-10-06)", [
        "PURPOSE: URL-level evidence behind the current-state findings. Every chart/number in 01 and 04 can be re-derived from these sheets.",
        "",
        "DATASET:",
        f"Own Python crawler (scripts/01_crawl.py): seeds = 709 sitemap URLs + homepage, BFS over internal links, robots.txt honoured, 1 request/s, single thread, no query strings. {summ['crawled']} URLs fetched, 0 blocked by robots, 0 errors.",
        "Head re-check pass (scripts/01b_head_recheck.py) re-read ALL robots/canonical tags (crawler v1 read only the first robots tag - bug found by cross-checking an AI-agent finding).",
        "Wayback CDX (1 API call) for historical URLs; legacy URLs re-checked hop-by-hop (scripts/05_legacy_redirects.py).",
        "Contextual inlinks = internal links that are NOT part of the sitewide template (per-target baseline heuristic, see 06 methodology §C/§I).",
        "",
        *EVIDENCE_LINES,
        "",
        "SHEETS:",
        "Summary - headline numbers | URL_Inventory - every crawled URL with metrics, proposed action, future role",
        "PageType_Rollup | Layer_Links - why products are under-linked | Indexability - effective noindex & hygiene",
        "Product_Pages - all product/hub pages | Intent_Overlap - title/H1/URL similarity pairs (cannibalization candidates)",
        "Territory_Clusters - all URLs per insurance territory | Content_Similarity - TF-IDF body-text pairs",
        "Orphans_Weak - zero-inlink and deep pages | Legacy_Redirects - historical URLs and where they resolve now",
        "Tech_Probes - host/protocol/404/AI-bot checks | PSI_CWV - PageSpeed lab + CrUX field data by template",
        "Schema_Coverage - structured data by page type | Content_Age - blog by year and insurance relevance",
        "",
        "NOT AVAILABLE (columns kept explicitly as DATA UNAVAILABLE): GSC clicks/impressions/queries, GA4 sessions/conversions, CRM leads, referring domains per URL.",
    ])
    ok = df[df.status == 200]
    rows = [
        ("URLs crawled", summ["crawled"], "FACT", "crawl"),
        ("URLs in XML sitemaps", summ["sitemap_urls"], "FACT", "sitemap_index.xml (Yoast, 10 child sitemaps)"),
        ("Status 200 / 3xx / 4xx-5xx", f"{(df.status==200).sum()} / {((df.status>=300)&(df.status<400)).sum()} / {(df.status>=400).sum()}", "FACT", "crawl"),
        ("200 URLs found via links but not in sitemap", summ["discovered_not_in_sitemap_200"], "FACT", "mostly case-study filter archives + /media/page/N"),
        ("Effective noindex pages (any robots tag)", len(noindex_urls), "FACT", "head re-check; ALL are in insurance-sitemap.xml"),
        ("Insurance product pages (excl. hubs)", int((ok.page_type == "insurance_product").sum()), "FACT", "/insurance/solutions/*"),
        ("Generic service + expertise + non-insurance industry URLs", int(ok.page_type.isin(["generic_service", "expertise_service", "industry_service", "industry_vertical_hub", "services_hub", "expertise_hub", "industry_hub"]).sum()), "FACT", "classification rules in scripts/04_analyze.py"),
        ("Insurance-relevant URLs (territory regex or term density >= 8/1k words)", summ["insurance_relevant_200"], "FACT (rule-based)", "04_analyze.py"),
        ("Blog posts / insurance-relevant", f"{(ok.page_type=='blog_post').sum()} / {int(ok[ok.page_type=='blog_post'].insurance_relevant.sum())}", "FACT (rule-based)", ""),
        ("Median contextual inlinks: products / insurance services / generic services", f"{ok[ok.page_type=='insurance_product'].inlinks_contextual.median():.0f} / {ok[ok.page_type=='insurance_service'].inlinks_contextual.median():.0f} / {ok[ok.page_type=='generic_service'].inlinks_contextual.median():.0f}", "FACT (heuristic)", "Layer_Links"),
        ("Template (header/nav/footer) links per page (median)", int(ok.outlinks_internal.median()), "FACT", "mega-menu"),
        ("Product pages with Product/SoftwareApplication schema", f"{summ['product_schema_on_products']} of {summ['products_total']}", "FACT", "JSON-LD parse"),
        ("Title > 60 chars", summ["title_over_60"], "FACT", "mostly blog posts"),
        ("Duplicate titles / H1 among 200 pages", f"{summ['dup_titles']} / {summ['dup_h1']}", "FACT", ""),
        ("Pages < 300 words", summ["thin_under_300w"], "FACT", "mostly archives/conversion pages"),
        ("Pages with zero inlinks from crawled pages (sitemap-only)", summ["orphan_total"], "FACT", "Orphans_Weak"),
        ("Crawl depth distribution (clicks from home)", json.dumps(summ["depth_dist"]), "FACT", "flat due to mega-menu"),
        ("Intent-overlap pairs (title/H1/URL similarity >= 0.55)", len(pd.read_csv(D / "intent_overlap.csv")), "FACT (similarity) / INFERENCE (cannibalization)", "Intent_Overlap"),
        ("Median HTML size (KB) / median TTFB (ms, our client)", f"{summ['median_html_kb']:.0f} / {summ['median_ttfb_ms']:.0f}", "FACT", "Cloudflare-cached"),
        ("Organic clicks, impressions, rankings, leads", "DATA UNAVAILABLE", "-", "requires GSC/GA4/CRM"),
    ]
    write_df(wb, "Summary", pd.DataFrame(rows, columns=["Metric", "Value", "Evidence", "Source / note"]), widths={"Metric": 70, "Value": 30, "Evidence": 26, "Source / note": 60})

    cols = ["url", "status", "page_type", "business_layer", "insurance_territories", "insurance_relevant", "in_sitemap", "sitemap",
            "indexable", "noindex_effective", "robots_all_tags", "canonical_self", "title", "title_len", "h1", "meta_desc_len", "word_count",
            "h2_count", "schema_types", "crawl_depth", "inlinks_all", "inlinks_contextual", "internal_pagerank", "top_inbound_anchors",
            "max_similarity", "most_similar_url", "published", "modified", "sitemap_lastmod", "redirect_to", "found_from",
            "proposed_action", "future_role", "priority", "gsc_clicks_12m", "referring_domains"]
    df["indexable"] = df.indexable & ~df.noindex_effective
    write_df(wb, "URL_Inventory", df[cols].sort_values(["business_layer", "url"]), note="One row per crawled URL. proposed_action is rule-based (scripts/08_build_excel.py::proposed) with explicit overrides for material pages from the transition table in 04. Destructive actions are never assigned without VALIDATE.",
             widths={"url": 70, "title": 50, "h1": 40, "schema_types": 40, "top_inbound_anchors": 40, "most_similar_url": 50, "proposed_action": 45, "future_role": 40, "robots_all_tags": 40},
             color_col="proposed_action")

    roll = ok.groupby(["business_layer", "page_type"]).agg(urls=("url", "count"), median_words=("word_count", "median"),
        median_ctx_inlinks=("inlinks_contextual", "median"), insurance_share=("insurance_relevant", "mean"),
        median_depth=("crawl_depth", "median"), median_title_len=("title_len", "median")).reset_index().sort_values("urls", ascending=False)
    roll["insurance_share"] = (roll.insurance_share * 100).round(0)
    write_df(wb, "PageType_Rollup", roll)

    ll = ok.groupby("page_type").agg(urls=("url", "count"), median_ctx_inlinks=("inlinks_contextual", "median"),
        mean_ctx_inlinks=("inlinks_contextual", "mean"), median_contextual_pagerank=("contextual_pagerank", "median")).reset_index().sort_values("median_ctx_inlinks", ascending=False)
    write_df(wb, "Layer_Links", ll.round(2), note="FACT: products (insurance_product) receive a median of ~24 contextual links vs ~94 for generic services - internal linking favours the secondary business. Template links excluded via per-target baseline heuristic (validated by manual spot checks - see 06 §I).")

    idx = pd.DataFrame([
        *[(u, "Effective NOINDEX,NOFOLLOW via second hard-coded <meta name=robots>", " | ".join(hr[u]["robots"]), "FACT", "In insurance-sitemap.xml -> conflicting signals; remove tag (P0)") for u in sorted(noindex_urls)],
        ("https://likeprod.diceus.com/*", "Staging host URLs in search index (returns 401 now)", "-", "FACT (search results; AI agent) ", "GSC removal + X-Robots-Tag on non-prod"),
        ("/solutions/<product>/ (legacy)", "Legacy product paths still indexed in some engines; now 301 -> /insurance/solutions/<product>/", "-", "FACT (HTTP 301 verified)", "No action beyond keeping 301 one-hop; monitor"),
        ("/industry/insurance/* (legacy)", "Old insurance section from previous migration", "-", "FACT (Wayback + Legacy_Redirects)", "See Legacy_Redirects"),
        ("http://www.diceus.com/", "2-hop redirect (http://www -> https://www -> https://diceus.com/)", "-", "FACT (probe)", "Collapse to 1 hop at Cloudflare"),
        ("https://diceus.com/index.php", "Returns 200 with homepage HTML (duplicate of /)", "-", "FACT (probe)", "301 to / (low priority; canonical mitigates)"),
        ("hreflang", "Only x-default self-reference on all pages; /da/ has 4 pages without reciprocal hreflang", "-", "FACT", "VALIDATE Nordic strategy"),
    ], columns=["URL", "Issue", "Robots tags found", "Evidence", "Recommendation"])
    write_df(wb, "Indexability", idx, widths={"URL": 75, "Issue": 70, "Robots tags found": 45, "Recommendation": 60})

    prod = df[df.page_type.isin(["insurance_product", "insurance_products_hub", "insurance_hub"])][
        ["url", "title", "h1", "word_count", "noindex_effective", "inlinks_contextual", "contextual_pagerank", "schema_types", "has_product_schema", "proposed_action", "future_role"]]
    write_df(wb, "Product_Pages", prod.sort_values("url"), widths={"url": 75, "title": 55, "h1": 45, "schema_types": 40}, color_col="proposed_action")

    io = pd.read_csv(D / "intent_overlap.csv")
    def handle(r):
        if "/" == r.path_a: return "Homepage cannibalization -> REPOSITION homepage (GSC-gated); /services/custom-software-development/ owns generic intent"
        if r.type_a == r.type_b == "generic_service" and r.title_similarity >= 0.85: return "CONSOLIDATE candidate (VALIDATE with GSC + backlinks)"
        if "insurance_product" in (r.type_a, r.type_b) and r.type_a != r.type_b: return "Product vs service/blog: product owns BOFU; other page re-angled + links to product"
        if r.type_a == r.type_b == "insurance_product": return "Parent/child product variants: differentiate by segment; parent owns head term"
        if "blog_post" in (r.type_a, r.type_b): return "Blog vs commercial: blog targets informational intent and links to commercial owner"
        return "Review in GSC (query overlap) before action"
    io["recommended_handling"] = io.apply(handle, axis=1)
    io["evidence"] = "FACT similarity / INFERENCE cannibalization - VALIDATE with GSC query-by-page"
    write_df(wb, "Intent_Overlap", io, widths={"recommended_handling": 80, "path_a": 55, "path_b": 55})

    write_df(wb, "Territory_Clusters", pd.read_csv(D / "cannibalization.csv"), note="All 200-status URLs whose URL/title/H1 maps to the same insurance territory (regex in 04_analyze.py). Large clusters = several URLs competing for one territory; the transition table assigns one owner.",
             widths={"url": 75, "title": 55, "h1": 45})
    nd = pd.read_csv(D / "near_duplicates.csv")
    mo = pd.read_csv(D / "money_page_overlap.csv")
    nd["scope"] = "all pages, cosine >= 0.80 (mostly /media/page/N pagination - expected)"
    mo["scope"] = "commercial/content pages only, cosine >= 0.50"
    write_df(wb, "Content_Similarity", pd.concat([mo, nd], ignore_index=True), widths={"url_a": 70, "url_b": 70})

    ow = df[(df.status == 200) & ((df.inlinks_all == 0) | (df.inlinks_contextual == 0) | (df.crawl_depth >= 4) | df.crawl_depth.isna())][
        ["url", "page_type", "in_sitemap", "inlinks_all", "inlinks_contextual", "crawl_depth", "word_count", "proposed_action"]]
    write_df(wb, "Orphans_Weak", ow.sort_values(["inlinks_all", "inlinks_contextual"]), widths={"url": 80})

    lr = D / "legacy_redirects.csv"
    if lr.exists():
        write_df(wb, "Legacy_Redirects", pd.read_csv(lr), note="Historical URLs (Wayback CDX, once 200) not in today's sitemap, followed hop-by-hop at 1 req/s. Final 404 on a URL with backlinks = lost equity (backlinks: DATA UNAVAILABLE - prioritise with Ahrefs/GSC links).",
                 widths={"legacy_path": 70, "final_url": 70})
    tp = D / "tech_probes.json"
    if tp.exists():
        write_df(wb, "Tech_Probes", pd.DataFrame(json.loads(tp.read_text())), widths={"url": 60, "location": 60})
    ps = D / "psi.json"
    if ps.exists():
        p = json.loads(ps.read_text())
        rows = []
        for k, v in p.items():
            tpl, strat = k.split("|")
            rows.append({"template": tpl, "strategy": strat, **{kk: (json.dumps(vv) if isinstance(vv, dict) else vv) for kk, vv in v.items()}})
        write_df(wb, "PSI_CWV", pd.DataFrame(rows), note="PSI API v5 failed (shared keyless quota exhausted) -> local Lighthouse 12, mobile emulation, 1 run per template (noisy). Field (CrUX) data: DATA UNAVAILABLE. Product template LCP element = Cookiebot consent text (render delay ~10.5 s) - HYP until field data.")
    sc = ok.assign(st=ok.schema_types.fillna("")).groupby("page_type").agg(
        urls=("url", "count"),
        Organization=("st", lambda s: s.str.contains("Organization").mean()),
        BreadcrumbList=("st", lambda s: s.str.contains("BreadcrumbList").mean()),
        FAQPage=("st", lambda s: s.str.contains("FAQPage").mean()),
        Article=("st", lambda s: s.str.contains("Article").mean()),
        Product_or_SoftwareApplication=("st", lambda s: s.str.contains("Product|SoftwareApplication").mean()),
    ).reset_index()
    for c in sc.columns[2:]:
        sc[c] = (sc[c] * 100).round(0)
    write_df(wb, "Schema_Coverage", sc, note="% of pages per type carrying each JSON-LD type (Yoast graph). Note FAQPage on many service pages; NO Product/SoftwareApplication anywhere.")
    b = ok[ok.page_type == "blog_post"].copy()
    b["year"] = pd.to_datetime(b.published, errors="coerce", utc=True).dt.year
    ca = b.groupby(["year", "insurance_relevant"]).size().unstack(fill_value=0).reset_index()
    ca.columns = ["year", "non_insurance_posts", "insurance_posts"]
    write_df(wb, "Content_Age", ca)
    wb.save(OUT / "02_Current_State_Audit.xlsx"); print("02 saved")


# ======================================================================================== 03
def build_03():
    wb = Workbook()
    readme(wb, "03 Search Market & Opportunity - DICEUS (US, English)", [
        "PURPOSE: independently derived search universe, competitive landscape and prioritised opportunities.",
        "",
        "DATA SOURCES & LIMITS:",
        "Keyword discovery: Google Autocomplete (US/en), 43 seeds x 10 modifiers, 1 req/1.2s -> 699 unique suggestions (513 relevant). Proves a query exists; does NOT give volume.",
        "Search volume / keyword difficulty: DATA UNAVAILABLE (no Ahrefs/Semrush/GSC). Demand is scored 1-5 as a PROXY from autocomplete breadth and SERP commerciality and is weighted lowest in the priority score.",
        "SERP sample: 44 queries via Claude Code WebSearch tool. PROXY, not a Google-US replica (locale duplicates, spam, staging hosts appear). Positions are directional only.",
        "AI panel: 20 prompts, Claude + web search, 1 run each. ChatGPT, Perplexity, Google AI Overviews: DATA UNAVAILABLE.",
        "",
        "DISTINGUISHING THE THREE AXES (as required by the brief):",
        "Search demand (does anybody search it?) -> 'demand_proxy' | Business relevance (does it sell DICEUS products?) -> 'relevance' | SEO feasibility (can DICEUS realistically rank?) -> 'feasibility'.",
        "Priority score = 0.45*relevance + 0.35*feasibility + 0.20*demand_proxy. Feasibility 0 = no evidence (generic services; no ranking data) - deliberately not prioritised until GSC shows otherwise.",
        "",
        *EVIDENCE_LINES,
    ])
    t = pd.DataFrame([(*x, S.territory_score(x)) for x in S.TERRITORIES],
                     columns=["id", "territory", "layer", "relevance", "demand_proxy", "feasibility", "current_visibility (FACT, SERP proxy)", "evidence", "play", "priority_score"])
    t = t.sort_values("priority_score", ascending=False)
    write_df(wb, "Territories", t, widths={"territory": 45, "current_visibility (FACT, SERP proxy)": 70, "evidence": 70, "play": 60}, wrap_cols=("current_visibility (FACT, SERP proxy)", "evidence", "play"))
    o = pd.DataFrame(S.OPPORTUNITIES, columns=["id", "opportunity", "territory", "funnel", "target_url", "action", "impact", "effort", "confidence", "evidence"])
    o["ice_score"] = (o.impact * o.confidence.map({"High": 1.0, "Medium": 0.8, "Low": 0.5}) / o.effort).round(2)
    write_df(wb, "Opportunities", o.sort_values("ice_score", ascending=False), widths={"opportunity": 60, "target_url": 60, "evidence": 70},
             wrap_cols=("opportunity", "target_url", "evidence"), color_col="action",
             note="Prioritised backlog. ice_score = impact x confidence / effort. Destructive actions (CONSOLIDATE/DEINDEX) carry VALIDATE.")
    write_df(wb, "Clusters", pd.read_csv(D / "clusters.csv").sort_values(["territory", "suggest_evidence"], ascending=[True, False]),
             widths={"sample_queries": 100}, note="Autocomplete queries clustered by rule (scripts/06_keywords.py). suggest_evidence = number of seed/modifier expansions returning the cluster's queries (relative demand PROXY).")
    write_df(wb, "Keywords", pd.read_csv(D / "keywords.csv"), widths={"query": 60})
    s = json.load(open(D / "serp_observations.json", encoding="utf-8"))
    flat, per = [], []
    for ob in s["observations"]:
        d_pos = [r["pos"] for r in ob["results"] if "diceus" in r["domain"]]
        types = Counter(r["page_type"] for r in ob["results"])
        per.append({"query": ob["query"], "territory": ob["territory"], "intent": ob["intent"], "diceus_present": ob["diceus_present"],
                    "diceus_positions": ",".join(map(str, d_pos)), "diceus_url": ob.get("diceus_url"),
                    "dominant_page_types": ", ".join(f"{k}:{v}" for k, v in types.most_common(3)), "observation": ob.get("observation")})
        for r in ob["results"]:
            flat.append({"query": ob["query"], "territory": ob["territory"], **{k: r.get(k) for k in ("pos", "domain", "url", "page_type", "note")}})
    write_df(wb, "SERP_Summary", pd.DataFrame(per), widths={"intent": 40, "observation": 90, "diceus_url": 60}, wrap_cols=("observation", "intent"),
             note=s["meta"]["caveat"])
    write_df(wb, "SERP_Results", pd.DataFrame(flat), widths={"url": 80, "note": 60})
    fl = pd.DataFrame(flat)
    comp = fl.groupby("domain").agg(queries=("query", "nunique"), territories=("territory", lambda x: ", ".join(sorted(set(x)))),
                                    page_types=("page_type", lambda x: ", ".join(f"{k}:{v}" for k, v in Counter(x).most_common(3))),
                                    best_pos=("pos", "min")).reset_index().sort_values("queries", ascending=False)
    write_df(wb, "Competitors", comp.head(80), widths={"territories": 60, "page_types": 50},
             note="Organic competitors = domains that appear across sampled SERPs (not just known business rivals). Qualitative structure notes: data/serp_competitors.md and 04 §4.3.")
    a = json.load(open(D / "ai_panel_results.json", encoding="utf-8"))
    ar = [{"id": x["id"], "prompt": x["prompt"], "intent_type": x["intent_type"], "diceus_mentioned": x["diceus_mentioned"],
           "diceus_cited_url": x.get("diceus_cited_url"), "brands_named": ", ".join(x["brands_named"]),
           "sources_cited": " | ".join(f"{c['domain']} ({c['type']})" for c in x["sources_cited"]), "notes": x.get("notes")} for x in a]
    write_df(wb, "AI_Panel", pd.DataFrame(ar), widths={"prompt": 55, "brands_named": 60, "sources_cited": 90, "notes": 80}, wrap_cols=("brands_named", "sources_cited", "notes"),
             note="Claude (Opus) + web search, 2026-10-06, 1 run per prompt. Non-deterministic; directional. Other engines DATA UNAVAILABLE.")
    sov, n_unb = S.ai_share_of_voice(D / "ai_panel_results.json")
    write_df(wb, "AI_Share_of_Voice", pd.DataFrame(sov.most_common(30), columns=["brand", "unbranded_prompts_named (of %d)" % n_unb]),
             note="Recomputed from raw panel JSON; product variants collapsed to vendor (e.g. 'Guidewire ClaimCenter' -> Guidewire); once per prompt. Agent's own summary said Guidewire 8 - recount = 7 (prompt #6 names Guidewire only as the subject). Noise brands kept for honesty.")
    ent = pd.DataFrame([
        ("Wikipedia", "No", "-", "FACT"), ("Wikidata", "No", "-", "FACT"), ("Crunchbase", "Yes (403 on fetch)", "n/a", "FACT"),
        ("Clutch", "Yes - 4.9, 49 reviews", "IT services / outsourcing, $25-49/hr", "FACT"), ("GoodFirms", "Yes - 4.9, 26 reviews", "Web development company", "FACT"),
        ("Gartner Peer Insights", "Product stubs (PAS, Captive, Reinsurance, Group, Portals)", "Product vendor; captive & reinsurance 'no reviews yet'", "FACT"),
        ("Capterra / GetApp / Software Advice", "Many listings, mostly non-US ccTLDs, 0 reviews", "Product vendor; listing names lack 'DICEUS'", "FACT"),
        ("G2", "Seller page only", "-", "FACT"), ("TrustRadius", "Yes", "-", "FACT"),
        ("Microsoft Marketplace", "PAS listed (Jun 2026)", "Product", "FACT (DICEUS news)"),
        ("Captive Review / Captive International / Insurance Journal", "No editorial coverage found", "-", "FACT (search)"),
        ("Celent / Datos Insights", "No profile found", "-", "FACT (search)"), ("Reddit / YouTube", "None found", "-", "FACT (search)"),
        ("llms.txt", "Exists; lists only PAS .md", "-", "FACT"), ("AI crawler access", "GPTBot/ClaudeBot/PerplexityBot/CCBot = 200", "-", "FACT"),
    ], columns=["surface", "present", "how DICEUS is described", "evidence"])
    write_df(wb, "Entity_Presence", ent, widths={"surface": 45, "present": 55, "how DICEUS is described": 55})
    wb.save(OUT / "03_Search_Market_and_Opportunity.xlsx"); print("03 saved")


# ======================================================================================== 05
def build_05():
    wb = Workbook()
    readme(wb, "05 90-Day Execution Plan - DICEUS SEO & AI Search", [
        "PURPOSE: the strategy converted into sequenced, owned, testable work.",
        "",
        "CLASSES: MUST DO = protects equity or unblocks everything else | HIGH-VALUE NEXT = strong evidence, start once dependencies clear | LATER / VALIDATE FIRST = blocked on data (GSC/GA4/CRM/product decisions).",
        "WAVES: Days 1-30 fix, baseline, decide | Days 31-60 reposition & build | Days 61-90 validate, consolidate, scale.",
        "GOVERNANCE: every destructive change (redirect, consolidate, deindex, retitle a ranking page) requires a GSC baseline + change-log entry + 14-day post-change check + rollback plan.",
        "",
        "SHEETS: Plan | By_Wave | Workstream_DoD | KPIs | Top5_Priorities | Not_Yet | Roles",
    ])
    p = pd.DataFrame(S.PLAN, columns=["id", "workstream", "task", "days", "class", "owner", "depends_on", "definition_of_done"])
    p["start_day"] = p.days.str.split("-").str[0].astype(int); p["end_day"] = p.days.str.split("-").str[1].astype(int)
    p["wave"] = p.start_day.map(lambda d: "Days 1-30" if d <= 30 else ("Days 31-60" if d <= 60 else "Days 61-90"))
    p["status"] = "Not started"
    p = p.sort_values(["wave", "start_day", "id"])
    p = p[["id", "wave", "workstream", "task", "class", "owner", "depends_on", "start_day", "end_day", "definition_of_done", "status"]]
    write_df(wb, "Plan", p, widths={"task": 80, "definition_of_done": 70, "depends_on": 25, "owner": 28}, wrap_cols=("task", "definition_of_done"), color_col="class")
    bw = p.groupby(["wave", "class"]).size().unstack(fill_value=0).reset_index()
    write_df(wb, "By_Wave", bw)
    dod = pd.DataFrame([
        ("Technical", "0 sitemap URLs with noindex; deploy guardrail live; staging de-indexed; legacy URLs with links resolve in 1 hop; no internal links to redirects"),
        ("Architecture", "Query-ownership map signed off; nav v2 live with products first and <=120 template links; homepage repositioned with no unexplained >20% non-brand click loss after 28 days"),
        ("Content", "Captive page per spec; alt-risk hub + 3 segment pages live with proof; each page indexed and has >=10 contextual inlinks"),
        ("Internal links", "Median contextual inlinks to product pages >= 60 (baseline 24); every insurance post links to its owner product"),
        ("AI Search", "Panel v2 baseline across 4 engines; schema valid on all product templates; Wikidata live; listings branded; SoV tracked monthly"),
        ("Authority", ">=15 review requests sent, >=5 published reviews on US listings; >=1 earned trade-press article"),
        ("Measurement", "GSC/GA4/CRM baselines stored; weekly automated digest; day-90 review delivered"),
        ("Automation", "Weekly crawl diff + GSC pull + AI panel run unattended; alerts on noindex/status/title changes for priority URLs"),
    ], columns=["workstream", "definition_of_done"])
    write_df(wb, "Workstream_DoD", dod, widths={"definition_of_done": 140}, wrap_cols=("definition_of_done",))
    kpi = pd.DataFrame([
        ("Indexed priority product URLs", "GSC URL Inspection / Pages report", "3 of 23 noindexed (FACT)", "23/23 indexed by day 14", "weekly"),
        ("Non-brand impressions - alt-risk cluster", "GSC (query regex)", "DATA UNAVAILABLE", "baseline +50% by day 90 (set after baseline)", "weekly"),
        ("Non-brand clicks to product pages", "GSC (page filter /insurance/solutions/)", "DATA UNAVAILABLE", "trend up vs baseline; no loss on owners", "weekly"),
        ("Demo requests from organic landing on products", "GA4 + CRM", "DATA UNAVAILABLE", "baseline then +25%", "monthly"),
        ("Median contextual inlinks to products", "Own crawler", "24 (FACT)", ">= 60", "monthly"),
        ("AI share of voice - unbranded prompts", "Prompt panel v2 (4 engines x 3 runs)", "Claude: 2/16 (FACT)", "Claude >= 5/16; establish others", "monthly"),
        ("Branded entity answer correct ('What is DICEUS?')", "Prompt panel", "Fail (FACT)", "Pass on >= 3 of 4 engines", "monthly"),
        ("Published reviews on US product listings", "G2 / Capterra / Gartner PI", "0 (FACT)", ">= 5", "monthly"),
        ("Generic-service clicks (guardrail)", "GSC", "DATA UNAVAILABLE", "no unexplained drop > 20%", "weekly"),
    ], columns=["KPI", "source", "baseline", "90-day target", "cadence"])
    write_df(wb, "KPIs", kpi, widths={"KPI": 50, "source": 40, "baseline": 30, "90-day target": 45})
    write_df(wb, "Top5_Priorities", pd.DataFrame(S.TOP5, columns=["decision", "evidence", "expected_impact", "rationale", "dependency_or_risk"]),
             widths={c: 60 for c in ["decision", "evidence", "expected_impact", "rationale", "dependency_or_risk"]}, wrap_cols=("decision", "evidence", "expected_impact", "rationale", "dependency_or_risk"))
    write_df(wb, "Not_Yet", pd.DataFrame(S.NOT_YET, columns=["decision_not_executed_yet", "what_is_unknown", "why_acting_now_is_risky", "evidence_needed"]),
             widths={c: 60 for c in ["decision_not_executed_yet", "what_is_unknown", "why_acting_now_is_risky", "evidence_needed"]}, wrap_cols=("decision_not_executed_yet", "what_is_unknown", "why_acting_now_is_risky", "evidence_needed"))
    roles = pd.DataFrame([
        ("SEO & AI Search lead (this role)", "Owns strategy, query-ownership map, measurement, AI panel, automation; approves every destructive change"),
        ("WordPress developer", "Templates, robots/schema, nav v2, redirects, deploy guardrails"),
        ("Product marketing / product owners", "Product truth table, features, proof, segment messaging"),
        ("Content writer(s) + insurance SME", "Segment pages, comparison page, refreshes; SME fact-check"),
        ("Designer / UX", "Homepage, nav, product page template"),
        ("Marketing / PR", "Listings, reviews, trade press, analyst relations"),
        ("CEO / Head of Growth", "Positioning sign-off (homepage), customer references"),
    ], columns=["role", "responsibilities"])
    write_df(wb, "Roles", roles, widths={"role": 40, "responsibilities": 120})
    wb.save(OUT / "05_90_Day_Execution_Plan.xlsx"); print("05 saved")


if __name__ == "__main__":
    which = sys.argv[1:] or ["02", "03", "05"]
    if "02" in which: build_02()
    if "03" in which: build_03()
    if "05" in which: build_05()
