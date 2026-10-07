"""
Renders the transition table + plan tables into Markdown fragments that the hand-written documents include,
so tables in 04 / 01 always match strategy_data.py and the Excel files.
Output: deliverables/_fragments/*.md
"""
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import strategy_data as S

OUT = ROOT / "deliverables" / "_fragments"
OUT.mkdir(parents=True, exist_ok=True)


def md_table(headers, rows):
    esc = lambda x: str(x).replace("|", "\\|").replace("\n", " ")
    lines = ["| " + " | ".join(headers) + " |", "|" + "---|" * len(headers)]
    lines += ["| " + " | ".join(esc(c) for c in r) + " |" for r in rows]
    return "\n".join(lines) + "\n"


(OUT / "transition.md").write_text(md_table(
    ["Page / group", "Current URL(s)", "Current role", "Evidence", "Future role", "Action", "Prio", "Risk", "Dependency", "Validation required"],
    S.TRANSITION), encoding="utf-8")
(OUT / "territories.md").write_text(md_table(
    ["ID", "Territory", "Rel.", "Demand (proxy)", "Feas.", "Score", "Play"],
    [(t[0], t[1], t[3], t[4], t[5], S.territory_score(t), t[8]) for t in sorted(S.TERRITORIES, key=S.territory_score, reverse=True)]), encoding="utf-8")
(OUT / "top5.md").write_text("\n".join(
    f"**{d}**\n\n- *Evidence:* {e}\n- *Expected impact:* {i}\n- *Rationale:* {r}\n- *Dependency / risk:* {k}\n" for d, e, i, r, k in S.TOP5), encoding="utf-8")
(OUT / "notyet.md").write_text("\n".join(
    f"**{n+1}. {d}**\n\n- *Unknown:* {u}\n- *Why acting now is risky:* {w}\n- *Evidence needed first:* {e}\n" for n, (d, u, w, e) in enumerate(S.NOT_YET)), encoding="utf-8")
import pandas as pd
lr = ROOT / "data" / "legacy_redirects.csv"
if lr.exists():
    L = pd.read_csv(lr)
    L["final"] = L.final_status.astype(str)
    piv = L.groupby(["group", "final"]).size().unstack(fill_value=0)
    rows = [(g, int(r.sum()), *[int(r.get(c, 0)) for c in ("200", "404", "410")], int(L[(L.group == g)].hops.ge(2).sum())) for g, r in piv.iterrows()]
    txt = (f"Wayback CDX returned 2,098 historical HTML URLs (1,475 clean paths); **785** are not in today's sitemaps. "
           f"We re-checked **{len(L)}** of them hop-by-hop: all insurance-related and section paths, plus deterministic samples of case studies and root-level posts.\n\n"
           + md_table(["Group", "Checked", "Final 200", "Final 404", "Final 410", "Chains (≥2 hops)"], rows))
    bad = L[(L.final.isin(["404", "410"])) & (L.group.isin(["insurance", "section"]))]
    if len(bad):
        txt += ("\n**FACT — legacy insurance/section URLs that now end in 404/410 (equity-loss candidates; prioritise by referring domains, DATA UNAVAILABLE):**\n\n"
                + md_table(["Legacy path", "First seen (Wayback)", "Chain"], bad[["legacy_path", "wayback_first_seen", "chain"]].values.tolist()[:25]))
    ok_ins = L[(L.group == "insurance") & (L.final == "200")]
    txt += (f"\n**INF:** the `/industry/insurance/*` → `/insurance/*` migration and the 'vitaminise' rename were mostly redirected "
            f"({len(ok_ins)} of {(L.group == 'insurance').sum()} insurance legacy URLs resolve to a 200). REC: fix 404s that have backlinks, collapse chains to one hop (plan W1-05). Full list: 02 › Legacy_Redirects.\n")
    (OUT / "legacy.md").write_text(txt, encoding="utf-8")
else:
    (OUT / "legacy.md").write_text("Legacy check: NOT CHECKED (data/legacy_redirects.csv missing).\n", encoding="utf-8")
print("fragments written")

# ---- assemble documents: docs_src/*.md with {{fragment}} placeholders -> deliverables/*.md
SRC = ROOT / "docs_src"
for src in sorted(SRC.glob("*.md")):
    txt = src.read_text(encoding="utf-8")
    for frag in OUT.glob("*.md"):
        txt = txt.replace("{{" + frag.stem + "}}", frag.read_text(encoding="utf-8"))
    (ROOT / "deliverables" / src.name).write_text(txt, encoding="utf-8")
    print("built", src.name)
