# DICEUS: Company and Market Research (public information)

Research date: 2026-10-06. Scope: public web pages only (WebSearch plus a handful of WebFetch calls). No outreach, no logins.
Labels: **FACT** (with source), **INFERENCE** (reasoned from facts), **HYPOTHESIS** (needs validation), **NOT VERIFIED** (looked for it, could not confirm).
Note: some page summaries came through a fetch tool that summarizes pages. Check the exact figures on the live pages before quoting them externally.

---

## 1. Company basics

| Item | Finding | Label / Source |
|---|---|---|
| Founded | 2011, by Illia Pinchuk (CEO) | FACT [S2] |
| Legal HQ | Wilmington, Delaware, USA (2810 N Church St, Ste 94987). This is a registered-agent style address. | FACT for the address [S1][S3]. INFERENCE: it is a US legal entity, not an operating office. |
| Origin / delivery | Kyiv, Ukraine. Copenhagen Capacity (2023) describes it as a "Kyiv-based IT firm". Clutch still lists a Kyiv location. The diceus.com About page lists 9 offices (Lithuania, Denmark, USA, UAE, Faroe Islands, Poland, Austria, Jordan, Spain) and does **not** show Ukraine. | FACT [S2][S9][S12]. INFERENCE: Ukraine has been taken out of the brand-facing office list, probably to reduce perceived risk for Western buyers. |
| Nordic entity | DICEUS Nordic ApS (Hellerup/Copenhagen). It has operated in Denmark since 2018, and the Nordic HQ opened in Oct 2023. Poul Ørum is CEO of DICEUS Nordics. In 2023 the company said it "considered opening in the USA, but we chose Copenhagen." | FACT [S9][S2] |
| Size | Own site: "250+ tech professionals", "150+ projects", "8 ready-made insurance software products". Clutch: 50-249 employees. | FACT [S1][S2][S12]. The headcount figures conflict, so treat the exact size as NOT VERIFIED. |
| Leadership | Illia Pinchuk (CEO), Kateryna Monastyrska (Head of Sales/Marketing), Dmytro Kazymir (Head of Growth), Elena Didukh (Head of HR), Poul Ørum (CEO Nordics), Oddur Friang Rasmussen (Regional Sales Manager) | FACT [S2] |
| Ownership / funding | No external funding round found. The company appears founder-owned. | NOT VERIFIED. Crunchbase and CB Insights profiles exist [S20][S21] but were not opened. |
| Partnerships | Microsoft, Oracle, Google Cloud (technology partners). Microsoft for Startups Founders Hub (Jun 2025). Atlassian program (Sep 2025). InsureMO (Apr 2026, EMEA/APAC). VCIA technology partner (Jun 2026). Kruzr (Jul 2026, connected motor). Blink Payment (Oct 2024). Claim Technology (Jun 2024). Fadata. Memberships: Insurtech UK (associate, May 2024) and Swiss InsurTech Hub (May 2024). | FACT [S1][S2][S4][S5][S6] |
| Certifications | ISO 9001:2015. The site also lists team certifications (Google Cloud, IBM Design Thinking, CBAP, iSQI). | FACT [S1][S2]. ISO 27001 NOT VERIFIED (not found). SOC 2 NOT VERIFIED (not found). |
| Awards | Inc. 5000 (2019). Clutch Top Cloud Consulting Company 2024. Global Insurtech Awards 2025: Super App named "Best Customer Engagement Software". Finalist, British Insurance Technology Awards 2026. | FACT [S1][S4] |
| Named clients | UNIQA, Vienna Insurance Group, Fairfax Group, WTW/Willis, BriteCore, Raiffeisen Bank, Fadata, AvelaLaw | FACT [S1][S2]. **No named US captive, RRG or MGA client was found.** (NOT VERIFIED that none exist.) |

**INFERENCE:** The company is mid-sized, has Ukrainian engineering roots, and sells mainly into Europe (DACH, Nordics, UK). Its US presence is a Delaware legal entity plus marketing and partnerships. No physical US sales team was found.

## 2. Product portfolio: product or services in product clothing?

The homepage lists insurance "solutions" next to more than 100 IT services: custom development, staff augmentation, outstaffing, QA, DevOps and others [S1].

