# Generic log-to-consumer trace protocol v0.1

Status: DESIGN / STATIC RULES ONLY. Product-specific examples belong in a separate Product Pack.

## Why trace consumers
A source logger event may describe only one stage of an operation. Interpret a message by following return values, caught exceptions and subsequent consumers, rather than treating a log as a successful end-to-end result.

## Required evidence
- Pin repository, commit, file, method and line for producer and each consumer.
- Trace normal, recoverable, rethrown, silent, empty-result and callback-failure paths.
- Record whether an event is emitted on each path, and what value/state reaches the next component.
- Separate event presence from success, absence from failure, and empty output from valid emptiness.
- Classify Evidence, Verified Claim, Inference and Unknown independently.
- Track Severity (impact) separately from Confidence (strength of evidence).
- Track inspected source files separately from unique logger callsites; do not sum overlapping samples.
- Do not capture credentials, payloads, personal data or configuration values in examples or test logs.

## Consumer trace record
Source commit | producer file/method/lines | exception class | path category | logged level | rethrow? | fallback/return | consumer file/method/lines | consumer validation | emitted completion event | meaning | limits | Evidence | Claim | Inference | Unknown | Severity | Confidence | static status | behavioral status.

## Suggested negative and positive regressions — NOT RUN
1. Valid producer result reaches consumer and completion event.
2. Recoverable exception returns fallback; completion event is not over-interpreted.
3. Fatal exception propagates; verify no success event is inferred.
4. Unhandled/silently handled category; verify whether evidence is missing.
5. Empty result: distinguish valid empty data from failed retrieval.
6. Consumer catches per-item errors and still completes: verify partial-success semantics.
7. Callback exception: verify logging details, state and event ordering.
8. Version mismatch or absent runtime logs: mark UNKNOWN rather than PASS.

## Exit gate
PASS only for source-pinned branch matrix and consumer mapping with independently reviewed interpretation boundaries. Behavioral PASS requires actual harness execution and observed assertions. Otherwise use NOT RUN or BLOCKED with reason.
