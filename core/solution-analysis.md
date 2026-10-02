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
3. code/architecture has been inspected when technically relevant;
4. external research has been performed when it materially affects the decision.

If these conditions are not met:
- present credible options neutrally;
- do not rank or recommend them;
- state what evidence or decision is still needed.

## Preliminary recommendation exception

If the human PO explicitly asks for an opinion before full validation, a provisional opinion is allowed, but it must be labeled:

**Preliminary Recommendation — based on current information, not yet validated**

It must:
- state what has not yet been validated;
- identify the evidence still needed;
- not be treated as a final decision;
- not be copied into the final Story as an approved solution unless later validated and approved.

## Validated recommendation

After the Recommendation Gate is satisfied, end with:

**Recommendation — requires human approval**

Include:
- recommended option
- evidence-based reasons
- conditions that could change the recommendation
- required human approver(s), usually PO/TL as appropriate
