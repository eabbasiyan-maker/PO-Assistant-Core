# Changelog

## v1.0.5 — Requirement isolation and research sequencing

### Added
- Requirement Context Isolation: same product does not imply that prior stories, planned features, or proposed designs belong to the current requirement.
- Leakage check for cross-requirement dependencies and constraints.
- External Research Gate with default order: Internal Evidence → Unresolved Question → External Research → Applicability Check.
- Requirement-boundary fields in the Analysis template.

### Changed
- Prior same-product work can affect a new requirement only when authoritative evidence establishes the dependency/constraint or the PO explicitly links it.
- Automatic best-practice research is deferred until it can materially inform a specific unresolved decision.

### Reason
Cold-start testing showed same-product context leakage through unrelated QC/Audit work and external research occurring before internal evidence discovery was complete.

## v1.0.4 — Decision routing and workflow hardening

### Added
- Decision Routing for every material unknown: Evidence-resolvable, PO Decision, Technical Decision, External Reference, or Non-blocking Unknown.
- Hard guard: never fill an unresolved human-owned decision with assistant preference.
- Evidence-first question routing and question minimization.
- Source authority fields in the Jira template.
- Gate-aware Analysis template with Evidence Conflicts and Proposed Enhancements.

### Changed
- External research now follows internal evidence discovery by default and cannot substitute for product truth or human decisions.
- Example workflow now demonstrates evidence discovery before clarification.
- README version and workflow summary updated.

### Reason
Cold-start testing showed that the assistant could identify useful unknowns but still answer product decisions with its own preferred behavior, ask questions before exhausting relevant knowledge, and let external patterns influence product behavior too early.

## v1.0.3 — Cold-start Test #2 corrections

### Added
- Evidence-before-Question Gate.
- Strict neutral clarification before the Recommendation Gate, unless the PO explicitly requests an early opinion.

### Reason
Testing showed that relevant product knowledge should be searched before asking the PO and that preference wording during clarification needed stronger enforcement.

## v1.0.2 — Cold-start Test #1 follow-up

### Added
- Decision Dependency Gate.
- Scope Expansion Gate.
- Source Validation Gate using Authority, Freshness, and Applicability.
- Knowledge Discovery beyond Git, limited to relevant available sources.
- Evidence Conflict handling for disagreements between code, documents, and other product knowledge.
- Rule that absence from a searched snapshot is not proof of absence from the product.

### Reason
Testing showed that source authority, knowledge discovery, unresolved human decisions, and unapproved scope additions need explicit workflow gates.

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
