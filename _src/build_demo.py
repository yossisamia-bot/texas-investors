# -*- coding: utf-8 -*-
"""עמוד דמה פנימי - תוספות מוצעות בהשראת ניתוח מצגת R-M (12/07/2026).
לא חלק מהאתר הרשמי: מסומן באדום "גרסת דמה", לא מקושר משום עמוד.
12/07 ערב: מקטע "המספרים של יוסטון" אושר ע"י יוסי ועבר לעמודים החיים (STATS_SECTION
ב-build.py, מוצג במקוצר אחרי "למה טקסס" ובמלא בסוף). כאן נשארו לבחינה: טעויות נפוצות + למי מתאים.
בנייה: python _src/build_demo.py  ->  demo/index.html (בונה אגב גם את שני העמודים הרגילים)."""
import os
from build import page_head, TOPBAR, STATS_SECTION, HERE

OUT_DEMO = os.path.join(os.path.dirname(HERE), 'demo', 'index.html')

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
  <p>מקטעים לבחינה. מקטע "המספרים של יוסטון" כבר אושר ועבר לעמודים החיים - כאן נשארו השניים הבאים</p>
</div></div>

<main>
  <section><h2>טעויות נפוצות של משקיעים ישראלים בנדל&quot;ן אמריקאי</h2>
    <p>לפני שמדברים על יתרונות, שווה להכיר את הדפוסים שחוזרים אצל משקיעים שנכוו. המודל שלנו נבנה, בין השאר, כדי לעקוף אותם:</p>
    <ul class="mlist">{mist_html}</ul>
    <p style="margin-top:14px">אף אחת מהטעויות האלה לא הופכת השקעה לרעה בהכרח - אבל כולן יחד מסבירות למה בנינו את המודל בדיוק כך.</p></section>

  <section><h2>למי המודל מתאים</h2>
    <p>המודל נבנה עבור משקיע שמעריך בעלות ושליטה, חושב בטווח של שנים ולא של חודשים, ורוצה תהליך מלווה שבו כתובת אחת אחראית לחבר את כל החלקים - נכס, חברה, בנק, מימון, ביטוח, שוכר וניהול.</p>
    <p>מי שמחפש ספקולציה קצרה או הבטחת תשואה - כנראה ימצא מודלים אחרים שמתאימים לו יותר, וזה בסדר גמור. אנחנו מעדיפים התאמה נכונה על פני עוד עסקה.</p></section>

  {STATS_SECTION}
</main>

<div class="disclaimer">
  <h3>גרסת דמה - הבהרה</h3>
  <p>עמוד זה הוא טיוטה פנימית לבחינת תוספות תוכן. הוא אינו חלק מהמצגת הרשמית ואינו מיועד להפצה. מקטע המספרים מוצג כאן לרפרנס - הגרסה החיה שלו נמצאת בעמודים הרשמיים.</p>
</div>
<footer><b>Aspect Boutique Investments</b> &nbsp;×&nbsp; <b>PrimeVest Realty</b><br>גרסת דמה פנימית</footer>
</body>
</html>"""

os.makedirs(os.path.dirname(OUT_DEMO), exist_ok=True)
open(OUT_DEMO, 'w', encoding='utf-8').write(HTML_DEMO)
print('wrote demo/index.html -', round(os.path.getsize(OUT_DEMO)/1024), 'KB')
