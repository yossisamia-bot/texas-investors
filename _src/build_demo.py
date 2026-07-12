# -*- coding: utf-8 -*-
"""עמוד דמה פנימי - תוספות מוצעות בהשראת ניתוח מצגת R-M (12/07/2026).
לא חלק מהאתר הרשמי: מסומן באדום "גרסת דמה", לא מקושר משום עמוד.
נתונים: _src/data/houston_stats.json - נמשכו מ-FRED ואומתו על ידינו (לא הועתקו).
בנייה: python _src/build_demo.py  ->  demo/index.html (בונה אגב גם את שני העמודים הרגילים)."""
import json, os
from build import page_head, TOPBAR, HERE

OUT_DEMO = os.path.join(os.path.dirname(HERE), 'demo', 'index.html')
D = json.load(open(os.path.join(HERE, 'data', 'houston_stats.json'), encoding='utf-8'))

# ---------- גרף SVG מאפס: מחירי בתים מול שכר דירה, 1995=100 ----------
hpi  = {int(k): v for k, v in D['hpi_q1'].items()}
rent = {int(k): v for k, v in D['rent_jan'].items()}
rent_base = rent[1995]
years = sorted(hpi)

X0, X1, Y0, Y1 = 60, 690, 20, 300           # אזור השרטוט בתוך viewBox 720x360
VMIN, VMAX = 80, 440

def sx(year): return X0 + (year - 1995) / (2026 - 1995) * (X1 - X0)
def sy(val):  return Y1 - (val - VMIN) / (VMAX - VMIN) * (Y1 - Y0)

def polyline(series, norm=1.0):
    return ' '.join(f'{sx(y):.1f},{sy(series[y] / norm * (100 if norm != 1.0 else 1)):.1f}'
                    for y in years)

pts_hpi  = ' '.join(f'{sx(y):.1f},{sy(hpi[y]):.1f}' for y in years)
pts_rent = ' '.join(f'{sx(y):.1f},{sy(rent[y] / rent_base * 100):.1f}' for y in years)

grid = '\n'.join(
    f'<line x1="{X0}" y1="{sy(v):.0f}" x2="{X1}" y2="{sy(v):.0f}" stroke="#e6edf0" stroke-width="1"/>'
    f'<text x="{X0-8}" y="{sy(v)+4:.0f}" font-size="12" fill="#7c8a91" text-anchor="end">{v}</text>'
    for v in (100, 200, 300, 400))
ticks = '\n'.join(
    f'<text x="{sx(y):.0f}" y="{Y1+22}" font-size="12" fill="#7c8a91" text-anchor="middle">{y}</text>'
    for y in (1995, 2000, 2005, 2010, 2015, 2020, 2026))

CHART = f"""<svg viewBox="0 0 720 360" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto;background:#fff;border:1px solid #e6edf0;border-radius:14px" role="img" aria-label="מחירי בתים מול שכר דירה ביוסטון">
{grid}
{ticks}
<polyline points="{pts_hpi}" fill="none" stroke="#1d4e5d" stroke-width="3" stroke-linejoin="round"/>
<polyline points="{pts_rent}" fill="none" stroke="#36a7da" stroke-width="3" stroke-dasharray="7 5" stroke-linejoin="round"/>
<text x="{sx(2026)-6:.0f}" y="{sy(hpi[2026])-10:.0f}" font-size="13" font-weight="700" fill="#1d4e5d" text-anchor="end">מחירי בתים ×{hpi[2026]/100:.1f}</text>
<text x="{sx(2026)-6:.0f}" y="{sy(rent[2026]/rent_base*100)-10:.0f}" font-size="13" font-weight="700" fill="#36a7da" text-anchor="end">שכר דירה ×{rent[2026]/rent_base:.1f}</text>
<rect x="{X0}" y="325" width="14" height="4" fill="#1d4e5d"/><text x="{X0+20}" y="331" font-size="12.5" fill="#3a4a52">מדד מחירי בתים - יוסטון (FHFA)</text>
<rect x="{X0+240}" y="325" width="14" height="4" fill="#36a7da"/><text x="{X0+260}" y="331" font-size="12.5" fill="#3a4a52">מדד שכר דירה - יוסטון (BLS)</text>
</svg>"""

