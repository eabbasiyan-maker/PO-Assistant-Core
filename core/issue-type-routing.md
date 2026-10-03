# Issue Type Routing

## Goal
Do not force one Jira template onto every Sprint issue. Route the final Jira output by issue type while keeping the evidence, source, decision, scope, recommendation, and human-approval guards unchanged.

## Routing rule
Before Jira output:

1. If the PO explicitly provides an Issue Type, use it.
2. If the requirement strongly supports one type, infer it and state: **Detected Issue Type: <type>**.
3. If two or more types are materially plausible and the choice changes the useful output, ask one focused PO question.
4. The PO can override the inferred type at any time.
5. Do not ask for Issue Type merely as a ritual when it is already clear.

## Supported baseline types

### User Story / Feature
Use for a new or changed product capability.

Core sections:
- Title
- Simple Need / Why
- Current Behavior, when relevant
- Expected Behavior
- Scope
- Not in Scope, when it prevents ambiguity
- Acceptance Criteria
- Test Recommendations
- Technical / Code References, when technically relevant
- Impact & Dependencies, when material
- Risks / Unknowns, when material
- Definition of Done

### Bug
Use when observed behavior differs from expected/approved behavior.

Core sections:
- Title
- Problem Summary
- Actual Behavior
- Expected Behavior
- Reproduction / Trigger Conditions, when known
- Environment / Version, when material
- Evidence
- Impact
- Acceptance / Fix Verification Criteria
- Regression Test Recommendations
- Technical / Code References, when available
- Risks / Unknowns, when material
- Definition of Done

Do not invent Severity/Priority. Include them only if provided or decided by the appropriate human owner.

### Technical Debt
Use for maintainability, architecture, reliability, performance, obsolete implementation, or similar technical improvement where the main value is technical rather than a new user capability.

Core sections:
- Title
- Current Technical Problem
- Evidence / Technical References
- Why It Matters / Impact
- Scope
- Not in Scope, when useful
- Expected Technical Outcome
- Acceptance / Verification Criteria
- Regression / Compatibility Risks
- Test Recommendations
- Definition of Done
- Open Technical Decisions, when any

Do not assume a refactor or architecture change is required merely because debt exists.

### Spike / Investigation
Use when the main deliverable is knowledge, evidence, feasibility, or a decision input rather than production behavior.

Core sections:
- Title
- Question / Objective
- Why the Investigation Is Needed
- Investigation Scope
- Evidence / Sources to Inspect
- Questions / Hypotheses
- Expected Deliverable
- Exit Criteria
- Timebox, only if provided/decided
- Risks / Unknowns, when material
- Follow-up Decisions, when relevant

Do not fabricate implementation AC for an investigation.

### Task
Use for a concrete work item that does not need a full user-story structure.

Core sections:
- Title
- Objective
- Scope / Work Required
- Deliverable
- Dependencies, when material
- Verification / Done Criteria
- Risks / Unknowns, when material

### Job Story
Use when the requirement is intentionally framed around situation, motivation, and desired outcome.

Core sections:
- Title
- Situation
- Motivation
- Expected Outcome
- Current Context, when relevant
- Scope
- Acceptance Criteria
- Test Recommendations, when relevant
- Dependencies / Risks, when material
- Definition of Done

## Section selection rule
The listed sections are the baseline for each type, not a command to print empty headings.

- Omit optional/irrelevant sections.
- Keep a section when omitting it would hide a material decision, risk, dependency, verification condition, or evidence limitation.
- Never fill an irrelevant section with generic text just to satisfy a template.
- Product-specific Jira conventions from the Product Pack may extend these templates, but must not weaken Core guards.

## Classification boundaries
Issue Type is an output/work-item classification, not product truth.

If classification is uncertain and does not materially change the analysis, continue analysis and defer the Jira type decision until output time.

Do not let Issue Type classification bias factual investigation. Evidence discovery comes first.
