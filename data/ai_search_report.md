# DICEUS: AI search / GEO visibility experiment (Claude + web search)

Run date: 2026-10-06 · Market: US English · Raw data: `ai_panel_results.json`

Labels: **[FACT]** = directly observed in search output, fetched pages or HTTP responses during this run. **[INFERENCE]** = my interpretation or recommendation.

---

## 1. Method

- **Engine tested:** Claude (Opus) using its built-in WebSearch tool (US-only index) and WebFetch. This measures how "Claude with web search" behaves: what it retrieves, which brands it names, and which URLs it cites.
- **Panel:** 20 prompts in three groups. 15 unbranded-category prompts, 1 unbranded-informational prompt (#15) and 4 branded prompts (#16–19). Each prompt was sent as a single standard-mode search, written the way an assistant would phrase it. I recorded the brands named in the synthesized answer, the cited URLs (classified by source type), and whether DICEUS was mentioned or cited.
- **Robustness checks:** I ran 6 extra variant queries: "captive management software", "RRG policy administration and claims software vendors", "fronting carrier program administration software", "DICEUS insurance software company", "DICEUS alternative risk platform" and "captive vendors Origami/Ventiv/Riskonnect". I also fetched the top listicles to check whether DICEUS appears in their body text.
- **Entity checks:** I used search and fetch on Wikipedia, Wikidata, Crunchbase, LinkedIn, G2, Capterra/GetApp/Software Advice, Clutch, GoodFirms, Gartner Peer Insights, TrustRadius, trade press and Reddit.
- **Technical checks:** I fetched robots.txt, llms.txt and product pages with curl, using browser, Googlebot, GPTBot, ClaudeBot, PerplexityBot and CCBot user-agents. I made no attempt to bypass any block.

## 2. Limitations (read before using numbers)

- **Single run per prompt.** LLM answers and search results are non-deterministic, and a re-run can change the brand lists. Treat counts as directional, not statistically significant.
- **Claude only.** ChatGPT (Bing-backed), Perplexity, Google AI Overviews/AI Mode, Gemini and Copilot were **not tested** and are marked **DATA UNAVAILABLE**. I found no reliable public third-party evidence of DICEUS visibility in those engines.
- Claude's search index differs from Google's. Pages that rank on Google may not appear here, and the reverse is also true. Evidence of this: noindexed DICEUS pages still surfaced (see §6).
- There is no personalization or location effect beyond the "US-only" search setting. No logged-in or authenticated sources were used. G2, Gartner and Crunchbase returned 403 to fetch, so their presence is inferred from search snippets.
- Some "brands named" come from irrelevant or noisy results (for example Qualtrics in #1, Creditsafe in #3). They are kept in the JSON for honesty but flagged in the notes.

## 3. Headline results

| Metric | Value |
|---|---|
| Prompts where DICEUS is named in the answer | **5 / 20** (#2, #3, #17, #18, #19) |
| Unbranded prompts where DICEUS is named | **2 / 16 (12.5%)**: #2 (multi-captive management), #3 (RRG software) |
| Unbranded prompts where DICEUS-owned listings surfaced but the brand was lost | 1 (#1: Capterra/GetApp listings titled generically "Captive Management Platform") |
| Non-captive product categories won (PAS, claims, UW, reinsurance, group, GL, DWH, custom dev, modernization) | **0 / 11** |
| Branded "What is DICEUS?" answered correctly | **No.** It was confused with DICE acronyms and a video game "Dicedus" |
| Branded prompts with any independent review evidence | **None.** Directory listings show 0 user reviews |

**[FACT]** DICEUS wins only where the category is very narrow and has almost no competing content: multi-captive management and risk retention groups. On #2 and #3 DICEUS was the first vendor named, and diceus.com was the top citation.
**[FACT]** In each broader category the answer is built from analyst vendor lists (Celent, Datos Insights/Aite-Novarica), G2/Capterra "alternatives" and category pages, and listicles. DICEUS is absent from all of these sources.

## 4. Share of voice: brand mentions across 16 unbranded prompts (#1–15, #20)

A brand is counted once per prompt if the synthesized answer names it.

| Rank | Brand | Prompts named (of 16) | Where |
|---|---|---|---|
| 1 | Guidewire | 8 | #1, 4, 5, 6, 7, 10, 13, 14 |
| 2 | Majesco | 7 | #1, 5, 6, 9, 10, 13, 14 |
| 3 | Duck Creek | 6 | #5, 6, 7, 10, 13, 14 |
| 3 | Sapiens | 6 | #1, 6, 10, 12, 13, 14 |
| 5 | Insurity | 5 | #1, 5, 6, 9, 13 |
| 6 | BriteCore | 3 | #4, 6, 7 |
| 6 | AdvantageGo | 3 | #9, 10, 13 |
| 8 | **DICEUS** | **2** | **#2, #3** (+1 unattributed listing in #1) |
| 8 | Origami Risk | 2 | #1, 6 (plus present in branded #19) |
| 8 | Riskonnect (incl. Ventiv) | 2 | #7, 8 (plus RRG variant) |
| 8 | FINEOS | 2 | #8, 11 |
| 8 | FIS | 2 | #10, 12 |
| 8 | OneShield | 2 | #1, 6 |
| 8 | StoneRiver | 2 | #10, 12 |
| 8 | Hexaware | 2 | #13, 15 |
| – | ~70 other brands | 1 each | e.g. Vertafore, Socotra, EIS, Snapsheet, Appian, Swiss Re, TAI, Sentro, Vitech, Luzern Risk, RaftLabs, ScienceSoft |

**Captive / alternative-risk subset (#1, 2, 3, 20 plus variant queries):** DICEUS is named in 2 of the 4 core prompts and in the RRG variant. Origami Risk is named in 1 of 4 (gitnux #2). Riskonnect/Ventiv appears in the RRG variant. Luzern Risk owns the "alternative risk platform / fronting" phrasing through fresh funding news. **[INFERENCE]** In the captive niche, DICEUS currently has share of voice comparable to or ahead of Origami Risk on Claude. That rests on DICEUS's own pages, not third-party validation, so it is fragile.

## 5. Most-cited domains (all 20 prompts plus variants)

| Domain group | Approx. citations | Source type | Role |
|---|---|---|---|
| capterra.* / getapp.* / softwareadvice.* (mostly non-US ccTLDs: .ca, .co.uk, .co.za, .com.au, .in, .nz, .ie) | ~30 URLs across 7 prompts | Software directories (Gartner Digital Markets) | Dominant in captive and branded prompts. Mostly **DICEUS's own** listings, all with 0 reviews |
| g2.com | ~12 | Review site (alternatives and category pages) | Drives #3–8. No DICEUS product listing with reviews surfaced (only a seller page, g2.com/sellers/diceus) |
| diceus.com | 9 | Vendor product pages and blog | Wins #2 and #3. Main source for branded prompts |
| datos-insights.com / aite-novarica.com / celent.com | ~11 | Analyst | Drives PAS/MGA, UW, reinsurance, GL and DWH vendor lists |
| guidewire.com | 7 (one release in 7 languages) | Vendor press release citing Celent award | #4 |
| insurance-canada.ca | 5 | Trade news covering analyst reports and customer wins | #10, 11, 13 |
| rfp.wiki, us.fitgap.com, sourceforge.net | ~9 | AI-generated comparison and directory sites | #5, 8, 9, 10, 11, 19 |
| gartner.com (Peer Insights) | 5 | Review platform | Branded prompts. DICEUS has product stubs there |
| Listicles (gitnux, whatfix, guideflow, geekflare, medium, dev.to, raftlabs, purrweb, relevant.software, stratoflow) | ~12 | Third-party and self-serving listicles | #1, 5, 6, 7, 14 |
| Trade news (beinsure, reinsurancene.ws, insurance-edge, coverager, dig-in, commercialriskonline) | ~8 | News | #20 (Luzern Risk funding), #11 (Sentro customer wins) |

**[FACT]** Listicles I fetched: gitnux "Top 10 captive insurance software" lists Sapiens, Origami Risk, Guidewire, Sovos, OneShield, Majesco, A1 Tracker, Insurity, InsCipher and Marsh, with **no DICEUS**. RaftLabs, Relevant Software and Stratoflow "insurance software development companies" lists also have **no DICEUS**.

## 6. Entity / brand presence

| Surface | Present? | How DICEUS is described | Evidence |
|---|---|---|---|
| Wikipedia | **No** [FACT] | n/a. Search returns only an unrelated album track | en.wikipedia.org search |
| Wikidata | **No** [FACT] | n/a. Results are a Latin hymn, "Dikaios Painter" and "Dicaeus" (myth) | wikidata.org search |
| Google Knowledge Panel | Not verifiable here | **[INFERENCE]** Unlikely to be strong without Wikidata. Check manually in an incognito US Google search | — |
| Crunchbase | Yes [FACT] (indexed URL crunchbase.com/organization/diceus; fetch returned 403) | Not readable | search result |
| LinkedIn company page | Not confirmed (no LinkedIn URL surfaced in search; not fetched, since login is required) | — | search |
| Clutch | **Yes, strong** [FACT] | 4.9/5, 49 reviews. Service lines: Cloud consulting & SI 40%, IT strategy 20%, BI 10%, custom dev 10%, low-code 10%, web dev 10%. HQ Wilmington DE plus 7 offices. Rate $25–49/hr, min $10k. **Framed as an IT services / outsourcing firm** | clutch.co/profile/diceus |
| GoodFirms | Yes [FACT] | 4.9, 26 reviews. "Top web development company in Wilmington". **Outsourcer framing** | goodfirms.co/company/diceus |
| Gartner Peer Insights | Yes, partial [FACT] | Product stubs: Policy Administration System, Captive Management Platform ("no reviews yet"), Reinsurance Financial & Data Exchange Platform ("no reviews yet"), Individual & Group Insurance Mgmt Platform, plus "Custom Software Development Services" (5.0). The diceus.com page shows "Gartner 5/5 (6 reviews)" | gartner.com/reviews/product/diceus-* |
| Capterra / GetApp / Software Advice | Yes, many listings, **0 reviews** [FACT] | Product vendor framing (Captive Management Platform, Captive Owner Portal, PAS, Individual & Group platform, Underwriting Workbench). Mostly surfaced on **non-US** ccTLDs. capterra.ca shows "Top-rated for Overall Quality … by 0 users" | capterra.ca/software/1096952 |
| G2 | Seller page only [FACT] (g2.com/sellers/diceus, g2.com/products/diceus/discuss) | No reviewed product surfaced | search |
| TrustRadius | Yes [FACT] | trustradius.com/products/diceus | search |
| Captive Review / Captive International | **No editorial coverage found** [FACT] | Only DICEUS's own news post about attending the Airmic Captives Forum | search |
| Insurance Journal / Carrier Management / Insurtech Insights | **No coverage found** [FACT] | — | search |
| Sponsored press | Yes [FACT] | bkreader.com "How DICEUS software products help insurance businesses" (sponsored) | search |
| YouTube | No demo surfaced [FACT] | — | search |
| Reddit | **None** [FACT] | Query returns the game "Dicedus" and dice subreddits | search |
| Staging subdomain | likeprod.diceus.com URLs are **still in the search index** [FACT] and now return 401 | Duplicate-content and hygiene issue | curl |

**[INFERENCE] Positioning split:** review and directory ecosystems with real reviews (Clutch, GoodFirms) describe DICEUS as a $25–49/hr software development outsourcer. Product directories describe it as a product vendor but carry no reviews. In #18 Claude mixed the two: it quoted "$25–49/hour development rate" as the PAS pricing.

## 7. Technical AI-crawler readiness

| Check | Result |
|---|---|
| robots.txt | [FACT] Single `User-agent: *` group with standard WordPress disallows. **No rules for GPTBot, ClaudeBot, PerplexityBot, Google-Extended or CCBot**, so all are allowed. Sitemap declared. |
| Bot access | [FACT] Product page returns HTTP 200 to GPTBot, ClaudeBot, PerplexityBot, CCBot and Googlebot UAs. No WAF blocking observed. |
| llms.txt | [FACT] **Exists** (200, text/plain) but is minimal: 7 lines, one link to `policy-administration-system.md`. That .md file exists (200) and is clean Markdown. Captive, RRG, alternative-risk, reinsurance and other products are not listed. |
| Server rendering | [FACT] Captive Management Platform page is server-rendered HTML (~258 KB). H1 "Captive Management Platform". 16 module descriptions (~3,500 words) are readable without JS. No FAQ, no customer names, no pricing. |
| Structured data | [FACT] Only Yoast-style `Organization`, `WebSite`, `WebPage`, `BreadcrumbList` and `ImageObject`. **No `SoftwareApplication`/`Product`, `FAQPage` or `Review`/`AggregateRating`** schema. |
| **Noindex on key pages** | **[FACT] CRITICAL:** 3 URLs listed in `insurance-sitemap.xml` carry a second, hard-coded `<meta name="robots" content="noindex, nofollow" />` alongside Yoast's `max-image-preview:large`: **/insurance/solutions/captive-insurance/captive-management-platform/**, **/insurance/solutions/risk-retention-group-management-platform/** and /insurance/solutions/group-insurance-management-platform/health/. These are the **exact pages that won unbranded prompts #2 and #3** in this test. |

**[INFERENCE]** Claude's index still returned these pages, probably because of index lag or a different index. Google and Bing honor noindex, so these pages are likely to drop out of Google, AI Overviews and Bing-grounded ChatGPT/Copilot. That puts the only unbranded AI wins at risk. Listing them in the sitemap while noindexing them is also a conflicting signal.

## 8. What drives inclusion (observed patterns)

1. **[FACT]** **Exact-match long-tail vendor content wins narrow niches.** DICEUS's blog "why captive managers are moving away from spreadsheets" and its RRG page won #2 and #3. Claimable and Riskonnect blogs won #8 the same way.
2. **[FACT]** **Analyst vendor lists win broad categories.** Celent VendorMatch and Datos/Aite-Novarica Market Navigators supply the lists for #5, 9, 10, 12 and 13.
3. **[FACT]** **G2/Capterra "alternatives" and category pages plus listicles** win the "best X" and "alternatives to Guidewire" prompts (#6, #7). Competitors seed self-authored listicles (Openkoda on dev.to; RaftLabs, Relevant and Stratoflow ranking themselves first).
4. **[FACT]** **Named customer-win news and marketplace listings** let small vendors win. Sentro (#11) won through Microsoft AppSource and coverager/insurance-canada; Hexaware (#13) through a case study; Luzern Risk (#20) through funding news.
5. **[FACT]** **Generic product names lose the brand.** "Captive Management Platform" listings surfaced in #1 without the DICEUS name being carried into the answer.

## 9. Evidence-based recommendations (prioritized)

All recommendations are **[INFERENCE]**, each tied to an observation above.

1. **Remove the stray `noindex, nofollow`** from the Captive Management Platform, RRG Management Platform and Group Health pages, or take them out of the sitemap if the noindex is intentional. These pages produced 100% of DICEUS's unbranded wins (§7). This is the highest-impact, lowest-effort fix.
2. **Rename directory listings to carry the brand**, for example "DICEUS Captive Management Platform" on Capterra, GetApp, Software Advice, Gartner and G2, and **collect real reviews**. All listings show 0 reviews and Gartner shows "no reviews yet". Prioritize US capterra.com and G2, since G2 drives #3–8. This addresses the brand loss in #1 and the "no independent reviews" answer in #17.
3. **Build an entity foundation:** create a Wikidata item (instance of: business; industry: insurance software; official website; founding 2011; HQ Wilmington, DE; products as separate items or "product or material produced"). Add `Organization` `sameAs` links to Clutch, Crunchbase, LinkedIn, G2 and Gartner. This targets the #16 failure, where the bare brand was disambiguated as DICE/"Dicedus".
4. **Add `SoftwareApplication` schema** (with `applicationCategory`, `offers`/pricing model, `aggregateRating` only where reviews are genuine) and **FAQPage** blocks to each product page. Expand **llms.txt** to list every product .md (captive, RRG, alternative risk, reinsurance, UW workbench life/health, GL, DWH, group).
5. **Get into analyst vendor lists.** Submit to Celent VendorMatch (MGA, reinsurance, captive categories) and Datos Insights Market Navigator briefings. Analyst lists source 5 of the 11 non-captive categories (§5).
6. **Publish comparison and alternatives content** that the panel showed is missing: "DICEUS vs Origami Risk for captive managers" (#19 found no comparison anywhere), "Origami Risk / Riskonnect alternatives for captive managers", and "RRG software options". Seed placements in third-party listicles that are already cited (gitnux captive list, G2 alternatives pages).
7. **Earn trade-press coverage with named customers.** Captive Review, Captive International, Carrier Management and coverager are the channels where Sentro and Luzern Risk won (#11, #20). Lead with a named US captive manager or RRG case study.
8. **Separate the product-vendor narrative from outsourcing.** Clutch and GoodFirms dominate third-party reviews with a "$25–49/hr dev shop" framing, which leaked into the PAS pricing answer (#18). Add a clear "Products" vs "Services" split on About and Organization schema, and give product pages their own pricing-model language.
9. **Hygiene:** get the stale `likeprod.diceus.com` staging URLs removed from search (it already returns 401; use Search Console removals) and keep staging from being indexed again.
10. **Re-measure:** rerun this 20-prompt panel monthly (≥3 runs per prompt) and add ChatGPT, Perplexity and Google AI Overviews, which are DATA UNAVAILABLE in this study.