# ---------- CSS ייעודי לדמה ----------
DEMO_CSS = """
:root{--maxw:740px}
.demo-ribbon{position:sticky;top:0;z-index:99;background:#b3261e;color:#fff;text-align:center;
font-weight:700;font-size:14.5px;padding:9px 14px;letter-spacing:.2px}
.pagehead{background:var(--teal-deep);color:#fff;padding:34px 22px}
.pagehead .in{max-width:var(--maxw);margin:0 auto}
.pagehead h1{font-size:clamp(24px,6vw,38px);font-weight:800;line-height:1.25;margin-bottom:8px}
.pagehead p{color:#c4dde4;font-size:16.5px;margin:0}
h2{font-size:clamp(23px,5.8vw,32px)}
.mlist{list-style:none;margin:10px 0 2px}
.mlist li{background:var(--tint);border:1px solid var(--line);border-right:4px solid var(--teal);
border-radius:12px;padding:14px 16px;margin-bottom:11px;font-size:16.5px;line-height:1.75;color:var(--ink)}
.mlist b{color:var(--teal)}
.stats{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin:18px 0}
.stats div{background:var(--tint);border:1px solid var(--line);border-right:4px solid var(--blue);
border-radius:14px;padding:15px 16px}
.stats b{display:block;color:var(--teal);font-size:clamp(17px,4.6vw,21px);margin-bottom:4px}
.stats span{font-size:14px;color:var(--body);line-height:1.55;display:block}
.src{font-size:12.5px;color:var(--muted);line-height:1.7;margin-top:10px}
.src a{color:var(--blue)}
@media(min-width:600px){.stats{grid-template-columns:1fr 1fr 1fr 1fr}}
"""

MISTAKES = [
    ("רכישה באזור עם ביקוש שכירות חלש.",
     "לא כל כתובת בארה״ב מושכרת בקלות. לכן הסינון אצלנו מתחיל בביקוש - תעסוקה, נגישות, בתי ספר והמשך אכלוס - ולא במחיר הנמוך ביותר."),
    ("בית ישן שנראה זול - ומתגלה כיקר.",
     "מערכות בסוף חייהן, תחזוקה שלא תוקצבה והפתעות אחרי הרכישה. בית חדש עם אחריות קבלן לא מבטל סיכון, אבל משנה מהותית את נקודת הפתיחה."),
    ("מבנה השקעה לא שקוף.",
     "קופות משותפות, שותפויות מרובות-משקיעים והבטחות כלליות. אצלנו המבנה פשוט: LLC בבעלות המשקיע, חשבון בנק שלו, והבית רשום על שם החברה שלו."),
    ("ניהול מרחוק בלי כתובת ברורה.",
     "בלי גורם מקצועי שמלווה את ההשקעה, ניהול מעבר לים נשען על התכתבויות באנגלית מול גורמים מתחלפים. אצלנו: חברת ניהול מקומית בשטח, ומענה גם בעברית."),
    ("רכישה דרך מתווכים בלי שליטה בתהליך.",
     "כשלא ברור מי אחראי על מה, בעיות נופלות בין הכיסאות. אצלנו התהליך שקוף מקצה לקצה, וכל החלטה עוברת דרך המשקיע."),
    ("החלטה על סמך אקסל אופטימי.",
     "תרחישים ורודים בלי רזרבות ובלי תקופות ללא שוכר. אנחנו בוחנים כל נכס גם בתרחישים שמרניים - וחלק מהתפקיד שלנו הוא לפעמים להמליץ לא להתקדם."),
]
mist_html = '\n'.join(f'<li><b>{m}</b> {a}</li>' for m, a in MISTAKES)

