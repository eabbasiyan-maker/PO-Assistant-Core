# Log Intelligence — Canonical Knowledge Governance v1.0
Status: STATIC DESIGN / reconciliation control; not a behavioral pass.
This is the single generic index for conflict resolution. Product-specific findings and source locations belong in the Chat Product Pack.

## One record per source fact
Canonical key: product + repository + commit + path + method + callsite line + invocation.
Maintain stable display ID and revision history; when source commit changes, create a versioned successor rather than silently changing evidence.
Fields: logger API, trigger, event meaning, non-claims, exception/retry/timeout/correlation, Evidence, Claim, Inference, Unknown, Severity, Confidence, runtime status, test status.

## Conflict protocol
1. Read current branch heads, active PRs, existing catalogs and all relevant prior artifacts before writing.
2. Normalize statements by canonical key and assertion scope (source / config / runtime / hypothesis).
3. Mark exact duplicates DEDUPED; compatible assertions MERGED; disagreements OPEN-CONFLICT until source checked.
4. A newer source-pinned fact may SUPERSEDE an older UNKNOWN, but only after direct source validation. Never convert a reported observation into verified evidence without rereading source.
5. Record provenance and resolution reason. Preserve old statement as superseded; do not erase history.
6. Source config and runtime config are distinct. A logged completion is not end-to-end success. File coverage is not callsite coverage.
7. Keep product-specific references in Chat repository; generic policies and templates here.

## Gate / regression checks
- G01 same callsite in two samples => one canonical record (DESIGNED, NOT RUN).
- G02 old UNKNOWN vs later source-pinned emitter => verify source, then supersede (DESIGNED, NOT RUN).
- G03 source-defined JSON appender vs runtime route => runtime UNKNOWN until measured (DESIGNED, NOT RUN).
- G04 overlapping file samples => no summed coverage without dedup (DESIGNED, NOT RUN).
- G05 severity != confidence; no promotion of STATIC PASS to BEHAVIORAL PASS (DESIGNED, NOT RUN).
- G06 separate product pack and core; no modifications to fix/v1.0.10-issue-consistency or PR #2 (STATIC POLICY).

Step 1 completion requires exhaustive inventory of prior relevant artifacts, resolved/open conflict ledger, and both product and generic canonical indexes; any unreviewed evidence remains OPEN. Phase 1 exit remains OPEN.
