// DICEUS micro-presentation: "Від аутсорс-студії до вендора страхового ПЗ"
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
pres.title = "DICEUS - план SEO та AI-пошуку";
pres.author = "Кандидат на позицію Senior Technical SEO & AI Search";
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
    { text: { text: "DICEUS · план SEO та AI-пошуку · конфіденційно", options: { x: 0.6, y: 7.0, w: 6, h: 0.3, fontSize: 10, color: SLATE, fontFace: "Calibri", margin: 0 } } },
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
  s.addText("Від аутсорс-студії до вендора страхового ПЗ", { placeholder: "title" });
  s.addText("План SEO та AI-пошуку для diceus.com: чому сайт не працює на продуктову стратегію, що змінити, і план на 90 днів", { placeholder: "body" });
  T(s, "Докази: власний краул 815 URL · 44 видачі · AI-панель з 20 запитів · 13 конкурентів · 7 кейсів півоту   |   жовтень 2026", { x: 0.8, y: 6.5, w: 11.7, h: 0.4, fontSize: 13, color: "94A3B8" });
  s.addNotes("Мета: погодити напрям і перші 30 днів. Усі дані публічні; доступу до GSC, GA4 і CRM не було — це позначено в повних матеріалах (01-06).");
}

// ================================================================ 2 Answer first
{
  const s = content("Відповідь на одному слайді", "Змінюємо вагу, а не URL: виправити, перепозиціонувати, першими виграти alternative risk",
    "Піраміда: головне — спочатку. 1) Безкоштовне виправлення захищає єдину територію, де DICEUS уже виграє. 2) Сайт і сутність бренду досі кажуть «аутсорс»; перепозиціонування — через головну, навігацію, посилання та schema, без міграції URL. 3) Alternative risk — територія з найвищою релевантністю × досяжністю; будуємо її як перший повний продуктовий кластер зі справжніми доказами.");
  const cols = [
    ["1", CORAL, "Виправити цього тижня", "3 продуктові сторінки закриті noindex, серед них Captive Management і RRG — саме ті, де DICEUS уже виграє в пошуку та AI-відповідях", "Прибрати зайвий тег · захист при деплої"],
    ["2", NAVY, "Перебудова: дні 1-60", "Головна, навігація та внутрішні посилання досі продають розробку на замовлення. Зробити продукти найсильнішими сторінками, послуги — другою лінією", "Головна · меню · посилання · schema"],
    ["3", TEAL, "Alt-risk: дні 1-90", "ПЗ для captive і RRG можна виграти вже зараз: DICEUS №1 у нашій вибірці, категорію ніхто не займає. Додати докази, матеріали для покупців і факти для AI", "Хаб · докази · відгуки · порівняння"],
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
  const s = content("Сьогодні сайт каже Google, покупцям і AI: «аутсорс»", "П'ять виміряних симптомів (власний краул і панелі, 6 жовтня 2026)",
    "Джерела: краул 815 URL (02_Current_State_Audit.xlsx: Summary, Layer_Links, Indexability); AI-панель (03 AI_Panel). Контекстні посилання — без ~300 посилань мегаменю на кожній сторінці. AI-панель = Claude з веб-пошуком, 1 прогін на запит, орієнтовно.");
  const stats = [
    ["23 : 192", "продуктових сторінок проти сторінок загальних послуг, експертиз і нестрахових галузей", NAVY],
    ["24 vs 93", "медіана посилань у тексті на продуктову сторінку проти сторінки загальної послуги", NAVY],
    ["3", "продуктові сторінки виключені noindex: Captive Mgmt, RRG, Group Health", CORAL],
    ["2 / 16", "небрендових AI-запитів, де названо DICEUS (лише captive і RRG)", NAVY],
    ["0 / 23", "продуктових сторінок мають product schema; 0 відгуків у продуктових лістингах", NAVY],
  ];
  stats.forEach(([big, lbl, col], i) => {
    const x = 0.6 + (i % 3) * 4.1, y = i < 3 ? 1.95 : 4.45;
    card(s, x, y, 3.85, 2.2, MIST, "stat" + i);
    T(s, big, { x: x + 0.3, y: y + 0.25, w: 3.3, h: 0.95, fontSize: 44, bold: true, color: col, fontFace: "Cambria" });
    T(s, lbl, { x: x + 0.3, y: y + 1.2, w: 3.3, h: 0.9, fontSize: 14, color: INK });
  });
  card(s, 8.8, 4.45, 3.85, 2.2, NAVY, "homepage-quote");
  T(s, "H1 головної", { x: 9.1, y: 4.65, w: 3.3, h: 0.35, fontSize: 13, color: "94A3B8" });
  T(s, "\"Custom software development company\"", { x: 9.1, y: 5.0, w: 3.3, h: 1.0, fontSize: 20, bold: true, color: "FFFFFF", fontFace: "Cambria" });
  T(s, "оновлено 2022 · збіг title 0,99 зі сторінкою послуги", { x: 9.1, y: 6.05, w: 3.3, h: 0.5, fontSize: 12, color: "CBD5E1" });
}

// ================================================================ 4 Homepage now vs proposed
{
  const s = content("Головна розповідає спершу історію агенції", "Поточний порядок H2 (краул) проти запропонованого: спершу продукти, сегменти й докази, послуги — одним блоком",
    "Поточні H2 взято дослівно з краулу (сайт англомовний, тому ліва колонка — оригінал). Пропозиція: title 'DICEUS - Insurance Software for Carriers, MGAs & Captives'; H1 'Insurance software products for carriers, MGAs and alternative risk'. Поетапно: спершу передати загальний запит 'custom software development company' сторінці /services/custom-software-development/, перевірити GSC, потім змінити title головної (з планом відкату).");
  const now = ["Need a custom software solution?", "Ready-made insurance software", "Custom software services and solutions", "Case studies · Focus industries · Clients", "Benefits of custom software solutions", "Software development life cycle", "Why choose DICEUS as a business software development company?", "Tech stack · Team · Articles · FAQ"];
  const next = ["H1: страхове ПЗ для страховиків, MGA та alt-risk", "Оберіть шлях: captive · RRG · MGA · страховики", "Родини продуктів: core, дистрибуція, фінанси, alt-risk", "Смуга доказів: результати, партнер VCIA, відгуки", "Як впроваджуємо: тижні, безпека й довіра", "Блок послуг: впровадження, модернізація, розробка", "Експертиза: гайди про captive, RRG і PAS", "Замовити демо"];
  [["ЗАРАЗ (дослівно з сайту)", now, CORAL, 0.6], ["ПРОПОНУЄМО", next, TEAL, 6.8]].forEach(([h, list, col, x]) => {
    T(s, h, { x, y: 1.85, w: 5.9, h: 0.4, fontSize: 14, bold: true, color: col });
    list.forEach((t, i) => {
      card(s, x, 2.3 + i * 0.56, 5.9, 0.48, i === 0 ? (col === CORAL ? "FDE7E1" : "DDF3EF") : MIST, h + i);
      T(s, `${i + 1}  ${t}`, { x: x + 0.2, y: 2.3 + i * 0.56, w: 5.6, h: 0.48, fontSize: 14, color: INK, valign: "middle", bold: i === 0 });
    });
  });
}

// ================================================================ 5 Product pages vs competitors
{
  const s = content("Продукти програють на доказах, а не на функціях", "У DICEUS найглибший опис функцій для captive, але немає сигналів довіри, які шукають покупці та AI",
    "Розбір конкурентів (data/competitor_teardown.md): Luzern Risk (4 анонімні відгуки з посадами + кейси з цифрами, напр. ~$55M премій; ручний llms.txt з моделлю flat rate; калькулятори), Riskonnect (іменна цитата Municipal Association of SC, buying guide + RFP-шаблон, FAQ, сторінка Platform Security з SOC 2 Type 2; G2 — 35 відгуків), Insly (тарифи за сегментами, ціни за запитом), Socotra (ISO 27001, SOC 1 T2; Gartner MQ Visionary 2021) / hx (SOC 2 + ISO 27001 на головній), Vertafore MGA Systems (schema SoftwareApplication + FAQPage). Факт-чек 6.10.2026: data/factcheck_external.md. Рейтинги DICEUS Gartner 5/5 і Clutch 4.9 — оцінки компанії як сервісного бізнесу, а не продуктів.");
  const rows = [
    ["", "DICEUS", "Luzern Risk", "Riskonnect", "Insly", "Socotra / hx"],
    ["Глибина функцій для captive", "Сильна", "Середня", "Низька", "н/з", "н/з"],
    ["Докази клієнтів з цифрами", "Немає", "Анонім. кейси", "Іменна цитата", "Іменні керівники", "Логотипи + цифри"],
    ["Відгуки саме про продукт", "0", "-", "G2: 35", "-", "Аналітики"],
    ["Пояснена модель ціни", "Немає", "Flat rate", "Немає", "Тарифи без цін", "Немає"],
    ["Сторінка безпеки / довіри", "Немає", "-", "Сторінка SOC 2", "-", "ISO 27001, SOC"],
    ["Матеріали для покупця", "Немає", "Калькулятори", "Гайд + RFP", "Глосарій", "Документація"],
    ["FAQ + product schema", "Немає", "FAQ schema", "FAQ", "-", "-"],
    ["Ручний llms.txt", "Лише PAS", "Так", "Авто", "Немає", "Авто / немає"],
  ];
  const good = new Set(["Сильна", "Так", "Анонім. кейси", "Іменна цитата", "Іменні керівники", "Логотипи + цифри", "Flat rate", "Тарифи без цін", "Сторінка SOC 2", "Гайд + RFP", "Калькулятори", "ISO 27001, SOC", "FAQ schema", "G2: 35", "Аналітики"]);
  const bad = new Set(["Немає", "0", "Лише PAS"]);
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
  const P = JSON.parse(fs.readFileSync(path.join(__dirname, "pivot_slide_ua.json"), "utf8"));
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
  const s = content("Де конкурувати: спершу alternative risk", "Бал = 0,45 бізнес-релевантність + 0,35 SEO-досяжність + 0,20 ознаки попиту (обсягів немає, тож попит важить найменше)",
    "З 03_Search_Market_and_Opportunity.xlsx / Territories. Перевірка чутливості: з рівними вагами топ-2 (captive, RRG) і низ-2 (послуги) не змінюються. У PAS найбільший попит, але head-запити тримають Oracle/Guidewire/G2 — вигравати треба довгий хвіст (PAS для MGA / captive / RRG).");
  const labels = ["Captive: страхування й управління", "Risk retention groups (RRG)", "Страховий GL / облік", "Policy administration (PAS)", "Self-insured і пули", "Брокерські та клієнтські портали", "Сховище даних і аналітика", "Групове страхування", "MGA / програмні адміністратори", "Управління збитками (claims)", "Розробка для страхування", "Загальні IT-послуги"];
  const vals = [4.6, 4.4, 3.8, 3.75, 3.6, 3.35, 3.35, 3.25, 3.1, 2.95, 2.4, 1.45];
  s.addChart(pres.charts.BAR, [{ name: "Бал пріоритету", labels: labels.slice().reverse(), values: vals.slice().reverse() }], {
    x: 0.6, y: 1.8, w: 7.6, h: 5.0, barDir: "bar", chartColors: ["9AA5B8"], invertedColors: ["9AA5B8"],
    showValue: true, dataLabelPosition: "outEnd", dataLabelFontSize: 11, dataLabelColor: INK, dataLabelFontFace: "+mn-lt", dataLabelFormatCode: "0.00",
    catAxisLabelFontSize: 12, catAxisLabelColor: INK, catAxisLabelFontFace: "+mn-lt", valAxisHidden: true, valAxisMaxVal: 5,
    valGridLine: { style: "none" }, catGridLine: { style: "none" }, showLegend: false, barGapWidthPct: 45,
  });
  // highlight bars by overlaying a second chart is not needed: callout cards carry the message
  card(s, 8.6, 1.85, 4.1, 2.35, "DDF3EF", "win");
  T(s, "Вигравати зараз", { x: 8.85, y: 2.0, w: 3.6, h: 0.4, fontSize: 17, bold: true, color: TEAL, fontFace: "Cambria" });
  T(s, "Captive + RRG: DICEUS №1 у вибірці, слабка конкуренція, партнер VCIA (червень 2026), ~262 RRG і 40 доміцилів captive у США", { x: 8.85, y: 2.45, w: 3.6, h: 1.7, fontSize: 14, color: INK });
  card(s, 8.6, 4.4, 4.1, 2.35, MIST, "longtail");
  T(s, "Вигравати довгий хвіст", { x: 8.85, y: 4.55, w: 3.6, h: 0.4, fontSize: 17, bold: true, color: NAVY, fontFace: "Cambria" });
  T(s, "PAS, андеррайтинг, перестрахування: сегментні варіанти («for MGAs», «for captives») і відгуки, а не head-запити Guidewire, Oracle і G2", { x: 8.85, y: 5.0, w: 3.6, h: 1.7, fontSize: 14, color: INK });
}

// ================================================================ 8 Whitespace
{
  const s = content("Вільна ніша, яку ще ніхто не зайняв", "Прогалини, які не закриває жоден конкурент (розбір 13 вендорів)",
    "Luzern Risk залучив $45M і є AI-native captive-МЕНЕДЖЕРОМ: він конкурує з покупцями DICEUS, тому позиція «лише ПЗ для незалежних captive-менеджерів» — реальний клин. Origami і Riskonnect не згадують captive на головних; сторінка captive у Websure — ~250 слів. Авторитетного гайду «best captive management software» немає: за точним запитом лише каталоги (зокрема лістинги DICEUS на Capterra/GetApp) і слабкі агрегатори.");
  const items = [
    ["Лише ПЗ для captive-менеджерів", "Luzern ($45M Series B) сам керує captive і конкурує з менеджерами — покупцями DICEUS. Позиція: платформа незалежних менеджерів."],
    ["Родина captive + RRG + self-insured", "В Origami і Riskonnect captive — підфункція RMIS; на головних про них ані слова."],
    ["Пошук по RRG майже без конкурентів", "У видачі — DICEUS, прес-реліз 2022 р. і сторінки часів Ventiv. Хаб про RRG (LRRA, доміцилі, календар NAIC) може забрати тему."],
    ["Немає гайду категорії і llms.txt", "Авторитетного гайду «best captive management software» немає — лише каталоги й слабкі агрегатори. Жоден вендор ПЗ для captive не має насиченого фактами llms.txt."],
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
  const s = content("Цільова архітектура: продукти першими, URL ті самі", "Ієрархія через навігацію, хаби та посилання; послуги й контент посилаються вгору на продукти",
    "Хаб продуктів /insurance/solutions/, хаб Alternative Risk (сторінка AROP), сторінки покупців для MGA і self-insured груп. Captive-менеджерів, RRG і брокерів обслуговують їхні продуктові сторінки — щоб не канібалізувати самих себе. Загальні послуги лишаються, але виходять з головного меню, доки GSC/CRM не покажуть їхню цінність.");
  s.addImage({ path: path.join(__dirname, "..", "deliverables", "assets", "fig5_future_architecture_ua.png"), x: 1.35, y: 1.75, w: 10.6, h: 5.1, sizing: { type: "contain", w: 10.6, h: 5.1 } });
}

// ================================================================ 10 Before / after
{
  const s = content("Що змінюється на сайті", "Конкретні зміни — кожна з доказом і прикладом найкращої практики",
    "Приклади: Decerto — окремі меню Products і Services на одному домені; Luzern — навігація за сегментами; сторінка PAS у Riskonnect (іменна цитата, buying guide, RFP-шаблон, FAQ); тарифи Insly (ціни за запитом); сторінки безпеки Socotra/hx; schema SoftwareApplication у Vertafore.");
  const rows = [
    ["Зона", "Сьогодні (факт)", "Зміна", "Взірець"],
    ["Головна", "H1 «Custom software development company»", "H1 з продуктовою категорією, вибір сегмента, смуга доказів, блок послуг", "Decerto, Luzern"],
    ["Навігація", "~300 посилань, мегаменю з перевагою послуг", "Продукти · Alt-risk · Покупці · Послуги · Ресурси; 30-40 пунктів меню (≤120 посилань/стор.)", "Luzern, Insly"],
    ["Продуктові сторінки", "Лише модулі + переваги", "Для кого, відео, інтеграції, докази, модель ціни, FAQ, безпека", "Riskonnect, Vertafore"],
    ["Сторінки captive", "Noindex; дві сторінки цілять в одну аудиторію", "Виправити; розділити менеджерів і власників; ТЗ у 04, дод. A", "-"],
    ["Докази", "Рейтинги Gartner / Clutch на рівні компанії", "2-3 кейси alt-risk; 10+ відгуків про продукти", "Luzern, Riskonnect"],
    ["Нові сторінки", "Немає", "/trust/, /pricing/ (модель), хаб RRG, порівняння, RFP-шаблон", "Socotra, Insly, Riskonnect"],
    ["Готовність до AI", "Немає product schema; llms.txt = PAS", "SoftwareApplication + FAQ schema; ручний llms.txt; Wikidata", "Vertafore, Luzern"],
  ];
  const tbl = rows.map((r, ri) => r.map((c, ci) => ({ text: c, options: { bold: ri === 0 || ci === 0, fontSize: 12.5, color: ri === 0 ? "FFFFFF" : (ci === 1 ? "9A3412" : INK), fill: { color: ri === 0 ? NAVY : (ri % 2 ? "FFFFFF" : MIST) }, valign: "middle" } })));
  s.addTable(tbl, { x: 0.6, y: 1.85, w: 12.1, colW: [1.95, 3.3, 4.75, 2.1], rowH: 0.6, border: { type: "solid", pt: 0.75, color: GRID }, fontFace: "Calibri" });
}

// ================================================================ 11 AI search (native chart)
{
  const s = content("AI-пошук: стати відповіддю про captive і RRG", "Бренди, названі в 16 небрендових запитах (Claude + веб-пошук, 1 прогін, орієнтовно)",
    "Широкі відповіді збираються зі списків аналітиків (Celent, Datos), категорій G2/Capterra і листиклів — DICEUS немає в жодному. На «What is DICEUS?» модель видала омоніми (немає Wikidata). Лістинги з'являлися без назви бренду і з 0 відгуків. ChatGPT, Perplexity і Google AI Overviews ще не виміряні (панель v2 — дні 5-20).");
  s.addChart(pres.charts.BAR, [{ name: "Запитів із брендом", labels: ["DICEUS", "Origami Risk", "OneShield", "AdvantageGo", "BriteCore", "Insurity", "Duck Creek", "Sapiens", "Majesco", "Guidewire"], values: [2, 2, 2, 3, 3, 5, 6, 6, 7, 7] }], {
    x: 0.6, y: 1.8, w: 6.4, h: 5.0, barDir: "bar", chartColors: ["9AA5B8"],
    showValue: true, dataLabelPosition: "outEnd", dataLabelFontSize: 11, dataLabelColor: INK, dataLabelFontFace: "+mn-lt",
    catAxisLabelFontSize: 12, catAxisLabelColor: INK, catAxisLabelFontFace: "+mn-lt", valAxisHidden: true, valAxisMaxVal: 8,
    valGridLine: { style: "none" }, catGridLine: { style: "none" }, showLegend: false, barGapWidthPct: 45,
  });
  const lev = [["Бути в індексі", "Прибрати noindex зі сторінок, що вже виграють"], ["Нести бренд", "«DICEUS Captive Management Platform» у кожному лістингу"], ["Бути цитованим іншими", "Відгуки, Celent VendorMatch, галузеві медіа captive"], ["Бути зручним для цитування", "SoftwareApplication + FAQ schema, llms.txt, Wikidata, модель ціни"]];
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
  const s = content("90 днів: виправити, перепозиціонувати, довести", "Руйнівні зміни (редиректи, злиття, видалення) — лише після доказів із GSC/CRM",
    "Повний план із власниками, залежностями та Definition of Done: 05_90_Day_Execution_Plan.xlsx (32 задачі). Правила: базова лінія + журнал змін + перевірка через 14 днів + відкат для кожної ризикової зміни.");
  const ph = [
    ["Дні 1-30", "Виправити · виміряти · вирішити", CORAL, ["Прибрати noindex + захист при деплої", "GSC, GA4, CRM; база по кожному URL", "Таблиця правди: що є продуктом", "Карта запитів: 1 URL на кластер", "Нова сторінка Captive Management (ТЗ)", "Бренд у лістингах; збір відгуків", "AI-панель v2 у 4 системах"]],
    ["Дні 31-60", "Перепозиціонувати · будувати", NAVY, ["Головна у 2 кроки з контролем GSC", "Меню v2: продукти першими, 30-40 пунктів", "Хаб Alt-Risk + сторінка self-insured", "Посилання з 86 страхових постів", "Сторінки /trust/ і /pricing/ (модель)", "Порівняння + RFP-шаблон", "Wikidata; пітч галузевим медіа"]],
    ["Дні 61-90", "Перевірити · масштабувати", TEAL, ["Сторінка для MGA і програмних адміністраторів", "Злиття — лише де доведе GSC", "Claims / функції — після перевірки", "Noindex архівів кейсів, якщо 0 трафіку", "Щотижневий автозвіт: краул + GSC + AI", "Огляд на 90-й день, нові пріоритети", ""]],
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
  const s = content("Чого поки не робимо, що потрібно, як міряємо", "Спершу докази, потім незворотні кроки",
    "Поки ні: (1) видаляти ~190 сторінок загальних послуг — їхній трафік і ліди невідомі; (2) переносити продукти в нову папку /products/ — під загрозою вага й посилання з каталогів, доказів шкоди поточного шляху немає; (3) зливати дві сторінки captive чи перетини послуг — потрібні дані GSC «запит × сторінка».");
  const cols = [
    ["Поки ні (спершу перевірка)", CORAL, ["Видаляти чи редиректити ~190 сторінок загальних послуг", "Переносити продукти в нову папку /products/", "Зливати дві сторінки captive чи перетини послуг"]],
    ["Що потрібно від DICEUS", NAVY, ["Доступ до GSC, GA4, CRM і логів Cloudflare", "Таблиця правди: що продається вже сьогодні", "Один референсний клієнт alt-risk у США", "Факти про безпеку (статус ISO / SOC)"]],
    ["KPI на 90-й день", TEAL, ["23/23 продуктових сторінок в індексі (зараз 20/23)", "Посилання в тексті на продукти: медіана 24 → 60+", "Частка голосу в AI: 2/16 → 5/16+ (Claude)", "5+ відгуків про продукти (зараз 0)", "Покази alt-risk і демо відносно бази"]],
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
  s.addText("Перший крок: виправити три теги цього тижня", { placeholder: "title" });
  s.addText("Далі — зробити продукти найсильнішими сторінками diceus.com, а DICEUS — відповіддю про ПЗ для captive і RRG у пошуку та AI.", { placeholder: "body" });
  s.addNotes("Завершити рішенням: затвердити дні 1-30 (виправлення, доступ до даних, таблиця правди продуктів, перебудова сторінки captive).");
}

(async () => {
  const out = path.join(__dirname, "..", "deliverables", "DICEUS_SEO_AI_Search_micro_deck_UA.pptx");
  await pres.writeFile({ fileName: out });
  await applyTheme(out, THEME);
  console.log("saved", out);
})();
