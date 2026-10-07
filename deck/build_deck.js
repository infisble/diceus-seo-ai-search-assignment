// DICEUS micro-presentation: "From dev shop to insurance software vendor"
// Data sources: ../data/*.md|csv (crawl, SERP, AI panel, competitor teardown, pivot cases), ../scripts/strategy_data.py
const pptxgen = require("pptxgenjs");
const path = require("path");
const fs = require("fs");
const { applyTheme } = require("./apply_theme.js");

const THEME = {
  name: "DICEUS Strategy",
  headFontFace: "Cambria",
  bodyFontFace: "Calibri",
  colors: {
    dk1: "111827", lt1: "FFFFFF", dk2: "14213D", lt2: "EEF2F7",
    accent1: "14213D", accent2: "0F9D8A", accent3: "E4572E", accent4: "F2A541", accent5: "6B7A99", accent6: "9AA5B8",
    hlink: "0F9D8A", folHlink: "6B7A99",
  },
};
const NAVY = "14213D", TEAL = "0F9D8A", CORAL = "E4572E", AMBER = "F2A541", SLATE = "6B7A99", MIST = "EEF2F7", INK = "111827", GRID = "D9DEE7";

const pres = new pptxgen();
pres.layout = "LAYOUT_WIDE"; // 13.33 x 7.5
pres.theme = { headFontFace: THEME.headFontFace, bodyFontFace: THEME.bodyFontFace };
pres.title = "DICEUS - SEO & AI Search plan";
pres.author = "Senior Technical SEO & AI Search candidate";
const C = pres.SchemeColor;

// ---------------------------------------------------------------- layouts
pres.defineSlideMaster({
  title: "DARK", background: { color: NAVY },
  objects: [
    { placeholder: { options: { name: "title", type: "title", x: 0.8, y: 2.2, w: 11.7, h: 1.6, fontSize: 44, bold: true, color: "FFFFFF", fontFace: "Cambria", valign: "bottom", align: "left" }, text: "" } },
    { placeholder: { options: { name: "body", type: "body", x: 0.8, y: 3.95, w: 11.7, h: 1.4, fontSize: 20, color: "CBD5E1", fontFace: "Calibri", valign: "top" }, text: "" } },
  ],
});
pres.defineSlideMaster({
  title: "CONTENT", background: { color: "FFFFFF" },
  slideNumber: { x: 12.5, y: 7.0, w: 0.5, h: 0.3, fontSize: 10, color: SLATE, fontFace: "Calibri" },
  objects: [
    { text: { text: "DICEUS · SEO & AI Search plan · confidential", options: { x: 0.6, y: 7.0, w: 6, h: 0.3, fontSize: 10, color: SLATE, fontFace: "Calibri", margin: 0 } } },
    { placeholder: { options: { name: "title", type: "title", x: 0.6, y: 0.35, w: 12.1, h: 0.9, fontSize: 32, bold: true, color: NAVY, fontFace: "Cambria", valign: "middle", margin: 0, align: "left" }, text: "" } },
    { placeholder: { options: { name: "kicker", type: "body", x: 0.6, y: 1.2, w: 12.1, h: 0.45, fontSize: 15, color: SLATE, fontFace: "Calibri", margin: 0 }, text: "" } },
  ],
});

const T = (s, text, opts) => s.addText(text, Object.assign({ isTextBox: true, fontFace: "Calibri", color: INK, margin: 0, valign: "top" }, opts));
const card = (s, x, y, w, h, fill, name) => s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y, w, h, rectRadius: 0.08, fill: { color: fill }, line: { color: fill }, objectName: name });
const dot = (s, x, y, color, label) => {
  s.addShape(pres.shapes.OVAL, { x, y, w: 0.42, h: 0.42, fill: { color }, line: { color } });
  T(s, label, { x, y, w: 0.42, h: 0.42, fontSize: 14, bold: true, color: "FFFFFF", align: "center", valign: "middle" });
};
const content = (title, kicker, notes) => {
  const s = pres.addSlide({ masterName: "CONTENT" });
  s.addText(title, { placeholder: "title" });
  if (kicker) s.addText(kicker, { placeholder: "kicker" });
  if (notes) s.addNotes(notes);
  return s;
};