| Offering | Evidence of a real product | Assessment |
|---|---|---|
| Policy Administration System (PAS) | Listed on Microsoft Marketplace (Jun 2026) [S4][S13]. Gartner Peer Insights product page [S14]. Capterra/GetApp/Software Advice listings (AU, UK) [S15]. Modules: products, policies, COI, bulk renewals, claims, billing. | **Most product-like.** FACT that it has listings. Public pricing: NOT VERIFIED (none found). |
| Captive Insurance Software / PAS for captives | Product page has screenshots, modules (Policies, Products, Invoicing and Billing, Claims, Exposure and Bordereaux, Clients) and a low-code configuration layer. Integrations named: DocuSign, RSign, CRM, accounting, DWH. Described as MACH architecture. CTAs: "Book a demo". No pricing and no named clients. | FACT [S7]. INFERENCE: the product is real but customer evidence is thin. |
| Captive Management Platform | Listed on Capterra (several non-US country sites) and Software Advice AU [S16]. Listings say pricing is "customized … annual subscription or license-based". Covers policy, claims, reinsurance, compliance and actuarial work. | FACT [S16]. INFERENCE: this is the PAS-for-captives re-packaged as a separate SKU. |
| Captive Owner Portal | Software Advice AU listing [S17]. Offered to VCIA members [S5]. | FACT. Maturity NOT VERIFIED. |
| Alternative Risk Operating Platform ("AROP") | Product page targets captive managers, PCC/cell administrators, RRGs, reciprocals (AIF), self-insurance funds and program administrators. Features: bordereau reconciliation, multi-entity ledger, statements, statutory-filing tracker, actuarial module. Demo CTA, no pricing, no clients. | FACT [S8]. INFERENCE: US alternative-risk vocabulary is used correctly (NAIC, domiciles, AIF). The positioning looks recent (2026). |
| Risk Retention Group Management Platform | Appears only as a nav item or sibling page [S7][S8]. | NOT VERIFIED as a separate product. HYPOTHESIS: a landing page for search and positioning built on the same core. |
| Group / Individual Insurance Management Platform | Gartner Peer Insights and GetApp listings [S14][S18] | FACT that it is listed. |
| Reinsurance (Financial and Data Exchange) Platform | GetApp CA/UK listing [S18] | FACT that it is listed. |
| Underwriting Workbench (Commercial / Health / Life, "AI-powered") | Site pages [S1]. Referenced in the InsureMO deal ("intelligent submission intake") [S6]. | FACT that the pages exist. Product maturity NOT VERIFIED. |
| Broker Portal, Customer Web Portal, Insurance Super App (Health, Life/Unit-linked, Car), AI Chatbot (with "Autopilot" feature, Nov 2024) | Site pages [S1]. Award for Super App [S4]. Gartner listing "insurance web portal development and ready made portals" [S14b]. | Mixed. The Gartner listing's name, "web portal **development** and ready-made portals", is itself the services/product hybrid. |
| General Ledger Platform, Data Warehouse for Insurance | Site pages and nav items [S1][S8] | NOT VERIFIED as standalone products. HYPOTHESIS: accelerators or reusable components delivered through services projects. |

**INFERENCE (key):** The portfolio is wide: about 15 solution pages against "8 ready-made products" on the About page. This looks like a services company that has turned its reusable components into products and listed them on marketplaces and review sites. The strongest product signals are PAS and the captive line (Marketplace listing, Gartner and Capterra listings, demo flows, screenshots, VCIA partnership). Weak signals across all products: no public pricing, no named product customers, no release notes or changelog found, no documentation or developer portal found (NOT VERIFIED).

## 3. News and press, 2024-2026 (from diceus.com/media [S4] unless noted)

