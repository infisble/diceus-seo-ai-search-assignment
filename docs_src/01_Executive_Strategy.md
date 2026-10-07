# 01 · Executive Strategy — DICEUS SEO & AI Search

*Prepared 2026-10-06 · Subject: https://diceus.com/ · Market: US, English · Evidence: public data only. GSC, GA4 and CRM are DATA UNAVAILABLE.*

## The situation in three sentences
DICEUS is becoming a product-led insurance software company, but diceus.com still reads as a custom-development agency to people, search engines and AI assistants. The one territory where DICEUS already wins organically and in AI answers is **captive insurance and risk retention groups**. The core pages for that territory are currently **excluded from Google by a stray `noindex` tag**. The fastest, lowest-risk path to growth is to fix that, build alternative risk out as the first complete product cluster, and re-weight the site toward products without a risky URL migration.

## Major findings

| # | Finding | Evidence |
|---|---|---|
| 1 | **3 product pages are noindexed** (Captive Management Platform, RRG Platform, Group Health). They sit in the XML sitemap, and a second hard-coded `noindex, nofollow` overrides Yoast | FACT: raw HTML, re-check of all 815 URLs |
| 2 | **The site's weight sits with the secondary business.** 23 product pages vs ~190 generic service, expertise and non-insurance industry pages. Products receive a median of **24** contextual internal links vs **93** for generic services. Every page carries ~300 mega-menu links | FACT: own crawl, 815 URLs |
| 3 | **The homepage targets the wrong query.** Title and H1: "Custom software development company", last modified 2022. It is 0.99-similar to `/services/custom-software-development/`, so the two compete for the same generic term | FACT: crawl + title-intent similarity |
| 4 | **Alternative risk is winnable now.** In our SERP sample diceus.com is **#1** for *captive insurance software* and *risk retention group software*. Competing SERPs are thin, and the VCIA partnership (Jun 2026) adds credibility | FACT (SERP proxy) + public news |
| 5 | **Core product head terms are not winnable in 90 days.** PAS, claims and underwriting heads are owned by Oracle, Guidewire, G2, Gartner and listicles; DICEUS appears only via 0-review directory listings | FACT (SERP proxy) |
| 6 | **AI assistants barely know DICEUS.** It is named in 2 of 16 unbranded prompts (captive and RRG only) and 0 of 11 broad categories. *"What is DICEUS?"* returned homonyms. There is no Wikidata entry, all product listings have 0 reviews, and an assistant quoted the $25–49/hr services rate as PAS pricing | FACT: Claude + web search panel (other engines DATA UNAVAILABLE) |
| 7 | **The technical base is mostly healthy**, with two product-specific gaps. Healthy: no errors, no duplicate titles or canonicals, server-rendered HTML, AI crawlers allowed, Cloudflare caching. Gaps: **0/23** product pages have product schema, and the **product template is slowest**: lab mobile LCP of 12.2 s on the captive page vs 3.4 s on a service page, because the cookie-consent text becomes the LCP element | FACT: crawl; Lighthouse (1 lab run; field data is DATA UNAVAILABLE, so the LCP cause is HYP) |

![Inventory vs strategy](assets/fig1_inventory_vs_strategy.png)

## Proposed direction
1. **Products first, URLs kept.** Express the Products > Solutions > Services > Content hierarchy through the homepage, navigation, hubs, internal links, titles and schema. Keep the existing URLs, which protects equity and the directory and marketplace links already pointing at them.
2. **Alternative risk is the first complete cluster.** The AROP page becomes the hub, with captive management, captive insurance, owner portal, RRG, self-insured and a comparison page under it. Then the same playbook goes to PAS and MGAs.
3. **Services stay, but secondary.** No pruning of generic services until GSC, GA4 and CRM show what they earn.
4. **AI search is treated as an entity and third-party-source problem**, not a page-tweaking exercise: branded listings, reviews, analyst and trade-press inclusion, Wikidata and schema, measured with a repeatable prompt panel.

![Opportunity matrix](assets/fig3_opportunity_matrix.png)

## Five priorities

{{top5}}

## Three things we will not do yet

{{notyet}}

## Major risks
- **Homepage repositioning could cut generic-development leads.** Mitigation: a two-step move, gated by GSC, with a rollback plan.
- **Captive and RRG demand is low-volume.** The upside rests on deal value, not traffic (volumes DATA UNAVAILABLE). Mitigation: measure demo requests, not sessions.
- **Proof gap.** No public named US captive, RRG or MGA customer exists. BOFU pages and PR depend on securing at least one reference.
- **AI visibility is noisy to measure.** Mitigation: 3 runs per prompt per engine, control prompts, and trend lines.

## Key unknowns
GSC performance per URL and query · leads by landing page · referring domains per URL · real search volumes · ChatGPT, Perplexity and AI Overviews visibility · which "products" are sellable SKUs. See `06 §J` for how each would change a decision.

## 90-day shape
- **Days 1–30:** fix indexation, baseline the data, decide the product truth table and query ownership, rebuild the captive page.
- **Days 31–60:** reposition the homepage and navigation, build the alternative-risk hub and segments, add internal links, start entity and reviews work.
- **Days 61–90:** run consolidations only where validated, add the MGA segment page, then hold a day-90 review.

Detail is in `05_90_Day_Execution_Plan.xlsx`.

![90-day plan](assets/fig7_90_day_gantt.png)