// ================================================================ 1 Title
{
  const s = pres.addSlide({ masterName: "DARK" });
  s.addText("From dev shop to insurance software vendor", { placeholder: "title" });
  s.addText("SEO & AI Search plan for diceus.com: why the site underperforms the product strategy, what to change, and the 90-day plan", { placeholder: "body" });
  T(s, "Evidence: own crawl of 815 URLs · 44 SERPs · 20-prompt AI panel · 13 competitors · 7 pivot case studies   |   October 2026", { x: 0.8, y: 6.5, w: 11.7, h: 0.4, fontSize: 13, color: "94A3B8" });
  s.addNotes("Purpose: agree the direction and the first 30 days. Everything shown is from public data; GSC, GA4 and CRM were not available and are marked as such in the full deliverables (01-06).");
}

// ================================================================ 2 Answer first
{
  const s = content("The answer on one slide", "Change the weight, not the URLs: fix, reposition, then win alternative risk first",
    "Pyramid: main message first. 1) A free fix protects the only territory where DICEUS already wins. 2) The site and entity still say 'dev shop'; repositioning is done through homepage, navigation, links and schema - no URL migration. 3) Alternative risk is the highest relevance x feasibility territory; build it as the first complete product cluster with real proof.");
  const cols = [
    ["1", CORAL, "Fix this week", "3 product pages are noindexed, including Captive Management and RRG: the pages where DICEUS already wins in search and AI answers", "Remove stray tag · deploy guardrail"],
    ["2", NAVY, "Reposition: days 1-60", "Homepage, navigation and internal links still sell custom development. Make products the strongest pages, keep services as a secondary line", "Homepage · nav · links · schema"],
    ["3", TEAL, "Win alt-risk: days 1-90", "Captive and RRG software is winnable now: DICEUS is #1 in our sample and no vendor owns the category. Add proof, buyer assets and AI-ready facts", "Hub · proof · reviews · comparisons"],
  ];
  cols.forEach(([n, col, h, b, f], i) => {
    const x = 0.6 + i * 4.1;
    card(s, x, 1.95, 3.85, 4.6, MIST, "col" + n);
    dot(s, x + 0.3, 2.2, col, n);
    T(s, h, { x: x + 0.3, y: 2.8, w: 3.3, h: 0.5, fontSize: 20, bold: true, color: NAVY, fontFace: "Cambria" });
    T(s, b, { x: x + 0.3, y: 3.4, w: 3.3, h: 2.2, fontSize: 15, color: INK });
    T(s, f, { x: x + 0.3, y: 5.85, w: 3.3, h: 0.5, fontSize: 13, color: col, bold: true });
  });
}

