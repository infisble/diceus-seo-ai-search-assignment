"""
Charts & diagrams for the deliverables (static PNG, light surface, 1600px wide).
Palette: dataviz reference instance (blue #2a78d6, orange #eb6834, aqua #1baf7a; gray for de-emphasis).
One series -> one color; emphasis = highlight the bar that carries the story, gray the rest.
Output: deliverables/assets/*.png
"""
import json, sys
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import strategy_data as S

D = ROOT / "data"
OUT = ROOT / "deliverables" / "assets"
OUT.mkdir(parents=True, exist_ok=True)

BLUE, ORANGE, AQUA = "#2a78d6", "#eb6834", "#1baf7a"
GRAY, GRAY_L = "#a3a29c", "#d9d8d3"
INK, INK2, MUTED = "#0b0b0b", "#52514e", "#8a8984"
SURF = "#fcfcfb"
plt.rcParams.update({
    "figure.facecolor": SURF, "axes.facecolor": SURF, "savefig.facecolor": SURF,
    "font.family": "DejaVu Sans", "font.size": 12, "axes.edgecolor": GRAY_L, "axes.labelcolor": INK2,
    "xtick.color": INK2, "ytick.color": INK2, "axes.spines.top": False, "axes.spines.right": False,
    "axes.grid": False, "axes.titleweight": "bold", "axes.titlesize": 16, "axes.titlecolor": INK,
})


def title(fig, t, sub=None):
    fig.text(0.02, 0.965, t, fontsize=19, fontweight="bold", color=INK, va="top")
    if sub:
        fig.text(0.02, 0.905, sub, fontsize=12, color=INK2, va="top")


def save(fig, name, src):
    fig.text(0.02, 0.015, "Source: " + src, fontsize=9.5, color=MUTED)
    fig.savefig(OUT / name, dpi=110)
    plt.close(fig)
    print("saved", name)


def hbar(ax, labels, values, highlight, fmt="{:.0f}"):
    colors = [BLUE if h else GRAY for h in highlight]
    y = range(len(labels))
    ax.barh(list(y), values, color=colors, height=0.62, edgecolor=SURF, linewidth=2)
    ax.set_yticks(list(y)); ax.set_yticklabels(labels)
    ax.invert_yaxis()
    ax.xaxis.grid(True, color="#eeede9", linewidth=1); ax.set_axisbelow(True)
    ax.spines["left"].set_visible(False); ax.tick_params(axis="y", length=0)
    for i, v in enumerate(values):
        ax.text(v + max(values) * 0.01, i, fmt.format(v), va="center", fontsize=11,
                color=INK if highlight[i] else INK2, fontweight="bold" if highlight[i] else "normal")


df = pd.read_csv(D / "urls_analyzed.csv")
ok = df[df.status == 200].copy()

# 1 ---------------------------------------------------------------- inventory vs strategy
def layer(r):
    t = r.page_type
    if t in ("insurance_product", "insurance_products_hub"): return "Insurance products (L1)"
    if t in ("insurance_service", "insurance_hub"): return "Insurance services (L2/L3)"
    if t in ("generic_service", "services_hub", "expertise_service", "expertise_hub"): return "Generic IT services + expertise"
    if t in ("industry_service", "industry_vertical_hub", "industry_hub"): return "Non-insurance industries"
    if t == "blog_post": return "Blog: insurance" if r.insurance_relevant else "Blog: non-insurance"
    if t in ("case_study", "case_hub"): return "Case studies"
    if t in ("media_news", "media_hub"): return "News / media"
    if t in ("pagination", "case_filter_archive", "author", "blog_archive"): return "Archives & pagination"
    return "Corporate / utility / other"
ok["layer"] = ok.apply(layer, axis=1)
inv = ok.layer.value_counts()
order = ["Insurance products (L1)", "Insurance services (L2/L3)", "Generic IT services + expertise", "Non-insurance industries",
         "Blog: insurance", "Blog: non-insurance", "Case studies", "News / media", "Archives & pagination", "Corporate / utility / other"]
vals = [int(inv.get(o, 0)) for o in order]
fig, ax = plt.subplots(figsize=(14.5, 7.2)); fig.subplots_adjust(left=0.25, right=0.95, top=0.82, bottom=0.1)
hbar(ax, order, vals, [o.startswith("Insurance products") for o in order])
title(fig, f"The strategic priority: {vals[0] - 1} product pages (+1 hub) of {sum(vals)} indexable URLs",
      "Indexable HTML URLs on diceus.com by business layer. Products are the primary strategy; generic services outnumber them ~7:1.")
