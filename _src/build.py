# -*- coding: utf-8 -*-
"""בונה עמוד נחיתה mobile-first עצמאי (base64 מוטמע) מתוכן מצגת טקסס."""
import base64, io, os

HERE   = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(HERE, 'assets')
OUT    = os.path.join(os.path.dirname(HERE), 'index.html')

def b64_img(name, max_w=None, quality=72, jpeg=True):
    path = os.path.join(ASSETS, name)
    raw = open(path, 'rb').read()
    mime = 'image/jpeg' if name.lower().endswith(('jpg','jpeg')) else 'image/png'
    if max_w:
        try:
            from PIL import Image
            im = Image.open(io.BytesIO(raw))
            if im.mode in ('RGBA','P') and jpeg:
                im = im.convert('RGB')
            if im.width > max_w:
                h = int(im.height * max_w / im.width)
                im = im.resize((max_w, h), Image.LANCZOS)
            buf = io.BytesIO()
            if jpeg:
                im.save(buf, 'JPEG', quality=quality, optimize=True); mime='image/jpeg'
            else:
                im.save(buf, 'PNG', optimize=True); mime='image/png'
            raw = buf.getvalue()
        except Exception as e:
            print('  (resize skipped for', name, '->', e, ')')
    b = base64.b64encode(raw).decode()
    print(f'  {name}: {len(b)//1024} KB base64')
    return f'data:{mime};base64,{b}'

print('encoding images...')
LOGO_ASPECT = b64_img('image1.png', jpeg=False)          # logo - keep png/transparent
LOGO_PRIME  = b64_img('image2.png', jpeg=False)
HERO        = b64_img('image3.jpg', max_w=1280, quality=74)  # Houston skyline
AERIAL      = b64_img('image7.jpg', max_w=1100, quality=72)  # master-planned aerial
STREET      = b64_img('image5.jpg', max_w=1100, quality=72)  # new-home street

CHECK = ("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'"
         "%3E%3Cpath fill='none' stroke='%2336a7da' stroke-width='3' stroke-linecap='round'"
         " stroke-linejoin='round' d='M5 13l4 4L19 7'/%3E%3C/svg%3E")

import urllib.parse
WA_NUM  = '972544668462'
WA_TEXT = urllib.parse.quote('היי, הגעתי מעמוד הבתים החדשים בטקסס ואשמח לשמוע עוד פרטים')
WA_LINK = f'https://wa.me/{WA_NUM}?text={WA_TEXT}'

# ---------- תוכן: נקרא מתוך מסמך המאסטר presentation.docx (מקור-אמת יחיד) ----------
# עורכים את presentation.docx -> python build.py -> האתר וקובץ ההורדה מתעדכנים יחד.
# מבנה מחייב במסמך: כותרת-מקטע = פסקה מודגשת קצרה; פריט-רשימה = שורה שמתחילה ב-"•".
from docx import Document
from docx.oxml.text.paragraph import CT_P
from docx.oxml.table import CT_Tbl
from docx.table import Table
from docx.text.paragraph import Paragraph

MASTER = os.path.join(os.path.dirname(HERE), 'presentation.docx')
HEADING_MAXLEN = 60

def _bold_first(p):
    for r in p.runs:
        if r.text.strip():
            return bool(r.bold)
    return False

def parse_master(path):
    items = []
    doc = Document(path)
    for ch in doc.element.body.iterchildren():
        if isinstance(ch, CT_P):
            p = Paragraph(ch, doc)
            t = p.text.strip()
            if t:
                items.append(('p', t, _bold_first(p)))
        elif isinstance(ch, CT_Tbl):
            tb = Table(ch, doc)
            cells = [c.text.strip() for row in tb.rows for c in row.cells]
            txt = '\n'.join(x for x in cells if x).strip()
            if txt:
                items.append(('tbl', txt, False))
    def is_heading(it):
        return it[0] == 'p' and it[2] and len(it[1]) < HEADING_MAXLEN
    intro_paras, sections, cur, mode = [], {}, None, 'intro'
    for it in items[2:]:                       # items[0]=כותרת, items[1]=כותרת-משנה (נשארות ב-HERO)
        if is_heading(it):
            cur = {'pre': [], 'bullets': [], 'post': []}
            sections[it[1]] = cur
            mode = 'section'
            continue
        text = it[1]
        if mode == 'intro':
            intro_paras.append(text)
        elif text.startswith('•'):
            cur['bullets'].append(text.lstrip('•').strip())
        elif cur['bullets']:
            cur['post'].append(text)
        else:
            cur['pre'].append(text)
    return intro_paras, sections

