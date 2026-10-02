# Best-Practice Research

## Purpose
External research informs product decisions; it does not replace product evidence or human decision ownership.

## Trigger
Use external research when:
- an external fact, provider behavior, standard, or industry pattern materially affects the decision;
- internal evidence leaves a meaningful design question where external comparison adds value;
- the PO explicitly requests research.

Typical areas include API design, security, architecture, reliability, performance, concurrency, observability, AI systems, protocols, and UX patterns.

## Ordering
Normally:
1. discover relevant internal product evidence;
2. identify the unresolved question;
3. research the external reference that can inform that question.

Research earlier only when the external fact itself is necessary to understand the requirement.

Do not use web research as a substitute for searching available product knowledge.

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
