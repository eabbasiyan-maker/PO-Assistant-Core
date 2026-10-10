# Log Catalog Extraction & Deduplication Contract v1.0
Status: STATIC DESIGN; no behavioral tests run. Generic rules only; no Chat-specific facts.

## Extraction unit
Input: repository + immutable commit + eligible source file inventory. Discover logger APIs, aliases, wrappers, and direct emitters. Classify DTO/entity and logger configuration separately. For each emitter capture source path, enclosing method, line, invocation, logger identity, level, branch trigger, message semantics, limitations, exception/retry/timeout/correlation, Evidence/Claim/Inference/Unknown.

## Identity and counting
Unique invocation key = repository + commit + path + method + line + invocation. A logical group can contain multiple invocations; report both counts explicitly. A single exception may cause multiple emitted events; never treat event count as incident count. Merge overlapping source samples by unique key. Never sum sample totals without deduplication.

## Coverage contract
Denominator A = all eligible production source files at pinned commit.
Numerator A = distinct files fully scanned for emitter discovery, NOT merely inspected for selected paths.
Denominator B = all distinct logging invocations after complete inventory.
Numerator B = distinct invocations with completed source-pinned semantic records.
If B is not established, report callsite coverage UNKNOWN. Selected-path reviews may report only inspected files and reviewed invocation counts; do not label those numbers repository coverage.

## Interpretation and conflict gates
- Logger configuration != active runtime routing.
- Completion INFO != end-to-end business success.
- Different timers in success/error branches are not directly comparable without scope.
- An earlier UNKNOWN can be superseded only by source revalidation, preserving revision history.
- Missing logs, retries, correlation and timeout behavior remain UNKNOWN unless inspected.
- Static PASS, behavioral NOT RUN, and BLOCKED are independent statuses.

## Proposed regression tests (NOT RUN)
T1 duplicate source sample => one invocation identity.
T2 two logger calls in one exception branch => two invocation identities, one exception path.
T3 log DTO without logger invocation => zero emitter sites.
T4 changed source commit => separate version, not silent overwrite.
T5 selected-path review => no fabricated full coverage percentage.
T6 INFO after partial work => completion-only semantics.
T7 active config unavailable => runtime routing UNKNOWN.

Step 2 exit requires complete emitter enumeration and denominator, semantic records, exception/retry/timeout/correlation coverage, source-linked product pack, and verified tests. All still OPEN beyond the verified incremental slice.
