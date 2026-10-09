# Test Recommendation Rules

Test Recommendations are distinct from Acceptance Criteria and verification/exit criteria.

## Applicability
Apply `core/issue-type-routing.md` before Jira output.
- User Story / Feature: include relevant Test Recommendations.
- Bug: include fix verification and regression recommendations where relevant.
- Technical Debt: include relevant regression, compatibility and technical verification recommendations.
- Job Story: include tests when relevant to the desired outcome.
- Task: use Verification / Done Criteria; add separate tests only if materially useful.
- Spike / Investigation: use evidence-backed deliverables and Exit Criteria; do not fabricate implementation tests.

Never require a generic Test Recommendations heading for every issue. Never omit material verification or regression risks merely to keep output short.

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
- Retry / idempotency
- Observability / logging

## Quality rules
- Make scenarios concrete and observable.
- Link high-risk tests to identified risks.
- Avoid generic test suggestions.
- Include regression targets when validated code-path analysis identifies impacted behavior.
- Do not present unknown behavior as a confirmed expected result.
