# SERP & Organic Competitor Research: diceus.com (US English)

Collected 2026-10-06. Raw data: `serp_observations.json` (44 queries, 11 territories).

## Method and caveats (read first)

- **FACT:** I ran one search per query with the WebSearch tool (standard mode, US). No paid SEO tools (Ahrefs, Semrush, GSC) were available, so this file has **no search volumes, keyword difficulty or traffic estimates**.
- **CAVEAT: WebSearch results are a proxy, not a Google US SERP replica.** The backend often returns:
  - several locale copies of the same page (Oracle x5, Guidewire x8, Marsh x7, GetApp/Capterra x9);
  - staging hosts and `?p=` IDs;
  - parasite spam on hacked subdomains, which Google would normally cluster or filter.
  
  Read positions as directional only. Two brand queries ("DICEUS", "DICEUS captive") failed to resolve the brand at all. That is almost certainly a proxy artefact. Check both manually in Google US (incognito, US VPN).
- Labels used below:
  - **FACT/OBSERVED**: seen in the SERP sample or on a fetched page.
  - **INFERENCE**: my interpretation.
- I fetched 8 competitor/DICEUS pages, one request each: Origami Risk, Insurity, Duck Creek, Insly, Sapiens, BriteCore, Innowise and DICEUS captive.

## 0. Headline numbers (OBSERVED, proxy)

