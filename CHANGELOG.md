# Changelog

## v1.0.8 — Named External Question gate

### Added
- Mandatory **External Question** before automatic web/best-practice research.
- Mandatory **Decision Impact** mapping showing which decision, Unknown, Story section, architecture/API choice, or risk assessment could materially change from external evidence.
- Output preflight check removing automatically used External References that do not map to a named unresolved external question and material impact.

### Changed
- Generic background research, examples, and best-practice browsing no longer satisfy the External Research Gate.
- Default research order is now: Internal Evidence → Named External Question → Decision Impact → External Research → Applicability Check.

### Compatibility validation
Changes were staged on `test/v1.0.8-external-question-gate` before main. The branch was 2 commits ahead and 0 behind main and touched only `SKILL.md` and `core/best-practice-research.md`. Regression checks confirmed that Requirement Isolation, Internal Evidence Completion, human decision ownership, technical-fact routing, blocker-to-scope protection, Recommendation Gate, and Scope Expansion Gate remain intact.

### Reason
Two independent Chat Server cold-start tests showed the same failure pattern: internal evidence was still incomplete, yet external sources were used for generic messaging/pagination background that did not resolve a named external question or affect the next decision.

## v1.0.7 — Evidence-resolvable escalation guard

### Added
- Explicit distinction between missing technical facts and actual Technical Decisions.
- Evidence-resolvable escalation guard: inspect relevant implementation evidence before asking TL/Developer/Architect for a factual answer.
- **Technical confirmation needed** state for unresolved technical facts after evidence search.
- Guard preventing unresolved technical blockers from becoming implementation Scope/AC/DoD/API changes.
- Output preflight checks for premature technical escalation and blocker-to-scope conversion.

### Changed
- Technical Decision now means an actual technical choice after relevant facts are established.
- Clarification must not imply that all Story information is complete while evidence discovery can still reveal material questions.

### Compatibility validation
Changes were staged on `test/v1.0.7-routing-guard` before main. Diff against v1.0.6 touched only `SKILL.md`, `core/clarification.md`, and `core/decision-routing.md`. Existing guards for human decision ownership, requirement isolation, external research ordering, recommendation, and scope control remained present.

### Reason
Cold-start testing showed that a missing implementation fact such as whether `botId` is already available could be escalated to TL too early and then incorrectly converted into required implementation scope.

## v1.0.6 — Hard enforcement of isolation and research gates

### Added
- Mandatory Requirement Isolation Gate before using prior same-product context.
- Mandatory Internal Evidence Completion Gate before automatic external research.
- Output Preflight that rejects context leakage, premature external research, assistant-filled human decisions, and silent scope expansion.
- Requirement provenance check for dependencies/constraints imported from prior work.

### Changed
- Empty GitHub Code Search no longer counts as completed internal discovery when other relevant internal sources are available.
- Unrelated prior work should not even be surfaced unless a material relationship is evidenced or explicitly requested.
- External research is blocked rather than merely discouraged until internal discovery is sufficient, except for explicit research requests or externally-defined facts required to understand the request.

### Reason
Cold-start retest repeated two v1.0.5 failures: unrelated QC/Audit context leaked into a new History Retention requirement, and OpenAI research occurred after only a GitHub search. The prior rules were advisory enough to be ignored, so v1.0.6 converts them into preflight gates.

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
