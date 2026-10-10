# Structured diagnostic event semantics — generic protocol v0.1

Status: DESIGN / STATIC METHOD ONLY; no behavioral tests executed. Product-specific source records belong in Product Packs, not Core.

## Discover and classify
1. Pin repository, source commit, configuration candidate, runtime build identity and environment separately.
2. Locate logger declarations and aliases, including named loggers, wrapper calls and structured DTO emitters. Distinguish the DTO class from the invocation that emits it.
3. For each actual invocation, record file/class/method/line, logger API, level, triggering branch, exception type, correlation fields and measurement window.
4. Trace the preceding operation and the subsequent operation. An INFO event emitted after a synchronous method returns proves only that local return path; it does not prove asynchronous delivery, persistence or acknowledgement.
5. Enumerate sibling branches: success, explicit error callback, caught typed exception, unexpected exception, early return and denied operation. An error in a branch with no structured event must not be inferred from another branch's event.
6. Distinguish metrics by timer start and stop points. Identically named duration fields with different measurement windows are not directly comparable.
7. Resolve named logger-to-appender routing in candidate configuration, then verify effective runtime configuration and actual output. A source-level producer is not proof of runtime collection.
8. Classify fields that might be personal identifiers; record schema/masking/access/retention as UNKNOWN until verified. Use only synthetic identifiers in tests.

## Required record
`source_commit | file | class | method | line | logger_alias | API | level | trigger | event_payload_type | duration_start | duration_end | correlation_fields | meaning | interpretation_limit | Evidence | Claim | Inference | Unknown | static_status | behavioral_status`

## Regression matrix (DESIGNED, NOT RUN)
- Structured INFO after a successful local operation: verify emission, but do not assert downstream delivery.
- Typed exception within success callback: verify error event and timer boundaries.
- Error callback: determine whether it emits the same event type; do not infer absence of all logging from one missing callsite.
- Unexpected exception: verify handling path and whether structured event is emitted.
- Different source and effective logging configuration: return CONFIG_UNKNOWN until routing is verified.
- Synthetic identifier: verify event correlation and redaction without production tokens or personal data.
- Version mismatch: invalidate source-pinned conclusions and request a new scan.

## Coverage and Exit Gate
- [ ] Complete eligible source-file tree and inclusion rules recorded.
- [ ] All relevant named logger declarations and direct emitters enumerated with a defensible denominator.
- [ ] Callback/exception branch matrix and timer boundaries source-pinned.
- [ ] Runtime routing and output schema verified where available; otherwise BLOCKED.
- [ ] Regression scenarios executed in a harness; otherwise NOT RUN.
- [ ] Severity, evidence confidence, privacy risk and unknowns reported separately.

STATIC PASS is never BEHAVIORAL PASS. Do not count helper invocations as independent logger emission callsites. Keep product evidence outside Core.