| Metric | Value |
|---|---|
| Queries sampled | 44 |
| Queries where a **diceus.com** URL appears | 7 (6 non-brand) |
| Queries where only a **DICEUS directory listing** appears (GetApp/Capterra/SoftwareAdvice) | 6 |
| Any DICEUS presence | 13 / 44 (30%) |
| diceus.com at #1 | 5: *captive insurance software*, *risk retention group software*, *alternative risk management software*, *insurance general ledger software*, *insurance data warehouse* |
| diceus.com in top 3 (not #1) | *broker portal software insurance* (#2 + #3, duplicate URLs) |
| Head terms with DICEUS owned page | 0 (PAS, claims, underwriting, reinsurance, MGA, services) |

**DICEUS directory listings (FACT for some, INFERENCE for others):**
- **FACT:** GetApp listing 2089539 "Policy Administration System" has vendor = Diceus and 0 reviews (WebFetch).
- **FACT:** The 2092898 "Reinsurance Financial and Data Exchange Platform" snippet names DICEUS.
- **INFERENCE:** The other GetApp/Capterra listings are also DICEUS. They use the same ID ranges and DICEUS product names:
  - Broker Web Portal
  - Insurance customer portal
  - Insurance Data Warehouse
  - Underwriting Workbench
  - Captive Management Platform
  - Captive Owner Portal

  All appear to have **0 reviews**.

## 1. Organic competitor matrix

How often each domain appeared across the 44 queries (unique domain per query, OBSERVED):

### (a) Product vendors

| Domain | Queries | Where seen | Tier / relevance to DICEUS |
|---|---|---|---|
| guidewire.com (+ marketplace) | 4 | P&C PAS, UW software, data platform, GL marketplace | Tier-1; head terms. Indexes `.md` copies of product pages (FACT), which makes it LLM-friendly |
| sapiens.com | 3 | reinsurance software, reinsurance accounting (#1), statutory | Tier-1; **direct rival in reinsurance** |
| fineos.com | 2 (+ snippets in 3 more) | UW software, group benefits, self-insured | Rival in **group / self-insured** |
| insurity.com | 2 | MGA software, UW for MGAs (both PR pages) | Rival in **MGA / program** |
| insly.com | 2 (5 URLs) | MGA software (#1 + self-made listicles), broker portal glossary | **Closest mid-market analogue**: product-led, modular, MGA-focused |
| oracle.com | 2 | PAS head term, PAS modernization | Tier-1 |
| salesforce.com (+ trailhead) | 3 | claims, group benefits, insurance data model | Platform vendor |
| hyperexponential.com | 2 | UW workbench (#1 blog), UW for MGAs (#1) | Rival in **UW workbench / MGA** |
| vertafore.com (MGA Systems, Surefyre) | 2 | PAS for MGAs, UW for MGAs | Rival in **MGA / program admin** |
| britecore.com | 1 | PAS for MGAs (#2) | Mid-market PAS |
| selectsys.com (Expert Insured) | 3 | PAS for MGAs, accounting, UW for MGAs | Mid-market MGA/program; uses **programmatic state pages** |
| marsh.com / aon.com | 2 | captive insurance software (#2), captive mgmt system (#1) | **Captive managers with in-house tech.** They are the visible captive "competitors" in the proxy |
| origamirisk.com | 1 | captive mgmt system | **Key captive/RRG/risk pool/TPA rival** (INFERENCE: stronger in real Google) |
| riskonnect.com | 2 | self-insured claims, self-insurance admin | RMIS; self-insured rival |
| appian.com | 1 (8 URLs) | life UW workbench | Monopolizes its own named-product SERP |
| fisglobal.com / sovos.com | 2 / 1 | statutory / accounting | Finance specialists |
| duckcreek.com | 1 | reinsurance mgmt (blog) | Tier-1 |
| Others seen once | | | Insuresoft, Comarch, Meon, Vitech, Sentro, Claimable, Optalitix, Loss Run Pro, Appulate, FurtherAI, AccountingSeed, NetSuite, Illumifin, IBM |

**Not seen in this proxy sample (INFERENCE: likely present in real Google US):**
- Majesco, EIS, Socotra, OneShield, Ventiv, Instec, Global Captive Management System.
- They should be checked manually for "captive insurance software" and "PAS for MGAs".

### (b) Aggregators, directories, analysts, marketplaces

| Domain | Queries | Note |
|---|---|---|
| GetApp / Capterra / SoftwareAdvice (Gartner Digital Markets) | 10 | The most frequent domain group. Mostly **DICEUS's own 0-review listings** |
| g2.com | 6 | Claims, health claims, "alternatives" pages. **No DICEUS presence seen** |
| celent.com (VendorMatch) | 5 | PAS NA report, reinsurance, MGA, data. **Claim a DICEUS profile** |
| sourceforge.net | 4 | Reinsurance (6 URLs), agency mgmt, data |
| trustradius.com | 3 | Has a DICEUS profile (FACT) |
| us.fitgap.com | 3 | Thin AI category pages (group, self-insured) |
| platform.softwareone.com / AWS / MS AppSource / InsureMO partner apps / Guidewire Marketplace | 3 / 1 / 2 / 3 / 1 | **Marketplaces rank well for niche product terms.** DICEUS is an InsureMO partner (FACT, logo on site) |
| gartner.com Peer Insights | 1 | #1 for "insurance claims management system". DICEUS shows a Gartner 5/5 (6 reviews) badge (FACT) |
| cbinsights.com, verdantix, aite-novarica | 3 / 1 / 1 | Analyst profiles |

### (c) Dev agencies / services competitors

| Domain | Queries | Note |
|---|---|---|
| damcogroup.com | 4 | Ranks on product-style terms (P&C PAS, health claims, PAS software, legacy modernization) with **solution pages under `/insurance/`**. Closest structural analogue to DICEUS's hybrid model |
| cleveroad.com | 2 | #1 agency mgmt, #3 legacy modernization (long guides) |
| hexaware.com | 2 | #1 legacy modernization, #2 PAS modernization |
| innowise.com, spaceo.ca | 2 each | Services head terms |
| decerto.com | 2 | Polish insurance software house. #1 "insurance PAS software", #3 "UW workbench" (blog). **Direct CEE peer** |
| Seen once | | solulab, leewayhertz, cmarix, codica, mindinventory, 8seneca, engineerbabu, visionet, hicron, botree, bacancy, 75way, netguru, msg-global, xceedance, centric, deloitte |

- **Not seen in this sample:** ScienceSoft, Itransition, Intellias (named only inside a listicle snippet), N-iX, SoftServe, Openkoda.
- **INFERENCE:** Several of these likely rank in real Google for services terms.

### (d) Publishers / trade press

- insurancebusinessmag.com (2)
- Captive Review (captive mgmt)
- insurancethoughtleadership.com, insurancetech.com, insurancejournal.com, propertycasualty360.com, roughnotes.com, commercialriskonline.com, postonline.co.uk, fintechfutures.com, businesswire.com
- Listicle hosts: whatfix, flowforma, connecteam, shoeboxed, dribbble, riseuplabs, lowcode.agency, avixa xchange

**INFERENCE:** For alt-risk, Captive Review and Captive.com are the main PR and link targets.

## 2. Competitor structure deep-dives (OBSERVED via WebFetch)

| Competitor | IA model (Products vs Solutions vs Segments vs Services) | Product/segment page pattern | Proof | CTA |
|---|---|---|---|---|
| **Origami Risk** | **Platform** (Admin portal, Integrations/API, AI, Reporting, Mobile, Implementation) → **Solutions** by suite (P&C Insurance: Policy Admin, Billing, Claims, MPL, WC; RMIS; EHS; GRC; Healthcare) → **Industries** (P&C Insurance page addresses Carriers, MGAs, **Risk Pools, TPAs**) | One platform, many configured "solutions". Segment pages cover alt-risk buyers (pools, TPAs) | Logos, analyst | "Request a demo" in header and footer |
| **Insurity** | **Platform** with clean product URLs `/platform/ratio-policy-ai`, `/platform/workers-comp-suite`, `/platform/premium-audit`, `/platform/billing-as-a-service`. Segments (Commercial, Personal, Specialty, MGAs, WC, TPAs) are handled outside the product tree | Product = branded module, segment = audience page. PR used heavily for ranking ("five of top 10 MGAs") | "Trusted by 500+ insurers", named Chubb/Zurich/Nationwide, outcome metrics (45-sec risk assessment, 98% retention) | "Book a demo" as a **top-level nav item** |
| **Duck Creek** | Most mature split: **Intelligent Applications** (Policy, Rating, Billing, Claims, UW) / **Beyond Core** (Portals, Distribution, Reinsurance, Loss Control) / **Platforms** / **Agents** (Agentic UW Workbench, FNOL) + **Who We Help** by **LOB** (`/solutions/[line]/`) and by **role** (Underwriters, Claims leaders, Tech leaders) + region | `/product/[name]/` vs `/solutions/[lob]/` vs `/resources/[type]/` | 390+ customers, 33 of top-50 NA carriers, Gartner MQ Leader, Everest PEAK, Celent Luminary | "Talk with an Expert" |
| **Insly** (closest mid-market analogue) | **Solutions** split **By company type** (MGAs / Insurers / Brokers) and **By solution** (Product Builder, Distribution, Accounting, Claims, AI "Nora" on a sub-domain). Pricing page exists | Segment page H1 "Low-risk MGA Insurance Software". 4 modular cards → 6 "why" blocks → 1 testimonial → **3-step implementation timeline with durations (2-3 wks / 1-3 mo / 3+ mo)** → CTA. No FAQ, no logos. Also **self-published "Top MGA software providers" listicles** that rank | 1 testimonial | "Book a demo", pricing link (no prices) |
| **Sapiens** | **Offerings** (Core, Business Apps, Platform, Services) vs **Business Lines** (P&C, L&A, WC, Reinsurance, MPL, Specialty). **Regional folders** `/us/` | `/us/reinsurance/` is a thin hub (H1 "Reinsurance", 2 benefit sections, 2 product cards linking to ReinsuranceMaster/ReinsurancePro). **No proof, no FAQ on page.** It ranks through brand authority + Celent + video | None on page | "Learn more", "Contact us" |
| **BriteCore** | Single **Platform** + **Solutions** in 3 axes: by **role** `/why-britecore-by-role/[fn]`, by **type** `/why-britecore/for-mgas`, by **driver** (`/why-britecore/modernization`) | MGA page: H1 benefit statement, 5 pillars of 2-3 sentences, 1 CEO quote. Shallow but intent-matched | 1 quote | "Get a Demo" |
| **Innowise** (services rival) | Insurance sits under `/finance/insurance/`. Services-first IA | Long page: 10 solution types → tech → services → features → stack → process → cases → testimonials → **7-Q FAQ** → form | Clutch, ISO, cloud partner badges | "Contact us" x6 |
| **DICEUS** (for contrast) | `Insurance` → **Solutions** (`/insurance/solutions/[name]/`) / **Services** (`/insurance/[service]/`) / Insights / Resources / Case studies | Captive page: H1 exact-match; tabbed modules with **deep feature lists** (Policies 11, Invoicing 9, Products 8, Config 11); 4-Q FAQ; 12 related-product cards; MACH/API; DocuSign | Gartner 5/5 (6), Clutch 4.9 (49), partner logos (VCIA, InsureMO). **No customer logos, case study or metrics specific to captives** on page | "Book a demo" + contact form |

Schema was not visible through WebFetch's markdown conversion. **Not assessed**; check with Rich Results Test.

**Patterns that win (INFERENCE from the above + SERPs):**
1. **Segment pages per buyer type** ("for MGAs", "for risk pools/TPAs", "for program administrators") sit separately from module/product pages. They are what rank for "X for MGAs" queries (hx `/segments/mga`, BriteCore `/why-britecore/for-mgas`, Optalitix `/organisations/mgas`).
2. **Clean, single product URL per module.** Insurity uses `/platform/x`, Duck Creek uses `/product/x`. DICEUS has two live URL sets (`/solutions/x` and `/insurance/solutions/x`), plus legacy `/industry/insurance/...` URLs, plus an indexed staging host.
3. **Proof is quantified and named** for tier-1/2 vendors (customer counts, logos, analyst badges). Mid-market (Insly, BriteCore) gets by with 1 testimonial + implementation timeline.
4. **Multi-surface distribution** (marketplaces, directories, PR, self-published listicles) lets mid-size vendors take several SERP slots. Examples: Appian 8/9 on "life underwriting workbench", Insly 4/9 on "MGA software", Sentro on MS AppSource.

## 3. Where DICEUS can and cannot compete

### Can compete / already winning (alt-risk, finance and data niches)

| Query cluster | Status | Why winnable |
|---|---|---|
| captive insurance software | #1 + #3 (OBSERVED) | Rivals are captive managers (Marsh/Aon), not SEO-optimized vendors |
| risk retention group software | #1, the only software page (OBSERVED) | Rest is news/law/spam |
| alternative risk (platform) | #1 (OBSERVED) | But SERP intent is muddled by "alternatives to" ERM. Re-target to "alternative risk transfer software", "captive & RRG platform", "self-insured fund software" (INFERENCE) |
| insurance general ledger software / insurance data warehouse | #1 (OBSERVED) | Low competition; analyst + marketplace pages only |
| broker portal software insurance | #2-3 (OBSERVED) | Fix the duplicate URLs to consolidate signals |
| self-insurance administration software; claims admin for self-insured; program administrator software; group insurance admin software | Absent, **weak SERPs** (FitGap thin pages, 2006 articles, PDFs) | Low-effort gaps that fit the alt-risk product line (INFERENCE) |
| captive management software; captive insurance management system | Own page absent (directory only / Marsh, Aon, Origami) | Close variants of a term DICEUS already owns. Add H2/sections and supporting pages (INFERENCE) |
| reinsurance accounting software | 4 directory slots, own page absent | Sapiens dominant but beatable for the long tail ("reinsurance data exchange", "bordereaux reinsurance accounting") |
| UW workbench / UW for MGAs | Absent | Mid-tier field (hx, Insly, Optalitix, Decerto). Needs a dedicated MGA segment page + explainer (INFERENCE: medium difficulty) |

### Cannot realistically compete (head terms)

| Query | Who owns it | Recommended play |
|---|---|---|
| policy administration system / P&C PAS / insurance underwriting software | Guidewire, Oracle, FINEOS, Celent | Don't target head-on; go for long-tail ("PAS for captives", "PAS for RRGs", "PAS for MGAs") |
| claims management software for insurance / insurance claims management system | Listicles (Whatfix), G2, Gartner Peer Insights, TrustRadius | **Get included and reviewed** (Gartner Peer Insights, G2, Capterra reviews) rather than outrank |
| statutory accounting software | Sovos, FIS, Sapiens | Adjacent only (e.g. Schedule F for RRGs/captives) |
| insurance software development company/services, insurance app development | ~15 outsourcing agencies + parasite spam + listicles | Keep services pages for existing demand; listicle inclusion; not the growth bet |
| insurance data model, health claims mgmt, captive owner portal, DICEUS (bare) | Off-intent SERPs (Salesforce Trailhead, provider RCM, Wi-Fi captive portals, homonyms) | Avoid or re-phrase |

## 4. Technical / entity flags found incidentally (OBSERVED)

1. **Duplicate product URLs indexed.** `diceus.com/solutions/broker-web-portal` and `/insurance/solutions/broker-web-portal/` both rank. The same applies to `insurance-data-warehouse`.
2. **Staging host indexed:** `likeprod.diceus.com/insurance/agency-management/`.
3. **Legacy path indexed:** `diceus.com/industry/insurance/claims-management`.
4. **Brand+category SERP surfaces services pages** ("...software development services" titles), not product pages. This conflicts with the product-led positioning.
5. **Many DICEUS directory listings have 0 reviews.** The listings rank, but without reviews they cannot win comparison/"best X" placement. G2 shows no DICEUS listing in the sampled SERPs.
6. **Brand-entity weakness (INFERENCE, verify in Google):**
   - The proxy could not resolve "DICEUS" or "DICEUS captive".
   - A homonym game ("Dicedus", Jan 2026) exists.
   - There are no Wikipedia/Wikidata-type entity signals.
