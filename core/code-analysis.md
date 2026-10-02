# Code Analysis Rules

## Goal
Understand actual current behavior and implementation impact, not just locate a keyword.

## Validate the code source first

Before using a repository/branch as the basis for a material technical conclusion:
1. identify repository and branch/tag/commit when available;
2. check whether it is authoritative/current for the target product and environment;
3. distinguish a validated current source from an observed snapshot;
4. if authority is unknown and matters to the decision, request confirmation.

Do not turn:
> "I did not find X in this snapshot"

into:
> "X does not exist in the product."

Use the Source Validation Gate in `evidence-policy.md`.

## For existing behavior
Trace the execution path far enough to explain:
- entry point
- routing/dispatch
- business logic
- persistence/integration
- response/event
- relevant validation and error handling

## References
Whenever possible include:
- repository/module
- branch/tag/commit
- file
- class
- method
- relevant condition/query/config
- authority status when not confirmed

## New feature with no code yet
Do not say "no code, so no analysis."
Instead:
1. inspect relevant product knowledge and current architecture
2. locate the most relevant extension point
3. identify current constraints
4. explain required change
5. identify compatibility/regression risk
6. compare alternatives when needed

If code and documentation disagree, report an **Evidence Conflict** rather than silently selecting one.

## Change justification
Changing existing architecture/code is allowed if justified.
Explain:
- why current structure is insufficient
- benefit
- implementation/operational cost
- risks
- migration/backward compatibility concerns

Any architectural expansion beyond the original requirement must pass the Scope Expansion Gate and, when applicable, the Decision Dependency Gate.
