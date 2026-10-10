# Log Discovery Record Template v0.1

Use this generic template for any product. Store actual callsite data in a product-specific Product Pack, never in Core.

## Source identity
- Product / environment / target release:
- Repository / commit / branch:
- Source access: Verified / Unavailable / Not Checked
- Source authority: Confirmed / Unconfirmed / Conflicting
- Framework / adapter / wrapper:
- Runtime configuration authority:

## Callsite record
- Log ID:
- File / class / method / line:
- Logger API / level / message pattern (redacted where needed):
- Trigger condition and surrounding code path:
- Exception / retry / timeout / correlation context:
- Intended diagnostic meaning:
- Interpretation limits (what this log does NOT prove):
- Evidence / Claim / Inference / Unknown:
- Supporting source references:

## Coverage
- Production files total / inspected:
- Callsite denominator / catalogued:
- Wrappers and dynamic logging patterns inspected:
- Not checked / inaccessible categories:
- Known gaps with severity and owner:

## Exit Gate
- [ ] Source identity and authority assessed
- [ ] Relevant callsites and wrappers inventoried with measurable coverage
- [ ] Trigger and interpretation limits validated against source
- [ ] Exception/retry/timeout/correlation reviewed
- [ ] Unknowns and conflicts documented
- [ ] Static evidence distinguished from runtime/behavioral tests

Result: PASS / FAIL / BLOCKED / OPEN. Never claim repository-wide coverage from a sample.

## Counting protocol (generic)
- Pin the source commit and list the exact production file denominator, inclusion rules, and inspected file paths.
- Separate **file coverage** (inspected/eligible files) from **callsite coverage** (catalogued/total active emitters). Do not derive the second from a partial sample.
- Enumerate active logger invocations with a comment-aware parser; exclude commented examples, declarations without invocation, DTOs, and appender configuration. Record direct calls, aliases, wrappers, and dynamically dispatched emitters separately.
- For each callsite, record its exact source line, containing method, condition/exception path, meaning, and what cannot be concluded from its appearance.
- Reconcile overlapping samples by unique `repository + commit + path + method + line + invocation` keys before summing; track additions, deletions, and moved lines across versions.
- Distinguish source-verified emission paths from observed runtime events. A logger call in source is not a behavioral test, and a configured timeout or threshold warning is not proof that a timeout happened.
- If code search returns zero results, check search authority/index coverage before treating it as an empty inventory. A complete file-tree listing alone does not establish full callsite coverage.
- Record status per check as PASS / FAIL / BLOCKED / OPEN, with explicit evidence and the next targeted search.
