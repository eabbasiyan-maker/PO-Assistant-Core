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
