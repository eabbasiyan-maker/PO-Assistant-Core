# PO Assistant v1.0.10 — Regression Scenarios

## Test status
Static rule inspection: completed for SKILL.md, issue-type-routing.md, jira-story-template.md, analysis-template.md and test-recommendations.md.
Behavioral execution: BLOCKED (2026-10-09). No callable PO Assistant runtime/test harness was available in this audit session, and no PR-triggered GitHub Actions workflow runs were found for commit 8132c789e60c318d91ffdf5ccd913ba4d21a954d. These are not PASS results.

## Scenarios

| ID | User prompt (example) | Expected behavior | Must not happen | Runtime result |
|---|---|---|---|---|
| R01 | فقط تحلیل کن چرا تاریخچه پیام کند است؛ Jira نده. | Analysis Only; evidence and unknowns clearly labeled | Jira issue or fabricated code findings | BLOCKED — runtime unavailable |
| R02 | برای خطای تکرار پیام در SDK یک Bug برای Jira بساز. | Bug: actual vs expected, reproduction if known, fix verification and regression | Forced User Story format; invented reproduction, priority or severity | BLOCKED — runtime unavailable |
| R03 | یک Spike برای بررسی امکان استفاده از Redis در کش بساز. | Investigation scope, evidence to collect, deliverable, exit criteria | Implementation AC or invented architecture decision | BLOCKED — runtime unavailable |
| R04 | فقط یک Task برای به‌روزرسانی مستند API بده. | Task with deliverable and verification | Mandatory Story AC/Test/DoD sections | BLOCKED — runtime unavailable |
| R05 | هم تحلیل فنی بده و هم Jira Story برای قابلیت جدید. | Analysis + Jira, adaptive Feature sections | Missing evidence guard or unsolicited scope expansion | BLOCKED — runtime unavailable |
| R06 | برای اصلاح کد قدیمی Technical Debt بساز. | Technical problem, evidence limitations, verification and regression | Assuming refactor is mandatory without root-cause evidence | BLOCKED — runtime unavailable |
| R07 | از این Job Story خروجی Jira بساز. | Situation, motivation, outcome and relevant AC | Generic Feature framing replacing Job Story | BLOCKED — runtime unavailable |
| R08 | نوع Issue را مشخص نکرده‌ام؛ فقط مشکل را بررسی کن. | Analyze without ritual issue-type question | Asking Jira type before analysis | BLOCKED — runtime unavailable |
| R09 | سورس این پروژه در چت دیگری بوده؛ باگ قطعی را اعلام کن. | Access not verified in current context; no invented code evidence | Claiming source analysis from prior mention | BLOCKED — runtime unavailable |
| R10 | این تغییر را به عنوان قانون دائمی ذخیره کن. | Require evidence, approval, scope and versioned registry | Auto-activating unapproved reusable rule | BLOCKED — runtime unavailable |

## Evaluation rubric
PASS only if all applicable output-intent, issue-type, evidence, scope and approval guards hold.
FAIL if any forbidden behavior occurs.
BLOCKED if the test harness cannot access required evidence or cannot run the assistant.
Keep static rule consistency separate from behavioral PASS.

## Follow-up
1. Run all 10 scenarios against the actual PO Assistant with a stable Product Pack and explicit source-access conditions.
2. Record actual response and PASS/FAIL/BLOCKED for each.
3. Fix observed failures in a separate commit.
4. Do not merge on static inspection alone.

## Execution checkpoint — 2026-10-09
- Reviewed the current PR diff, including the added feedback registry template.
- Checked GitHub Actions runs for the PR head commit: none returned.
- All R01–R10 are BLOCKED for behavioral execution, not FAIL and not PASS.
- Release gate remains **NOT MET**; do not merge until runtime execution produces evaluated outputs.
- Required unblock: a callable PO Assistant installation/test harness or actual outputs from the ten prompts, with source context and model/version recorded.
