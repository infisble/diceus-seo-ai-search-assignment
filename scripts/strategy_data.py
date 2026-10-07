"""
Single source of truth for the strategy tables. Imported by the Excel / Markdown / chart builders so
every deliverable shows the same numbers and decisions.

Evidence labels used throughout:  FACT = observed in our data | INF = inference | HYP = hypothesis |
REC = recommendation | DATA UNAVAILABLE | VALIDATION REQUIRED
"""

# ------------------------------------------------------------------------------------------------
# 1. Territory scoring (03_Search_Market). Scores 1-5.
#   Business relevance  : brief hierarchy (Products > Solutions > Services) + product-maturity evidence
#   Demand evidence     : PROXY only (autocomplete breadth + SERP commerciality). No volumes (DATA UNAVAILABLE)
#   SEO feasibility     : who ranks in the SERP sample + current DICEUS position
#   Priority score      = 0.45*Relevance + 0.35*Feasibility + 0.20*Demand
#   Demand is weighted lowest on purpose: it is the weakest-evidenced input, and in a niche B2B market
#   one closed captive-manager deal outweighs thousands of informational visits.
# ------------------------------------------------------------------------------------------------
TERRITORIES = [
    # id, territory, layer, relevance, demand, feasibility, current DICEUS visibility (FACT, SERP proxy), evidence, play
    ("T01", "Captive insurance / captive management software", "L1 Product (Alt Risk)", 5, 3, 5,
     "diceus.com #1 + #3 'captive insurance software'; directory-only for 'captive management software'; 'captive insurance management system' = Marsh/Aon/Origami. AI panel: DICEUS named 1st on multi-captive prompt.",
     "37 autocomplete queries across 2 clusters; VCIA partnership Jun-2026; product pages + Capterra/Gartner listings exist. Main page is NOINDEXED (FACT).",
     "Defend & expand: fix noindex, split 'captive insurance software' (owners) vs 'captive management software' (managers), add proof"),
    ("T02", "Risk retention group (RRG) software", "L1 Product (Alt Risk)", 5, 2, 5,
     "diceus.com #1 (only software page in SERP). AI panel: DICEUS named 1st on RRG prompt.",
     "~262 US RRGs, ~$5B premium (Captive International 2026). RRG page is NOINDEXED (FACT).",
     "Defend: fix noindex, add RRG-specific proof, compliance (NAIC/LRRA) content"),
    ("T03", "Self-insurance / pools / TPA administration", "L1/L2 Product+Solution (Alt Risk)", 4, 2, 4,
     "Absent. SERP = thin directory pages (FitGap), Riskonnect blog, old PDFs (FACT, proxy).",
     "Brief lists self-insurance as Alt-Risk territory; AROP page already names self-insurance funds.",
     "CREATE segment page after product-capability validation"),
    ("T04", "MGA / program administrator software", "L2 Solution (segment)", 4, 3, 2,
     "Absent. Insly (4/9 results), Insurity, Vertafore, hx, BriteCore own 'for MGAs' pages (FACT, proxy).",
     "InsureMO partnership targets MGAs; PAS supports multi-entity. Competitors win with dedicated segment pages.",
     "CREATE 'for MGAs & program administrators' segment page; long-tail first"),
    ("T05", "Policy administration system (PAS)", "L1 Product (Core)", 5, 4, 2,
     "Head term: Oracle/Guidewire/guides; DICEUS only via GetApp listing (0 reviews). 'PAS for MGAs' absent.",
     "Most product-like asset (MS Marketplace, Gartner, Capterra). 54 autocomplete queries, mostly informational.",
     "Win long-tail ('PAS for captives / MGAs / RRGs', 'PAS modernization'), build reviews; head term = authority play, not 90-day target"),
    ("T06", "Claims management", "L1 Product (Core)", 4, 4, 1,
     "Absent. Listicles, G2, Gartner Peer Insights, TrustRadius dominate (FACT, proxy).",
     "No standalone claims PRODUCT page exists - only a services page (/insurance/claims-management-development/). Claims is a PAS module.",
     "VALIDATE product scope first; then product page + review-site inclusion rather than head-on ranking"),
    ("T07", "Underwriting workbench", "L1 Product (Core)", 4, 3, 2,
     "Directory listing only. hx, Appian, Insly, Decerto (blog) rank (FACT, proxy).",
     "3 UW pages (commercial / life / health) + AI positioning; InsureMO 'submission intake'.",
     "OPTIMIZE existing 3 pages; MGA-underwriting long-tail"),
    ("T08", "Reinsurance software", "L1 Product (Core)", 4, 3, 2,
     "Directory listings for 'reinsurance accounting software'; Sapiens dominant (FACT, proxy).",
     "Reinsurance Financial & Data Exchange Platform listed on GetApp/Gartner (0 reviews).",
     "Long-tail: reinsurance data exchange, bordereaux, captive reinsurance; reviews"),
    ("T09", "Group insurance administration", "L1 Product (Core)", 4, 2, 3,
     "Absent; SERP = directories + FINEOS/Vitech (FACT, proxy). Group Health page NOINDEXED.",
     "Group platform listed on Gartner/GetApp; 3 URLs (parent, health, life&pensions).",
     "Fix noindex, OPTIMIZE parent page as owner of 'group insurance administration software'"),
    ("T10", "Broker & customer portals", "L1 Product (Distribution)", 3, 3, 4,
     "#2 + #3 'broker portal software insurance' (FACT, proxy). /insurance/portal/ vs /insurance/solutions/customer-portal/ overlap (title sim 0.76).",
     "Award: Global Insurtech Awards 2025 (Super App).",
     "OPTIMIZE + resolve portal overlap (VALIDATE)"),
    ("T11", "Insurance general ledger / accounting", "L1 Product (Finance)", 4, 3, 4,
     "#1 'insurance general ledger software' (FACT, proxy). 'insurance accounting software' SERP = agency accounting (intent mismatch).",
     "GL Platform page exists; multi-entity ledger is core captive-manager need.",
     "OPTIMIZE; tie into captive accounting cluster"),
    ("T12", "Insurance data warehouse & analytics", "L1 Product (Data)", 3, 3, 4,
     "#1-2 'insurance data warehouse' (FACT, proxy). 'insurance data model' = Salesforce Trailhead (off-intent).",
     "DWH product page + 2 analytics service pages.",
     "KEEP/OPTIMIZE; avoid 'data model' head term"),
    ("T13", "Legacy insurance system modernization", "L3 Service / bridge content", 3, 3, 3,
     "Absent; Hexaware, Cleveroad, guides rank (FACT, proxy).",
     "Bridges services -> products ('replace legacy PAS with DICEUS PAS'). White paper exists.",
     "MOFU content hub feeding PAS"),
    ("T14", "Insurance software development services", "L3 Service (insurance)", 2, 4, 2,
     "Absent; ~15 agencies + spam (FACT, proxy).",
     "Secondary business line per brief. 18 /insurance/<service>/ pages exist.",
     "KEEP & consolidate overlaps; not a growth bet"),
    ("T15", "Generic IT services (custom dev, outsourcing, staff aug, AI dev)", "L3 Service (generic)", 1, 5, 0,
     "DATA UNAVAILABLE (no GSC / rank data). Homepage + /services/custom-software-development/ both target 'custom software development company' (title sim 0.99).",
     "190 URLs (104 services, 30 expertise, 56 industry). Receive the MOST contextual internal links (median 93 vs 24 for products).",
     "VALIDATE BEFORE ACTION: keep, demote in nav, consolidate exact duplicates only after GSC"),
]


