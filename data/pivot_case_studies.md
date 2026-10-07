# Services -> Product Pivots: Case Studies for the DICEUS SEO Strategy

Research date: 2026-10-06. Method: WebSearch, plus a few public-page fetches per company (live homepages fetched with WebFetch/curl, old homepages from Wayback Machine `id_` snapshots via curl). Labels: **FACT** (with source), **INFERENCE** (my reading of the evidence), **NOT VERIFIED** (claimed or likely but not confirmed).

## 0. Candidate screening

| Candidate | Services-first? | Kept as case? | Reason |
|---|---|---|---|
| Adacta -> Adacta Fintech / AdInsure | Yes (Microsoft Dynamics/ERP/BI integrator + AdInsure) | **Yes** | Clean services divestment in 2019 |
| Decerto -> Higson + product suite | Yes (Polish software house/outsourcer) | **Yes** | Closest to DICEUS's current state |
| Stratoflow -> Openkoda | Yes (Java/Salesforce dev shop) | **Yes** | Separate product brand, services kept |
| Mastek -> Majesco | Yes (Indian IT services) | **Yes** | Demerger into a separate listed company |
| Exigen -> EIS | Yes (Exigen Group: BPO/app development) | **Yes** | Services spun off, product renamed |
| Damco -> InsureEdge | Yes (offshore dev) | **Yes (as a counter-example)** | Product left inside the services site |
| 37signals -> Basecamp | Yes (web design agency) | **Yes (adjacent B2B SaaS)** | The standard example of a single-product refocus |
| msg -> msg insur:it | Consultancy group, products in subsidiaries | Brief mention | Co-brand model, not a clean pivot |
| Duck Creek | No. It started as a product company, Accenture bought it (2011) and carved it out (2016) | Dropped | A product leaving a services parent, not a services firm pivoting |
| Fadata, Insly, Keylane, Comarch | Product-first or merged product companies | Dropped | Not pivots |
| Sollers Consulting | Consulting/SI for Guidewire and others, no own core product found | Dropped | No pivot |
| Xceedance | Services, consulting and BPO with tools around them | Dropped | No clear product-led repositioning found (NOT VERIFIED) |

## 1. Adacta -> Adacta Fintech (AdInsure)

