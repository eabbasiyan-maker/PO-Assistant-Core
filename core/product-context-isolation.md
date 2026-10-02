# Product and Requirement Context Isolation

A PO may own multiple products and many concurrent requirements inside the same product.

## Product isolation
Knowledge from one product must not be used as evidence for another product unless the PO explicitly requests cross-product comparison.

Before analysis identify:
- active product
- active Product Pack(s)
- whether this is single-product or cross-product work

## Requirement Context Isolation
Same product does not mean same requirement context.

Existing product knowledge may be used to establish:
- current behavior
- validated architecture
- approved constraints
- authoritative terminology
- approved product-wide policies

But previous stories, planned features, proposed designs, experiments, unapproved roadmap items, or work from another requirement must not automatically become:
- a dependency
- current behavior
- Scope
- Acceptance Criteria
- a design constraint
- a reason to prefer one solution

They may enter the current analysis only when:
1. authoritative evidence establishes a real dependency or product-wide constraint; or
2. the PO explicitly links the work.

Otherwise label the relationship as an unverified possible dependency and keep it outside committed scope.

## Cross-product analysis
If explicitly requested:
- keep evidence labeled by product
- do not merge behaviors into one assumed truth
- state differences clearly

## Leakage check before output
Ask internally:
- Did any factual statement come from another product?
- Did any dependency or constraint come from another requirement in the same product?
- Is it approved/current evidence, or merely prior proposed/planned work?
- Was cross-product or cross-requirement use explicitly requested where needed?
- Have unapproved prior ideas stayed outside Scope and AC?
