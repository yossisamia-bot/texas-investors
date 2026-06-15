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

# ---------- תוכן ----------
intro = [
 ("lead","אנחנו קבוצת יזמים עצמאית הפועלת בנדל״ן בישראל למעלה מחמש עשרה שנה. לאורך הדרך הקמנו וניהלנו חברות נדל״ן, ליווינו מאות משפחות ומשקיעים, והובלנו תהליכים מורכבים משלב איתור הקרקע והתכנון, דרך מימון, ביצוע ופיקוח, ועד אכלוס וניהול נכסים."),
 ("","את המודל הנוכחי לא בנינו כמוצר מדף או כמצגת שיווקית, אלא מתוך אותה דרך עבודה שמלווה אותנו שנים: לבדוק לעומק, לפעול קודם בעצמנו, לפרק תהליך מורכב לגורמים, ורק לאחר מכן לחבר אותו למערכת השקעה מסודרת שאפשר להציע גם למשקיעים נוספים."),
 ("","בשנים האחרונות, כשהשוק השתנה ועלויות הבנייה והריבית עלו, שאלנו את עצמנו שאלה פשוטה: אם היינו משקיעים את כספנו היום - איפה ואיך היינו עושים זאת?"),
 ("","לא חיפשנו את העסקה שנראית הכי טוב במצגת, אלא מודל שנראה לנו הגיוני גם אחרי בדיקה עמוקה: נכס אמיתי, בעלות ברורה, תהליך מסודר ואפשרות להחזיק לאורך זמן. מתוך הבדיקה הזו הגענו למודל של רכישת בתים חדשים מקבלנים ציבוריים גדולים בטקסס."),
 ("","המסמך הזה נועד להסביר את דרך החשיבה, את המבנה שבנינו סביב הנכס, ואת הדברים שחשוב להבין לפני שמתקדמים."),
]
learned = [
 "בחנו כמה מסלולים במקביל: פעילות בישראל ובהולנד, רכישת קרקעות, בנייה עצמית בארצות הברית, עסקאות יזמיות ומודלים שונים של החזקה וניהול. חלק מהמסלולים מעניינים בפני עצמם, וחלקם עדיין נבחנים על ידינו.",
 "אבל ככל שהעמקנו, חזרנו שוב ושוב לאותה שאלה: לא רק מה אפשר לבצע, אלא מהו היחס הנכון בין סוג הנכס, מחיר, מימון, שליטה, תזרים, ניהול וגמישות עתידית.",
 "מתוך הזווית הזו התחלנו להתעמק בבתים חדשים מקבלנים ציבוריים גדולים בטקסס - לא כתחליף פשוט ליזמות, אלא כמודל שנראה לנו מאוזן יותר ביחס לתקופה, לשוק ולמבנה ההחזקה שרצינו לבנות סביב המשקיע.",
]
texas = [
 "סביבת הריבית הגבוהה בארצות הברית הקשתה על שוק הנדל״ן כולו. אבל דווקא המצב הזה יצר לחץ גם אצל קבלנים ציבוריים גדולים, שמחזיקים מלאי משמעותי של בתים חדשים ומחויבים להמשיך למכור, לייצר תזרים ולהציג פעילות שוטפת.",
 "בפגישות שקיימנו עם קבלנים, מלווים ואנשי מקצוע מקומיים, ראינו נכונות גבוהה יותר מהרגיל להעניק הטבות, שדרוגים, סיוע בעלויות סגירה ולעיתים גם תנאי מימון שלא היו זמינים באותה צורה בשנים אחרות. זה לא אומר שאין סיכון או שכל עסקה תקבל תנאים כאלה; זה אומר שנוצר מצב שוק ששווה לבחון ברצינות.",
 "כיזמים אנחנו רגילים לחשוב על קרקע, רישוי, תכנון ובנייה. כאן מצאנו נקודת כניסה אחרת: הקרקע כבר נרכשה, הבית כבר תוכנן ונבנה או קרוב למסירה, והמשקיע נכנס בשלב שבו הנכס כבר קיים, ניתן לבדיקה הנדסית, ניתן לבחינת מימון וניתן להשכרה בפרק זמן קצר יחסית.",
 "הבתים שאנו בוחנים נמצאים בשכונות חדשות ומתוכננות באזור יוסטון רבתי ובאזורים דומים בטקסס. הדגש שלנו אינו על סיפור יפה של עיר או שכונה, אלא על מיקומים שנבחנים לפי פרמטרים מעשיים: ביקוש לשכירות, תעסוקה, תשתיות, בתי ספר, נגישות, שכונות בשלבי אכלוס וצמיחה, וחברת ניהול שמסוגלת לפעול בשטח לאורך זמן.",
]
logic_intro = "הבחירה בבתים חדשים לא נבעה מגורם אחד, אלא משילוב של כמה שכבות שמתחברות יחד:"
logic_bullets = [
 "בית חדש שנבנה על ידי קבלן גדול ומבוסס, ולא נכס ישן שדורש הערכת תחזוקה עמוקה כבר ביום הראשון.",
 "אחריות קבלן בשנים הראשונות, בהתאם לתנאי האחריות וההסכמים הרלוונטיים, שמקטינה חלק מההפתעות שמאפיינות נכסים ותיקים.",
 "אפשרות לבצע בדק בית מסודר לפני סגירה ולפעול מול הקבלן לתיקון ליקויים לפני המסירה.",
 "אפשרות לבחון מימון מסוג DSCR במקרים מתאימים ובכפוף לאישור מלווה - הלוואה שמבוססת בעיקר על הכנסות הנכס ולא על הכנסותיו האישיות של המשקיע.",
 "אפשרות לאכלס את הנכס בשוכר בפרק זמן קצר יחסית לאחר הסגירה, במקום להמתין לסיום תכנון ובנייה.",
 "שכונות חדשות ומתוכננות, שבהן חלק מהפוטנציאל נובע מהמשך האכלוס והבשלת הסביבה לאורך זמן.",
]
logic_close = "זה לא הופך את ההשקעה לחסרת סיכון. שוכר יכול להתחלף, השוק יכול לנוע, הוצאות יכולות להופיע וריבית יכולה להשפיע. אבל בהשוואה למסלולים יזמיים מורכבים יותר, אהבנו את העובדה שהמודל אינו נשען על אירוע אחד שחייב להצליח כדי שהעסקה תהיה הגיונית."
model = [
 "הבית הוא רק חלק מהסיפור. מבחינתנו, הערך המרכזי נמצא בתשתית שמאפשרת למשקיע להחזיק נכס בארצות הברית בצורה מסודרת: חברה, בנק, מימון, טייטל, ביטוח, ניהול, דיווחים וליווי שוטף.",
 "כל משקיע מחזיק את הנכס באמצעות LLC ייעודית שבבעלותו. החברה שייכת למשקיע, חשבון הבנק שייך לחברה, הנכס נרשם על שם החברה, והמשקיע נשאר בעל השליטה בהחלטות. הכסף אינו נכנס לקופה משותפת, ואין תלות בין משקיעים שונים.",
 "סביב כל עסקה פועלת מעטפת מקצועית: רואה חשבון שמטפל בהקמת החברה הייעודית, קבלת מספר המס הפדרלי (EIN) והיבטי מס ודיווח; בנק אמריקאי; מלווה במידת הצורך; חברת טייטל; חברת ביטוח; אינספקשן; חברת ניהול מקומית; וצוות מקומי שמכיר את השטח. גם נושאים ייחודיים למשקיעים זרים, לרבות מבנה החזקה, דיווחים והיבטי מס, נבחנים מול אנשי המקצוע המתאימים. התפקיד שלנו הוא לחבר את כל הגורמים האלה לתהליך אחד ברור, ללוות את המשקיע בהחלטות ולוודא שהדברים לא נופלים בין הכיסאות.",
 "בחרנו גם במבנה אינטרסים פשוט: אנחנו לא רואים את עצמנו כגורם שמסתפק באיתור נכס ובסגירת עסקה. המודל שלנו בנוי כך שהתגמול מגיע מהמשקיע בלבד, ולא מעמלות או תמריצים מגורמים המעורבים בעסקה. המטרה היא שנשב בצד של המשקיע, נבחן את העסקה בעיניים שלנו, ונוכל לומר בכנות אם משהו נראה לנו נכון או לא נכון.",
]
role = [
 "הערך שלנו בתהליך מגיע מהניסיון המצטבר בניהול תהליכים מורכבים בשטח. עסקאות נדל״ן לא נופלות בדרך כלל בגלל סעיף אחד, אלא בגלל חיבור לא נכון בין פרטים: מימון, תזרים, בדיקות, ביטוח, לוחות זמנים, שוכר, ניהול, מסמכים ותקשורת בין גורמים.",
 "שם אנחנו מרגישים בבית. לאורך השנים נדרשנו שוב ושוב להדביק יחד חלקים רבים לכדי תהליך אחד שעובד, לפתור בעיות תוך כדי תנועה, לנהל משברים, ולשמור על התמונה הרחבה בלי לפספס את הפרטים הקטנים. זו גם הסיבה שאנחנו בוחנים דברים על עצמנו לפני שאנחנו מציעים אותם לאחרים.",
 "אנחנו פועלים בעיקר מפה לאוזן ולא דרך שיווק חיצוני רחב. לכן האמון הוא הנכס המרכזי שלנו. המטרה היא לטפל בכל תהליך כאילו הוא שלנו: לשאול שאלות קשות, לא להתאהב בעסקה, ולא להתקדם אם התמונה הכוללת לא מספיק ברורה.",
]
clarify = "המודל מבוסס על בעלות עצמאית, שליטה ותהליך מסודר סביב נכס ספציפי. הוא לא נועד להיות קרן, קבוצת רכישה או מוצר פיננסי משותף. לכן חשוב להבחין בין מה שאנחנו עושים לבין מבנים אחרים שקיימים בשוק."
steps_intro = "התהליך בנוי בשלבים פשוטים יחסית, אך כל שלב חשוב בפני עצמו:"
steps = [
 "שיחת התאמה והגדרת מסגרת: הון זמין, העדפת מימון, טווח השקעה ורמת סיכון מתאימה.",
 "הקמת החברה הייעודית וקבלת מספר EIN באמצעות רואה חשבון שמכיר פעילות משקיעים זרים בארצות הברית.",
 "פתיחת חשבון בנק אמריקאי בבעלות החברה של המשקיע.",
 "העברת הון ראשוני לחשבון החברה, כדי שניתן יהיה לפעול במהירות כאשר נכס מתאים עולה.",
 "איתור נכס מתוך מלאי מצומצם שעבר סינון מוקדם לפי מיקום, מחיר, שכירות צפויה, מצב השכונה ותנאי עסקה.",
 "הגשת Application, חתימה על הסכם רכישה, בדיקות טייטל, אינספקשן, ביטוח והשלמת מימון במידת הצורך.",
 "סגירה, רישום הנכס על שם ה-LLC, העברה לחברת ניהול, פרסום, סינון שוכרים, גבייה ותחזוקה שוטפת.",
]
steps_close = "בארצות הברית, ובמיוחד בעבודה מול קבלנים גדולים, מוכנות מוקדמת משנה את איכות התהליך. משקיע שמגיע עם חברה, חשבון בנק והון זמין נתפס כרוכש רציני יותר. לכן אנחנו מעדיפים לבנות את התשתית לפני בחירת הנכס, ולא לחפש נכס ואז לגלות שהמשקיע עדיין לא מוכן טכנית להתקדם."
view = [
 "מבחינתנו, ההשקעה הזו אינה מוצר מדף. כל נכס נבחן בפני עצמו: מחיר רכישה, שכירות צפויה, ארנונה, HOA, ביטוח, עלויות סגירה, מימון, רזרבות, שכונה, ניהול ותרחישים שמרניים יותר. רק לאחר מכן יש טעם לדבר על תשואה או על פוטנציאל השבחה.",
 "אנחנו לא מנסים לשכנע שכל בית בטקסס הוא השקעה טובה. להפך. חלק מהעבודה שלנו הוא לסנן, לשלול, לשאול שאלות, ולפעמים גם לא להתקדם. מה שמעניין אותנו הוא התמונה המלאה: נכס חדש, שכונה מתפתחת, ביקוש לשכירות, תנאי מימון אפשריים, ניהול מקומי, שליטה משפטית ופיננסית של המשקיע, ואפשרות להחזיק את הנכס לאורך זמן.",
 "החזקה כזו יכולה להתפתח לכיוונים שונים: החזקת נכס אחד לשנים, מיחזור מימון בעתיד, רכישת נכסים נוספים, או מכירה כאשר התנאים מתאימים. אין לנו דרך לדעת איך ייראה השוק בעוד חמש או עשר שנים, ולכן אנחנו מעדיפים מודל שלא כופה החלטה אחת מראש, אלא משאיר למשקיע כמה שיותר אפשרויות פעולה.",
]
consider = [
 "כמו בכל השקעת נדל״ן, גם כאן יש משתנים שצריך לקחת בחשבון: תקופות ללא שוכר, תחזוקה, שינויי ריבית ומס, שינויי שוק, התנהלות מול קבלן או חברת ניהול, והוצאות שלא ניתן לצפות מראש. בית חדש ואחריות קבלן אינם מבטלים את הסיכונים, אבל הם מאפשרים להיכנס לתהליך מנקודת פתיחה מסודרת וברורה יותר.",
 "לכן חשוב לנו שההחלטה תתקבל אחרי הבנת התמונה המלאה. המודל מתאים בעיקר למשקיע שמעריך בעלות ושליטה, מוכן להחזיק נכס לאורך זמן, ורוצה תהליך מלווה שבו מישהו מנוסה בודק עבורו בעיניים שלו ומחבר את כל הגורמים המקצועיים למערכת אחת שעובדת.",
 "ההשקעה היא בנכס - לא בנו. המשקיע מחזיק את החברה, את חשבון הבנק ואת הבית, בכפוף כמובן להסכמי הרכישה, המימון והדין הרלוונטי. התפקיד שלנו הוא לבנות את התשתית, ללוות את התהליך, להאיר סיכונים, ולרכז עבור המשקיע תמונה מסודרת ככל האפשר לקבלת החלטה מושכלת.",
]
nextsteps = [
 "מי שמרגיש שהמודל מתאים לו, עובר לשלב מעשי יותר: הגדרת מסגרת השקעה, בחינת מספרים ראשונית, החלטה אם להתקדם להקמת התשתית, ולאחר מכן הקמת LLC, פתיחת חשבון, בחירת נכס וסגירה.",
 "בשלב הבא נרכז עבור המשקיע רשימת פעולות קצרה וברורה: מסמכי זיהוי, כתובת מגורים באנגלית, פתיחת חברה וחשבון, העברת הון ראשוני, ולאחר מכן בחינת נכס ספציפי עם פרופורמה, תנאי עסקה ולוחות זמנים. מטרת המסמך הנוכחי היא לא להחליף את השלב הזה, אלא לאפשר להבין את ההיגיון שלפניו.",
]
disclaimer = "המידע במסמך זה נועד לצורכי הסברה כללית בלבד ואינו מהווה הצעה לרכישת נכס, ייעוץ השקעות, ייעוץ פיננסי, ייעוץ משפטי, ייעוץ מס או התחייבות לתוצאה כלשהי. נתונים, דוגמאות, טווחים ותחזיות שיוצגו בעל פה או בכתב הם אינדיקציות בלבד ועשויים להשתנות בהתאם לשוק ולגורמים שאינם בשליטתנו. כל משקיע נדרש לבצע בדיקות עצמאיות ולהיעזר ביועצים מקצועיים מתאימים לפני קבלת החלטה. המסמך מיועד לנמענים רלוונטיים בלבד ואינו מיועד להפצה פומבית או שימוש מסחרי ללא אישור מראש ובכתב."

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
