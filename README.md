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
- Route Jira output by Issue Type and produce only the sections useful for that work item.
- Produce both a readable analysis and a concise Jira-ready issue.
- Preserve product context isolation and isolate concurrent requirements within the same product.

## Adaptive Jira output

The Core does not force one fixed template on every Sprint issue. Before Jira output it routes the work item as one of the baseline types:
- User Story / Feature
- Bug
- Technical Debt
- Spike / Investigation
- Task
- Job Story

If the type is clear, the assistant may infer it and state the detected type. If the classification is materially ambiguous, it asks the PO one focused question. The PO can always override it.

Each type has its own relevant baseline sections; irrelevant headings should not be printed.

## Repository structure

- `SKILL.md` — entry point and execution rules
- `core/` — reusable PO analysis rules, including evidence validation, decision routing, scope control, and solution gates
- `templates/` — reusable output and onboarding templates
- `examples/` — example usage
- `CHANGELOG.md` — version history

## Product model

One PO may own multiple products. Each product gets its own **Product Pack**. Product knowledge must not leak into another product unless the PO explicitly requests a cross-product comparison.

## Version

Current baseline: **v1.0.10**