- **2026:** Captive.com coverage, "How AI and automation are reshaping captive insurance operations" (Sep 8). PropertyCasualty360 article (Jul 23). Kruzr partnership (Jul 13). Startups Magazine (Jul 6). BITA 2026 finalist (Jul 1). PAS on Microsoft Marketplace (Jun 19). **VCIA technology partner** (Jun 10), offering the Captive Management Platform and Captive Owner Portal to 400+ VCIA members. CEO quote: "Captive managers have been working around legacy software solutions for too long" [S5]. Risk-!n Zurich (May 26). Insurance Thought Leadership, "AI accelerates policy admin system implementation" (May 25). **InsureMO partnership** (Apr 30; EMEA/APAC, aimed at group carriers and MGAs) [S6]. CEO pitched at ITC London (Feb 2). The captive product page promoted a live webinar on Sep 8, 2026 [S7].
- **2025:** European Captive Forum (Nov 12). Insurance Innovators Summit London (Nov 11). Global Insurtech Award for Super App (Oct 27). SIH Roadshow pitch (Sep 29). Atlassian program (Sep 9). Insurtech UK and Deloitte event (Aug 6). Microsoft Founders Hub (Jun 26).
- **2024:** Insurtech UK events, Swiss InsurTech Hub Summit, Google Cloud Summit London, Blink Payment, Claim Technology. Insurtech UK and SIH memberships.
- FACT: no ITC Vegas, CICA or VCIA annual conference (Aug 11-13, 2026) attendance was found in DICEUS's newsroom [S4][S19]. NOT VERIFIED whether they exhibited.
- FACT: no funding announcements were found.
- **INFERENCE:** Until 2025 the event footprint was almost entirely UK/Swiss/European. The US captive push (VCIA, Captive.com, PC360, AROP) is a 2026 pivot.

## 4. Third-party presence

| Platform | URL | Listed as | Notes |
|---|---|---|---|
| Clutch | https://clutch.co/profile/diceus | **IT services / outsourcing** | 4.9/5, 49 reviews. $25-49/hr, $10k minimum project. Service mix: Cloud consulting and SI 40%, IT strategy 20%, others 10% each. FACT [S12] |
| G2 | https://www.g2.com/products/diceus/reviews | Vendor profile (reviews praise "dedicated team", chatbot dev) | Category NOT VERIFIED (403 on fetch). INFERENCE: services-flavored [S10] |
| Gartner Peer Insights | https://www.gartner.com/reviews/product/diceus-policy-administration-system ; .../diceus-individual-and-group-insurance-management-platform ; .../insurance-web-portal-development-and-ready-made-portals | **Product vendor** | The vendor blurb still says "custom software development services since 2011". The homepage claims "5/5 (6 reviews)" [S1][S14] |
| Capterra / GetApp / Software Advice (Gartner Digital Markets) | e.g. https://www.capterra.co.uk/software/1096952/Captive-Management-Platform ; https://www.softwareadvice.com.au/software/534593/Policy-Administration-System ; https://www.softwareadvice.com.au/software/549128/Captive-Owner-Portal ; https://www.getapp.ca/software/2092898/reinsurance-financial-and-data-exchange-platform | **Product vendor** | Found on CA, UK, AU, IN, ZA, SG and IL country domains. **A US capterra.com listing was NOT VERIFIED** (not surfaced). [S15-S18] |
| Microsoft Marketplace | announced at https://diceus.com/media/diceus-policy-administration-system-microsoft-marketplace/ | Product (PAS) | FACT [S13] |
| Crunchbase / CB Insights | https://crunchbase.com/organization/diceus ; https://www.cbinsights.com/compare/diceus-vs-intellectsoft-ltd | CB Insights compares it with **outsourcers** (Intellectsoft, Innowise) | FACT that the comparison exists [S20][S21] |
| DesignRush, Kompass, softwarefinder, SourceForge | https://www.designrush.com/agency/profile/diceus ; https://softwarefinder.com/insurance-software/diceus-policy-administration | DesignRush lists it as an **agency**; softwarefinder lists a product | FACT [S22] |
| The Hub (Denmark) | https://thehub.io/startups/diceus-nordic-aps | Startup | FACT |
| Paid / sponsored | https://www.bkreader.com/sponsored/how-diceus-software-products-help-insurance-businesses-11977061 | Sponsored product article | FACT. INFERENCE: paid link building or PR |
| Wikipedia / Wikidata | none found | | NOT VERIFIED (not found). This is an entity-SEO gap. |
| GoodFirms | none surfaced | | NOT VERIFIED |
| Celent / Novarica (Datos) / Aite-Novarica, Insurtech Insights | no DICEUS mention found | | NOT VERIFIED (not found). By contrast, Celent profiles competitors such as Riskonnect Policy [S23] |
| Captive trade media | Captive.com article (Sep 2026) [S4]. Captive Review / Captive International: no DICEUS article found | | Partial |