def territory_score(t):
    _, _, _, rel, dem, feas, *_ = t
    return round(0.45 * rel + 0.35 * feas + 0.20 * dem, 2)


# ------------------------------------------------------------------------------------------------
# 2. Opportunity backlog (03 + 05). type: FIX / OPTIMIZE / CREATE / CONSOLIDATE / AUTHORITY / GEO
# ------------------------------------------------------------------------------------------------
OPPORTUNITIES = [
    # id, opportunity, territory, funnel, target URL (existing or proposed), action, impact 1-5, effort 1-5, confidence, evidence
    ("O01", "Remove stray 'noindex, nofollow' from 3 product pages", "T01/T02/T09", "BOFU",
     "/insurance/solutions/captive-insurance/captive-management-platform/ ; /insurance/solutions/risk-retention-group-management-platform/ ; /insurance/solutions/group-insurance-management-platform/health/",
     "FIX", 5, 1, "High", "FACT: raw HTML has 2 robots metas, 2nd = noindex,nofollow; pages are in insurance-sitemap.xml; produced both unbranded AI-panel wins"),
    ("O02", "Alternative Risk hub: make AROP page the hub, link all alt-risk products + segments", "T01-T04", "BOFU/MOFU",
     "/insurance/solutions/alternative-risk-platform/", "REPOSITION/GROW", 5, 2, "High",
     "FACT: AROP = 24 contextual inlinks, no hub role; /insurance/solutions/captive-insurance/ has 0 contextual inlinks"),
    ("O03", "Split captive query ownership: 'captive insurance software' (captive owners/insurers) vs 'captive management software' (captive managers, multi-captive ops)", "T01", "BOFU",
     "/insurance/solutions/captive-insurance/captive-insurance-software/ vs /insurance/solutions/captive-insurance/captive-management-platform/",
     "OPTIMIZE (+VALIDATE)", 5, 2, "Medium", "FACT: both pages target captive software; one is #1, one is noindexed; SERP for 'captive management software' has no vendor page from DICEUS"),
    ("O04", "Homepage repositioning to insurance-software product company", "Brand", "Brand/BOFU",
     "/", "REPOSITION (staged, GSC-gated)", 5, 2, "Medium", "FACT: title/H1 'Custom software development company'; title similarity 0.99 with /services/custom-software-development/"),
    ("O05", "Internal-link re-weighting toward products (contextual links from 86 insurance posts + insurance services)", "All L1", "All",
     "86 insurance blog posts, 18 insurance service pages -> product pages", "OPTIMIZE", 4, 2, "High",
     "FACT: median contextual inlinks: products 24, insurance services 75, generic services 93"),
    ("O06", "Navigation: Products-first mega-menu; generic services collapsed under one 'Services' hub", "All", "All",
     "Global template", "REPOSITION", 4, 3, "Medium", "FACT: ~300 template links per page; generic services in primary nav; products sit beside 100+ services"),
    ("O07", "Captive-manager segment = the Captive Management page itself (NO separate segment page, to avoid self-cannibalization); page rebuilt per spec", "T01", "BOFU", "/insurance/solutions/captive-insurance/captive-management-platform/", "OPTIMIZE (spec)", 5, 2, "Medium",
     "SERP: buyer-specific pages win 'X for Y' queries (BriteCore, Insly, hx); captive-manager needs documented (bordereaux, cells, filings); a separate /for/captive-managers/ page would compete with the product page"),
    ("O08", "Segment page: Self-insured groups, pools & TPAs", "T03", "BOFU", "NEW /insurance/for/self-insured-groups-and-pools/", "CREATE (VALIDATE capability)", 4, 3, "Medium",
     "SERP: thin competition (FitGap, old PDFs); brief names self-insurance"),
    ("O09", "Segment page: MGAs & program administrators", "T04", "BOFU", "NEW /insurance/for/mgas-and-program-administrators/", "CREATE", 4, 3, "Medium",
     "SERP: competitors own 'for MGAs' pages; InsureMO deal targets MGAs"),
    ("O10", "Comparison content: 'Origami Risk alternatives for captive managers' / 'DICEUS vs Origami Risk'", "T01", "BOFU", "NEW /insurance/compare/origami-risk-alternatives/", "CREATE", 3, 2, "Medium",
     "AI panel #19: no comparison page exists anywhere; G2/listicles drive 'alternatives' prompts"),
    ("O11", "Long-tail PAS segment ownership: 'policy administration system for captives / MGAs / RRGs'", "T05", "BOFU", "/insurance/solutions/policy-administration-system/ (+ H2 sections, FAQs)", "OPTIMIZE", 4, 2, "Medium",
     "SERP: head term unwinnable (Oracle/Guidewire); segment variants weak"),
    ("O12", "Feature pages with search demand: bordereaux management, captive / cell accounting, statutory filing tracker", "T01/T11", "MOFU/BOFU", "NEW under AROP hub", "CREATE (VALIDATE demand)", 3, 3, "Low",
     "HYP: niche demand; autocomplete weak - validate with Ahrefs/GSC before building"),
    ("O13", "Product schema + FAQ + llms.txt expansion", "All L1", "All", "All 23 product pages + /llms.txt", "OPTIMIZE", 3, 1, "High",
     "FACT: 0/23 product pages have SoftwareApplication/Product schema; llms.txt lists only PAS"),
    ("O14", "Branded directory listings + US reviews (Capterra US, G2, Gartner PI)", "GEO/Authority", "BOFU", "Off-site", "AUTHORITY", 4, 3, "Medium",
     "AI panel: listings surface but lose the brand ('Captive Management Platform'); all 0 reviews; G2 drives 'best X' prompts"),
    ("O15", "Entity foundation: Wikidata item, Organization sameAs, consistent 'insurance software vendor' description", "GEO", "Brand", "Off-site + homepage schema", "AUTHORITY", 3, 1, "Medium",
     "AI panel #16: 'What is DICEUS?' answered with DICE/'Dicedus' homonyms; no Wikidata"),
    ("O16", "Analyst & trade-press inclusion (Celent VendorMatch, Datos, Captive Review, Captive International)", "GEO/Authority", "BOFU", "Off-site", "AUTHORITY", 4, 4, "Medium",
     "AI panel: analyst lists source 5/11 non-captive categories; captive press = no DICEUS coverage"),
    ("O17", "Consolidate exact-duplicate generic service pairs (after GSC)", "T15", "-", "mvp-development x2, vendor-portal x2, software-support x3, IT mgmt consulting x2, HIPAA x3", "CONSOLIDATE (VALIDATE)", 2, 2, "Medium",
     "FACT: title similarity 0.89-1.00"),
    ("O18", "Insurance services overlap: policy-administration vs policy-management; claims vs health-claims; portal vs customer-portal", "T05/T06/T10", "-", "/insurance/policy-administration/ + /insurance/policy-management/ etc.", "CONSOLIDATE (VALIDATE)", 3, 2, "Medium",
     "FACT: title similarity 0.59-0.77; both service pages target the same product territory"),
    ("O19", "Legacy URL redirect repair (Wayback inventory)", "Tech", "-", "see 02 / Legacy_Redirects", "FIX", 3, 1, "Medium", "FACT: see legacy redirect sheet (chains / 404s)"),
    ("O20", "Remove indexed staging host likeprod.diceus.com", "Tech", "-", "GSC removals + 401/noindex already", "FIX", 2, 1, "Medium", "FACT (search index, AI agent): likeprod URLs indexed; host returns 401"),
    ("O21", "Job posts published as blog posts -> careers section, expire with 410/noindex after close", "Tech/Content", "-", "~10 vacancy posts", "REPOSITION", 1, 1, "High", "FACT: vacancy URLs in post-sitemap"),
    ("O22", "Case-study filter archives (/case-studies/service|industry|expertise|country/) noindex,follow", "Tech", "-", "~128 thin archive URLs", "DEINDEX (VALIDATE)", 2, 1, "Medium",
     "FACT: ~220 words, templated; 106 not in sitemap. VALIDATE no organic entrances first"),
    ("O24", "Product-template LCP: Cookiebot consent text becomes the LCP element after ~10.5 s render delay (lab, mobile, 1 run)", "All L1", "-",
     "Product page template (/insurance/solutions/*)", "FIX (VALIDATE with CrUX/RUM)", 3, 2, "Low",
     "FACT (Lighthouse 12 local): captive page LCP 12.2 s vs 3.4 s generic service, 3.8 s home; LCP element = #CybotCookiebotDialogBodyContentText. HYP until field data"),
    ("O25", "Trust / security page (/trust/) linked from every product page", "All L1", "BOFU", "NEW /trust/", "CREATE", 4, 1, "High",
     "Teardown: Socotra /security/ (ISO 27001, SOC 1 T2), hx SOC 2 + ISO 27001 on homepage, Riskonnect Platform Security page (SOC 2 T2); DICEUS has none - RFP blocker for regulated captive data"),
    ("O26", "Pricing-MODEL page (/pricing/: subscription vs licence, price drivers, implementation range - no numbers)", "All L1", "BOFU", "NEW /pricing/", "CREATE", 4, 1, "High",
     "Teardown: Insly pricing tiers by segment (custom quotes, no figures), Luzern flat-rate model; AI panel #18 quoted DICEUS's $25-49/hr services rate as PAS price"),
    ("O27", "Buyer-enablement: Captive Management Software RFP template + RRG Platform Buyer's Guide (ungated HTML + PDF)", "T01/T02", "MOFU", "NEW under AROP hub", "CREATE", 3, 2, "Medium",
     "Teardown: Riskonnect PAS page offers buying guide + RFP template; no captive vendor publishes one; no authoritative 'best captive management software' guide exists (only directories / thin aggregator lists)"),
    ("O28", "2-3 alternative-risk case studies (anonymised if names blocked) + 1 named quote per alt-risk product page", "T01/T02", "BOFU", "/case-studies/ + product pages", "CREATE", 5, 3, "Medium",
     "Teardown: Luzern 4 anonymised testimonials + quantified cases (~$55M premium), Riskonnect named pool quote; DICEUS has no captive/RRG proof"),
    ("O23", "Insurance case studies mapped to products (proof blocks on product pages)", "All L1", "BOFU", "118 case studies -> product pages", "OPTIMIZE", 4, 2, "Medium",
     "FACT: captive page has no captive-specific proof (SERP agent fetch); competitors win with named proof"),
]

