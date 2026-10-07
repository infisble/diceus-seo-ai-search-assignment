# DICEUS Competitive Teardown: Alternative Risk and Mid-Market PAS

> **Fact-check (6 Oct 2026):** see `factcheck_external.md`. Corrections: Luzern testimonials are anonymised (titles only) and their cases are quantified; Riskonnect has a Platform Security page (SOC 2 T2), not a trust center; Riskonnect G2 = 35 reviews / 4.1; Insly pricing tiers carry no figures; Socotra Gartner MQ = Visionary 2021 (Life PAS NA).

Research date: 2026-10-06. Method: public homepages plus 1-2 key product/segment pages per competitor (no more than 3 fetches each), `/llms.txt` probes (1 request per domain), raw-HTML JSON-LD and security-keyword scans (curl), and WebSearch for review counts, analyst mentions and "best of" lists.
Labels: **FACT (URL)** means observed directly on that page or in a search snippet. **INFERENCE** means analyst judgment.

**Fetch notes**
- Socotra returned a 5 KB shell to curl (bot/JS challenge), so its schema could not be read. WebFetch on the homepage and /security/ worked.
- hyperexponential.com/solutions/mgas, britecore.com/mga and insly.com/mga-software all returned 404 (guessed paths). Segment content came from homepages and search snippets.
- instec.com belongs to an unrelated lab-equipment company. Instec (insurance) was not found under that domain and is not analyzed. Vertafore MGA Systems is covered instead.
- Insurium.com now redirects to Spear Technologies (merger, Feb 2023). It surfaced as an RRG/pool competitor.
- DICEUS: 2 fetches used (the Captive Management Platform page and /llms.txt).

---

## 1. Competitor matrix

### 1a. Alternative risk / captive

