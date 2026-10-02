# Feedback and Learning

## Goal
Correct errors without poisoning reusable knowledge.

## Workflow
Wrong output → Root Cause → Correction → Evidence → Human Approval → Approved Learning

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