# ------------------------------------------------------------------------------------------------
# 3. Transition mapping (04 + 02). One row per material page / page group.
# ------------------------------------------------------------------------------------------------
TRANSITION = [
    # group, current URL(s), current role, evidence, future role, action, priority, risk, dependency, validation required
    ("Homepage", "/", "Services brand page: 'Custom software development company' (title+H1)",
     "FACT title/H1; title sim 0.99 with /services/custom-software-development/; 298 contextual inlinks (top)",
     "Brand + insurance-software product company entry; owns 'DICEUS', 'insurance software company/vendor'",
     "REPOSITION (2-step)", "P1", "High: may currently rank/convert for 'custom software development company'",
     "GSC query export; leads by landing page (CRM)", "GSC: queries & clicks to '/' last 16 months; if generic-dev queries > X% of non-brand clicks, move them to /services/custom-software-development/ FIRST, then retitle '/'"),
    ("Products hub", "/insurance/solutions/", "'Ready-made Insurance Software Products' catalog, 951 words",
     "FACT 107 contextual inlinks; no product schema", "L1 Products hub: owns 'insurance software products/platform'", "KEEP URL + GROW", "P1", "Low",
     "Nav redesign", "None for URL; measure clicks/impressions after content expansion"),
    ("Insurance hub", "/insurance/", "Mixed: 'Insurance Software Development and Ready-Made Solutions'",
     "FACT 191 contextual inlinks; mixes services and products -> overlaps homepage & products hub",
     "Insurance technology SERVICES hub (implementation, modernization, integration, data, QA, support)",
     "REPOSITION", "P2", "Medium: strong internal authority; queries unknown", "Homepage repositioning", "GSC: which queries '/insurance/' gets; keep any product-intent queries routed to /insurance/solutions/"),
    ("Alt-risk hub", "/insurance/solutions/alternative-risk-platform/", "New (2026) AROP product page",
     "FACT #1 'alternative risk management software' (ambiguous intent); 24 contextual inlinks", "Alternative Risk HUB: links captive, RRG, self-insured, MGA/program segments + features",
     "GROW", "P1", "Low", "Product marketing input", "Track impressions for alt-risk cluster in GSC"),
    ("Captive mgmt platform", "/insurance/solutions/captive-insurance/captive-management-platform/", "Product page, NOINDEXED",
     "FACT 2nd robots meta = noindex,nofollow; in sitemap; won AI prompt #2", "Owner of 'captive management software' (captive MANAGERS, multi-captive ops)",
     "FIX + OPTIMIZE (page spec, Appendix A)", "P0", "Low (restoring)", "Dev access to template", "URL Inspection after fix; confirm indexed within 14 days"),
    ("Captive insurance software", "/insurance/solutions/captive-insurance/captive-insurance-software/", "Product page; #1 'captive insurance software'",
     "FACT #1 + #3 in SERP sample; 27 contextual inlinks", "Owner of 'captive insurance software' (captive OWNERS / insurers: policy, billing, claims)",
     "KEEP + OPTIMIZE", "P1", "Medium: current #1 - avoid changing title/URL abruptly", "Query split with O03", "GSC: confirm the two captive URLs don't swap rankings after split"),
    ("Captive parent", "/insurance/solutions/captive-insurance/", "'Captive Insurance Company: Examples, Benefits, and Software' (informational, 964 words)",
     "FACT 0 contextual inlinks (weakest product-tree page); mixed intent", "Captive insurance knowledge hub (TOFU/MOFU) feeding 3 captive products",
     "VALIDATE BEFORE ACTION -> REPOSITION", "P2", "Medium: may rank for informational captive queries", "GSC", "GSC queries; if informational, keep URL and become knowledge hub; else merge into AROP hub (301)"),
    ("Captive owner portal", "/insurance/solutions/captive-insurance/captive-owner-portal/", "Product page",
     "FACT 'captive owner portal' SERP = Wi-Fi captive portals (off-intent)", "Child product; target 'captive owner reporting portal' variants",
     "OPTIMIZE", "P2", "Low", "-", "Track branded + long-tail"),
    ("RRG platform", "/insurance/solutions/risk-retention-group-management-platform/", "Product page, NOINDEXED",
     "FACT noindex,nofollow 2nd meta; #1 in SERP sample; won AI prompt #3", "Owner of 'risk retention group software'", "FIX + OPTIMIZE", "P0", "Low", "Dev", "URL Inspection; index within 14 days"),
    ("Core products", "PAS, UW (3), Reinsurance, Group (3), GL, DWH, Broker portal, Customer portal, Super app (4), Chatbot",
     "Product pages (23 total)", "FACT 0/23 with product schema; median 24 contextual inlinks", "L1 product pages, one URL per product, each owning one query cluster",
     "KEEP + OPTIMIZE", "P1", "Low", "Product data (features, integrations, proof)", "Per-page GSC baseline before edits"),
    ("Group health", "/insurance/solutions/group-insurance-management-platform/health/", "Product sub-page, NOINDEXED",
     "FACT noindex,nofollow", "Child of group platform", "FIX (or intentionally noindex + remove from sitemap)", "P0", "Low", "Confirm with product team if noindex intended", "Ask owner; then fix"),
    ("Claims product (gap)", "(none) - only /insurance/claims-management-development/ (service)", "Gap",
     "FACT no claims product page; brief lists Claims as product territory", "L1 Claims Management product page", "VALIDATE BEFORE ACTION -> CREATE", "P2",
     "Medium: creating a 'product' page for a module could mislead buyers", "Product team: is claims sold standalone?", "Product confirmation + demand check (Ahrefs/GSC)"),
    ("Segment pages (gap)", "(none)", "Gap",
     "SERP: segment pages win 'for MGAs' etc.", "L2 Solutions by buyer: self-insured & pools, MGAs/program admins, P&C carriers, L&H insurers (captive managers, RRGs, brokers are served by their product pages)",
     "CREATE", "P1 (alt-risk) / P2 (others)", "Low", "Messaging per ICP", "Indexed + ranking top-20 for target cluster within 90 days"),
    ("Insurance services", "/insurance/<service>/ (18 pages)", "Insurance software DEVELOPMENT services ('Custom ... Software Development')",
     "FACT median 75 contextual inlinks (3x products); overlap pairs (policy-admin vs policy-mgmt 0.59, claims vs health-claims 0.77, portal vs customer-portal 0.76)",
     "L3 services around products (implementation, customization, integration, migration)", "KEEP + OPTIMIZE; overlaps = VALIDATE -> CONSOLIDATE",
     "P2", "Medium", "GSC per-URL", "GSC: query overlap per pair; consolidate only where both URLs rank for same queries"),
    ("Generic services", "/services/* (104)", "Generic outsourcing services", "FACT 104 URLs; median 93 contextual inlinks; no evidence of traffic (DATA UNAVAILABLE)",
     "L3 'Technology services' - secondary, out of primary product nav", "KEEP (demote) / VALIDATE BEFORE ACTION", "P3", "High if pruned blindly: may be the current lead engine",
     "GSC + GA4 + CRM", "Traffic + leads per URL (12 months); prune only URLs with 0 clicks, 0 links, 0 leads"),
    ("Generic service duplicates", "mvp-development(-services), vendor-portal-(software|development), software-support x3, it-(service-)management-consulting",
     "Exact/near-exact duplicates", "FACT title similarity 0.89-1.00", "One URL per intent", "CONSOLIDATE (301) after validation", "P3", "Medium",
     "GSC + backlinks", "Pick survivor by clicks + referring domains"),
    ("Expertise", "/expertise/* (30)", "Tech-capability services (AI, BI, cloud, data)", "FACT AI cluster has 6+ overlapping pages (generative AI consulting vs development 0.68)",
     "L3 services; AI pages re-angled to 'AI for insurance' where possible", "KEEP / VALIDATE", "P3", "Medium", "GSC", "Per-URL clicks"),
    ("Non-insurance industries", "/industry/* (56: banking, finance, healthcare, retail, logistics, construction)", "Vertical services",
     "FACT 56 URLs, no insurance relevance", "Secondary; out of primary nav", "KEEP (demote) / VALIDATE BEFORE ACTION", "P3", "High if removed: unknown traffic/leads",
     "GSC + CRM", "Same rule as generic services"),
    ("Insurance blog", "86 insurance-relevant posts (root-level URLs)", "Authority content, weakly linked to products",
     "FACT 86/219 posts insurance-relevant; median 7 contextual inlinks per post", "L4 authority clusters linked to product hubs (hub-and-spoke by territory)",
     "KEEP + OPTIMIZE (links, refresh)", "P1", "Low", "Topic->product map", "Contextual links added; GSC impressions trend"),
    ("Generic blog", "~133 non-insurance posts", "Generic dev/outsourcing content", "FACT 133 posts; median 3,000 words",
     "Supports services; not product authority", "KEEP / VALIDATE (prune later)", "LATER", "Medium", "GSC", "Prune only 0-click, 0-link posts after 12-month review"),
    ("Vacancy posts", "~10 job posts in post-sitemap", "Careers", "FACT", "Careers section; expire properly", "REPOSITION / 410 when closed", "P3", "Low", "-", "-"),
    ("Case studies", "/case-studies/* (118)", "Proof", "FACT 118 cases; few US/alt-risk", "Proof layer linked from product pages by product/segment", "KEEP + OPTIMIZE", "P2", "Low", "Case->product tagging", "-"),
    ("Case filter archives", "/case-studies/(service|industry|expertise|country)/... (~128)", "Thin templated archives", "FACT ~220 words; 106 not in sitemap; 6 country archives have zero inlinks",
     "Utility navigation", "DEINDEX (noindex,follow) - VALIDATE first", "LATER", "Low", "GSC", "Confirm zero organic entrances"),
    ("Media / news", "/media/* (97)", "Company news", "FACT VCIA, MS Marketplace, InsureMO news = entity evidence", "PR/entity proof; link from relevant products", "KEEP", "P3", "Low", "-", "-"),
    ("Legacy URLs", "Wayback-only URLs (785 historical paths not in sitemap)", "Past migrations (/industry/insurance/* -> /insurance/*, vitaminise rename)",
     "See 02/Legacy_Redirects", "301 to closest live equivalent", "REDIRECT (fix chains/404 with equity)", "P2", "Low", "Backlink data", "Check referring domains (Ahrefs/GSC links) before choosing targets"),
    ("Danish /da/", "/da/ (4 pages)", "Localized stubs", "FACT 4 pages; hreflang only x-default", "Nordic market support", "VALIDATE BEFORE ACTION", "LATER", "Low", "Nordic marketing", "Decide DA strategy; add reciprocal hreflang if kept"),
]

