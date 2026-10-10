# Generic Log Security & Observability Review Contract v1.0
Status: STATIC DESIGN; not runtime-verified.

## Input and evidence
Use immutable source SHA, exact callsite, runtime config only if observed, and sanitized test samples. Distinguish verified emission code from actual production exposure. Never copy secrets, raw tokens, credentials, message payloads or private data into audit artifacts.

## Checks
Confidentiality: raw tokens, credentials, settings, PII, request/response payload, exceptions, identifiers and masking.
Integrity: log injection, untrusted newlines, spoofed correlation fields, tampering and unauthorized log modification.
Availability/cost: noisy duplicate events, excessive volume, expensive serialization, retention and cardinality.
Diagnosability: precise stage vs outcome, exception types, retry/timeout, correlation/trace, partial success, source/runtime config parity.

## Finding schema
id | product | source commit | path:line | evidence | risk | severity | confidence | actual exposure (UNKNOWN until observed) | recommended change | negative test | owner | status.

## Gate
Propose fixes without silently editing product code. Report security findings as CONFIRMED SOURCE BEHAVIOR / RISK / OPEN INVESTIGATION; do not claim production incidents from static evidence. Separate log severity from security priority and source confidence. Re-run synthetic tests and verify effective runtime logger routes before declaring remediation.