ax.set_xlabel("URLs (status 200)")
save(fig, "fig1_inventory_vs_strategy.png", f"own crawl of diceus.com, 2026-10-06 ({len(ok)} URLs, 1 req/s)")

# 2 ---------------------------------------------------------------- contextual links by layer
med = ok.groupby("layer").inlinks_contextual.median().reindex(order[:6])
fig, ax = plt.subplots(figsize=(14.5, 6.2)); fig.subplots_adjust(left=0.25, right=0.95, top=0.8, bottom=0.12)
hbar(ax, list(med.index), list(med.values), [i.startswith("Insurance products") for i in med.index])
title(fig, "Internal links point away from the products",
      "Median contextual (non-template) internal links received per page. Products get ~1/4 of what generic services get.")
ax.set_xlabel("Median contextual inlinks per page")
save(fig, "fig2_contextual_links_by_layer.png", "own crawl + link graph (template links removed by per-target baseline heuristic, see methodology)")

# 3 ---------------------------------------------------------------- opportunity matrix
from collections import defaultdict
from matplotlib.lines import Line2D
fig = plt.figure(figsize=(16, 8.6))
ax = fig.add_axes([0.06, 0.1, 0.52, 0.72])
pts = defaultdict(list)
for t in S.TERRITORIES:
    pts[(t[5], t[3])].append(t)
for (feas, rel), ts in pts.items():
    for k, t in enumerate(ts):
        dx = (k - (len(ts) - 1) / 2) * 0.32
        sc = S.territory_score(t)
        col = BLUE if sc >= 4.2 else (ORANGE if sc >= 3.0 else GRAY)
        ax.scatter(feas + dx, rel, s=160 + t[4] * 200, color=col, alpha=0.9, edgecolor=SURF, linewidth=2, zorder=3)
        ax.text(feas + dx, rel, t[0][1:], ha="center", va="center", fontsize=9, color="white", fontweight="bold", zorder=4)
ax.set_xlim(-0.6, 5.7); ax.set_ylim(0.4, 5.6)
ax.set_xlabel("SEO feasibility  ->  easier"); ax.set_ylabel("Business relevance  ->  higher")
ax.grid(True, color="#eeede9"); ax.set_axisbelow(True)
leg = [Line2D([0], [0], marker="o", color="w", markerfacecolor=c, markersize=12, label=l) for c, l in
       ((BLUE, "Priority 1 (score >= 4.2)"), (ORANGE, "Priority 2 (3.0-4.2)"), (GRAY, "Maintain / validate (< 3.0)"))]
ax.legend(handles=leg, loc="upper left", frameon=False, fontsize=10, title="Bubble size = demand evidence (proxy)", title_fontsize=9.5)
ranked = sorted(S.TERRITORIES, key=S.territory_score, reverse=True)
fig.text(0.62, 0.82, "Territories ranked by priority score", fontsize=12.5, fontweight="bold", color=INK)
for i, t in enumerate(ranked):
    sc = S.territory_score(t); col = BLUE if sc >= 4.2 else (ORANGE if sc >= 3.0 else GRAY)
    y = 0.775 - i * 0.044
    fig.text(0.62, y, "●", color=col, fontsize=13, va="center")
    fig.text(0.64, y, f"{t[0][1:]}  {t[1][:52]}", fontsize=10.2, color=INK, va="center")
    fig.text(0.975, y, f"{sc:.2f}", fontsize=10.2, color=INK2, va="center", ha="right")
title(fig, "Where to compete: relevance vs feasibility",
      "Score = 0.45 relevance + 0.35 feasibility + 0.20 demand. Demand = autocomplete/SERP proxy only (volumes: DATA UNAVAILABLE).")
save(fig, "fig3_opportunity_matrix.png", "03_Search_Market_and_Opportunity.xlsx / Territories")

