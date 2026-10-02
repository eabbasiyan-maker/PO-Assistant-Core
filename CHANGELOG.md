# Changelog

## v1.0.1 — Cold-start Test #1 corrections

### Changed
- Added a Recommendation Gate: the assistant must not prefer or recommend an option before relevant evidence and analysis are sufficient.
- During Clarification, options may be presented but must remain neutral until the Recommendation Gate is satisfied.
- Added a controlled preliminary-opinion exception when the PO explicitly asks for an early opinion; it must be labeled as unvalidated.
- Clarification must not claim that no further PO questions will be needed; later code/document analysis may reveal new material questions.

### Reason
Cold-start Test #1 showed that the assistant correctly identified unknowns and deferred technical design until code analysis, but prematurely preferred one feedback behavior before reviewing product evidence, code/architecture, and relevant trade-offs.

## v1.0.0 — Initial baseline

### Added
- Reusable PO Assistant Core workflow
- Evidence / Claim / Inference / Unknown model
- Product context isolation
- Multi-product PO support
- Batched clarification rules
- TL escalation workflow
- Deep code-path investigation rules
- Best-practice research rules
- Up to three solution alternatives
- Cost / Benefit / Risk / Trade-off comparison
- **Recommendation — requires human approval**
- Mandatory Scope
- Mandatory Not in Scope
- Mandatory Acceptance Criteria
- Mandatory Test Recommendations
- Two-layer Definition of Done
- Analysis template
- Jira story template
- Product Pack template
- PO Preferences template
- Feedback and root-cause learning workflow