**INFERENCE:** The third-party footprint is split. Profiles that carry authority with procurement teams (Clutch, CB Insights peers, DesignRush) frame DICEUS as an **outsourcer**. Gartner Digital Markets and Microsoft frame it as a **product vendor**. The entity signal is mixed both for search engines and LLMs and for analyst-minded insurance buyers.

## 5. Hiring signals

- FACT: **Senior SEO & AI Search Automation Specialist**, based at DICEUS Nordic ApS (Hellerup, DK). The posting describes the company as "a product company focused on building innovative SaaS solutions for the global insurance and financial services markets". It explicitly says the role is "not … manually collecting keywords … or monitoring rankings in spreadsheets" and asks for an AI-first approach to search [S11][S24].
- FACT: Marketing Manager (hands-on, multiple campaigns). Product Owner (Insurance Tech Solutions). Product Owner / Project Manager (Insurance). "CEO Operation Manager". Interns: BA, QA, HR. Most roles are remote and posted on DOU (Ukraine) [S24].
- **INFERENCE:** The company is building in-house product and marketing capacity: product owners, AI-search SEO, and a lean marketing team. Hiring is still Ukraine-centric (DOU, Djinni) and cost-efficient (interns). No US-based sales or marketing roles were found (NOT VERIFIED).
- **HYPOTHESIS:** Organic and AI search (GEO/AEO) is meant to stand in for an expensive US field-sales and analyst-relations motion.

## 6. Pain points and challenges

1. **Brand ambiguity (INFERENCE, strong).** The homepage leads with "custom software development company" and "100+ IT services", while the About page and job posts say "product-led company" or "product company … SaaS". Clutch prices them at $25-49/hr. Buyers and LLMs may file DICEUS as an offshore dev shop [S1][S2][S12][S24].
2. **Proof gap (INFERENCE).** No named US captive, RRG or MGA product customers and no public pricing were found. The named logos are European services clients (UNIQA, VIG, Raiffeisen).
3. **US market entry (INFERENCE).** The company has a Delaware address but no evident US team. In 2023 it chose Copenhagen over the US [S9]. VCIA (Jun 2026) is the first visible US channel.
4. **Competition (INFERENCE).** In core PAS for carriers: Guidewire, Duck Creek, Majesco, Sapiens, Insurity. In the captive and alternative-risk niche: Origami Risk, Riskonnect (which acquired Ventiv in 2024), Websure (captive-specific), AdInsure. Captive managers also run accounting tools and spreadsheets [S23][S25][S26]. The niche is less crowded than core PAS. HYPOTHESIS: "captive management software" is a winnable SERP. DICEUS pages already surface for it in searches run during this research (two blog posts and two product pages).
5. **Portfolio sprawl (INFERENCE).** About 15 solution pages across P&C, life, health, group, reinsurance, motor and captives dilute topical authority and the "who is it for" message.
6. **Ukrainian origin (HYPOTHESIS).** Some US buyers may see vendor-risk or continuity concerns. This may explain why the office list omits Ukraine.

## 7. Alternative risk market context (US)

- FACT: Captive International "Captives by the Numbers 2026" (May 29, 2026) estimates about 8,180 licensed captives worldwide. **40 of 88 global domiciles are in the US.** Vermont has 667 active licenses (1,413 issued since 1981). The same piece identifies **262 RRGs** in 2024 data with roughly **$5B** in premium [S27].
- FACT: Other counts: Vermont 683 licensed captives, 41 new in 2024. Delaware 638 (including cells). Utah 605 (including cells, YE2025). North Carolina 263 (188 pure, 48 PCC, 9 RRGs, 18 SPC). More than 30 states have captive laws [S28]. The two Vermont figures differ by source and definition (licensed vs active).
- FACT: 6,290 captives worldwide at YE2024 (Business Insurance domicile rankings, via Captive.com) [S29]. Marsh-managed captives wrote **$79.1B GWP** in 2025, with 118 new formations (92 in 2024), even as commercial pricing fell 4% (Marsh 2026 benchmarking report, via Insurance Business, May 28, 2026) [S28].
- FACT: VCIA calls itself the world's largest captive trade association, with 400+ member organizations. Its 41st annual conference ran Aug 11-13, 2026 [S5][S19].
- FACT: RRG premium in California alone was about $604M in 2025, led by medical professional liability (claims-made, 36%) [S30].
- **What captive managers need (INFERENCE, from vendor messaging and trade press):** multi-captive and multi-entity administration, cell/PCC accounting, bordereau ingestion and reconciliation, statutory and regulatory filing calendars by domicile, owner/participant statements, loss-ratio and capital dashboards, and a way off spreadsheets. DICEUS's AROP messaging targets exactly these needs [S8].
- **HYPOTHESIS (search demand):** US queries cluster around "captive management software", "captive insurance software", "risk retention group software", "cell captive accounting", "captive reporting", "bordereaux management" and "captive manager" plus domicile names. These are low-volume, high-intent, B2B terms. Volumes are NOT VERIFIED and need a keyword tool.

