# Example Workflow

## Raw request
«برای API یک محدودیت جدید اضافه کنیم تا درخواست تکراری دوباره پردازش نشود.»

## Assistant behavior

### 1. توضیح ساده
نیاز این است که اگر یک درخواست به دلیل retry دوباره ارسال شد، سیستم همان عملیات را دوباره انجام ندهد و نتیجه قابل پیش‌بینی داشته باشد.

### 2. Clarification
قبل از Story نهایی باید مشخص شود:
- شناسه یکتای درخواست داریم یا باید اضافه شود؟
- رفتار مورد انتظار برای retry موفق چیست؟
- چه مدت باید درخواست قبلی قابل شناسایی باشد؟

### 3. Code investigation
Assistant مسیر API تا persistence/integration را بررسی می‌کند و محل مناسب برای کنترل تکرار را پیدا می‌کند.

### 4. Best practice
برای مفهوم idempotency، official/reference material بررسی می‌شود و لینک داده می‌شود.

### 5. Options
در صورت وجود چند راه:
- application-level idempotency store
- database uniqueness/transaction control
- upstream/gateway enforcement

هر کدام با Cost/Benefit/Risk مقایسه می‌شود.

### 6. Recommendation
**Recommendation — requires human approval**

### 7. Final story
Story شامل Scope، Not in Scope، AC، Test Recommendations، Code References، Impact، Risk و DoD است.
