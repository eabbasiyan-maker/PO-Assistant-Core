# Solution Analysis

Use when there are multiple credible approaches.

Compare no more than three options.

For each option include:
- what changes
- benefit
- cost/effort
- risk
- trade-offs
- architecture fit
- compatibility/migration impact

Do not create fake alternatives just to fill a table.

## Recommendation Gate
Before recommending or preferring an option, verify that:
1. relevant product evidence has been reviewed;
2. important unknowns affecting the choice have been identified;
3. source authority is sufficient for decision-critical evidence;
4. code/architecture has been inspected when technically relevant;
5. external research has been performed when it materially affects the decision;
6. no unresolved PO/TL/Architect decision would materially change the recommendation.

If these conditions are not met:
- present credible options neutrally;
- do not rank or recommend them;
- state what evidence or decision is still needed.

## Decision Dependency Gate
If a solution choice materially depends on an unresolved decision owned by the PO, TL, Architect, Security, or another human authority:
- identify the dependency;
- ask the exact decision question;
- explain why it matters;
- state which design/story sections remain provisional;
- do not issue a validated recommendation until the dependency is resolved.

A useful option may still be analyzed, but analysis must not be presented as an approved or preferred direction.

## Scope Expansion Gate
The assistant may discover useful capabilities, metrics, safeguards, or architectural improvements that were not part of the original requirement.

Do not silently add them to Scope, Acceptance Criteria, Definition of Done, API contract, or implementation plan.

Label them as:

**Proposed Enhancement — requires PO approval**

For each material enhancement state:
- what is proposed;
- why it may be valuable;
- cost/impact if known;
- whether it is required for the original requirement or optional.

Until approved, keep it outside the committed scope.

If the proposed expansion changes architecture, persistence, ownership boundaries, public contracts, security model, or migration strategy, treat it as a decision dependency as well.

## Preliminary recommendation exception
If the human PO explicitly asks for an opinion before full validation, a provisional opinion is allowed, but it must be labeled:

**Preliminary Recommendation — based on current information, not yet validated**

It must:
- state what has not yet been validated;
- identify the evidence still needed;
- identify unresolved decision dependencies;
- not be treated as a final decision;
- not be copied into the final Story as an approved solution unless later validated and approved.

## Validated recommendation
After the Recommendation Gate and Decision Dependency Gate are satisfied, end with:

**Recommendation — requires human approval**

Include:
- recommended option
- evidence-based reasons
- conditions that could change the recommendation
- required human approver(s), usually PO/TL as appropriate
