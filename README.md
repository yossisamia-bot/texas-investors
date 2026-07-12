# texas-investors

עמוד נחיתה נייד (mobile-first, RTL) של מצגת המשקיעים "בתים חדשים מקבלנים ציבוריים בטקסס".
מותג: Aspect Boutique Investments × PrimeVest Realty.

- `index.html` - קובץ עצמאי אחד (כל התמונות והלוגואים מוטמעים ב-base64, ~880KB).
- חי: **https://texas.primevest-realty.com/** (דומיין מותג; קובץ `CNAME` ברפו, תת-דומיין על דומיין החברה ב-Wix). `yossisamia-bot.github.io/texas-investors/` מפנה אליו ב-301.
- `noindex, nofollow` - לא נסרק ע"י גוגל; שיתוף בלינק ישיר בלבד (תואם לדיסקליימר "לא להפצה פומבית").

## עדכון תוכן - מקור-אמת יחיד: `presentation.docx`
`presentation.docx` (בשורש הריפו) הוא **המסמך העוגן**: ממנו נבנה האתר. מסמך אחד -> האתר תמיד בעקבותיו.

1. עורכים את `presentation.docx` (Word). הגוף מיושר לימין רגיל (לא justify).
2. מריצים `python _src\build.py` -> קורא את המסמך ובונה `index.html` (קובץ עצמאי, base64 מוטמע).
3. commit + push (`presentation.docx` + `index.html`) -> GitHub Pages מעדכן. **הלינק לא משתנה.**

להפקת קובץ DOCX/PDF לשליחה ידנית (לא באתר): המאסטר עצמו = ה-DOCX; ל-PDF ממירים את המאסטר דרך Word (SaveAs PDF).

מבנה מחייב במסמך (אחרת ה-build נכשל בכוונה ומדווח מה חסר - לא דריסה שקטה):
- **כותרת-מקטע** = פסקה מודגשת (bold) קצרה (< 60 תווים).
- **פריט-רשימה** = שורה שמתחילה ב-"•".
- שאר הפסקאות = טקסט גוף. 2 הפסקאות הראשונות (כותרת ראשית + משנה) מקודדות ב-HERO שב-`build.py`.
- 11 כותרות-המקטע מאומתות ב-build; שינוי שם כותרת -> שגיאה ברורה.

תמונות העמוד מנוהלות בנפרד ב-`_src\assets\` (יציבות; לא נקראות מהמסמך).

## גרסה מקוצרת - `presentation-short.docx` -> `short/index.html`
מ-12/07/2026 יש גם גרסה מקוצרת (בהשראת המבנה של yw-abi: עיקרי המודל בכמה דקות קריאה + כפתור לגרסה המלאה):
- חיה: **https://texas.primevest-realty.com/short/**
- מקור-אמת: `presentation-short.docx` בשורש הריפו (אותם כללי מבנה; 7 כותרות-מקטע מאומתות ב-build).
- `python _src\build.py` בונה את **שני** העמודים בפקודה אחת. אם `presentation-short.docx` חסר - העמוד המלא נבנה והמקוצר מדולג.
- **המאסטר המלא `presentation.docx` נשאר המקור השלם - המקוצר נגזר ממנו ולא מחליף אותו.** כל שינוי תוכן מהותי עושים קודם במלא, ואז משקפים למקוצר לפי הצורך.
- GA4: העמוד המקוצר מדווח `page_title: Texas Investors Short` (נפרד מהמלא); קליק על "למסמך המלא" = אירוע `tool_click {tool:'full_version'}`.

CTA תחתון: מחשבון -> prop-compare, מפה -> houston-map. כפתור וואטסאפ הוסר ביוזמת יוסי (שולח הכל בעצמו).
