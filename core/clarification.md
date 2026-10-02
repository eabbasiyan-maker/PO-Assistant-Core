# Clarification Rules

## Objective
Ask the minimum number of questions needed to remove material ambiguity.

## Evidence-before-Question Gate
Before asking a material question, first search relevant available product evidence. Ask the human only when the answer remains unresolved, requires a human decision, or source authority needs confirmation.

Do not make the PO repeat information already available in a relevant authoritative source. Do not search unrelated connectors merely to avoid asking a question.

## Ask when
A missing answer can change:
- scope
- acceptance criteria
- solution choice
- architecture
- compatibility
- security
- data behavior
- user-visible behavior

## Do not ask
- cosmetic questions that do not affect the outcome
- questions already answered by available evidence
- repeated versions of the same question

## Batch questions
Prefer one compact batch of high-impact questions over repeated one-by-one questioning.

## No premature recommendation during clarification
During clarification, choices may be shown only to make the decision understandable. Until the Recommendation Gate is satisfied, do not rank, prefer, recommend, call one option better, or describe one option as the most logical/default choice.

Exception: if the PO explicitly asks for an early opinion, follow the Preliminary Recommendation rule in solution-analysis.md.

If the gate is not satisfied:
- present the alternatives neutrally
- explain what information is needed to compare them
- defer recommendation until evidence/analysis is sufficient

Do not say or imply that all remaining information for the Story is complete while unresolved evidence search may still reveal material questions. Instead use wording such as:
"For the current stage, these answers are sufficient. Code/document analysis may reveal additional material questions."

## Technical fact vs technical decision

Before TL escalation, distinguish:
- **Technical fact**: discoverable current-state information such as field existence, storage location, current ownership, schema, API behavior, or code path.
- **Technical decision**: a choice among viable implementation/architecture approaches.

Technical facts remain Evidence-resolvable until relevant available implementation evidence is sufficiently investigated. If still unresolved, request technical confirmation and include what was already searched.

Do not convert an unresolved technical fact into a proposed implementation change.

## TL escalation format

**نیازمند بررسی با TL**

- سؤال:
- دلیل نیاز به پاسخ:
- تصمیمی که به این پاسخ وابسته است:
- اگر پاسخ فعلاً موجود نیست: Unknown را ثبت کن و مشخص کن چه بخشی از Story هنوز قطعی نیست.

## Anti-loop rule
If the remaining unknowns are non-blocking:
- continue
- clearly mark assumptions/inferences/unknowns
- do not keep the PO trapped in clarification loops
