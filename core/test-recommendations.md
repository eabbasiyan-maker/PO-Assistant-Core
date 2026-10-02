# Test Recommendation Rules

Test Recommendations are mandatory in the final story.

They are not a duplicate of Acceptance Criteria.

## Purpose
Acceptance Criteria defines what must be true for the story to be accepted.
Test Recommendations identify valuable ways to prove correctness and discover regressions/failures.

## Candidate categories
Use only relevant ones:
- Functional / Happy Path
- Negative / Error handling
- Boundary / Edge Cases
- Regression
- Integration
- Compatibility
- Security
- Performance / Load
- Concurrency
- Data / DB consistency
- Retry / idempotency where relevant
- Observability / logging

## Quality rules
- make scenarios concrete
- connect high-risk tests to identified risks
- avoid generic "test performance/security" lines without context
- include regression targets when code-path analysis identifies impacted behavior
