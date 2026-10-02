# PO Assistant Core

Reusable, evidence-first framework for Product Owners to analyze requirements and produce implementation-ready Jira stories across multiple products.

## Goals

- Reuse one PO workflow across different products and teams.
- Keep **PO Core** separate from each product's knowledge.
- Require evidence for factual claims.
- Search relevant evidence before asking the PO questions, then route unresolved decisions to the correct owner.
- Ask targeted clarification questions without getting stuck in an endless question loop.
- Review relevant code paths when code exists.
- Complete relevant internal evidence discovery before automatic external best-practice research, unless an explicit exception applies.
- Compare up to three viable solutions and provide a recommendation that still requires human approval.
- Produce both a readable analysis and a concise Jira story.
- Preserve product context isolation and isolate concurrent requirements within the same product.

## Core output

Every final story must include:
- Simple non-technical summary
- Current behavior
- Expected behavior
- Scope
- Not in Scope
- Acceptance Criteria
- Test Recommendations
- Technical / Code References
- Impact & Dependencies
- Risks / Unknowns
- Definition of Done

## Repository structure

- `SKILL.md` — entry point and execution rules
- `core/` — reusable PO analysis rules, including evidence validation, decision routing, scope control, and solution gates
- `templates/` — reusable output and onboarding templates
- `examples/` — example usage
- `CHANGELOG.md` — version history

## Product model

One PO may own multiple products. Each product gets its own **Product Pack**. Product knowledge must not leak into another product unless the PO explicitly requests a cross-product comparison.

## Version

Current baseline: **v1.0.7**