// ================================================================ 3 Diagnosis numbers
{
  const s = content("Today the site tells Google, buyers and AI: \"dev shop\"", "Five measured symptoms (own crawl and panels, 6 Oct 2026)",
    "Sources: crawl of 815 URLs (02_Current_State_Audit.xlsx Summary, Layer_Links, Indexability); AI panel (03 AI_Panel). Contextual links exclude the ~300 sitewide mega-menu links. AI panel = Claude with web search, 1 run per prompt, directional.");
  const stats = [
    ["23 : 192", "product pages vs generic service, expertise and non-insurance industry pages", NAVY],
    ["24 vs 93", "median in-content links a product page gets vs a generic service page", NAVY],
    ["3", "product pages excluded by noindex: Captive Mgmt, RRG, Group Health", CORAL],
    ["2 / 16", "unbranded AI prompts that name DICEUS (captive and RRG only)", NAVY],
    ["0 / 23", "product pages with product schema; 0 reviews on product listings", NAVY],
  ];
  stats.forEach(([big, lbl, col], i) => {
    const x = 0.6 + (i % 3) * 4.1, y = i < 3 ? 1.95 : 4.45;
    card(s, x, y, 3.85, 2.2, MIST, "stat" + i);
    T(s, big, { x: x + 0.3, y: y + 0.25, w: 3.3, h: 0.95, fontSize: 44, bold: true, color: col, fontFace: "Cambria" });
    T(s, lbl, { x: x + 0.3, y: y + 1.2, w: 3.3, h: 0.9, fontSize: 14, color: INK });
  });
  card(s, 8.8, 4.45, 3.85, 2.2, NAVY, "homepage-quote");
  T(s, "Homepage H1", { x: 9.1, y: 4.65, w: 3.3, h: 0.35, fontSize: 13, color: "94A3B8" });
  T(s, "\"Custom software development company\"", { x: 9.1, y: 5.0, w: 3.3, h: 1.0, fontSize: 20, bold: true, color: "FFFFFF", fontFace: "Cambria" });
  T(s, "last modified 2022 · 0.99 title match with a services page", { x: 9.1, y: 6.05, w: 3.3, h: 0.5, fontSize: 12, color: "CBD5E1" });
}

// ================================================================ 4 Homepage now vs proposed
{
  const s = content("The homepage tells the agency story first", "Current H2 order (crawl) vs proposed order: products, segments and proof first, services as one strip",
    "Current H2 sequence taken verbatim from the crawl. Proposed: title 'DICEUS - Insurance Software for Carriers, MGAs & Captives'; H1 'Insurance software products for carriers, MGAs and alternative risk'. Staged change: first hand the generic 'custom software development company' query to /services/custom-software-development/, check GSC, then retitle the homepage (rollback ready).");
  const now = ["Need a custom software solution?", "Ready-made insurance software", "Custom software services and solutions", "Case studies · Focus industries · Clients", "Benefits of custom software solutions", "Software development life cycle", "Why choose DICEUS as a business software development company?", "Tech stack · Team · Articles · FAQ"];
  const next = ["H1: Insurance software for carriers, MGAs & alt-risk", "Choose your path: captives · RRGs · MGAs · carriers", "Product families: core, distribution, finance & data, alternative risk", "Proof band: named outcomes, VCIA partner, product reviews", "How we deliver: implementation in weeks, security & trust", "Services strip: implementation, modernization, custom dev", "Insights: captive, RRG and PAS guides", "Book a demo"];
  [["NOW", now, CORAL, 0.6], ["PROPOSED", next, TEAL, 6.8]].forEach(([h, list, col, x]) => {
    T(s, h, { x, y: 1.85, w: 5.9, h: 0.4, fontSize: 14, bold: true, color: col });
    list.forEach((t, i) => {
      card(s, x, 2.3 + i * 0.56, 5.9, 0.48, i === 0 ? (col === CORAL ? "FDE7E1" : "DDF3EF") : MIST, h + i);
      T(s, `${i + 1}  ${t}`, { x: x + 0.2, y: 2.3 + i * 0.56, w: 5.6, h: 0.48, fontSize: 14, color: INK, valign: "middle", bold: i === 0 });
    });
  });
}

