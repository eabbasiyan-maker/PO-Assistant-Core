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

### 8. Final Jira issue
بعد از کافی بودن Evidence و تصمیم‌ها برای نوع Issue انتخاب‌شده، خروجی مطابق `core/issue-type-routing.md` تولید می‌شود. این مثال یک User Story / Feature است؛ بنابراین Scope، AC، Test Recommendations، validated Code References، Impact، Risk و DoD فقط در صورت مرتبط‌بودن استفاده می‌شوند. برای Bug، Spike، Task و سایر انواع، بخش‌های مناسب همان نوع انتخاب می‌شوند. Proposed Enhancements تأییدنشده وارد Issue نمی‌شوند.