# ------------------------------------------------------------------------------------------------
# 4. 90-day plan (05)
# ------------------------------------------------------------------------------------------------
PLAN = [
    # id, workstream, task, wave(days), class, owner, depends on, definition of done
    ("W1-01", "Measurement", "Get GSC (domain property), GA4, CRM landing-page lead export; snapshot 16-month baselines per URL & query", "1-7", "MUST DO", "SEO lead + Marketing ops", "-", "Baseline sheet per URL: clicks, impressions, avg pos, leads; stored in BigQuery/Sheets"),
    ("W1-02", "Technical", "Remove stray noindex,nofollow on 3 product pages; re-submit sitemap; URL Inspection", "1-5", "MUST DO", "WP developer", "-", "Raw HTML shows only 1 robots meta, no noindex; GSC 'URL is on Google' for all 3"),
    ("W1-03", "Technical", "Template audit: find source of hard-coded robots meta (theme/ACF field) and add CI check that fails deploy if a sitemap URL has noindex", "1-10", "MUST DO", "WP developer + SEO", "W1-02", "Automated check runs on every deploy; alert to Slack"),
    ("W1-04", "Technical", "Staging hygiene: likeprod.diceus.com removals in GSC, X-Robots-Tag noindex on all non-prod hosts", "1-10", "MUST DO", "DevOps", "W1-01", "0 staging URLs in site: search; GSC removal approved"),
    ("W1-05", "Technical", "Legacy redirects: fix 404s/chains from Wayback inventory that have backlinks", "10-30", "MUST DO", "SEO + developer", "W1-01 (links data)", "All legacy URLs with >=1 referring domain resolve in 1 hop to a relevant 200"),
    ("W1-06", "Architecture", "Decision workshop: product catalogue truth table (which products are sellable SKUs, which are modules/accelerators)", "5-15", "MUST DO", "CEO/Product + SEO", "-", "Signed-off list; drives which pages are 'product' vs 'capability'"),
    ("W1-07", "Architecture", "Query-ownership map v1: one owner URL per cluster (from 03 clusters + GSC)", "10-25", "MUST DO", "SEO lead", "W1-01, W1-06", "Every priority cluster has exactly one owner URL; conflicts listed"),
    ("W1-08", "Content", "Captive Management Platform page rebuild per spec (Appendix A of 04)", "10-30", "MUST DO", "Product marketer + SEO + designer", "W1-02, W1-06", "Spec acceptance criteria all met"),
    ("W1-09", "AI Search", "Prompt panel v2: 40 prompts x 3 runs x (Claude, ChatGPT, Perplexity, Google AI Overviews/AI Mode) baseline", "5-20", "MUST DO", "SEO/AI automation", "-", "Baseline SoV table + cited-source list stored; rerunnable script"),
    ("W1-10", "AI Search", "Schema: Organization (sameAs, description as insurance software vendor), SoftwareApplication on product pages, FAQPage where visible FAQ exists; expand llms.txt", "10-30", "MUST DO", "Developer + SEO", "W1-06", "Rich Results Test passes on all product templates; llms.txt lists every product .md"),
    ("W1-12", "Technical", "Product-template performance: confirm with CrUX/RUM; load consent banner without delaying LCP (preload/inline CSS, async config); collapse http://www 2-hop redirect to 1 hop", "10-30", "HIGH-VALUE NEXT", "WP developer", "W1-01", "Mobile LCP < 2.5 s (p75 field, or lab median of 3) on product template; http://www -> https://diceus.com in 1 hop"),
    ("W1-13", "Proof", "Alt-risk proof sprint: secure 1-3 captive/RRG/MGA references; write 2-3 case studies (anonymised fallback)", "5-45", "MUST DO", "CEO/Sales + writer", "-", ">=2 alt-risk case studies live and linked from captive/RRG pages"),
    ("W2-11", "Content", "/trust/ (security, hosting, data ownership, cert status) and /pricing/ (model, drivers, implementation range) pages", "31-50", "MUST DO", "Product + SEO + legal", "W1-06", "Both live, linked from all product pages; claims verified by legal"),
    ("W2-12", "Content", "Captive Management Software RFP template + RRG Buyer's Guide (ungated HTML + PDF)", "40-60", "HIGH-VALUE NEXT", "Product marketer + SME", "W1-06", "Both live under AROP hub; pitched to VCIA / captive trade media"),
    ("W1-11", "Authority", "Rename directory listings to 'DICEUS <Product>'; claim/complete US Capterra, G2, Gartner PI; start review program with existing clients", "5-30", "MUST DO", "Marketing", "-", "All listings branded; review requests sent to >=15 clients"),
    ("W2-01", "Architecture", "Homepage step 1: strengthen /services/custom-software-development/ as owner of generic dev queries (title, internal links from services hub)", "31-40", "MUST DO", "SEO", "W1-01 (GSC gate)", "Owner page live; internal links updated"),
    ("W2-02", "Architecture", "Homepage step 2: new title/H1/hero/sections per 04 §4.4 (products-first), keep a services strip", "40-50", "MUST DO", "SEO + design + dev", "W2-01", "Live; GSC monitored daily for 14 days; rollback plan documented"),
    ("W2-03", "Architecture", "Navigation v2: Products | Alternative Risk | Solutions by segment | Services | Resources; generic services collapsed under Services hub", "31-55", "MUST DO", "UX + dev + SEO", "W1-06, W1-07", "Template links per page reduced from ~300 to <=120; products in first menu column"),
    ("W2-04", "Content", "Alternative Risk hub (AROP) expansion + segment page Self-insured groups & pools (captive managers -> captive mgmt page; RRGs -> RRG product page)", "31-60", "MUST DO", "Product marketer + writer + SEO", "W1-06, W1-08", "Hub + new segment page live, hub<->spoke links to all 6 alt-risk pages, each with proof block"),
    ("W2-05", "Internal links", "Contextual links: 86 insurance posts + 18 insurance services -> owner product pages (scripted suggestions, human approval)", "31-50", "MUST DO", "SEO + editor", "W1-07", "Median contextual inlinks to products >= 60 (from 24)"),
    ("W2-06", "Content", "Comparison page: Origami Risk alternatives for captive managers (fact-checked, fair)", "45-60", "HIGH-VALUE NEXT", "Writer + product", "W1-06", "Live, legal-reviewed, cites public sources"),
    ("W2-07", "Content", "PAS page: segment H2s + FAQs for captives/MGAs/RRGs; modernization guide links", "40-60", "HIGH-VALUE NEXT", "SEO + writer", "W1-07", "Page owns 'PAS for MGAs/captives' variants; FAQ schema valid"),
    ("W2-08", "Authority", "Trade press: pitch VCIA case/insight piece to Captive Review / Captive International / Carrier Management", "31-60", "HIGH-VALUE NEXT", "PR/CEO", "Named customer (if available)", ">=1 earned article with link to alt-risk hub"),
    ("W2-09", "AI Search", "Entity: Wikidata item (notability-safe, factual), consistent descriptions across Clutch/Crunchbase/LinkedIn as 'insurance software vendor + services'", "31-45", "HIGH-VALUE NEXT", "Marketing + SEO", "-", "Wikidata item live with refs; profiles updated"),
    ("W2-10", "Automation", "Weekly pipeline: crawl diff + GSC pull + rank/AI-panel rerun + anomaly alerts (see 06 §L)", "31-60", "HIGH-VALUE NEXT", "SEO automation", "W1-01, W1-09", "Runs unattended weekly; Slack digest"),
    ("W3-01", "Content", "Segment page: MGAs & program administrators", "61-80", "HIGH-VALUE NEXT", "Writer + SEO", "W1-06", "Live + linked from PAS/UW/AROP"),
    ("W3-02", "Architecture", "Insurance services overlap consolidation (policy-admin/policy-mgmt, claims/health-claims, portal/customer-portal) - only pairs proven to cannibalize in GSC", "61-80", "LATER / VALIDATE FIRST", "SEO + dev", "W1-01, W1-07", "301s live, 0 chains, survivor gained impressions within 6 weeks"),
    ("W3-03", "Architecture", "Generic services: consolidate exact duplicates proven by GSC; leave rest", "65-85", "LATER / VALIDATE FIRST", "SEO + dev", "W1-01", "Only zero-value or duplicate URLs touched; change log kept"),
    ("W3-04", "Content", "Claims Management product page (only if W1-06 confirms standalone product)", "61-90", "LATER / VALIDATE FIRST", "Product marketer", "W1-06", "Live or explicitly declined"),
    ("W3-05", "Content", "Feature pages: bordereaux management, captive/cell accounting, statutory filing tracker (only clusters with validated demand)", "61-90", "LATER / VALIDATE FIRST", "Writer + SEO", "Ahrefs/GSC demand check", "Built only where demand confirmed"),
    ("W3-06", "Technical", "Case-study filter archives -> noindex,follow (if 0 organic entrances)", "61-75", "LATER / VALIDATE FIRST", "Developer", "W1-01", "Archives noindexed; sitemap cleaned"),
    ("W3-07", "Measurement", "Day-90 review: impressions/clicks per cluster, product-page leads, AI SoV vs baseline; re-prioritize", "85-90", "MUST DO", "SEO lead", "All", "Review deck + updated backlog"),
]