// ================================================================ 5 Product pages vs competitors
{
  const s = content("Product pages lose on proof, not on features", "DICEUS has the deepest captive feature content in the set, but none of the trust signals buyers and AI look for",
    "Competitor teardown (data/competitor_teardown.md): Luzern Risk (4 anonymised testimonials with titles + quantified cases e.g. ~$55M premium, hand-written llms.txt with flat-rate pricing model, calculators), Riskonnect (named Municipal Association of SC quote, buying guide + RFP template, FAQ, Platform Security page with SOC 2 Type 2; G2 35 reviews), Insly (pricing tiers by segment, custom quotes - no figures), Socotra (ISO 27001, SOC 1 T2 security page; 2021 Gartner MQ Visionary) / hx (SOC 2 + ISO 27001 on homepage), Vertafore MGA Systems (SoftwareApplication + FAQPage schema). Fact-checked 6 Oct 2026: data/factcheck_external.md. DICEUS's Gartner 5/5 and Clutch 4.9 are company-level ratings of the services business.");
  const rows = [
    ["", "DICEUS", "Luzern Risk", "Riskonnect", "Insly", "Socotra / hx"],
    ["Feature depth for captives", "Strong", "Medium", "Low", "n/a", "n/a"],
    ["Customer proof with metrics", "No", "Anon. cases", "Named quote", "Named execs", "Logos + metrics"],
    ["Product-level reviews", "0", "-", "G2: 35", "-", "Analyst"],
    ["Pricing model explained", "No", "Flat rate", "No", "Tiers, no prices", "No"],
    ["Security / trust page", "No", "-", "SOC 2 page", "-", "ISO 27001, SOC"],
    ["Buyer assets (guide, RFP, calculator)", "No", "Calculators", "Guide + RFP", "Glossary", "Docs"],
    ["FAQ + product schema", "No", "FAQ schema", "FAQ", "-", "-"],
    ["Curated llms.txt", "PAS only", "Yes", "Auto", "No", "Auto / no"],
  ];
  const good = new Set(["Strong", "Yes", "Anon. cases", "Named quote", "Named execs", "Logos + metrics", "Flat rate", "Tiers, no prices", "SOC 2 page", "Guide + RFP", "Calculators", "ISO 27001, SOC", "FAQ schema", "G2: 35", "Analyst"]);
  const bad = new Set(["No", "0", "PAS only"]);
  const tbl = rows.map((r, ri) => r.map((c, ci) => ({
    text: c, options: {
      bold: ri === 0 || ci === 0, fontSize: 13, color: ri === 0 ? "FFFFFF" : INK,
      fill: { color: ri === 0 ? NAVY : (ci === 1 ? (bad.has(c) ? "FDE7E1" : good.has(c) ? "DDF3EF" : "FFFFFF") : (good.has(c) && ci > 1 ? "F1FAF8" : "FFFFFF")) },
      align: ci === 0 ? "left" : "center", valign: "middle",
    },
  })));
  s.addTable(tbl, { x: 0.6, y: 1.85, w: 12.1, colW: [3.6, 1.7, 1.7, 1.7, 1.7, 1.7], rowH: 0.5, border: { type: "solid", pt: 0.75, color: GRAY() }, fontFace: "Calibri" });
}
function GRAY() { return GRID; }

// ================================================================ 6 Pivot case studies
{
  const P = JSON.parse(fs.readFileSync(path.join(__dirname, "pivot_slide.json"), "utf8"));
  const s = content(P.title, P.kicker, P.notes);
  P.cases.forEach((c, i) => {
    const x = 0.6 + (i % 3) * 4.1, y = 1.85 + Math.floor(i / 3) * 1.75;
    card(s, x, y, 3.85, 1.6, MIST, "case" + i);
    T(s, c.name, { x: x + 0.25, y: y + 0.15, w: 3.4, h: 0.4, fontSize: 16, bold: true, color: NAVY, fontFace: "Cambria" });
    T(s, c.move, { x: x + 0.25, y: y + 0.55, w: 3.4, h: 0.45, fontSize: 12.5, color: SLATE });
    T(s, c.lesson, { x: x + 0.25, y: y + 0.95, w: 3.4, h: 0.6, fontSize: 13, color: INK });
  });
  const yb = 1.85 + Math.ceil(P.cases.length / 3) * 1.75 + 0.05;
  card(s, 0.6, yb, 12.1, 6.75 - yb, NAVY, "verdict");
  T(s, P.verdict_head, { x: 0.9, y: yb + 0.15, w: 11.5, h: 0.4, fontSize: 17, bold: true, color: "FFFFFF", fontFace: "Cambria" });
  T(s, P.verdict, { x: 0.9, y: yb + 0.6, w: 11.5, h: 6.75 - yb - 0.7, fontSize: 14, color: "E2E8F0" });
}

