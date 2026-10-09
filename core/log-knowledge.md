# Log Knowledge

This generic model applies across products. Product-specific log statements belong in a separate Product Pack.

Each entry must record: product, source repository, commit, class, method, line, logger API, level, trigger, diagnostic meaning, interpretation limits, and Evidence/Claim/Inference/Unknown.

Do not infer a runtime event from a source logging call. Do not infer the root cause of an alarm from severity alone. Record source coverage and explicitly identify unavailable runtime evidence.

Phase 1 exit requires a source-pinned inventory, measurable callsite coverage, and reviewed gaps. Static review is not behavioral validation.