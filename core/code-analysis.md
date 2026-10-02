# Code Analysis Rules

## Goal
Understand actual current behavior and implementation impact, not just locate a keyword.

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
- file
- class
- method
- relevant condition/query/config

## New feature with no code yet
Do not say "no code, so no analysis."
Instead:
1. inspect current architecture
2. locate the most relevant extension point
3. identify current constraints
4. explain required change
5. identify compatibility/regression risk
6. compare alternatives when needed

## Change justification
Changing existing architecture/code is allowed if justified.
Explain:
- why current structure is insufficient
- benefit
- implementation/operational cost
- risks
- migration/backward compatibility concerns