# 4 ---------------------------------------------------------------- AI share of voice
sov_c, n_unb = S.ai_share_of_voice(D / "ai_panel_results.json")
sov = sov_c.most_common(10)
if "DICEUS" not in [b for b, _ in sov]: sov = sov[:9] + [("DICEUS", sov_c["DICEUS"])]
fig, ax = plt.subplots(figsize=(14.5, 6.6)); fig.subplots_adjust(left=0.16, right=0.95, top=0.8, bottom=0.12)
hbar(ax, [s[0] for s in sov], [s[1] for s in sov], [s[0] == "DICEUS" for s in sov])
ax.set_xlabel("Unbranded prompts (of 16) where the brand is named in the answer")
title(fig, "AI answers: DICEUS appears only in the captive / RRG niche",
      "Claude + web search, 16 unbranded prompts, 1 run each (directional). DICEUS wins 2: multi-captive management, RRG software.")
save(fig, "fig4_ai_share_of_voice.png", "AI prompt panel, 2026-10-06 (data/ai_panel_results.json). ChatGPT/Perplexity/AI Overviews: DATA UNAVAILABLE")

# 5 ---------------------------------------------------------------- future architecture
def box(ax, x, y, w, h, text, fc, ec, tc=INK, fs=10.5, bold=False):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.008,rounding_size=0.012", fc=fc, ec=ec, lw=1.6))
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center", fontsize=fs, color=tc, fontweight="bold" if bold else "normal", wrap=True)

def link(ax, x1, y1, x2, y2, c=GRAY):
    ax.plot([x1, x1, x2, x2], [y1, (y1 + y2) / 2, (y1 + y2) / 2, y2], color=c, lw=1.3, zorder=0)

fig = plt.figure(figsize=(18, 10.5)); ax = fig.add_axes([0, 0.03, 1, 0.87]); ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.axis("off")
title(fig, "Future-state architecture: products first, URLs kept",
      "Hierarchy is expressed through navigation, hubs and links - not a URL migration. NEW = page to create; FIX = indexation repair.")
LB = "#e8f1fc"; LO = "#fdeee7"; LA = "#e4f6ef"; LG = "#f1f0ec"
box(ax, 0.36, 0.89, 0.28, 0.08, "HOMEPAGE  /\nBrand + insurance-software product company", BLUE, BLUE, "white", 12, True)
# L1
box(ax, 0.03, 0.70, 0.30, 0.10, "PRODUCTS HUB  /insurance/solutions/\n'insurance software products'", LB, BLUE, fs=11, bold=True)
box(ax, 0.36, 0.70, 0.28, 0.10, "ALTERNATIVE RISK HUB\n/insurance/solutions/alternative-risk-platform/", LA, AQUA, fs=11, bold=True)
box(ax, 0.67, 0.70, 0.30, 0.10, "SOLUTIONS BY BUYER  NEW /insurance/for/...\ncarriers | L&H | MGAs | brokers | self-insured", LO, ORANGE, fs=10.5, bold=True)
for x in (0.18, 0.50, 0.82): link(ax, 0.5, 0.89, x, 0.80)
core = ["Policy Administration System", "Underwriting Workbench (commercial / life / health)", "Claims Mgmt  (VALIDATE -> NEW)", "Reinsurance Platform",
        "Group Insurance Platform (+ health FIX)", "General Ledger Platform", "Insurance Data Warehouse", "Broker & Customer Portals, Super App"]
for i, t in enumerate(core):
    y = 0.62 - i * 0.062
    box(ax, 0.05, y, 0.26, 0.05, t, "white", BLUE, fs=9.5)
    ax.plot([0.04, 0.04, 0.05], [0.70, y + 0.025, y + 0.025], color=GRAY, lw=1)
alt = ["Captive Management Software (FIX noindex) - managers", "Captive Insurance Software - captive owners", "Captive Owner Portal",
       "RRG Management Platform (FIX noindex)", "Self-insurance admin capability (validate)", "Features: bordereaux, cell accounting,\nfilings  NEW (validate demand)",
       "Compare: Origami Risk alternatives  NEW", "Captive knowledge hub /captive-insurance/"]
for i, t in enumerate(alt):
    y = 0.62 - i * 0.062
    box(ax, 0.38, y, 0.26, 0.05, t, "white", AQUA, fs=9.2)
    ax.plot([0.37, 0.37, 0.38], [0.70, y + 0.025, y + 0.025], color=GRAY, lw=1)