intro_paras, S = parse_master(MASTER)
EXPECTED = ['מה למדנו בדרך', 'מה מצאנו בטקסס', 'ההיגיון מאחורי הבחירה בבתים חדשים',
            'המודל שבנינו סביב הנכס', 'התפקיד שלנו בתהליך', 'חשוב להבהיר', 'איך זה עובד בפועל',
            'איך אנחנו מסתכלים על ההשקעה', 'כמה דברים שחשוב לקחת בחשבון', 'איך ממשיכים מכאן',
            'גילוי נאות ודיסקליימר']
_missing = [h for h in EXPECTED if h not in S]
if _missing:
    raise SystemExit('ERROR: כותרות חסרות במסמך המאסטר (שונו או נמחקו?): ' + ' | '.join(_missing))

intro         = [('lead', intro_paras[0])] + [('', p) for p in intro_paras[1:]]
learned       = S['מה למדנו בדרך']['pre']
texas         = S['מה מצאנו בטקסס']['pre']
logic_intro   = S['ההיגיון מאחורי הבחירה בבתים חדשים']['pre'][0]
logic_bullets = S['ההיגיון מאחורי הבחירה בבתים חדשים']['bullets']
logic_close   = S['ההיגיון מאחורי הבחירה בבתים חדשים']['post'][0]
model         = S['המודל שבנינו סביב הנכס']['pre']
role          = S['התפקיד שלנו בתהליך']['pre']
clarify       = S['חשוב להבהיר']['pre'][0]
steps_intro   = S['איך זה עובד בפועל']['pre'][0]
steps         = S['איך זה עובד בפועל']['bullets']
steps_close   = S['איך זה עובד בפועל']['post'][0]
view          = S['איך אנחנו מסתכלים על ההשקעה']['pre']
consider      = S['כמה דברים שחשוב לקחת בחשבון']['pre']
nextsteps     = S['איך ממשיכים מכאן']['pre']
disclaimer    = S['גילוי נאות ודיסקליימר']['pre'][0]

def paras(items):
    out=[]
    for it in items:
        if isinstance(it, tuple):
            cls, txt = it
            out.append(f'<p class="{cls}">{txt}</p>' if cls else f'<p>{txt}</p>')
        else:
            out.append(f'<p>{it}</p>')
    return '\n'.join(out)

def cards(items):
    li='\n'.join(f'<li>{x}</li>' for x in items)
    return f'<ul class="cards">{li}</ul>'

def stepslist(items):
    li='\n'.join(f'<li>{x}</li>' for x in items)
    return f'<ol class="steps">{li}</ol>'

