# Feedback and Learning

## Goal
Correct errors without poisoning reusable knowledge.

## Workflow
Wrong output → Root Cause → Correction → Evidence Validation → Human Approval → Registry Entry (Approved) → Versioned Source Update → Active Learning

## Root-cause categories
- Missing Knowledge
- Bad Retrieval
- Wrong Inference
- Outdated Document
- Missed Code Path
- Missing Clarification Question
- Incorrect Core Rule
- Product Context Leakage
- External Reference Misapplied

## Rule
User feedback alone is not automatically a verified fact.

When corrected:
- identify what was wrong
- explain why it happened
- inspect supporting evidence
- propose the correction
- ask for/record human approval if it should become reusable knowledge

## Learning scope
Classify approved learning as:
- Core rule change
- Organization rule
- Product-specific knowledge
- PO preference

Do not put product-specific learning into PO Core.

## Approved Learning Registry

Human approval is necessary but not sufficient to activate reusable learning. Record each approved item in a versioned, reviewable registry owned by the appropriate scope (Core, Organization, Product, or PO Preference).

Minimum record:
- Learning ID and concise rule or knowledge statement
- Scope and affected product/version/environment, if applicable
- Supporting evidence references and source authority
- Feedback/correction record reference
- Approver, approval date, and decision rationale
- Status: Proposed / Approved / Active / Superseded / Revoked
- Effective version/date and last-reviewed date
- Owner and superseding/revocation reference when applicable

Lifecycle:
1. Capture a proposed correction without changing reusable behavior.
2. Validate evidence, scope, and conflicts with existing active rules.
3. Obtain explicit approval from the authorized owner for that scope.
4. Register the approved decision; activate it only after the appropriate versioned source of truth is updated and linked.
5. When evidence changes, review, supersede, or revoke the entry; preserve history and stop applying inactive entries.

The registry is an audit trail, not a competing source of truth. An entry does not override current authoritative product facts, higher-priority rules, or requirement isolation. Never infer approval from silence.
