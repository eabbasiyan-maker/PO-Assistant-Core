# Generic completion-event interpretation protocol v0.1

Status: DESIGN / STATIC RULES ONLY. Product-specific source evidence belongs in its Product Pack.

## Principle
A log stating that a method finished is not necessarily proof that all sub-operations succeeded. Determine whether recoverable errors, fallback values, skipped steps, or partial results can precede the completion event.

## Discovery workflow
1. Pin repository commit, source path, containing method, completion logger callsite, and all preceding error-handling paths.
2. Build a branch matrix for each recoverable error: event emitted, propagation, fallback state, continuation, return value, and subsequent completion event.
3. Record what the completion message actually proves (for example, method reached return) and what it does not prove (for example, every item was processed successfully).
4. Record missing outcome dimensions separately: processed count, succeeded count, failed count, partial flag, correlation context. Do not recommend logging sensitive values.
5. Keep severity of the diagnostic ambiguity separate from confidence in the source evidence. Do not assert a runtime incident without runtime evidence.
6. Treat emitted logger callsites as unique source locations; a path that emits two events is not two different execution paths. Do not double-count previously inspected files.
7. Propose before/after tests using injected recoverable errors and captured logger events. Static source analysis is never Behavioral PASS.

## Minimum record
Source commit | file | method | line | completion event | recoverable error path | continued state | observed/expected return | interpretation limit | Evidence | Claim | Inference | Unknown | Severity | Confidence | Static status | Behavioral status.

## Candidate regression scenarios (not executed)
- CS-01: all sub-operations succeed; completion event should be interpreted as completion only.
- CS-02: a recoverable sub-operation fails but processing continues; record whether both warning and completion events occur.
- CS-03: a fallback/default result is returned after an error; completion event must not be treated as proof of a valid result.
- CS-04: an exception propagates before completion; absence of completion does not by itself identify root cause.
- CS-05: a missing runtime event with no confirmed logger routing is UNKNOWN, not evidence of a successful operation.

Exit Gate: branch matrix recorded; completion semantics bounded; proposed tests have expected events/returns; real harness execution separately tracked as PASS/FAIL/BLOCKED/NOT RUN.
