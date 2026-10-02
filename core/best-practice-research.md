# Best-Practice Research

## Purpose
External research informs product decisions; it does not replace product evidence or human decision ownership.

## Trigger
Use external research when:
- an external fact, provider behavior, standard, or industry pattern materially affects the decision;
- internal evidence leaves a meaningful design question where external comparison adds value;
- the PO explicitly requests research.

Typical areas include API design, security, architecture, reliability, performance, concurrency, observability, AI systems, protocols, and UX patterns.

## External Research Gate
Before automatic external research, answer:
1. Have relevant internal product sources been searched?
2. Is there a specific unresolved question that external evidence can materially inform?
3. Is external research needed now for the next decision?

If any answer is no, defer automatic web research.

Exceptions:
- the PO explicitly asks for external/web/best-practice research; or
- an external fact is itself necessary to understand the requirement.

Default order:
Internal Evidence → Unresolved Question → External Research → Applicability Check.

Do not browse merely because the topic has known industry best practices. Do not use web research as a substitute for product knowledge.

## Source order
Prefer:
1. official documentation and standards
2. reference product documentation
3. engineering publications
4. credible practitioner/community experience

## Output
For every useful external finding:
- pattern/practice
- source/link
- applicability to current product
- limitation or mismatch

External practice is **External Reference**, not product Evidence. It may inform options, but it must not decide an unresolved PO/TL/Architect choice.