// ================================================================ 7 Where to compete (native chart)
{
  const s = content("Where to compete: alternative risk first", "Priority score = 0.45 business relevance + 0.35 SEO feasibility + 0.20 demand evidence (volumes not available, so demand weighs least)",
    "From 03_Search_Market_and_Opportunity.xlsx / Territories. Sensitivity check: with equal weights the top two (captive, RRG) and bottom two (services) do not change. PAS has the most demand but Oracle/Guidewire/G2 own the head terms - win its long tail (PAS for MGAs / captives / RRGs) instead.");
  const labels = ["Captive insurance & management", "Risk retention groups", "Insurance GL / accounting", "Policy administration (PAS)", "Self-insured & pools", "Broker & customer portals", "Data warehouse & analytics", "Group insurance", "MGA / program admin", "Claims management", "Insurance dev services", "Generic IT services"];
  const vals = [4.6, 4.4, 3.8, 3.75, 3.6, 3.35, 3.35, 3.25, 3.1, 2.95, 2.4, 1.45];
  s.addChart(pres.charts.BAR, [{ name: "Priority score", labels: labels.slice().reverse(), values: vals.slice().reverse() }], {
    x: 0.6, y: 1.8, w: 7.6, h: 5.0, barDir: "bar", chartColors: ["9AA5B8"], invertedColors: ["9AA5B8"],
    showValue: true, dataLabelPosition: "outEnd", dataLabelFontSize: 11, dataLabelColor: INK, dataLabelFontFace: "+mn-lt", dataLabelFormatCode: "0.00",
    catAxisLabelFontSize: 12, catAxisLabelColor: INK, catAxisLabelFontFace: "+mn-lt", valAxisHidden: true, valAxisMaxVal: 5,
    valGridLine: { style: "none" }, catGridLine: { style: "none" }, showLegend: false, barGapWidthPct: 45,
  });
  // highlight bars by overlaying a second chart is not needed: callout cards carry the message
  card(s, 8.6, 1.85, 4.1, 2.35, "DDF3EF", "win");
  T(s, "Win now", { x: 8.85, y: 2.0, w: 3.6, h: 0.4, fontSize: 17, bold: true, color: TEAL, fontFace: "Cambria" });
  T(s, "Captive + RRG: DICEUS #1 in our sample, thin SERPs, VCIA partner (Jun 2026), ~262 US RRGs and 40 US captive domiciles", { x: 8.85, y: 2.45, w: 3.6, h: 1.7, fontSize: 14, color: INK });
  card(s, 8.6, 4.4, 4.1, 2.35, MIST, "longtail");
  T(s, "Win the long tail", { x: 8.85, y: 4.55, w: 3.6, h: 0.4, fontSize: 17, bold: true, color: NAVY, fontFace: "Cambria" });
  T(s, "PAS, underwriting, reinsurance: segment variants (\"for MGAs\", \"for captives\") and reviews, not head terms owned by Guidewire, Oracle and G2", { x: 8.85, y: 5.0, w: 3.6, h: 1.7, fontSize: 14, color: INK });
}