TOP5 = [
    ("1. Restore indexation of the alternative-risk product pages (and add a guardrail so it can't recur)",
     "FACT: 3 sitemap URLs carry a 2nd hard-coded <meta robots='noindex, nofollow'> (verified in raw HTML on 2026-10-06). Two of them (Captive Management Platform, RRG Platform) are the pages that won 100% of DICEUS's unbranded AI-answer mentions and hold #1 for 'risk retention group software' in our SERP sample.",
     "Protects the only territory where DICEUS already wins; prevents silent de-indexing of the strategic growth line.",
     "Zero-cost, zero-risk fix with asymmetric upside. Done first because every other alt-risk investment depends on these pages being indexable.",
     "Dependency: WordPress template/ACF access. Risk: the noindex may be intentional (e.g. unreleased page) -> confirm with product owner in 24h."),
    ("2. Make Alternative Risk the first fully built product cluster (hub + segment pages + proof)",
     "FACT: diceus.com #1 for 'captive insurance software', 'risk retention group software', 'alternative risk management software' (SERP proxy); competing SERPs are thin; VCIA partnership (Jun 2026); 262 US RRGs / 40 US captive domiciles. INF: most winnable commercial territory.",
     "Highest ratio of commercial value to SEO difficulty; aligned with the strategic growth bet.",
     "Feasibility 5/5 and relevance 5/5 - the only territory scoring top on both.",
     "Dependency: product truth table (what is sellable) + at least one referenceable customer. Risk: niche demand volume is unverified (DATA UNAVAILABLE)."),
    ("3. Reposition the Homepage from 'custom software development company' to an insurance-software product company - in two GSC-gated steps",
     "FACT: homepage title/H1 = 'Custom software development company'; title-similarity 0.99 with /services/custom-software-development/; brand SERP surfaces services pages; AI answer quoted '$25-49/hr' as PAS pricing.",
     "Aligns the site's strongest page and the entity description with the product strategy; resolves homepage cannibalization.",
     "The homepage is the main input to how search engines and LLMs classify DICEUS.",
     "Risk: HIGH if the homepage currently drives generic-dev leads. Mitigation: move generic intent to the services owner page first; monitor 14 days; rollback ready."),
    ("4. Re-weight internal architecture toward Products (nav + contextual links), without changing URLs",
     "FACT: median contextual inlinks - products 24, insurance services 75, generic services 93; ~300 template links on every page; 190 generic service/industry/expertise URLs vs 23 product URLs.",
     "Products become the strongest-linked commercial pages; clearer hierarchy for crawlers and LLMs.",
     "Achieves the architecture change with near-zero equity risk: hierarchy via links and hubs, not URL migration.",
     "Dependency: query-ownership map + nav design. Risk: demoting generic services could reduce their rankings -> monitor per-URL via GSC."),
    ("5. Build entity & third-party proof for AI search (branded listings, reviews, schema, Wikidata, analyst/trade inclusion)",
     "FACT: 'What is DICEUS?' resolved to homonyms; 0 reviews on all product listings; listings surface without the brand; analyst lists/G2 source most category answers; 0/23 product pages have product schema; llms.txt lists 1 product.",
     "Moves DICEUS from 2/16 to a measurable share of unbranded AI answers in priority categories.",
     "AI answers are assembled from third-party sources DICEUS doesn't control - on-site work alone can't fix it.",
     "Dependency: client cooperation for reviews. Risk: measurement noise (LLM non-determinism) -> 3 runs/prompt, track trends not points."),
]