HTML = f"""<!DOCTYPE html>
<html lang="he" dir="rtl">
<head>
<meta charset="utf-8">
<script async src="https://www.googletagmanager.com/gtag/js?id=G-S1E7F8WCWF"></script>
<script>
window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}
gtag('js',new Date());gtag('config','G-S1E7F8WCWF',{{page_title:'Texas Investors'}});
</script>
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="robots" content="noindex, nofollow">
<meta name="theme-color" content="#143a46">
<title>בתים חדשים מקבלנים ציבוריים בטקסס | Aspect × PrimeVest</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Heebo:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
<style>
:root{{--teal:#1d4e5d;--teal-deep:#143a46;--blue:#36a7da;--blue-soft:#eaf6fc;
--ink:#1d272d;--body:#3a4a52;--muted:#7c8a91;--line:#e6edf0;--bg:#fff;--tint:#f6f9fb;--maxw:690px;}}
*{{box-sizing:border-box;margin:0;padding:0}}
html{{scroll-behavior:smooth}}
body{{font-family:'Heebo',system-ui,-apple-system,sans-serif;color:var(--body);background:var(--bg);
font-size:18px;line-height:1.9;-webkit-text-size-adjust:100%;text-rendering:optimizeLegibility;}}
img{{max-width:100%;display:block}}
.progress{{position:fixed;top:0;right:0;height:3px;background:var(--blue);width:0;z-index:80;}}
.topbar{{position:sticky;top:0;z-index:60;background:rgba(255,255,255,.93);backdrop-filter:blur(10px);
border-bottom:1px solid var(--line);}}
.topbar .in{{max-width:var(--maxw);margin:0 auto;display:flex;align-items:center;justify-content:space-between;
gap:14px;padding:9px 20px}}
.topbar img.a{{height:23px}} .topbar img.p{{height:30px}}
.hero{{position:relative;min-height:64vh;display:flex;align-items:flex-end;background:#0b2a33;overflow:hidden}}
.hero .bg{{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;opacity:.5}}
.hero .gr{{position:absolute;inset:0;background:linear-gradient(to top,rgba(10,30,37,.96) 6%,rgba(10,30,37,.30) 58%,rgba(10,30,37,.55))}}
.hero .in{{position:relative;max-width:var(--maxw);margin:0 auto;padding:38px 22px 32px;color:#fff;width:100%}}
.eyebrow{{display:inline-block;color:#fff;background:var(--blue);font-weight:700;font-size:13px;
letter-spacing:.4px;padding:5px 12px;border-radius:30px;margin-bottom:14px}}
.hero h1{{font-size:clamp(27px,7.2vw,40px);line-height:1.22;font-weight:800;color:#fff;margin-bottom:12px;letter-spacing:-.5px}}
.hero .sub{{font-size:18px;color:#d4e6ec;font-weight:400}}
main{{max-width:var(--maxw);margin:0 auto;padding:0 22px}}
section{{padding:34px 0;border-bottom:1px solid var(--line)}}
h2{{font-size:clamp(21px,5.6vw,27px);color:var(--teal);font-weight:800;line-height:1.3;
margin-bottom:18px;padding-bottom:11px;position:relative;letter-spacing:-.3px}}
h2::after{{content:"";position:absolute;bottom:0;right:0;width:48px;height:3px;background:var(--blue);border-radius:2px}}
p{{margin-bottom:15px}} p:last-child{{margin-bottom:0}}
p.lead{{font-size:19.5px;color:var(--ink);font-weight:500;line-height:1.85}}
figure{{margin:22px -4px 6px;border-radius:18px;overflow:hidden;box-shadow:0 10px 30px -12px rgba(20,58,70,.4)}}
figure img{{width:100%;height:225px;object-fit:cover}}
ul.cards{{list-style:none;margin:6px 0 2px}}
ul.cards li{{background:var(--tint);border:1px solid var(--line);border-radius:14px;padding:14px 15px;
margin-bottom:11px;display:flex;gap:13px;align-items:flex-start;font-size:16.5px;line-height:1.7;color:var(--ink)}}
ul.cards li::before{{content:"";flex:0 0 auto;width:24px;height:24px;margin-top:2px;border-radius:8px;
background:var(--blue-soft) url("{CHECK}") center/15px no-repeat}}
ol.steps{{list-style:none;counter-reset:s;margin:8px 0 2px}}
ol.steps li{{counter-increment:s;position:relative;padding:3px 48px 20px 0;font-size:16.5px;line-height:1.7;color:var(--ink)}}
ol.steps li:last-child{{padding-bottom:0}}
ol.steps li::before{{content:counter(s);position:absolute;right:0;top:-2px;width:34px;height:34px;border-radius:50%;
background:var(--teal);color:#fff;font-weight:700;font-size:15px;display:flex;align-items:center;justify-content:center;z-index:2}}
ol.steps li:not(:last-child)::after{{content:"";position:absolute;right:16px;top:32px;bottom:4px;width:2px;background:var(--line)}}
.callout{{background:var(--blue-soft);border-radius:14px;padding:17px 18px;margin-top:18px;
font-size:16.5px;color:var(--teal-deep);font-weight:500;line-height:1.75}}
.note{{border-right:4px solid var(--blue);background:var(--tint);padding:15px 17px;border-radius:0 12px 12px 0;
font-size:17px;color:var(--ink)}}
.cta{{background:var(--teal);color:#fff;text-align:center;padding:44px 22px}}
.cta h2{{color:#fff;padding-bottom:13px}} .cta h2::after{{right:50%;transform:translateX(50%)}}
.cta p{{color:#c4dde4;font-size:17px;max-width:440px;margin:0 auto}}
.cta .btns{{display:flex;flex-direction:column;gap:12px;max-width:360px;margin:22px auto 0}}
.cta a.btn{{display:flex;align-items:center;justify-content:center;gap:9px;padding:15px;border-radius:13px;
font-weight:700;font-size:17px;text-decoration:none;transition:transform .12s}}
.cta a.btn:active{{transform:scale(.98)}}
.btn.solid{{background:#fff;color:var(--teal)}}
.btn.ghost{{background:rgba(255,255,255,.08);border:1.5px solid rgba(255,255,255,.45);color:#fff}}
.disclaimer{{max-width:var(--maxw);margin:0 auto;padding:26px 22px 46px;color:var(--muted);font-size:12.5px;line-height:1.7}}
.disclaimer h3{{font-size:13px;color:var(--body);margin-bottom:8px;font-weight:700;letter-spacing:.3px}}
footer{{background:var(--teal-deep);color:#9fc0cb;text-align:center;font-size:12.5px;padding:22px;line-height:1.8}}
footer b{{color:#e6f1f4;font-weight:600}}
.wa-line{{display:inline-flex;align-items:center;gap:8px;margin-top:18px;padding:11px 22px;border-radius:11px;
background:#2a8c5e;color:#fff;font-weight:600;font-size:15.5px;text-decoration:none;transition:background .15s,transform .12s}}
.wa-line:hover{{background:#23744d}}
.wa-line:active{{transform:scale(.97)}}
.wa-line svg{{width:18px;height:18px}}
@media(min-width:600px){{figure img{{height:300px}} body{{font-size:18.5px}}}}
@media print{{.progress,.topbar,.cta .btns{{display:none}} .hero{{min-height:auto}} section{{break-inside:avoid}}}}
</style>
</head>
<body>
<div class="progress" id="pg"></div>
<header class="topbar"><div class="in">
  <img class="a" src="{LOGO_ASPECT}" alt="Aspect Boutique Investments">
  <img class="p" src="{LOGO_PRIME}" alt="PrimeVest Realty">
</div></header>

<div class="hero">
  <img class="bg" src="{HERO}" alt="Houston skyline">
  <div class="gr"></div>
  <div class="in">
    <span class="eyebrow">Aspect × PrimeVest Realty</span>
    <h1>בתים חדשים מקבלנים<br>ציבוריים בטקסס</h1>
    <div class="sub">כיצד הגענו למודל, ומה מצאנו בדרך</div>
  </div>
</div>

<main>
  <section>{paras(intro)}</section>
  <section><h2>מה למדנו בדרך</h2>{paras(learned)}</section>
  <section><h2>מה מצאנו בטקסס</h2>{paras(texas)}
    <figure><img src="{AERIAL}" alt="שכונה חדשה ומתוכננת באזור יוסטון"></figure></section>
  <section><h2>ההיגיון מאחורי הבחירה בבתים חדשים</h2>
    <p>{logic_intro}</p>{cards(logic_bullets)}
    <figure><img src="{STREET}" alt="רחוב בשכונת בתים חדשים"></figure>
    <p style="margin-top:18px">{logic_close}</p></section>
  <section><h2>המודל שבנינו סביב הנכס</h2>{paras(model)}</section>
  <section><h2>התפקיד שלנו בתהליך</h2>{paras(role)}</section>
  <section><h2>חשוב להבהיר</h2><div class="note">{clarify}</div></section>
  <section><h2>איך זה עובד בפועל</h2><p>{steps_intro}</p>{stepslist(steps)}
    <div class="callout">{steps_close}</div></section>
  <section><h2>איך אנחנו מסתכלים על ההשקעה</h2>{paras(view)}</section>
  <section><h2>כמה דברים שחשוב לקחת בחשבון</h2>{paras(consider)}</section>
  <section><h2>איך ממשיכים מכאן</h2>{paras(nextsteps)}</section>
</main>

<div class="cta">
  <h2>רוצים להעמיק במספרים?</h2>
  <p>שני כלים אינטראקטיביים שבנינו כדי ללוות את הבדיקה:</p>
  <div class="btns">
    <a class="btn solid" href="https://yossisamia-bot.github.io/prop-compare/" target="_blank" rel="noopener" onclick="gtag('event','tool_click',{{tool:'calculator'}})">מחשבון השוואת השקעה</a>
    <a class="btn solid" href="https://yossisamia-bot.github.io/houston-map/" target="_blank" rel="noopener" onclick="gtag('event','tool_click',{{tool:'map'}})">מפת ההשקעות ביוסטון</a>
  </div>
  <a class="wa-line" href="{WA_LINK}" target="_blank" rel="noopener" onclick="gtag('event','whatsapp_click')"><svg viewBox="0 0 24 24" fill="#fff" xmlns="http://www.w3.org/2000/svg"><path d="M12.04 2c-5.46 0-9.91 4.45-9.91 9.91 0 1.75.46 3.45 1.32 4.95L2.05 22l5.25-1.38c1.45.79 3.08 1.21 4.74 1.21h.01c5.46 0 9.91-4.45 9.91-9.91 0-2.65-1.03-5.14-2.9-7.01A9.82 9.82 0 0 0 12.04 2zm5.8 14.13c-.24.68-1.42 1.31-1.95 1.36-.5.05-.96.24-3.23-.67-2.73-1.08-4.46-3.86-4.6-4.04-.13-.18-1.1-1.46-1.1-2.79 0-1.33.7-1.98.95-2.25.24-.27.53-.34.71-.34.18 0 .35 0 .51.01.16.01.39-.06.6.46.24.58.81 2 .88 2.14.07.14.12.31.02.49-.09.18-.14.29-.27.45-.14.16-.29.36-.41.48-.14.14-.28.29-.12.56.16.27.71 1.17 1.53 1.9 1.05.94 1.94 1.23 2.21 1.37.27.14.43.12.59-.07.16-.18.68-.79.86-1.06.18-.27.36-.22.6-.13.24.09 1.55.73 1.82.86.27.14.45.2.51.31.07.12.07.66-.17 1.32z"/></svg>דברו איתנו בוואטסאפ</a>
</div>

<div class="disclaimer">
  <h3>גילוי נאות ודיסקליימר</h3>
  <p>{disclaimer}</p>
</div>
<footer><b>Aspect Boutique Investments</b> &nbsp;×&nbsp; <b>PrimeVest Realty</b><br>המסמך מיועד לנמענים רלוונטיים בלבד</footer>

<script>
var pg=document.getElementById('pg');
function upd(){{var h=document.documentElement;var sc=h.scrollTop||document.body.scrollTop;
var mx=(h.scrollHeight-h.clientHeight)||1;pg.style.width=(sc/mx*100)+'%';}}
addEventListener('scroll',upd,{{passive:true}});upd();
</script>
</body>
</html>"""

open(OUT,'w',encoding='utf-8').write(HTML)
print('wrote index.html -', round(os.path.getsize(OUT)/1024), 'KB')
