# PO Assistant Core — Starter Kit for Product Owners

**Release type:** shareable framework snapshot, NOT a deployed agent.
**Core baseline:** v1.0.9. The feature branch additionally contains experimental Log Intelligence material.
**Language:** Persian by default; English technical terms when useful.

## 1. What you get
- `SKILL.md`: the operational instructions for a PO assistant.
- `core/`: generic evidence-first analysis, clarification, source review, decision and scope gates, Jira issue routing, test suggestions.
- `templates/`: Product Pack, analysis, adaptive Jira issue, feedback and PO preferences.
- `examples/`: one illustrative workflow.
- `tools/`, `tests/`, and `core/log-*`: **optional experimental Log Intelligence pilot**; NOT necessary for normal PO work, NOT a production incident agent.

## 2. Five-minute start
1. Unzip locally and read `README.md`, `SKILL.md`, and `core/evidence-policy.md`.
2. In your AI workspace, provide the complete `SKILL.md` and the referenced `core/` and `templates/` files as accessible project knowledge. A ZIP attachment by itself does not guarantee the assistant can read its contents or follow the skill.
3. Copy `templates/product-pack-template.md` for **your own product**, and fill in product name, approved business rules, source links, environment/version, source authority, API/docs and stakeholders.
4. Give the assistant one real requirement, the product name and its Product Pack. Ask it to follow the workflow in `SKILL.md` and produce a concise analysis plus the appropriate Jira issue.
5. Review the Evidence / Claim / Inference / Unknown labels, source authority, open decisions and Jira output before approving or publishing.

## 3. Suggested first prompt
«برای محصول [نام محصول] با استفاده از PO Assistant Core و Product Pack اختصاصی آن، این نیازمندی را تحلیل کن: [نیازمندی]. ابتدا شواهد داخلی و در صورت نیاز سورس را بررسی کن؛ فرضیات را واقعیت اعلام نکن؛ سؤال‌های تصمیم‌گیری را به PO/TL درست ارجاع بده؛ سپس تحلیل و Issue مناسب Jira با AC و تست‌های لازم را بده. اگر به منبع دسترسی نداری، صریح بگو.»

## 4. Boundaries
- Core is **not** an API integration, Jira connector, GitHub permission, autonomous background worker, or a guarantee of source access.
- Product Pack templates contain placeholders, not approved product facts. Each PO must validate authority/freshness.
- Do not share Chat Server-specific product packs, production logs, tokens, customer data, or internal secrets with other teams unless separately authorized.
- Research, code inspection and Jira changes require the assistant to have actual tools and permissions.
- A generated Jira-ready issue is text; it is **not automatically created in Jira**.
- Human approval remains required for product/architecture decisions.
- Optional Log tools require Python; `log_analyzer.py` uses a separate product pack, pinned source SHA and sanitized logs; it does not infer verified root cause.

## 5. Example acceptance check
Ask the assistant for a Story based on a requirement whose source it cannot access. It must label source access unavailable and avoid claiming it inspected code. Then supply an authoritative source and retry. The result should distinguish actual behavior from desired behavior and produce only the Jira sections relevant to the issue type.

## 6. Ownership and updates
Keep generic reusable rules in Core, product-specific evidence in each team's Product Pack. Log feedback through `templates/feedback-template.md`; do not turn an unverified correction into global truth.