// ================================================================ 8 Whitespace
{
  const s = content("The whitespace nobody owns yet", "Gaps no competitor fills, from the teardown of 13 vendors",
    "Luzern Risk raised $45M and is an AI-native captive MANAGER: it competes with DICEUS's buyers, so 'software-only platform for independent captive managers' is a real wedge. Origami and Riskonnect never mention captives on their homepages; Websure's captive page is ~250 words. No authoritative 'best captive management software' guide exists: the exact query returns directories (incl. DICEUS's own Capterra/GetApp listings) and thin aggregator listicles.");
  const items = [
    ["Software-only for captive managers", "Luzern ($45M Series B) now runs captives itself and competes with the managers who would buy DICEUS. Position as the platform independent managers run on."],
    ["One captive + RRG + self-insured family", "Origami and Riskonnect treat captives as an RMIS sub-feature; their homepages never mention them."],
    ["RRG search is almost uncontested", "SERP = DICEUS, a 2022 press release and Ventiv-era pages. An RRG hub (LRRA, domiciles, NAIC calendar) can own the topic."],
    ["No category guide, no curated llms.txt", "No authoritative 'best captive management software' guide: only directories and thin aggregator lists. No captive software vendor has a fact-dense llms.txt."],
  ];
  items.forEach(([h, b], i) => {
    const x = 0.6 + (i % 2) * 6.1, y = 1.9 + Math.floor(i / 2) * 2.45;
    card(s, x, y, 5.85, 2.2, MIST, "ws" + i);
    dot(s, x + 0.3, y + 0.3, TEAL, String(i + 1));
    T(s, h, { x: x + 0.95, y: y + 0.3, w: 4.7, h: 0.45, fontSize: 18, bold: true, color: NAVY, fontFace: "Cambria" });
    T(s, b, { x: x + 0.95, y: y + 0.85, w: 4.7, h: 1.25, fontSize: 14, color: INK });
  });
}

// ================================================================ 9 Architecture image
{
  const s = content("Target architecture: products first, URLs kept", "Hierarchy through navigation, hubs and links; services and content link up into products",
    "Products hub /insurance/solutions/, Alternative Risk hub (AROP page), buyer pages for MGAs and self-insured groups. Captive managers, RRGs and brokers are served by their product pages to avoid self-cannibalisation. Generic services stay live but leave the primary nav until GSC/CRM show their value.");
  s.addImage({ path: path.join(__dirname, "..", "deliverables", "assets", "fig5_future_architecture.png"), x: 1.35, y: 1.75, w: 10.6, h: 5.1, sizing: { type: "contain", w: 10.6, h: 5.1 } });
}

// ================================================================ 10 Before / after
{
  const s = content("What changes on the site", "Concrete changes, each tied to evidence and a best-in-class example",
    "Examples: Decerto keeps separate Products and Services menus on one domain; Luzern segment-first nav; Riskonnect PAS page (named quote, buying guide, RFP template, FAQ); Insly pricing tiers (custom quotes); Socotra/hx security pages; Vertafore SoftwareApplication schema.");
  const rows = [
    ["Area", "Today (fact)", "Change", "Model to copy"],
    ["Homepage", "H1 \"Custom software development company\"", "Product-category H1, segment self-select, proof band, services strip", "Decerto, Luzern"],
    ["Navigation", "~300 links, services-dominant mega-menu", "Products · Alternative risk · Buyers · Services · Resources; 30-40 menu links (<=120 links/page)", "Luzern, Insly"],
    ["Product pages", "Modules + benefits only", "Who it's for, video, integrations, proof, pricing model, FAQ, security", "Riskonnect, Vertafore"],
    ["Captive pages", "Noindex; two pages target the same audience", "Fix; managers vs owners split; spec in 04 App. A", "-"],
    ["Proof", "Company-level Gartner / Clutch ratings", "2-3 alt-risk case studies; 10+ product reviews", "Luzern, Riskonnect"],
    ["New pages", "None", "/trust/, /pricing/ (model), RRG hub, comparison, RFP template", "Socotra, Insly, Riskonnect"],
    ["AI readiness", "No product schema; llms.txt = PAS", "SoftwareApplication + FAQ schema; curated llms.txt; Wikidata", "Vertafore, Luzern"],
  ];
  const tbl = rows.map((r, ri) => r.map((c, ci) => ({ text: c, options: { bold: ri === 0 || ci === 0, fontSize: 12.5, color: ri === 0 ? "FFFFFF" : (ci === 1 ? "9A3412" : INK), fill: { color: ri === 0 ? NAVY : (ri % 2 ? "FFFFFF" : MIST) }, valign: "middle" } })));
  s.addTable(tbl, { x: 0.6, y: 1.85, w: 12.1, colW: [1.7, 3.4, 4.9, 2.1], rowH: 0.6, border: { type: "solid", pt: 0.75, color: GRID }, fontFace: "Calibri" });
}