seg = ["Captive managers -> Captive Mgmt page", "Risk retention groups -> RRG page", "Self-insured groups & pools  NEW", "MGAs & program admins  NEW", "P&C carriers  NEW (later)", "Life & health insurers  NEW (later)", "Brokers -> Broker portal"]
for i, t in enumerate(seg):
    y = 0.62 - i * 0.062
    box(ax, 0.69, y, 0.26, 0.05, t, "white", ORANGE, fs=9.5)
    ax.plot([0.68, 0.68, 0.69], [0.70, y + 0.025, y + 0.025], color=GRAY, lw=1)
# bottom layers
box(ax, 0.03, 0.03, 0.30, 0.09, "INSURANCE SERVICES HUB  /insurance/\nimplementation | modernization | integration | QA\n(18 pages; overlaps -> VALIDATE)", LG, GRAY, fs=9.5)
box(ax, 0.36, 0.03, 0.28, 0.09, "INSIGHTS & PROOF\n86 insurance posts -> spokes of product hubs\n118 case studies -> product proof blocks", LG, GRAY, fs=9.5)
box(ax, 0.67, 0.03, 0.30, 0.09, "TECHNOLOGY SERVICES (secondary)\n/services/ 104 | /expertise/ 30 | /industry/ 56\nkeep, demote from main nav, VALIDATE", LG, GRAY, fs=9.5)
ax.text(0.5, 0.135, "contextual links flow UP from services, insights and proof into product & segment pages", ha="center", fontsize=10.5, color=INK2, style="italic")
save(fig, "fig5_future_architecture.png", "04_Future_State_and_Transition.md")

# 6 ---------------------------------------------------------------- transition (page groups -> action)
groups = [("Homepage", 1, "REPOSITION"), ("Product pages", 23, "KEEP + OPTIMIZE"), ("Noindexed products", 3, "FIX"),
          ("Insurance services", 18, "KEEP / VALIDATE consolidate"), ("Generic services/expertise", 134, "KEEP (demote) / VALIDATE"),
          ("Non-insurance industries", 56, "KEEP (demote) / VALIDATE"), ("Insurance blog", 86, "OPTIMIZE (link to products)"),
          ("Other blog", 133, "KEEP / VALIDATE later"), ("Case filter archives", 128, "DEINDEX (validate)"), ("New pages (planned)", 7, "CREATE")]
acols = {"REPOSITION": ORANGE, "FIX": ORANGE, "CREATE": AQUA, "OPTIMIZE (link to products)": BLUE, "KEEP + OPTIMIZE": BLUE}
fig, ax = plt.subplots(figsize=(15, 8)); fig.subplots_adjust(left=0.02, right=0.98, top=0.83, bottom=0.08); ax.axis("off")
ax.set_xlim(0, 1); ax.set_ylim(0, len(groups) + 0.5)
for i, (g, n, a) in enumerate(groups):
    y = len(groups) - i - 0.5
    c = acols.get(a, GRAY)
    ax.add_patch(FancyBboxPatch((0.02, y - 0.33), 0.30, 0.66, boxstyle="round,pad=0.005,rounding_size=0.02", fc="#f4f3ef", ec=GRAY_L))
    ax.text(0.04, y, g, va="center", fontsize=12, color=INK); ax.text(0.30, y, str(n), va="center", ha="right", fontsize=12, color=INK2, fontweight="bold")
    ax.annotate("", xy=(0.55, y), xytext=(0.33, y), arrowprops=dict(arrowstyle="-|>", color=c, lw=2))
    ax.add_patch(FancyBboxPatch((0.56, y - 0.33), 0.42, 0.66, boxstyle="round,pad=0.005,rounding_size=0.02", fc="white", ec=c, lw=1.8))
    ax.text(0.58, y, a, va="center", fontsize=12, color=INK, fontweight="bold" if c != GRAY else "normal")
title(fig, "Current -> future: change the weight, not the URLs",
      "Page groups (URL counts) and their action. Destructive actions on unvalidated groups are VALIDATE BEFORE ACTION.")
save(fig, "fig6_transition_map.png", "04_Future_State_and_Transition.md / transition table")

