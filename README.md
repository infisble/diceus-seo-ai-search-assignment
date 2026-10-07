# DICEUS · Senior Technical SEO & AI Search: practical assignment

Confidential: shared privately with DICEUS. Not for publication.

**Start here:** [`deliverables/01_Executive_Strategy.md`](deliverables/01_Executive_Strategy.md), then the [micro-deck](deliverables/DICEUS_SEO_AI_Search_micro_deck.pptx).

## The six required deliverables
| # | Deliverable | Format |
|---|---|---|
| 1 | [01_Executive_Strategy](deliverables/01_Executive_Strategy.md) | Markdown |
| 2 | [02_Current_State_Audit.xlsx](deliverables/02_Current_State_Audit.xlsx) | Excel: 815 crawled URLs plus 15 analysis sheets |
| 3 | [03_Search_Market_and_Opportunity.xlsx](deliverables/03_Search_Market_and_Opportunity.xlsx) | Excel: territories, keywords, SERP sample, competitors, AI panel, backlog |
| 4 | [04_Future_State_and_Transition](deliverables/04_Future_State_and_Transition.md) | Markdown: architecture, transition map, AI search; **Appendix A is the page specification** |
| 5 | [05_90_Day_Execution_Plan.xlsx](deliverables/05_90_Day_Execution_Plan.xlsx) | Excel: 32 tasks with owners, dependencies, Definition of Done and KPIs |
| 6 | [06_Methodology_AI_Workflow_and_Data_Gaps.md](deliverables/06_Methodology_AI_Workflow_and_Data_Gaps.md) | Markdown |

## Supporting material
- **Micro-deck (14 slides):** [EN](deliverables/DICEUS_SEO_AI_Search_micro_deck.pptx) · [UA](deliverables/DICEUS_SEO_AI_Search_micro_deck_UA.pptx). Speaker notes cite the evidence.
- **Walkthrough video (~5 min):** [`deliverables/video/`](deliverables/video/)
- **Research behind the deck:** [competitor teardown](deliverables/competitor_teardown.md) · [services-to-product pivot cases](deliverables/pivot_case_studies.md) · [fact-check of external claims](deliverables/factcheck_external.md)
- **Charts and diagrams:** [`deliverables/assets/`](deliverables/assets/)

## Reproducibility
Every number in the deliverables comes from a script in [`scripts/`](scripts/), which reads raw data in [`data/`](data/). That data includes the crawl of 815 URLs (1 request/s, robots.txt respected), Wayback history, autocomplete, the SERP sample, AI-panel output and Lighthouse results. Strategy decisions live in one module, [`scripts/strategy_data.py`](scripts/strategy_data.py), which feeds the Excel, Markdown, charts, deck and video, so the deliverables cannot drift apart.

```bash
python -m venv .venv && .venv/Scripts/pip install requests beautifulsoup4 lxml openpyxl pandas matplotlib scikit-learn networkx imageio-ffmpeg pillow
# collection (polite, ~1 req/s):   01_crawl -> 01b_head_recheck -> 02_autocomplete -> 03_wayback_psi_tech -> 05_legacy_redirects
# analysis & builds:               04_analyze -> 06_keywords -> 07_charts -> 08_build_excel -> 09_build_docs -> 10_video
# deck:                            cd deck && npm i && node build_deck.js   (UA: python make_ua.py && node build_deck_ua.js)
```

Data access: public sources only. GSC, GA4 and CRM were not available, and every place that depends on them is marked **DATA UNAVAILABLE** or **VALIDATION REQUIRED**.
