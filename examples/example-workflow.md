# Example Workflow

## Raw request
«برای API یک محدودیت جدید اضافه کنیم تا درخواست تکراری دوباره پردازش نشود.»

## Assistant behavior

### 1. توضیح ساده
نیاز این است که اگر یک درخواست به دلیل retry دوباره ارسال شد، سیستم همان عملیات را دوباره انجام ندهد و نتیجه قابل پیش‌بینی داشته باشد.

### 2. Evidence discovery first
قبل از سؤال از PO:
- Product Knowledge و API contract مرتبط بررسی می‌شود.
- Source authority برای repository/branch مرتبط بررسی می‌شود.
- مسیر request تا persistence/integration trace می‌شود.
- مشخص می‌شود آیا request identifier، idempotency mechanism یا retry behavior فعلی وجود دارد.

موارد پیدا نشده فقط به شکل «در منابع بررسی‌شده مشاهده نشد» گزارش می‌شوند.

### 3. Route remaining unknowns
مثال:
- وجود شناسه یکتای فعلی → Evidence-resolvable
- رفتار محصول برای retry موفق → PO Decision اگر قبلاً تصویب نشده
- محل enforcement → Technical Decision اگر از معماری موجود قطعی نشود
- الگوهای استاندارد idempotency → External Reference
- جزئیات غیرضروری برای این مرحله → Non-blocking Unknown

### 4. Clarification
فقط تصمیم‌های حل‌نشده و لازم از مالک درست پرسیده می‌شوند. گزینه‌ها خنثی بیان می‌شوند؛ Assistant رفتار ترجیحی خودش را جای تصمیم PO/TL نمی‌گذارد.

### 5. Best practice
در صورت نیاز، official/reference material برای idempotency بررسی می‌شود. External practice به‌عنوان Product Evidence تلقی نمی‌شود.

### 6. Options
در صورت وجود چند راه معتبر، حداکثر سه گزینه با Cost/Benefit/Risk/Trade-off مقایسه می‌شوند.

### 7. Recommendation
فقط بعد از پاس شدن Recommendation Gate و حل Decision Dependencies:

**Recommendation — requires human approval**

### 8. Requested output
در درخواست خام، ساخت Jira Issue صراحتاً خواسته نشده است؛ بنابراین خروجی پیش‌فرض، تحلیل نیاز و Unknownها و تصمیم‌های لازم است، نه Jira Issue اجباری. اگر PO بعداً Jira بخواهد، ابتدا Output Intent و سپس Issue Type مطابق `core/issue-type-routing.md` تعیین می‌شود. نوع User Story / Feature فقط وقتی انتخاب می‌شود که ماهیت نیاز و قصد PO آن را پشتیبانی کند. Proposed Enhancements تأییدنشده وارد Issue نمی‌شوند.
