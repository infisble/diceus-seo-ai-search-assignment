"""
Narrated walkthrough video (1920x1080, ~3 min) built from the deliverable charts.
- Slides rendered with Pillow (title cards + chart scenes)
- Narration: Windows SAPI TTS (System.Speech) -> WAV per scene
- ffmpeg (imageio-ffmpeg binary): slow zoom + fades per scene, then concat
Output: deliverables/video/DICEUS_SEO_AI_Search_Strategy_walkthrough.mp4
"""
import subprocess, wave
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import imageio_ffmpeg

ROOT = Path(__file__).resolve().parents[1]
A = ROOT / "deliverables" / "assets"
V = ROOT / "deliverables" / "video"
TMP = V / "_tmp"
TMP.mkdir(parents=True, exist_ok=True)
FF = imageio_ffmpeg.get_ffmpeg_exe()
W, H = 1920, 1080
BG, INK, INK2, BLUE, ORANGE, AQUA = (252, 252, 251), (11, 11, 11), (82, 81, 78), (42, 120, 214), (235, 104, 52), (27, 175, 122)
F = lambda s, b=False: ImageFont.truetype("C:/Windows/Fonts/" + ("segoeuib.ttf" if b else "segoeui.ttf"), s)

SCENES = [
    ("card", ("DICEUS", "SEO & AI Search Strategy", "From a services website to a product-led insurance software brand", "Assignment walkthrough  ·  October 2026  ·  US English market"),
     "This is a walkthrough of the SEO and AI search strategy for DICEUS. The company is becoming a product-led insurance software vendor. The question is how its website and its presence in AI answers should change to support that."),
    ("card", ("Method", "Evidence first, public data only", "815 URLs crawled at 1 request per second  ·  709 sitemap URLs  ·  2,098 Wayback URLs\n699 autocomplete queries  ·  44 SERPs sampled  ·  20-prompt AI panel  ·  8 competitor pages", "No GSC, GA4 or CRM access: missing data is marked, never treated as zero"),
     "We crawled the full site politely, at one request per second. We pulled its URL history from the Wayback Machine, discovered the keyword universe through Google Autocomplete, and sampled forty-four search results pages. We also ran a twenty-prompt experiment on AI answers. Every number comes from a script, and missing data is labelled as missing."),
    ("fig", ("Finding 1", "fig1_inventory_vs_strategy.png"),
     "First finding. The strategic priority, insurance software products, is twenty-three product pages, plus one hub, out of eight hundred and fourteen indexable pages. Generic IT services, expertise and non-insurance industries add up to about one hundred and ninety. Structurally, the site is still a services website."),
    ("card", ("Finding 2  ·  critical", "Three product pages are excluded from Google", "<meta name='robots' content='noindex, nofollow' />\n\nCaptive Management Platform  ·  Risk Retention Group Platform  ·  Group Health", "In the XML sitemap, yet hidden by a second hard-coded robots tag. Verified in raw HTML on all 815 URLs."),
     "Second finding, and the most urgent. Three product pages carry a second, hard-coded robots tag that says no index, no follow. Two of them, captive management and risk retention groups, are exactly the pages where DICEUS wins today. This is a free fix with very high upside, so it is task number one."),
    ("fig", ("Finding 3", "fig2_contextual_links_by_layer.png"),
     "Third finding. Internal links point away from the products. A product page gets a median of twenty-four contextual links. A generic service page gets ninety-three. The mega menu adds about three hundred identical links to every page, which flattens any hierarchy."),
    ("card", ("Finding 4", "The homepage competes with a services page", "Homepage title:   DICEUS: Custom Software Development Company\nService page:     Custom Software Development Company | DICEUS\n\nTitle / H1 / URL similarity = 0.99", "The strongest page targets the opposite of the strategy. Fix: hand the generic query to the service page, then reposition the homepage - gated by GSC."),
     "Fourth finding. The homepage title and the custom software development service page are almost identical. The strongest page on the site is chasing the opposite of the strategy. We would move that generic query to the service page first, then reposition the homepage around insurance software products, gated by Search Console data."),
    ("fig", ("Where to compete", "fig3_opportunity_matrix.png"),
     "Where should DICEUS compete? We scored each territory on business relevance, SEO feasibility and evidence of demand. Captive insurance and risk retention group software come out on top. DICEUS already ranks first there, competition is thin, and the VCIA partnership adds credibility. Policy administration has more demand, but Guidewire and Oracle own the head terms."),
    ("fig", ("AI search baseline", "fig4_ai_share_of_voice.png"),
     "In AI answers, DICEUS appeared in two of sixteen unbranded prompts, both in the captive and R R G niche. Broad answers are assembled from analyst lists, review sites and listicles, and DICEUS is absent from all of them. Asked what DICEUS is, the assistant answered with unrelated homonyms. AI visibility is an entity and third-party proof problem."),
    ("fig", ("Future state", "fig5_future_architecture.png"),
     "The future architecture puts products first without migrating URLs. The homepage becomes the brand and product entry. There is a products hub, an alternative risk hub with six spokes, and pages by buyer type for M G As and self-insured groups. Services and content stay, and they link upward into the products."),
    ("fig", ("Transition", "fig6_transition_map.png"),
     "The transition changes the weight, not the URLs. We fix, reposition, optimize and create. Anything destructive, like pruning generic services or merging overlapping pages, waits until Search Console, analytics and backlink data prove it is safe."),
    ("card", ("Production-ready spec", "Captive Management Software page", "Owner of 'captive management software' for captive MANAGERS\nCaptive Insurance Software keeps 'captive insurance software' for OWNERS\nAnswer-first summary  ·  proof  ·  pricing model  ·  FAQ  ·  SoftwareApplication schema", "Acceptance: indexed in 14 days  ·  15+ contextual inlinks  ·  valid schema  ·  LCP < 2.5 s  ·  branded directory listings"),
     "The appendix has a production-ready specification for the captive management software page. It separates captive managers from captive owners so the two captive pages do not cannibalize each other. It defines the outline, the proof required, the schema, the internal links and testable acceptance criteria."),
    ("fig", ("90 days", "fig7_90_day_gantt.png"),
     "The ninety-day plan. Days one to thirty: fix indexation, baseline the data and decide query ownership. Days thirty-one to sixty: reposition the homepage and navigation, and build the alternative risk cluster. Days sixty-one to ninety: validate, consolidate only where proven, and review."),
    ("fig", ("How it was built", "fig8_workflow.png"),
     "Everything is reproducible: scripts collect, process and score the data, AI agents assist with research and synthesis, and every AI claim that drives a decision is verified against raw data. Thank you."),
]


