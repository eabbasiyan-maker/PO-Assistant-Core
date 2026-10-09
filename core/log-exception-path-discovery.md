# Generic exception-path log discovery protocol v0.1

Status: DESIGN / STATIC RULES ONLY. Applies to any product; keep product-specific findings in its Product Pack.

## Purpose
A list of logger calls alone misses diagnostic blind spots. Inspect *all branches of each catch*, including branches that emit no log and return a default value.

## Required workflow
1. Pin source commit, file, method, line span and the specific exception boundary.
2. Record catch type, ordered predicates (e.g. instanceof, error codes), fallback/else handling, rethrow, return, retry and cleanup paths.
3. Build an exhaustive **branch partition**: for each possible category of caught exception, mark log level, exception attachment, propagation, return value, and caller-visible status. Include an unmatched/default category.
4. Distinguish an emitted callsite from a **missing-event path**; missing-event paths are gap records, never added to the emitted-callsite count.
5. Check whether a default/empty return can be confused with success. Inspect caller validation before asserting user impact.
6. Assign Evidence / Claim / Inference / Unknown separately. Absence of a runtime log is not evidence that the exception did not occur.
7. Add candidate behavioral tests with explicit injected exception classes, expected return/rethrow, and expected captured logging events; mark NOT RUN until a harness actually executes them.
8. Keep a separate risk review for payload/secret/PII before suggesting logging the exception or request data.

## Record fields
- Source commit / file / method / lines
- Catch scope / ordered predicates / unmatched branch
- Event emitted? (yes/no/conditional), level, throwable attached?
- Rethrow / retry / return value / downstream handling
- Severity (operational risk) vs Confidence (evidence strength)
- Evidence / Claim / Inference / Unknown
- Static check status / Behavioral check status / Owner / Next step

## Static review cases (design only; NOT EXECUTED)
- EX-01: catch Exception with two independent instanceof guards and no else; unmatched subtype must be reported as a no-event path.
- EX-02: catch IOException with unconditional logger.warn and rethrow; must NOT report a missing-event path.
- EX-03: catch Exception with logger.error(message) but no throwable; record event present and stack/exception attachment absent, not a silent catch.
- EX-04: catch Exception with a return default; mark possible ambiguous success, but caller impact UNKNOWN until inspected.
- EX-05: duplicate calls to the same logger inside alternative branches count as distinct callsites, but branch occurrences are NOT runtime event counts.

## Exit Gate
- [ ] Catch branches and unmatched paths enumerated for the declared source scope.
- [ ] Missing-event gaps not mixed into callsite denominator.
- [ ] Caller-side outcomes reviewed or marked UNKNOWN.
- [ ] Behavioral scenarios run in a real harness or explicitly BLOCKED / NOT RUN.
- [ ] Scope and coverage recorded without inflating previously inspected-file counts.

Static design: PASS for documented method; no repository-wide or behavioral PASS claimed.
