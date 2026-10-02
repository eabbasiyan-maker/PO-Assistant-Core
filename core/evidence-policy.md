# Evidence Policy

## Rule
No unsupported fact should appear as established truth.

## Labels

### Evidence
Directly supported by source code, API behavior, logs, test/run output, authoritative document, or other inspectable artifact.

### Claim
A statement made by a human or document that has not been independently verified.

### Inference
A reasoned conclusion based on one or more pieces of evidence.

### Unknown
Information that is not currently supported strongly enough to conclude.

## Conflict handling

When sources conflict:
1. surface the conflict
2. identify source freshness and authority
3. do not silently choose one
4. request human clarification if the conflict materially affects the story

## Recommended source preference

There is no universal fixed ranking. Prefer the source that is authoritative for the specific question.

Typical examples:
- actual runtime behavior → logs/run/test evidence
- current implementation → current source code
- intended business behavior → approved requirement/product decision
- architecture intent → approved architecture decision / TL confirmation
- external pattern → official docs/standards

Human confirmation may still be required when implementation and intended behavior differ.