HTML_DEMO = f"""{page_head('גרסת דמה פנימית - תוספות מוצעות | Aspect × PrimeVest', 'Texas Demo Internal', DEMO_CSS)}
<body>
<div class="demo-ribbon">גרסת דמה פנימית - טיוטה לבדיקה בלבד, לא לשיתוף</div>
{TOPBAR}
<div class="pagehead"><div class="in">
  <h1>תוספות מוצעות למצגת</h1>
  <p>שלושה מקטעים לבחינה, בהשראת ניתוח מצגות מתחרים - כל הנתונים חושבו מחדש ממקורות רשמיים</p>
</div></div>

<main>
  <section><h2>טעויות נפוצות של משקיעים ישראלים בנדל&quot;ן אמריקאי</h2>
    <p>לפני שמדברים על יתרונות, שווה להכיר את הדפוסים שחוזרים אצל משקיעים שנכוו. המודל שלנו נבנה, בין השאר, כדי לעקוף אותם:</p>
    <ul class="mlist">{mist_html}</ul>
    <p style="margin-top:14px">אף אחת מהטעויות האלה לא הופכת השקעה לרעה בהכרח - אבל כולן יחד מסבירות למה בנינו את המודל בדיוק כך.</p></section>

  <section><h2>המספרים של יוסטון</h2>
    <p>ארבעה נתונים שמחזיקים את הסיפור - מחושבים על ידינו מסדרות רשמיות, לא מועתקים מאף מצגת:</p>
    <div class="stats">
      <div><b>‎+5.5%‎ לשנה</b><span>מחירי בתים ביוסטון - ממוצע 10 שנים (FHFA)</span></div>
      <div><b>‎+3.3%‎ לשנה</b><span>שכר דירה ביוסטון - ממוצע 10 שנים (BLS)</span></div>
      <div><b>‎7.3M+‎ תושבים</b><span>מטרו יוסטון; גידול של כ-20% בעשור (Census)</span></div>
      <div><b>‎×4.1 מול ×2.6‎</b><span>מחירי בתים מול שכר דירה מאז 1995 - הפער שדוחף משפחות לשכירות</span></div>
    </div>
    {CHART}
    <p style="margin-top:14px">הפער בין הקווים הוא הסיפור: מחירי הבתים עלו כמעט פי שניים יותר משכר הדירה, ולכן חלק גדל של משפחות נשאר בשכירות - הבסיס לביקוש שעליו נשען המודל.</p>
    <p class="src">מקורות: FRED, הבנק הפדרלי של סנט לואיס - מדד מחירי בתים
    <a href="https://fred.stlouisfed.org/series/ATNHPIUS26420Q" target="_blank" rel="noopener">ATNHPIUS26420Q</a> (FHFA),
    מדד שכר דירה <a href="https://fred.stlouisfed.org/series/CUURA318SEHA" target="_blank" rel="noopener">CUURA318SEHA</a> (BLS),
    אוכלוסייה <a href="https://fred.stlouisfed.org/series/HTNPOP" target="_blank" rel="noopener">HTNPOP</a> (Census).
    שני המדדים בגרף מנורמלים ל-100 בשנת 1995; נתוני 2026 - רבעון ראשון. עיבוד וחישוב: Aspect, יולי 2026.</p></section>

  <section><h2>למי המודל מתאים</h2>
    <p>המודל נבנה עבור משקיע שמעריך בעלות ושליטה, חושב בטווח של שנים ולא של חודשים, ורוצה תהליך מלווה שבו כתובת אחת אחראית לחבר את כל החלקים - נכס, חברה, בנק, מימון, ביטוח, שוכר וניהול.</p>
    <p>מי שמחפש ספקולציה קצרה או הבטחת תשואה - כנראה ימצא מודלים אחרים שמתאימים לו יותר, וזה בסדר גמור. אנחנו מעדיפים התאמה נכונה על פני עוד עסקה.</p></section>
</main>

<div class="disclaimer">
  <h3>גרסת דמה - הבהרה</h3>
  <p>עמוד זה הוא טיוטה פנימית לבחינת תוספות תוכן. הוא אינו חלק מהמצגת הרשמית, אינו מיועד להפצה, והנתונים בו - אף שחושבו ממקורות רשמיים - טרם עברו אישור סופי לפרסום.</p>
</div>
<footer><b>Aspect Boutique Investments</b> &nbsp;×&nbsp; <b>PrimeVest Realty</b><br>גרסת דמה פנימית</footer>
</body>
</html>"""

os.makedirs(os.path.dirname(OUT_DEMO), exist_ok=True)
open(OUT_DEMO, 'w', encoding='utf-8').write(HTML_DEMO)
print('wrote demo/index.html -', round(os.path.getsize(OUT_DEMO)/1024), 'KB')
