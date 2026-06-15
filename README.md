# texas-investors

עמוד נחיתה נייד (mobile-first, RTL) של מצגת המשקיעים "בתים חדשים מקבלנים ציבוריים בטקסס".
מותג: Aspect Boutique Investments × PrimeVest Realty.

- `index.html` - קובץ עצמאי אחד (כל התמונות והלוגואים מוטמעים ב-base64, ~880KB).
- חי ב-GitHub Pages: https://yossisamia-bot.github.io/texas-investors/
- `noindex, nofollow` - לא נסרק ע"י גוגל; שיתוף בלינק ישיר בלבד (תואם לדיסקליימר "לא להפצה פומבית").

## עדכון תוכן
מקור הבנייה נמצא בריפו עצמו: `_src\build.py` + `_src\assets\` (לוגואים + תמונות).
מריצים: `python _src\build.py` -> כותב `index.html` כאן (קובץ עצמאי, base64 מוטמע) -> commit + push.
**הלינק לא משתנה** בעדכון תוכן.

CTA תחתון: מחשבון -> prop-compare, מפה -> houston-map. כפתור וואטסאפ הוסר ביוזמת יוסי (שולח הכל בעצמו).
