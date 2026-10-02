# Best-Practice Research

## Purpose
External research informs product decisions; it does not replace product evidence or human decision ownership.

## Trigger
Use external research when:
- an external fact, provider behavior, standard, or industry pattern materially affects the decision;
- internal evidence leaves a meaningful design question where external comparison adds value;
- the PO explicitly requests research.

Typical areas include API design, security, architecture, reliability, performance, concurrency, observability, AI systems, protocols, and UX patterns.

## Internal Evidence Completion Gate
Automatic external research is blocked until relevant internal discovery is sufficiently attempted for the current question.

A repository lookup or keyword search alone is not enough when other relevant internal sources are available. Depending on the question, inspect relevant Product Pack/project knowledge, architecture/API docs, validated code paths, approved decisions, logs/runs/tests, or internal document stores.

Do not search every connector blindly. Search only source categories that could materially answer the current question.

If internal sources are unavailable or authority cannot be established, record that limitation. This does not automatically justify external research unless the External Research Gate below is also satisfied.

## External Research Gate
After the Internal Evidence Completion Gate, before automatic external research, answer:
1. Have relevant internal product sources been searched?
2. Is there a specific unresolved question that external evidence can materially inform?
3. Is external research needed now for the next decision?

If any answer is no, defer automatic web research. Do not browse simply to make the analysis look complete.

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
