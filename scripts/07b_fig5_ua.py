"""Ukrainian version of fig5 (future-state architecture) for the UA deck. URLs stay in English."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

OUT = Path(__file__).resolve().parents[1] / "deliverables" / "assets" / "fig5_future_architecture_ua.png"
BLUE, ORANGE, AQUA, GRAY = "#2a78d6", "#eb6834", "#1baf7a", "#a3a29c"
INK, INK2, SURF = "#0b0b0b", "#52514e", "#fcfcfb"
plt.rcParams.update({"font.family": "DejaVu Sans", "figure.facecolor": SURF, "savefig.facecolor": SURF})


def box(ax, x, y, w, h, text, fc, ec, tc=INK, fs=10.5, bold=False):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.008,rounding_size=0.012", fc=fc, ec=ec, lw=1.6))
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center", fontsize=fs, color=tc, fontweight="bold" if bold else "normal")


fig = plt.figure(figsize=(18, 10.5)); ax = fig.add_axes([0, 0.03, 1, 0.87]); ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.axis("off")
fig.text(0.02, 0.965, "Цільова архітектура: спершу продукти, URL зберігаємо", fontsize=19, fontweight="bold", color=INK, va="top")
fig.text(0.02, 0.905, "Ієрархія — через навігацію, хаби та посилання, без міграції URL. НОВА = створити сторінку; FIX = виправити індексацію.", fontsize=12, color=INK2, va="top")
LB, LO, LA, LG = "#e8f1fc", "#fdeee7", "#e4f6ef", "#f1f0ec"
box(ax, 0.33, 0.89, 0.34, 0.08, "ГОЛОВНА  /\nБренд + продуктова компанія страхового ПЗ", BLUE, BLUE, "white", 12, True)
box(ax, 0.03, 0.70, 0.30, 0.10, "ХАБ ПРОДУКТІВ  /insurance/solutions/\n«страхові програмні продукти»", LB, BLUE, fs=11, bold=True)
box(ax, 0.36, 0.70, 0.28, 0.10, "ХАБ ALTERNATIVE RISK\n/insurance/solutions/alternative-risk-platform/", LA, AQUA, fs=11, bold=True)
box(ax, 0.67, 0.70, 0.30, 0.10, "РІШЕННЯ ЗА ТИПОМ ПОКУПЦЯ  НОВІ /insurance/for/...\nстраховики | L&H | MGA | брокери | self-insured", LO, ORANGE, fs=10, bold=True)
for x in (0.18, 0.50, 0.82):
    ax.plot([0.5, 0.5, x, x], [0.89, 0.845, 0.845, 0.80], color=GRAY, lw=1.3, zorder=0)
cols = [
    (0.05, BLUE, ["Policy Administration System", "Underwriting Workbench (комерц. / life / health)", "Claims Mgmt  (ПЕРЕВІРИТИ -> НОВА)", "Reinsurance Platform",
                  "Group Insurance Platform (+ health FIX)", "General Ledger Platform", "Insurance Data Warehouse", "Брокерський і клієнтський портали, Super App"]),
    (0.38, AQUA, ["Captive Management (FIX noindex) — менеджери", "Captive Insurance Software — власники captive", "Captive Owner Portal",
                  "RRG Management Platform (FIX noindex)", "Self-insurance (перевірити можливості)", "Функції: bordereaux, облік комірок,\nзвітність  НОВІ (перевірити попит)",
                  "Порівняння: альтернативи Origami Risk  НОВА", "База знань /captive-insurance/"]),
    (0.69, ORANGE, ["Captive-менеджери -> сторінка Captive Mgmt", "RRG -> сторінка RRG", "Self-insured групи та пули  НОВА", "MGA та програмні адміністратори  НОВА",
                    "P&C страховики  НОВА (пізніше)", "Life & health страховики  НОВА (пізніше)", "Брокери -> Broker portal"]),
]
for x0, col, items in cols:
    for i, t in enumerate(items):
        y = 0.62 - i * 0.062
        box(ax, x0, y, 0.26, 0.05, t, "white", col, fs=9.2)
        ax.plot([x0 - 0.01, x0 - 0.01, x0], [0.70, y + 0.025, y + 0.025], color=GRAY, lw=1)
box(ax, 0.03, 0.03, 0.30, 0.09, "ХАБ СТРАХОВИХ ПОСЛУГ  /insurance/\nвпровадження | модернізація | інтеграція | QA\n(18 сторінок; перетини -> ПЕРЕВІРИТИ)", LG, GRAY, fs=9.5)
box(ax, 0.36, 0.03, 0.28, 0.09, "ЕКСПЕРТИЗА ТА ДОКАЗИ\n86 страхових постів -> спиці продуктових хабів\n118 кейсів -> блоки доказів на продуктах", LG, GRAY, fs=9.5)
box(ax, 0.67, 0.03, 0.30, 0.09, "ТЕХНОЛОГІЧНІ ПОСЛУГИ (другорядні)\n/services/ 104 | /expertise/ 30 | /industry/ 56\nзалишити, прибрати з головного меню, ПЕРЕВІРИТИ", LG, GRAY, fs=9.5)
ax.text(0.5, 0.135, "контекстні посилання йдуть ВГОРУ: з послуг, статей і кейсів — у продуктові та сегментні сторінки", ha="center", fontsize=10.5, color=INK2, style="italic")
fig.savefig(OUT, dpi=110); print("saved", OUT)