## Sources

- [S1] https://diceus.com/
- [S2] https://diceus.com/about/
- [S3] https://www.gartner.com/reviews/product/diceus-individual-and-group-insurance-management-platform (and search snippet with the HQ address)
- [S4] https://diceus.com/media/
- [S5] https://diceus.com/media/diceus-joins-vcia-as-a-technology-partner/
- [S6] https://coverager.com/insuremo-and-diceus-partner-to-accelerate-insurance-modernization-across-europe-middle-east-and-asia-pacific/
- [S7] https://diceus.com/insurance/solutions/captive-insurance/captive-insurance-software/
- [S8] https://diceus.com/insurance/solutions/alternative-risk-platform/
- [S9] https://www.copcap.com/cases/it-company-diceus-opens-nordic-headquarters-in-copenhagen
- [S10] https://www.g2.com/products/diceus/reviews
- [S11] https://jobbank.dk/job/3118192/diceus-nordic-aps/about-us/ (now 410 Gone; content from search snippet)
- [S12] https://clutch.co/profile/diceus
- [S13] https://diceus.com/media/diceus-policy-administration-system-microsoft-marketplace/
- [S14] https://www.gartner.com/reviews/product/diceus-policy-administration-system ; [S14b] https://www.gartner.com/reviews/product/insurance-web-portal-development-and-ready-made-portals
- [S15] https://www.softwareadvice.com.au/software/534593/Policy-Administration-System ; https://www.getapp.co.uk/software/2089539/policy-administration-system
- [S16] https://www.capterra.co.uk/software/1096952/Captive-Management-Platform ; https://www.softwareadvice.com.au/software/549129/Captive-Management-Platform ; https://www.diceus.com/insurance/solutions/captive-insurance/captive-management-platform/
- [S17] https://www.softwareadvice.com.au/software/549128/Captive-Owner-Portal
- [S18] https://www.getapp.ca/software/2089805/individual-and-group-insurance-management-platform ; https://www.getapp.ca/software/2092898/reinsurance-financial-and-data-exchange-platform
- [S19] https://www.captive.com/news/vcia-opens-registration-for-41st-annual-captive-insurance-conference
- [S20] https://crunchbase.com/organization/diceus
- [S21] https://www.cbinsights.com/compare/diceus-vs-intellectsoft-ltd
- [S22] https://www.designrush.com/agency/profile/diceus ; https://softwarefinder.com/insurance-software/diceus-policy-administration
- [S23] https://www.celent.com/en/directory/companies/ventiv-technology/solutions/443595081 ; https://www.cbinsights.com/compare/origami-risk-vs-ventiv-technology
- [S24] https://jobs.dou.ua/companies/diceus/vacancies/
- [S25] https://websure.com/wp-content/uploads/2024/02/Websure-for-Captives.pdf
- [S26] https://www.capterra.co.za/compare/200794/1096952/adinsure/vs/Captive-Management-Platform
- [S27] https://www.captiveinternational.com/captives-by-the-numbers-2026
- [S28] https://www.insurancebusinessmag.com/us/news/breaking-news/captive-insurance-premiums-hit-us79-billion-as-growth-defies-softening-market-577013.aspx
- [S29] https://www.captive.com/news/global-captive-market-grows-as-us-offshore-domiciles-compete
- [S30] https://www.insurance.ca.gov/01-consumers/120-company/04-mrktshare/2025/upload/RRGIndMktShr2025Prem.pdf
