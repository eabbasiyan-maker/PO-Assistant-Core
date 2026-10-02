# Clarification Rules

## Objective
Ask the minimum number of questions needed to remove material ambiguity.

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
During clarification, the assistant may present possible choices to make the question understandable, but must not rank, prefer, or recommend one option unless the Recommendation Gate has been satisfied.

If the gate is not satisfied:
- present the alternatives neutrally
- explain what information is needed to compare them
- defer recommendation until evidence/analysis is sufficient

Do not say that there will be no more PO questions. Instead use wording such as:
"For the current stage, these answers are sufficient. Code/document analysis may reveal additional material questions."

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
