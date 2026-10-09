# Log Knowledge

This generic model applies across products. Product-specific log statements belong in a separate Product Pack.

Each entry must record: product, source repository, commit, class, method, line, logger API, level, trigger, diagnostic meaning, interpretation limits, and Evidence/Claim/Inference/Unknown.

Do not infer a runtime event from a source logging call. Do not infer the root cause of an alarm from severity alone. Record source coverage and explicitly identify unavailable runtime evidence.

Phase 1 exit requires a source-pinned inventory, measurable callsite coverage, and reviewed gaps. Static review is not behavioral validation.
## Classify artifacts before cataloguing

Distinguish (1) logger configuration/appender, (2) actual logging callsite, (3) wrapper that invokes a logger, (4) structured log/event DTO, and (5) persistence entity. A class named `*Log` is not necessarily a logging wrapper or an emitted event. For each artifact record the inspected file/commit and whether an invocation or serialization path was traced. Do not count DTO definitions or appender declarations as emitting callsites. Treat configuration as potential routing, not proof of runtime emission. Track inspected-file coverage separately from verified callsite coverage and keep the latter UNKNOWN until a defensible denominator exists.