NOT_YET = [
    ("Prune / noindex / redirect the ~190 generic service, expertise and non-insurance industry pages",
     "Their organic clicks, rankings, backlinks and lead contribution (DATA UNAVAILABLE: no GSC, GA4, CRM).",
     "They may be today's main lead engine; services are 'commercially useful and real'. Blind pruning could destroy revenue and link equity.",
     "12-16 months GSC clicks/impressions per URL, GA4 conversions, CRM lead source by landing page, referring domains per URL."),
    ("Migrate product URLs to a new /products/ folder (or rename /insurance/solutions/)",
     "Backlinks and directory/marketplace links per product URL; whether the folder name has any measurable ranking effect.",
     "URL migration resets signals and risks equity loss (the site already shows legacy-migration debris); the hierarchy goal is achievable via nav, hubs and links.",
     "Referring-domain data per URL (Ahrefs/GSC links), GSC performance baseline; evidence that the current path hurts CTR or understanding."),
    ("Merge the two captive product pages (captive-insurance-software vs captive-management-platform) or the overlapping insurance-service pairs",
     "Which URL Google prefers per query, whether both rank for the same queries, and whether they are distinct SKUs.",
     "One of them is currently #1; consolidating the wrong way could lose the best position in the strategic niche.",
     "GSC query-by-page report (cannibalization check), product team confirmation of SKU boundaries, 4-6 weeks of post-split data."),
]


# ------------------------------------------------------------------------------------------------
# 5. AI share of voice, recomputed from raw panel JSON (single source for chart + Excel).
#    Brand variants ('Guidewire ClaimCenter') are collapsed to the vendor. A brand is counted once per prompt.
# ------------------------------------------------------------------------------------------------
CANON_BRANDS = ["Guidewire", "Majesco", "Duck Creek", "Sapiens", "Insurity", "BriteCore", "AdvantageGo", "DICEUS", "Origami Risk",
                "Riskonnect", "FINEOS", "FIS", "OneShield", "StoneRiver", "Hexaware", "Vertafore", "Socotra", "EIS", "Insly"]


def norm_brand(b):
    for c in CANON_BRANDS:
        if b.lower().startswith(c.lower()):
            return c
    return b.split(" (")[0]


def ai_share_of_voice(path):
    import json
    from collections import Counter
    a = json.load(open(path, encoding="utf-8"))
    unb = [x for x in a if x["intent_type"] != "branded"]
    return Counter(b for x in unb for b in {norm_brand(y) for y in x["brands_named"]}), len(unb)