// ================================================================ 11 AI search (native chart)
{
  const s = content("AI search: own the captive and RRG answer", "Brands named across 16 unbranded prompts (Claude + web search, 1 run each, directional)",
    "Broad answers are assembled from analyst lists (Celent, Datos), G2/Capterra category pages and listicles - DICEUS is in none. 'What is DICEUS?' resolved to homonyms (no Wikidata). Listings surfaced without the brand name and with 0 reviews. ChatGPT, Perplexity and Google AI Overviews: not measured yet (panel v2 in days 5-20).");
  s.addChart(pres.charts.BAR, [{ name: "Prompts naming the brand", labels: ["DICEUS", "Origami Risk", "OneShield", "AdvantageGo", "BriteCore", "Insurity", "Duck Creek", "Sapiens", "Majesco", "Guidewire"], values: [2, 2, 2, 3, 3, 5, 6, 6, 7, 7] }], {
    x: 0.6, y: 1.8, w: 6.4, h: 5.0, barDir: "bar", chartColors: ["9AA5B8"],
    showValue: true, dataLabelPosition: "outEnd", dataLabelFontSize: 11, dataLabelColor: INK, dataLabelFontFace: "+mn-lt",
    catAxisLabelFontSize: 12, catAxisLabelColor: INK, catAxisLabelFontFace: "+mn-lt", valAxisHidden: true, valAxisMaxVal: 8,
    valGridLine: { style: "none" }, catGridLine: { style: "none" }, showLegend: false, barGapWidthPct: 45,
  });
  const lev = [["Be indexable", "Fix noindex on the pages that win today"], ["Carry the brand", "\"DICEUS Captive Management Platform\" on every listing"], ["Be cited by third parties", "Product reviews, Celent VendorMatch, captive trade press"], ["Be easy to quote", "SoftwareApplication + FAQ schema, curated llms.txt, Wikidata, pricing model"]];
  lev.forEach(([h, b], i) => {
    const y = 1.85 + i * 1.22;
    card(s, 7.4, y, 5.3, 1.08, MIST, "lev" + i);
    dot(s, 7.6, y + 0.3, TEAL, String(i + 1));
    T(s, h, { x: 8.2, y: y + 0.12, w: 4.4, h: 0.4, fontSize: 16, bold: true, color: NAVY });
    T(s, b, { x: 8.2, y: y + 0.52, w: 4.4, h: 0.5, fontSize: 13, color: INK });
  });
}