| | **Origami Risk** | **Riskonnect (+Ventiv)** | **Luzern Risk** | **Websure** | **Spear Tech (ex-Insurium)** | **DICEUS (baseline)** |
|---|---|---|---|---|---|---|
| H1 / tagline | "One platform for modern risk, insurance, and safety operations." FACT (origamirisk.com) | "The platform built for how organizations actually manage risk." FACT (riskonnect.com) | "Turn your company's risk into an asset." / "AI-native captive manager" FACT (luzernrisk.com) | "Enterprise software solutions for Insurance." FACT (websure.com) | "P&C insurance software solutions" FACT (insurium.com, redirect page) | "Custom software development company" (baseline) |
| Who it's for | Insurers, MGAs, program admins, risk pools, TPAs, captives, self-insured (search snippet, Capterra) | Corporate risk, GRC, BC. Captives, RRGs and pools come via Ventiv FACT (riskonnect.com/resources/ventiv-technology-acquisition-overview/) | Captive owners, prospects, brokers. Middle market | Brokers, insurers, captives, MGAs, risk managers, TPAs | Carriers, captives, public-entity pools, SIGs, TPAs (CB Insights snippet) | Captive managers, RRGs, MGAs, carriers. Hidden behind a services-first homepage |
| Nav model | Platform / Solutions / **Industries** / Resources / About | Solutions grouped by problem (GRC / Insurable Risk / Resilience) | Platform / Services / **Brokers / Captive Owners** (by audience) / Resources | Markets (6 segments) / Functionality | n/a | ~300-link mega-menu, services-dominant |
| Product page anatomy | Sell sheets per segment, e.g. Risk Pools PDF FACT (origamirisk.com/wp-content/uploads/2025/10/OrigamiRisk_SellSheet_Risk_Pools_20251111.pdf) | PAS page: value prop, 8 highlights, **named customer quote** (Municipal Assoc. of SC), compliance, **ebook + buying guide + RFP template**, cross-sell, **FAQ** FACT (riskonnect.com/insurable-risk/policy-administration-software/) | Platform page: hero, single source of truth, connected, live financials, modeling tools, analytics, service integration, broker tools, **FAQ**, with dashboard screenshots FACT (luzernrisk.com/platform) | ~250 words: features bullet list, no proof, no CTA FACT (websure.com/captives/) | n/a | ~2,200 words: 16 modules, 4 values, related products. Company-level Gartner/Clutch ratings; no named customer, FAQ, security or integrations FACT (diceus.com/.../captive-management-platform/) |
| Proof | 19 logos (Macy's, Gallagher, Aon...), **Gartner MQ x3, G2 Leader, Celent Luminary, "RMIS leader 8 yrs"** FACT. G2 4.6 from 12 reviews (snippet) | 7 logos, metrics (Wendy's -5% losses, -34% claims), Gartner, Redhand RMIS report, Forrester TEI. G2 4.2 from 34 reviews for RMIS (snippet); 2,500+ customers post-Ventiv | 4 named client testimonials with titles, quantified cases ($55M premium, $25M+ pool), $45M Series B (Insight Partners) | Accreditations only (Cyber Essentials Plus, ACORD, MGAA). No customers | NCHARRP RRG press release (businesswire 2022) | No captive customer, 0 product reviews |
| Content hub | Case studies, blog, webinars, Elevate conference, product updates | "Definitive Guides" (RMIS, ERM, GRC), Risk@Work webinars, ROI calculators, **Cayman Captive Forum** presence | **Captive FAQ, glossary, Model-a-Captive pro forma, premium profit calculator, loss simulator, domicile comparison** | News, Captive Review feature | — | Large blog, services-led |
| AI-readiness | No llms.txt (404). Schema: WebSite/WebPage/Article only | llms.txt (Yoast auto-generated, noisy, contains shortcode junk) | **Hand-written llms.txt with definitions, key facts, pricing model, formation timelines, domicile count. FAQPage schema** on home and platform | llms.txt (AIOSEO auto) | — | llms.txt lists PAS only. No Product/SoftwareApplication schema |
| Better than DICEUS | Analyst badges, logo wall, Trust Center | Buyer-enablement assets (RFP template, buying guide), FAQ, captive events | Owns the captive buyer's language: calculators, FAQ, explicit pricing model, LLM-ready facts | Clear segment nav | — | — |
| DICEUS better | Captive-specific depth (domicile, reinsurance, actuarial modules). Origami has no captive page on its homepage | Dedicated captive/RRG product pages. Riskonnect never mentions captives on its homepage | Sells software to *captive managers* (Luzern *is* a manager, so it competes with DICEUS's buyers) | Far deeper feature content | — | Ranks #1 for "captive insurance software" / "risk retention group software" |

### 1b. Mid-market PAS / MGA

| | **Insly** | **BriteCore** | **Socotra** | **hyperexponential** | **Vertafore MGA Systems** | **Decerto / Higson** | **Adacta AdInsure** |
|---|---|---|---|---|---|---|---|
| H1 / tagline | "Low-risk insurance software..." / "Pricing aligned to growth. Low upfront costs. Fast set-up." FACT (insly.com) | "The Modern Core Platform for P&C Insurers" FACT (britecore.com) | "The Most Advanced Insurance Core Platform. Period." FACT (socotra.com) | "The #1 pricing and underwriting platform for commercial P&C" FACT (hyperexponential.com) | "Insurance Policy Administration Software for MGAs" FACT (vertafore.com/products/mga-systems) | "Insurance Software Your Team Uses This Quarter, Not in Three Years" FACT (decerto.com) | "Modernise your life and non-life business with a single insurance platform" FACT (adacta-fintech.com) |
| Who for | MGAs / insurers / brokers | P&C carriers + MGAs, plus nav by role | Carriers, by line of business | Commercial P&C, reinsurers, MGAs | MGAs, MGUs, wholesalers, **program administrators** | US P&C carriers, MGAs, TPAs | EU P&C/life. No captive or MGA mention |
| Nav | AI Platform / Solutions / Resources / **Pricing** / About | Platform / Why BriteCore (role, type, driver) / Resources / Services | Solutions / Implementation / **Developers** / Company | Platform / Solutions by segment / Use cases / Resources / Security | Product family | **Products** (flagship + core) and **Services** split cleanly | Solutions / Platform / Services / Clients |
| Proof | 3 named MGA execs. Metrics: 48 h to first quote, 7-14 days live, 93% GWP growth | 6 logos, "100+ US clients". Capterra 4.3 from 3 reviews (snippet) | AXA, IAG, MS Amlin. 99.997% uptime, 11k policies/min. **Gartner MQ Visionary** | Markel, Aviva, Banyan. "$75bn+ premium priced". 5 exec quotes | "Award-winning" (vague) | 14 enterprise logos, Clutch 4.9, Everest PEAK | Generali, Signal Iduna. Celent, ISG, Gartner, Everest |
| Pricing | **Public pricing page**: MGA tier and insurer tier, monthly base + modules, **unlimited users** FACT (insly.com/pricing) | None. Ebook gate | None. "Lowest TCO" | None | None | None. "4-6 weeks to config on your data" | None |
| Security | Accounting accuracy claim only | None on homepage | **ISO 27001, SOC 1 Type 2, HIPAA, GDPR**, pen-tests FACT (socotra.com/security/) | **SOC 2 Type 2, ISO 27001:2022** + regulators (NAIC, Lloyd's) FACT (homepage) | "SOC2" string in HTML FACT | — | QMS/ISMS footer |
| Content | Case studies, ebooks, **glossary** | AI Resource Center, **ROI calculator**, glossary, webinars | Public **docs.socotra.com**, evaluation license | Learning hub, events | FAQ, webinar, blog | Blog, webinars, video library | Analyst reports |
| AI-readiness | No llms.txt | llms.txt is a robots-style stub (86 bytes) | llms.txt (Rank Math auto) | No llms.txt | **SoftwareApplication + FAQPage + Audience + Breadcrumb schema** | **Hand-written llms.txt** with product facts and metrics (decerto.com + higson.io) | None |
| Better than DICEUS | Transparent pricing model, time-to-live metrics | Role-based nav, ROI tool | Trust/security page, dev docs, quantified SLAs | Security badges up front, exec quotes | Best schema in the set | **Same services-to-product pivot done cleanly**: products separated from services in nav | Analyst coverage |
| DICEUS better | US alt-risk coverage. Insly has no captive/RRG | Captive/RRG products | Mid-market fit; Socotra is enterprise | Full PAS (hx is pricing/UW only) | Modern stack, broader alt-risk | Captive/RRG depth | US + alt-risk |

### 1c. List and review-site presence
- "best captive management software": no editorial list exists. SERPs show only Capterra/GetApp listings, all of them DICEUS's own (Capterra UK/ZA/AE, GetApp AU/CA) FACT (capterra.co.uk/software/1096952/Captive-Management-Platform). **INFERENCE:** the category is unclaimed, and whoever publishes the definitive list or guide will define it.
- "best MGA software 2026": lists from Stratoflow, Gitnux, Zipdo, Worldmetrics and Medium feature Duck Creek, Guidewire InsuranceNow and Sapiens FACT (stratoflow.com/best-insurance-mga-software/, gitnux.org/best/mga-insurance-software/). DICEUS does not appear in the snippets.
- "risk retention group software" SERP: DICEUS #1, then Insurium/Spear, Riskonnect (Ventiv) and Spear FACT (search). Celent has no captive-specific vendor report in the results; its PAS North America edition is the closest fit (celent.com/en/insights/policy-administration-systems-p-and-c-insurance-north-america-edition).

---

## 2. Why DICEUS loses: 11 ranked gaps

| # | Gap | Evidence (best-in-class) | Fix on diceus.com | Effort | Expected effect |
|---|---|---|---|---|---|
| 1 | **Identity mismatch**: homepage says "custom software development company", so buyers and LLMs classify DICEUS as an IT vendor | Decerto, which made the same pivot, uses an H1 about product outcomes and a nav with separate **Products** and **Services** (FACT decerto.com). Vertafore page title names the category and audience directly | Change the homepage H1/title to a product-category claim ("Insurance software for captives, RRGs, MGAs and specialty carriers"). Split the nav into Products / Solutions by segment / Services, and move the ~190 service pages under one /services/ hub | M | Entity reclassification in Google and LLMs. Higher conversion from product queries the site already ranks for |
| 2 | **Stray noindex on Captive Management Platform and RRG pages** | Ranking pages must be indexable (baseline) | Remove noindex, request re-indexing, and add to sitemap and llms.txt | S | Protects the #1 positions. **INFERENCE:** current rankings likely come from sibling pages; the money pages are excluded |
| 3 | **No named alt-risk customer or captive case study** | Luzern: 4 named client quotes with titles + quantified outcomes ($55M premium) (FACT luzernrisk.com). Riskonnect PAS: named pool quote (FACT riskonnect.com/insurable-risk/policy-administration-software/) | Publish 2-3 captive/RRG/MGA case studies (anonymized "a Vermont pure captive manager, 14 captives, 3 domiciles" if names are blocked), plus 1 named quote per product page | M-L | Largest single conversion lift. Gives LLMs a citable proof fact |
| 4 | **Proof is company-level, not product-level** (Gartner 5/5 from 6 reviews and Clutch 4.9 measure services) | Socotra/hx: product metrics (uptime, $75bn priced) and product analyst badges (FACT socotra.com, hyperexponential.com) | Get 10+ reviews on the Capterra/GetApp/G2 *product* listings (current customers + VCIA network). Show product metrics (go-live weeks, modules, domiciles supported) | M | Review-site listings already rank for "captive management platform". Reviews turn them into a second SERP asset |
| 5 | **No security/trust page** | Socotra /security/ (ISO 27001, SOC 1 T2, HIPAA) FACT. hx shows SOC 2 Type 2 + ISO 27001 on the homepage FACT. Origami Trust Center | Build /trust/ listing certifications held (or roadmap), hosting (Azure/AWS region), encryption, pen-test cadence, data ownership, and NAIC/state data-security model law alignment. Link it from every product page | S (page), L (if SOC 2 is not held) | Removes an RFP blocker. Captive managers handle regulated financial data |
| 6 | **No pricing-model information** | Insly /pricing: tiers by segment, monthly base + modules, unlimited users (FACT insly.com/pricing). Luzern: "one flat rate" (FACT luzernrisk.com/llms.txt) | Add a /pricing/ page with the model, not numbers: subscription vs license, what drives price (captives under management, modules, users), implementation range, "from X weeks" | S | Qualifies leads. Answers "how much does captive software cost" in LLMs |
| 7 | **No buyer-enablement assets** | Riskonnect PAS page: ebook + **buying guide + RFP template** (FACT). Luzern: captive model calculator, loss simulator (FACT luzernrisk.com/llms.txt) | Ship a "Captive Management Software RFP Template" and an "RRG Platform Buyer's Guide" (ungated HTML + PDF), plus 1 calculator (e.g. "captive admin hours saved" or a domicile filing calendar) | M | Links, mid-funnel captures, LLM citations |
| 8 | **Product pages lack FAQ, integrations, screenshots of real desktop UI, and video** | Vertafore MGA Systems: FAQ + webinar + related products (FACT). Luzern platform: dashboard screenshots + FAQ (FACT) | Standard template: hero with outcome, who it's for, 3-minute demo video, modules, integrations (GL/accounting, actuarial, reinsurance, ACORD), security, proof, pricing model, FAQ (FAQPage schema), CTA | M | Long-tail capture, People Also Ask, AI answers |
| 9 | **No SoftwareApplication/Product schema; llms.txt lists only PAS** | Vertafore: SoftwareApplication + FAQPage + Audience schema (FACT, curl). Luzern and Decerto: hand-written llms.txt with key facts (FACT luzernrisk.com/llms.txt, decerto.com/llms.txt) | Add SoftwareApplication (applicationCategory, audience, offers model, aggregateRating once reviews are real) to all 23 product pages. Rewrite llms.txt Luzern-style: product list, definitions, key facts (domiciles, go-live time, deployment), customers | S | LLM answer inclusion for "captive software" / "RRG software" |
| 10 | **Mega-menu dilution (~300 links/page)** | Luzern nav has about 8 links; Insly about 6 top items (FACT) | Product-first nav of 30-40 links. Move services to a hub. Add segment hubs (/captives/, /risk-retention-groups/, /self-insured/, /mga-program-administrators/) | M | Concentrates internal PageRank on 23 product pages |
| 11 | **Absent from "best MGA software" lists and from comparison content** | Third-party lists name Duck Creek, Guidewire, Sapiens (FACT stratoflow, gitnux). No competitor owns "X vs Y" or alternatives pages; CB Insights and rfp.wiki fill the gap (FACT) | Pitch list authors with a fact sheet. Publish an honest "Best captive management software (2026)" and "Origami Risk / Riskonnect alternatives for captives" (see 3e) | M | Captures comparison intent no vendor serves |

---

## 3. Best-practice patterns to copy

### 3a. Homepage formula
Copy **Luzern** (luzernrisk.com) for alt-risk and **Decerto** (decerto.com) for the pivot.
1. H1 = category + audience + outcome (Luzern: "Turn your company's risk into an asset"; Decerto: "...uses this quarter, not in three years").
2. Self-select by segment right after the hero (Luzern: explorers / owners / brokers). DICEUS version: Captive managers / RRGs / Self-insured and pools / MGAs and program admins / Specialty carriers.
3. Proof band: named outcomes, not just logos (Luzern: $55M premium. Insly: 48 h to first quote).
4. Products grid (23 products, grouped), then a single "Services" tile. Decerto keeps services in the menu but subordinate.
5. Interactive tool CTA plus "Book a demo" (Luzern "Model a Captive").
6. Resources, FAQ (with schema), newsletter.

### 3b. Product page formula
Composite of Riskonnect PAS (riskonnect.com/insurable-risk/policy-administration-software/), Luzern platform (luzernrisk.com/platform) and Vertafore MGA Systems (vertafore.com/products/mga-systems):
Hero (outcome + who for + demo CTA), then 3 outcome cards with numbers, then a product screenshot/video tour, then modules (DICEUS already does this well, so keep it), then integrations, then security/compliance strip linking /trust/, then a named customer quote + case study, then the pricing model + implementation timeline, then a downloadable buyer's guide/RFP template, then an FAQ (8-10 Qs, FAQPage schema), then related products (cut from 15+ cards to 3-4).

### 3c. Segment page formula
Origami organizes by Industries and publishes per-segment sell sheets (Risk Pools PDF). Luzern has /captive-owners and /broker pages. Websure has a Markets nav but thin pages, which is the anti-pattern.
For each segment (captive managers, RRGs, self-insured groups/pools, MGAs/program administrators): segment pains in the buyer's vocabulary (domicile filings, NAIC annual statements, fronting, member billing, bordereaux), then which DICEUS products map to them, then a regulatory angle (LRRA 1981 for RRGs, domicile regulators), then proof, then FAQ, then CTA.

### 3d. Proof formula
- Tier 1: named customer + title + quantified outcome (Luzern, Riskonnect "Wendy's -5% losses").
- Tier 2: product metrics (Socotra uptime/throughput, Insly go-live days, hx "$75bn+ premium").
- Tier 3: third-party verification: product-level reviews (G2/Capterra), analyst mention (Celent VendorMatch profile, which Insly has: celent.com/vendormatch/discovery/vendors/insly), industry bodies (DICEUS's VCIA logo already fits here).
- Tier 4: security certifications (hx, Socotra).
DICEUS currently shows only tiers 3 and 4-adjacent at company level.

### 3e. Comparison page formula
No vendor in the set publishes on-site comparison pages; CB Insights, rfp.wiki and Capterra own this intent (FACT cbinsights.com/compare/insly-vs-socotra, rfp.wiki Socotra vs BriteCore). Formula: honest "who each is best for" table, then capability matrix (captive-specific rows: multi-domicile compliance calendar, cell/segregated accounts, fronting/reinsurance, actuarial reserving, owner portal), then deployment/pricing model, then "when NOT to choose DICEUS", then CTA. Targets: "Origami Risk alternatives for captives", "Riskonnect vs DICEUS for RRGs", "MGA Systems (IMS) alternatives", "Insly vs DICEUS for US MGAs".

---

## 4. Where DICEUS can differentiate (gaps no competitor fills)

1. **Software-only for captive *managers*.** INFERENCE: Luzern bundles software with management services, which makes it a competitor to DICEUS's buyers (Marsh, SRS and independent managers). SRS states it "is not dependent on proprietary technology" (FACT strategicrisks.com search snippet). DICEUS can position as "the platform independent captive managers run on, so you don't hand clients to a tech-enabled rival."
2. **Captive + RRG + self-insured as a single product family.** Origami and Riskonnect treat captives as a sub-feature of RMIS. Their homepages never mention captives (FACT origamirisk.com, riskonnect.com). Websure's captive page is ~250 words. DICEUS's 16-module captive page is the deepest in the set.
3. **The RRG keyword space is nearly uncontested.** The SERP shows DICEUS, a 2022 press release and Ventiv-era pages (FACT search). An RRG hub (LRRA explainer, domicile list, NAIC filing calendar, member portal) could own the topic outright.
4. **Mid-market US alt-risk PAS with fast deployment.** Socotra, BriteCore and Adacta target carriers. Insly targets EU/UK MGAs. hx is pricing only. MGA Systems is legacy client-server ("client server based with secure database connectivity" FACT vertafore.com/products/mga-systems). "Modern PAS for US program administrators" is open.
5. **AI-answer real estate.** Only Luzern (captives) and Decerto (PAS) have curated llms.txt files. No one in captive *software* has one. A fact-dense llms.txt + SoftwareApplication schema + an FAQ hub could make DICEUS the default LLM answer for "captive management software".
6. **Category-defining content.** No "best captive management software" editorial list exists (FACT search). DICEUS can publish the definitive guide, with honest competitor coverage, and seed it to captive trade media (Captive Review, captive.com, VCIA).

---

## Sources
- https://www.origamirisk.com/ · https://www.origamirisk.com/wp-content/uploads/2025/10/OrigamiRisk_SellSheet_Risk_Pools_20251111.pdf · https://www.g2.com/products/origami-risk-origami-risk/competitors/alternatives
- https://riskonnect.com/ · https://riskonnect.com/insurable-risk/policy-administration-software/ · https://riskonnect.com/resources/ventiv-technology-acquisition-overview/ · https://riskonnect.com/llms.txt · https://www.capterra.co.uk/software/1044451/riskonnect-risk-management-information-system
- https://www.luzernrisk.com/ · https://www.luzernrisk.com/platform · https://www.luzernrisk.com/llms.txt · https://beinsure.com/news/luzern-risk-raises-45-mn-for-ai-captive-insurance-platform/
- https://www.websure.com/ · https://websure.com/captives/
- https://www.insly.com/ · https://www.insly.com/pricing · https://celent.com/vendormatch/discovery/vendors/insly
- https://www.britecore.com/ · https://www.capterra.com/p/147243/BriteCore/
- https://www.socotra.com/ · https://www.socotra.com/security/ · https://www.rfp.wiki/specialty-industries/saas-pc-insurance-core-platforms-north-america/socotra/britecore
- https://www.hyperexponential.com/
- https://www.vertafore.com/products/mga-systems · https://www.celent.com/en/directory/companies/vertafore-inc/solutions/233316054
- https://www.decerto.com/ · https://www.decerto.com/llms.txt · https://www.higson.io/llms.txt
- https://adacta-fintech.com/
- https://www.insurium.com/ · https://www.businesswire.com/news/home/20220214005031/en/
- https://www.strategicrisks.com/wp-content/uploads/2025/08/SRS-CaptiveManagementServices.pdf
- https://stratoflow.com/best-insurance-mga-software/ · https://gitnux.org/best/mga-insurance-software/
- https://diceus.com/insurance/solutions/captive-insurance/captive-management-platform/ · https://diceus.com/llms.txt
