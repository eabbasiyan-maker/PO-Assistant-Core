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
After the Internal Evidence Completion Gate, automatic external research is allowed only if all of the following are explicitly identifiable:

1. **External Question** — the exact unresolved question that requires external evidence.
2. **Decision Impact** — the decision, Unknown, Story section, API/architecture choice, or risk assessment that could materially change based on the answer.
3. Relevant internal product sources have already been searched sufficiently for that question.
4. The external answer is needed now for the next analysis or decision step.

If the **External Question** or **Decision Impact** cannot be stated clearly, do not browse automatically.

Do not use web research for background color, examples, generic best practices, or to make the analysis look complete when it does not resolve a named external question.

Before browsing, the workflow should be able to express:

```
External Question: ...
Decision Impact: ...
```

If either field is empty, defer external research.

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