// ================================================================ 12 90 days
{
  const s = content("90 days: fix, reposition, prove", "Destructive changes (redirects, merges, pruning) only after GSC/CRM evidence",
    "Full plan with owners, dependencies and Definition of Done: 05_90_Day_Execution_Plan.xlsx (32 tasks). Governance: baseline + change log + 14-day check + rollback for every risky change.");
  const ph = [
    ["Days 1-30", "Fix · baseline · decide", CORAL, ["Remove noindex + deploy guardrail", "Connect GSC, GA4, CRM; baseline per URL", "Product truth table (what is a sellable SKU)", "Query-ownership map: one URL per cluster", "Rebuild Captive Management page (spec)", "Brand directory listings; start review drive", "AI panel v2 across 4 engines"]],
    ["Days 31-60", "Reposition · build", NAVY, ["Homepage in 2 GSC-gated steps", "Nav v2: products first, 30-40 menu links", "Alternative Risk hub + self-insured page", "+ contextual links from 86 insurance posts", "/trust/ and /pricing/ (model) pages", "Comparison page + RFP template", "Wikidata entity; trade-press pitch"]],
    ["Days 61-90", "Validate · scale", TEAL, ["MGA & program administrator page", "Merge overlaps only where GSC proves it", "Claims / feature pages only if validated", "Case-study archives noindex if 0 traffic", "Weekly automated crawl + GSC + AI digest", "Day-90 review and re-prioritisation", ""]],
  ];
  ph.forEach(([h, sub, col, items], i) => {
    const x = 0.6 + i * 4.1;
    card(s, x, 1.85, 3.85, 0.95, col, "ph" + i);
    T(s, h, { x: x + 0.25, y: 1.92, w: 3.4, h: 0.45, fontSize: 19, bold: true, color: "FFFFFF", fontFace: "Cambria" });
    T(s, sub, { x: x + 0.25, y: 2.35, w: 3.4, h: 0.35, fontSize: 13, color: "FFFFFF" });
    card(s, x, 2.9, 3.85, 3.85, MIST, "phb" + i);
    T(s, items.filter(Boolean).map((t, k, a) => ({ text: t, options: { bullet: true, breakLine: k < a.length - 1 } })), { x: x + 0.2, y: 3.05, w: 3.5, h: 3.6, fontSize: 14, color: INK, paraSpaceAfter: 6 });
  });
}

// ================================================================ 13 Not yet + asks + KPIs
{
  const s = content("What we won't do yet, what we need, how we'll measure", "Evidence before irreversible moves",
    "Not yet: (1) pruning ~190 generic service pages - their traffic and leads are unknown; (2) moving products to a new /products/ URL folder - equity and directory links at risk, no evidence the path hurts; (3) merging the two captive pages or overlapping service pages - need GSC query-by-page data.");
  const cols = [
    ["Not yet (validate first)", CORAL, ["Prune or redirect the ~190 generic service pages", "Move products to a new /products/ URL folder", "Merge the two captive pages or service overlaps"]],
    ["What we need from DICEUS", NAVY, ["GSC, GA4, CRM and Cloudflare log access", "Product truth table: what is sellable today", "One referenceable US alt-risk customer", "Security facts (ISO / SOC status)"]],
    ["KPIs at day 90", TEAL, ["23/23 product pages indexed (now 20/23)", "Product in-content links: median 24 to 60+", "AI share of voice: 2/16 to 5/16+ (Claude)", "5+ published product reviews (now 0)", "Alt-risk impressions and demos vs baseline"]],
  ];
  cols.forEach(([h, col, items], i) => {
    const x = 0.6 + i * 4.1;
    card(s, x, 1.85, 3.85, 4.9, MIST, "nb" + i);
    T(s, h, { x: x + 0.25, y: 2.0, w: 3.4, h: 0.5, fontSize: 18, bold: true, color: col, fontFace: "Cambria" });
    T(s, items.map((t, k) => ({ text: t, options: { bullet: true, breakLine: k < items.length - 1 } })), { x: x + 0.2, y: 2.6, w: 3.5, h: 4.0, fontSize: 14, color: INK, paraSpaceAfter: 8 });
  });
}

// ================================================================ 14 Close
{
  const s = pres.addSlide({ masterName: "DARK" });
  s.addText("First step: fix three tags this week", { placeholder: "title" });
  s.addText("Then make products the strongest pages on diceus.com, and make DICEUS the answer for captive and RRG software in search and AI.", { placeholder: "body" });
  s.addNotes("Close on the decision: approve days 1-30 (fix, data access, product truth table, captive page rebuild).");
}

(async () => {
  const out = path.join(__dirname, "..", "deliverables", "DICEUS_SEO_AI_Search_micro_deck.pptx");
  await pres.writeFile({ fileName: out });
  await applyTheme(out, THEME);
  console.log("saved", out);
})();