1. **Pivot facts.** FACT: In January 2016 the adacta.si homepage put "AdInsure – Informacijski sistem za zavarovalniško industrijo" next to Microsoft Dynamics NAV/AX ERP, CRM and BI (Qlik). Its hero promoted Dynamics NAV license discounts (Wayback 20160123 snapshot of adacta.si). FACT: On 6 Aug 2019 BE-terna and Deutsche Private Equity bought the "Adacta services business" (about 300 employees, Microsoft Dynamics, Qlik and Cornerstone). The insurance software (AdInsure) moved into the newly created **Adacta Fintech**, which Adacta Holding kept (https://www.be-terna.com/about-us/news/be-terna-and-deutsche-private-equity-acquire-adacta). The services company was renamed BE-terna in local markets in July 2020 (https://www.amcham.hr/en/news/adacta-is-now-be-terna). Volpi Capital invested in Aug 2021 (https://www.adacta-fintech.com/news/adacta-joins-forces-with-volpi-capital).
2. **Brand/domain.** FACT: adacta.si returns a 301 redirect to www.adacta-fintech.com (checked with curl). The company name (Adacta) and product name (AdInsure) stayed. The services brand left with the buyer and now runs as BE-terna. No adinsure.com site was found (it did not resolve).
3. **Homepage before/after.** Before (2016): ERP promotions plus a list of four solutions with AdInsure first. After: H1 "Modernise your life and non-life business with a single insurance platform", subline "Meet AdInsure, the digital platform…", title tag "Life and Non-life insurance software platform" (live fetch).
4. **IA today.** Solutions (by segment: P&C, Life, Commercial, Brokers, plus Claims/PAS modules), Platform (capabilities, Studio, AI, Cloud), Services (implementation only), Clients, Resources (including a dedicated "Analyst Reports" section), About.
5. **Legacy services content.** It was sold. Non-insurance content disappeared, and the old domain's equity is consolidated into the new product domain by a 301 redirect.
6. **Proof.** Gartner Market Guide 2023, Celent (Technology Standout, 2026 P&C Claims), ISG Provider Lens Leader, Everest PEAK Matrix, named logos (Generali, Signal Iduna, Triglav, die Haftpflichtkasse). Source: live homepage.
7. **Outcome.** Gartner MQ P&C Europe 2019–2021 and Celent XCelence 2021 (https://cbinsights.com/company/adacta-fintech); PE investment in 2021.
8. **Lesson (INFERENCE).** Being cited by analysts only started once the company was purely insurance. A single entity (one name, one domain, one category) is what analysts, buyers and LLMs can classify. Sending the old domain to the product domain with a 301 kept the equity.

## 2. Decerto (software house -> insurance product suite + Higson)

1. **Pivot facts.** FACT: In Dec 2017 decerto.pl had the title "Systemy informatyczne dla biznesu", a top bar "Hyperon | ECS | Outsourcing", and three pillars: Systemy IT, Usługi, Outsourcing ("programiści, analitycy, testerzy"). It described itself as "polska firma informatyczna … Producent wielu rozwiązań IT, w tym systemu Hyperon" (Wayback 20171230). Hyperon was later renamed Higson (https://alternativeto.net/software/hyperon/about).
2. **Brand/domain.** It uses a hybrid. FACT: decerto.pl redirects to decerto.com/us (curl), and decerto.com carries all products, including /higson ("Higson by Decerto"). FACT: **higson.io is still a separate live product site** (title "Higson | Ultra-Fast Business Rules Engine for Insurance", own pricing, docs and download pages, 2 mentions of Decerto). Neither page sets a canonical tag. INFERENCE: The two sites target the same "insurance rules engine/product configurator" queries, which risks cannibalization.
3. **Homepage after.** H1 "Insurance Software Your Team Uses This Quarter, Not in Three Years" (live fetch of decerto.com).
4. **IA today.** Products (Flagship: Agent Portal, Higson, Claims AI. Core: PAS, Commission, Claims, Anti-fraud, Underwriting Workbench, ODS …) | Solutions (Carriers, MGAs & Brokers) | **Services** (Custom Software Development, API & Integration, Data Migration, Managed Services, IT Consulting & Audit, IT Outsourcing).
5. **Legacy services content.** It was kept, moved into third position in the nav, and reframed around insurance. Generic, non-insurance "systems for business" positioning is gone.
6. **Proof.** "1 of 14 vendors named in Everest PEAK Matrix Underwriting Orchestration", Clutch 4.9, 16 logos (Allianz, Generali, VIG, Talanx, Unum), "4–6 weeks to first working configuration", "50,000+ agents" (live fetch). Higson is listed on G2 (4.5), TrustRadius and Celent's directory (https://www.celent.com/en/directory/companies/decerto/solutions/higson).
7. **Outcome.** Everest PEAK inclusion, Celent directory listing, and "best automated insurance software 2025" award (https://www.decerto.com/eu/news/higson-named-best-automated-insurance-software-2025).
8. **Lesson (INFERENCE).** This is the closest match to DICEUS. It is one domain led by products, with insurance-only services as a supporting third nav item. The separate higson.io shows the cost of a second domain: split authority and duplicate pages. A tool sold to developers (a rules engine) can justify that cost. A core-system suite usually cannot.

## 3. Stratoflow -> Openkoda

1. **Pivot facts.** FACT: In Dec 2020 Stratoflow was "Your Salesforce and MuleSoft experts" (Wayback 20201208). The founders built products (Recostream, which GetResponse acquired, and ScanRepeat). They then published Openkoda as an open-source low-code platform and later refocused it on insurance (Openkoda 2.0 with GenAI, https://www.insurtechinsights.com/openkoda-unveils-openkoda-2-0-revolutionising-insurance-applications-with-generative-ai/; insurance product-build launch Nov 2024, https://insurance-edge.net/2024/11/01/openkoda-launches-new-product-build-platform-for-insurance-brands/). Stratoflow's own case study says: "Openkoda builds and licenses the platform; Stratoflow configures products, integrates systems, migrates data and supports the result". Openkoda is a "sister company" (https://stratoflow.com/case_studies/openkoda-insurance-application-development-platform/).
2. **Brand/domain.** It runs a **separate brand and domain** (openkoda.com), and the services brand continues unchanged. Stratoflow's H1 today is "Modernize critical Java systems without a risky rewrite". The openkoda.com homepage does not mention Stratoflow (live fetch).
3. **Homepage after.** Openkoda H1 "Policy administration software", tagline "Launch Insurance Innovations with AI".
4. **IA.** Platform | Solutions (by operating model/goal) | Openkoda AI | Resources | **Pricing** ("Three plans, published prices… no per-seat fees") | Company.
5. **Legacy services content.** It stayed on stratoflow.com, where insurance appears as an industry and the work is reframed as Openkoda implementation.
6. **Proof.** Published pricing, open source (code ownership, "no vendor lock-in"), trade-press logos. The homepage logo wall (Santander, Barclays, Swiss Re, Lloyd's…) is NOT VERIFIED as Openkoda platform customers.
7. **Outcome.** Trade-press coverage. Stratoflow's case study dates the first implementations to 2025–26. No analyst placement was found (NOT VERIFIED).
8. **Lesson (INFERENCE).** A new domain starts with no authority, which works when the product is new and greenfield. The product site can also say "PAS" without services noise. DICEUS is in a different position: its insurance product pages and insurance equity already live on diceus.com (for example, /insurance/solutions/captive-insurance/ ranks for captive queries, as seen in SERP), so starting over elsewhere would discard that.

## 4. Mastek -> Majesco

1. **Pivot facts.** FACT: Mastek's board approved demerging the "Insurance Products and Services business" into Majesco on 15 Sep 2014. The stated reason was the "differing risk-reward profile" of the two businesses and alignment of "business models, capital allocation and decision making" (https://www.mastek.com/wp-content/uploads/2024/04/mastek-limited-demerge-insurance-products-services-business-separate-listed-company.pdf). Majesco listed in the US and Thoma Bravo acquired it in 2020 for about $729M (https://app.dealroom.co/companies/majesco).
2. **Brand/domain.** It became a separate company on majesco.com, while Mastek continued as an IT services company on mastek.com.
3. **Homepage before/after.** Feb 2016 (Wayback): title "Majesco – Insurance Technology Systems & Solutions". The nav mixed Software (P&C/L&A suites) with Cloud, Implementation, Consulting, Development, Data, Digital and Testing Services. Today: H1 "Intelligent solutions that move insurance and retirement forward", and the top nav (Intelligent Solutions, Who We Serve, Why AI Matters, Resources, Why Majesco) has **no Services item** (live fetch).
4. **IA today.** Platforms by line (P&C, L&AH, Retirement, CoreConnect for MGAs) and solutions by job to be done. Services is no longer in the top nav.
5. **Legacy services content.** It was demoted over about 10 years. "Development/Testing Services" pages disappeared from the main nav (INFERENCE from the before/after nav comparison).
6. **Proof.** "375+ market leaders", "1,400+ implementations", "95% of customers on the cloud", Gartner MQ Leader (SaaS P&C core, 2025), Celent Luminary/XCelent 2026 (live fetch).
7. **Outcome.** NYSE listing, then a $729M take-private.
8. **Lesson (INFERENCE).** Even inside one insurance company, services nav items stayed for years and were dropped only once product proof (analyst reports, counts) could carry the site. Getting there was a staged demotion, not an overnight switch.

## 5. Exigen -> EIS Group

1. **Pivot facts.** FACT: Exigen Group (1999) spun Exigen Services off as an application-development company in 2006. Exigen Insurance Solutions became separate in 2008 and rebranded to "EIS" in 2014 (https://en.wikipedia.org/wiki/Exigen_Services; https://www.eisgroup.com/company/).
2. **Brand/domain.** Separate companies. The product took a short derived brand and its own domain (eisgroup.com).
3. **Homepage today.** Title "Digital Insurance Transformation Platform – EIS SaaS Coretech". Nav: Why EIS | By Outcome | By Market | Offerings (By Product, By Platform Enhancement, By Use Case) | Resources.
4. **Legacy services content.** It went with the spun-off services firm.
5. **Proof and outcome.** Analyst coverage and a Tier-1 reference base. Not re-verified in this pass.
6. **Lesson (INFERENCE).** The IA is organized by outcome, by market and by product, which suits LLM retrieval for prompts like "PAS for group benefits". DICEUS's group insurance and GL products could follow the same "By market group" pattern.

## 6. Damco Solutions -> InsureEdge (counter-example)

1. **Facts.** Founded 1996. In Jan 2016 its title was "Offshore Software Development Services Company, Custom Development", with "P&C Insurance" as one item under Solutions (Wayback 20160103). InsureEdge is a PAS/claims/reinsurance suite with "20+ global insurers", listed on GetApp/SoftwareOne (https://www.getapp.co.uk/software/2050444/insureedge).
2. **Brand/domain/IA today.** The domain is still services-first. The H1 is "AI Has Changed How We Build Software", and InsureEdge sits **under the Services menu** as "InsuranceTech" in the /insurance/ subfolder (live fetch).
3. **Proof.** Mostly ROI percentages. No analyst placement appeared in the searches (NOT VERIFIED).
4. **Lesson (INFERENCE).** This is what DICEUS looks like today. A product nested under a generic services entity is read as "an outsourcer's accelerator". It shows up in software directories but not in analyst quadrants or vendor shortlists.

## 7. 37signals -> Basecamp (adjacent B2B SaaS)

FACT: 37signals was a web-design firm founded in 1999 and launched Basecamp in 2004. Product revenue passed design revenue in 2005. In Feb 2014 it renamed the company "Basecamp" and dropped or spun off its other products (https://en.wikipedia.org/wiki/37signals; https://betanews.com/2014/02/05/37signals-becomes-basecamp-and-drops-all-but-its-eponymous-product/). It later went back to the 37signals name once it had several products again (HEY, ONCE). **Lesson (INFERENCE):** Agency services were cut once the product outearned them. Focusing on one flagship product made the entity unambiguous, and the company name became a container for products, not the thing being sold.

## Brief: msg insur:it (co-brand model)

FACT: The msg consultancy group (1980) set up msg nexinsure in 2018. msg life and msg nexinsure have shared the co-brand "msg insur:it" since Dec 2021, with about 2,000 staff and about €300M revenue (https://msg.group/en/press/msg-establishes-new-company-in-the-field-of-insurance; https://corporate.ansa.it/pressrelease/economia/2021/12/06/...). This works at large-group scale but takes heavy brand investment. Not relevant on DICEUS's budget.

## 8. Comparison table

| Company | Pivot (when) | Model | Domain outcome | Services fate | Top nav today | Key proof |
|---|---|---|---|---|---|---|
| Adacta | ERP integrator + PAS -> pure insurance platform (2019) | C (divest services) + one-domain product | adacta.si 301 -> adacta-fintech.com | Sold to BE-terna | Solutions / Platform / Services / Clients / Resources | Gartner, Celent, ISG, Everest |
| Decerto | Software house/outsourcing -> insurance products (2018–2024) | A (one domain, products first) + one satellite domain | decerto.pl -> decerto.com; higson.io kept | Kept, nav #3, insurance-only | Products / Services / Solutions | Everest, Clutch, logos, G2 |
| Stratoflow/Openkoda | Dev shop -> insurance PAS platform (2023+) | B (separate product brand and domain) | openkoda.com new; stratoflow.com stays services | Separate sister brand = implementation partner | Platform / Solutions / Pricing | Published pricing, open source |
| Mastek/Majesco | IT services -> insurance software (2014–15) | C (demerger) | majesco.com separate from mastek.com | Stayed with Mastek; Majesco demoted its own services | Solutions / Who we serve / Why Majesco | Gartner MQ Leader, Celent, 375+ customers |
| Exigen/EIS | BPO/dev -> core platform (2006–2014) | C (spin-off + rename) | eisgroup.com | Spun off | By outcome / market / product | Analysts (not re-verified) |
| Damco | Offshore dev, product added | Nested (anti-pattern) | damcogroup.com/insurance/ | Dominant | Services > InsuranceTech | ROI stats only |
| 37signals | Agency -> SaaS (2004–2014) | A-extreme (rename to product) | basecamp.com, later 37signals.com | Discontinued | Product only | Customer counts |

## 9. Strategic models observed

- **Model A: one domain, products first, insurance-only services demoted** (Decerto, Majesco after the demerger, Adacta after the divestment). *SEO:* keeps all link equity and history. *Entity/LLM:* clear when the homepage H1, title, Organization schema and nav all say "insurance software vendor". *Cons:* needs a heavy prune or redirect of generic services pages, or the entity stays mixed.
- **Model B: separate product brand and domain** (Openkoda, higson.io). *SEO:* starts from zero authority, splits links, and creates cannibalization risk when both sites cover the product (Decerto). *Entity/LLM:* a very clean product entity, but it must earn citations from scratch. *Cost:* two sites, two content programs.
- **Model C: spin-off or divestment of services** (Adacta, Majesco, EIS). *SEO:* the product keeps the main domain, or a 301 brings it over. *Entity:* the cleanest result, and the one that produced analyst recognition in every case. *Cons:* a corporate transaction, which is out of scope for a website budget.
- **Model D: nested product inside a services site** (Damco). Cheapest, but the product never becomes its own entity. **Avoid.**

## 10. Recommendation for DICEUS (INFERENCE)

**Adopt Model A on diceus.com, applying the Model C logic to content only (a "virtual spin-off" of the generic services).** The reasons:

1. **Budget and equity.** DICEUS's insurance pages already rank and are listed in directories (diceus.com/insurance/solutions/captive-insurance/ appears in captive-software SERPs, and Capterra lists "Diceus Captive Management Platform", https://www.capterra.ca/software/1096952/Captive-Management-Platform). A new domain (Model B) would throw this away. Openkoda shows that a new domain fits a greenfield product, not one with existing traction.
2. **Entity clarity.** Copy Adacta and Majesco: change the homepage H1 and title from "Custom software development company" to an insurance-software-vendor statement focused on alternative risk (captive/RRG). Put **Products | Solutions (by market: captives, RRGs, MGAs, group, reinsurance) | Services (implementation, integration, migration, insurance-only) | Proof | Resources** in the nav, in the same order as Decerto.
3. **Legacy services.** Decerto and Adacta both dropped non-insurance positioning. Prune or consolidate the roughly 190 generic service pages with 301 redirects into a small set of insurance-scoped services pages, and send non-insurance traffic to a single "Engineering services" hub (or noindex it) rather than deleting the domain's history.
4. **Proof stack.** Every successful pivot led with analyst presence, so build toward Celent, Everest, ISG and Gartner directories and briefings (Decerto reached Everest PEAK while it was still a mid-sized software house). Add named captive/RRG logos, review profiles (G2/Capterra, already started), and US/VCIA-oriented case studies. Consider published pricing or packaging for the captive platform (Openkoda pattern).
5. **Avoid satellite domains** for individual products unless one is a tool sold to developers (higson.io shows the cannibalization cost).

### Three strongest supporting examples
1. **Adacta Fintech**: dropped non-insurance services, 301'd its old domain into a single product domain, then got Gartner and Celent recognition and PE funding.
2. **Decerto**: the closest analogue (a CEE software house). It is products-first on one domain with insurance-only services as nav #3, and won Everest PEAK inclusion. higson.io is a warning about splitting domains.
3. **Majesco**: services removed from the top nav after the pivot, with proof carried by analyst reports and customer counts. Outcome: Gartner MQ Leader and a $729M exit.