# 7 ---------------------------------------------------------------- 90-day gantt
cls_col = {"MUST DO": BLUE, "HIGH-VALUE NEXT": AQUA, "LATER / VALIDATE FIRST": GRAY}
plan = sorted(S.PLAN, key=lambda p: (p[0][:2], int(p[3].split("-")[0]), p[0]))
fig, ax = plt.subplots(figsize=(18, 11.5)); fig.subplots_adjust(left=0.40, right=0.98, top=0.88, bottom=0.07)
for i, p in enumerate(plan):
    a, b = [int(x) for x in p[3].split("-")]
    ax.barh(i, b - a + 1, left=a, color=cls_col[p[4]], height=0.6, edgecolor=SURF, linewidth=2)
def short(t, n=72):
    if len(t) <= n: return t
    cut = t[:n].rsplit(" ", 1)[0].rstrip(",;:(")
    return cut + " ..."
ax.set_yticks(range(len(plan))); ax.set_yticklabels([f"{p[0]}  {short(p[2])}" for p in plan], fontsize=9.3)
ax.invert_yaxis(); ax.set_xlim(0, 91)
for x in (30, 60):
    ax.axvline(x + 0.5, color=GRAY_L, lw=1)
ax.set_xticks([1, 15, 30, 45, 60, 75, 90]); ax.set_xlabel("Day")
ax.spines["left"].set_visible(False); ax.tick_params(axis="y", length=0)
for x, t in ((15, "Days 1-30: fix, baseline, decide"), (45, "Days 31-60: reposition & build"), (75, "Days 61-90: validate & scale")):
    ax.text(x, -1.3, t, ha="center", fontsize=11, color=INK, fontweight="bold")
leg = [Line2D([0], [0], color=c, lw=8, label=l) for l, c in cls_col.items()]
ax.legend(handles=leg, loc="lower left", frameon=False, fontsize=10)
title(fig, "90-day execution plan", "Workstreams, waves and classes (05_90_Day_Execution_Plan.xlsx).")
save(fig, "fig7_90_day_gantt.png", "05_90_Day_Execution_Plan.xlsx")

# 8 ---------------------------------------------------------------- workflow pipeline
steps = [("SOURCE", "diceus.com (sitemaps,\nHTML), Wayback CDX,\nGoogle Autocomplete,\nWeb search, PSI/CrUX,\npublic directories"),
         ("COLLECTION", "Python crawler 1 req/s,\nrobots-aware; collectors;\n3 Claude Code sub-agents\n(company, SERP, AI panel)"),
         ("PROCESSING", "pandas / networkx /\nscikit-learn: classify,\nlink graph, TF-IDF,\nclusters, scoring"),
         ("AI ANALYSIS", "Claude (Opus) in Claude\nCode: hypotheses, intent\nreading, synthesis,\ncode generation"),
         ("HUMAN VALIDATION", "raw-HTML re-checks,\nmanual SERP/URL spot\nchecks, rejected AI\nclaims logged"),
         ("OUTPUT", "6 deliverables,\ncharts, video,\nreusable scripts")]
fig = plt.figure(figsize=(18, 5.2)); ax = fig.add_axes([0, 0, 1, 0.8]); ax.axis("off"); ax.set_xlim(0, 1); ax.set_ylim(0, 1)
w = 0.145
for i, (h, t) in enumerate(steps):
    x = 0.015 + i * (w + 0.018)
    c = AQUA if h == "HUMAN VALIDATION" else (ORANGE if h == "AI ANALYSIS" else BLUE)
    ax.add_patch(FancyBboxPatch((x, 0.08), w, 0.8, boxstyle="round,pad=0.005,rounding_size=0.02", fc="white", ec=c, lw=2))
    ax.add_patch(FancyBboxPatch((x, 0.72), w, 0.16, boxstyle="round,pad=0.005,rounding_size=0.02", fc=c, ec=c))
    ax.text(x + w / 2, 0.8, h, ha="center", va="center", color="white", fontsize=11.5, fontweight="bold")
    ax.text(x + w / 2, 0.40, t, ha="center", va="center", color=INK, fontsize=10.2)
    if i < len(steps) - 1:
        ax.annotate("", xy=(x + w + 0.017, 0.48), xytext=(x + w + 0.001, 0.48), arrowprops=dict(arrowstyle="-|>", color=GRAY, lw=1.6))
title(fig, "Workflow: Source -> Collection -> Processing -> AI analysis -> Human validation -> Output")
save(fig, "fig8_workflow.png", "06_Methodology_AI_Workflow_and_Data_Gaps.md")