def wrap_lines(draw, text, font, maxw):
    out = []
    for para in text.split("\n"):
        line = ""
        for w in para.split(" "):
            t = (line + " " + w).strip()
            if draw.textlength(t, font=font) <= maxw:
                line = t
            else:
                out.append(line); line = w
        out.append(line)
    return out


def render_card(i, kicker, head, body, foot):
    im = Image.new("RGB", (W, H), BG); d = ImageDraw.Draw(im)
    d.rectangle([0, 0, 24, H], fill=BLUE)
    d.text((140, 170), kicker.upper(), font=F(34, True), fill=ORANGE if "critical" in kicker else BLUE)
    y = 230
    for l in wrap_lines(d, head, F(78, True), 1640):
        d.text((140, y), l, font=F(78, True), fill=INK); y += 100
    y += 40
    mono = "<meta" in body or "Homepage title" in body
    bf = ImageFont.truetype("C:/Windows/Fonts/consola.ttf", 40) if mono else F(42)
    for l in wrap_lines(d, body, bf, 1640):
        d.text((140, y), l, font=bf, fill=INK if mono else INK2); y += 60
    for k, l in enumerate(wrap_lines(d, foot, F(34), 1640)):
        d.text((140, 900 + k * 46), l, font=F(34), fill=INK2)
    p = TMP / f"s{i:02d}.png"; im.save(p); return p


def render_fig(i, kicker, fig):
    im = Image.new("RGB", (W, H), BG); d = ImageDraw.Draw(im)
    d.rectangle([0, 0, W, 90], fill=BLUE)
    d.text((60, 18), kicker, font=F(44, True), fill=(255, 255, 255))
    f = Image.open(A / fig).convert("RGB")
    sc = min((W - 100) / f.width, (H - 130) / f.height)
    f = f.resize((int(f.width * sc), int(f.height * sc)), Image.LANCZOS)
    im.paste(f, ((W - f.width) // 2, 100 + (H - 110 - f.height) // 2))
    p = TMP / f"s{i:02d}.png"; im.save(p); return p


def tts(i, text):
    wav = TMP / f"s{i:02d}.wav"
    ps = (f"Add-Type -AssemblyName System.Speech; $s=New-Object System.Speech.Synthesis.SpeechSynthesizer; "
          f"try {{ $s.SelectVoice('Microsoft Zira Desktop') }} catch {{}}; $s.Rate=0; "
          f"$s.SetOutputToWaveFile('{wav}'); $s.Speak(@'\n{text}\n'@); $s.Dispose()")
    subprocess.run(["powershell", "-NoProfile", "-Command", ps], check=True)
    with wave.open(str(wav)) as w:
        return wav, w.getnframes() / w.getframerate()


def main():
    parts = []
    for i, (kind, args, narr) in enumerate(SCENES):
        img = render_card(i, *args) if kind == "card" else render_fig(i, *args)
        wav, dur = tts(i, narr)
        dur = dur + 1.2
        n = int(dur * 30)
        out = TMP / f"s{i:02d}.mp4"
        vf = (f"scale=3840:-1,zoompan=z='min(zoom+0.00025,1.05)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={n}:s={W}x{H}:fps=30,"
              f"fade=t=in:st=0:d=0.5,fade=t=out:st={dur - 0.5:.2f}:d=0.5,format=yuv420p")
        subprocess.run([FF, "-y", "-loglevel", "error", "-i", str(img), "-i", str(wav), "-filter_complex",
                        f"[0:v]{vf}[v];[1:a]apad=pad_dur=1.2,afade=t=in:d=0.2[a]", "-map", "[v]", "-map", "[a]",
                        "-t", f"{dur:.2f}", "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-c:a", "aac", "-b:a", "128k", "-ar", "44100", str(out)], check=True)
        parts.append(out); print(f"scene {i} {dur:.1f}s", flush=True)
    lst = TMP / "list.txt"
    lst.write_text("\n".join(f"file '{p.as_posix()}'" for p in parts))
    final = V / "DICEUS_SEO_AI_Search_Strategy_walkthrough.mp4"
    subprocess.run([FF, "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", str(lst), "-c", "copy", "-movflags", "+faststart", str(final)], check=True)
    print("video:", final)


if __name__ == "__main__":
    main()
