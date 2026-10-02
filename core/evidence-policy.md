# Evidence Policy

## Rule
No unsupported fact should appear as established truth.

Finding a source is not the same as proving that it is authoritative, current, or applicable to the active product/version/environment.

## Labels

### Evidence
Directly supported by an inspectable artifact whose relevance and authority are sufficient for the claim being made.

### Claim
A statement made by a human or document that has not been independently verified.

### Inference
A reasoned conclusion based on one or more pieces of evidence.

### Unknown
Information that is not currently supported strongly enough to conclude.

## Source Validation Gate

Before treating source code, documentation, or another artifact as authoritative evidence for a material decision, assess when relevant:

- **Authority** — is this repository/document/artifact an approved or canonical reference for this question?
- **Freshness** — is the branch/tag/commit/document version current enough for the target release/environment?
- **Applicability** — does it belong to the active product, version, environment, and use case?

For code, capture where possible:
- repository
- branch/tag
- commit
- module/path
- target environment/release

If authority cannot be confirmed, label the finding clearly, for example:

**Source found — authority not confirmed**

Do not describe absence from an unvalidated snapshot as proof that a capability does not exist. Prefer precise language such as:

> "Not observed in the searched source snapshot."

If source authority materially affects the decision, ask the PO/TL/Architect to confirm the canonical source before finalizing the design.

## Knowledge Discovery

Knowledge may exist outside Git. Search the **relevant available sources**, not every connected source blindly.

Depending on the environment and task, relevant sources may include:
- Product Pack / approved product knowledge
- Project files and project knowledge
- source repositories
- architecture/design documents and ADRs
- API specifications
- Jira/requirements/approved decisions
- logs, runs, test evidence, and runtime observations
- connected document stores when relevant and available
- explicit human statements

Rules:
- `Not found in Git` does not mean `does not exist`.
- `Not found in available sources` does not mean `does not exist`.
- Report what source categories were actually searched when absence is material.
- Do not search unrelated connectors merely because they are available.

## Conflict handling

When sources conflict:
1. surface the conflict explicitly as **Evidence Conflict**
2. identify each source and what it supports
3. assess authority, freshness, and applicability
4. do not silently choose one
5. request human clarification if the conflict materially affects the story or recommendation

Example:

**Evidence Conflict**
- Source A: current code snapshot shows ...
- Source B: approved architecture document defines ...
- Impact: ...
- Required confirmation: ...

## Recommended source preference

There is no universal fixed ranking. Prefer the source that is authoritative for the specific question.

Typical examples:
- actual runtime behavior → logs/run/test evidence
- current implementation → validated current source code
- intended business behavior → approved requirement/product decision
- architecture intent → approved architecture decision / TL confirmation
- external pattern → official docs/standards

Human confirmation may still be required when implementation and intended behavior differ.
