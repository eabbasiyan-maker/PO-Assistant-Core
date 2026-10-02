# Decision Routing

## Goal
Do not treat every unknown as a PO question and do not fill unresolved human decisions with assistant preferences.

## Classify every material unknown
Before asking, recommending, or designing around an unknown, classify it as one of:

### Evidence-resolvable
The answer should be discoverable from relevant product evidence such as approved knowledge, validated source code, API specs, logs, runs, tests, or architecture documents.

Action: investigate first. Ask a human only if the evidence remains insufficient or conflicting.

### PO Decision
The answer defines desired product behavior, user experience, scope, policy, priority, or acceptance behavior and is not already approved in evidence.

Action: ask the PO. Do not infer the desired behavior from current code or external best practice.

### Technical Decision
The answer concerns a choice between implementation approaches, architecture, technical ownership, platform constraints, deployment, persistence strategy, or another decision owned by TL/Architect/technical authority.

A missing technical fact is **not** automatically a Technical Decision. Questions such as "does field X exist?", "where is Y stored?", "which component currently owns Z?", or "is identifier A persisted?" are Evidence-resolvable until relevant implementation evidence has been sufficiently investigated.

Action:
1. investigate relevant available implementation evidence first;
2. if the fact is found, use it as validated evidence subject to Source Validation;
3. if evidence is insufficient/conflicting and human confirmation of the fact is required, escalate it as **Technical confirmation needed**, not as a design decision;
4. only classify as a Technical Decision when an actual technical choice remains after the facts are established.

### External Reference
The question is about industry patterns, provider behavior, standards, or external constraints.

Action: research authoritative external sources. Treat the result as external reference, not product truth.

### Non-blocking Unknown
The answer is not needed to continue the current stage.

Action: record it as Unknown and continue. Do not force a decision prematurely.

## Ownership rule
Current implementation can reveal what the system does today. It cannot by itself decide what the product should do tomorrow.

External best practice can inform a decision. It cannot replace a PO/TL decision.

## Hard guard
**Never fill an unresolved PO/TL/Architect decision with your own preferred behavior.**

If a decision owner has not decided:
- keep alternatives neutral;
- show evidence and consequences;
- identify the owner;
- ask only when the decision becomes necessary for the next step.

## Question minimization
After evidence discovery and classification:
- ask only blocking or high-impact human decisions;
- batch questions by owner where useful;
- do not ask evidence-resolvable questions before searching;
- do not ask non-blocking questions merely to make the analysis look complete.


## Evidence-resolvable escalation guard
Before asking TL/Developer/Architect a technical factual question:
- identify the implementation fact being sought;
- inspect the relevant available code path/docs/API/schema/log/test evidence;
- record what was searched and what remains unresolved;
- validate source authority where material.

Escalate only when the fact cannot be resolved reliably from available evidence or when canonical-source confirmation is itself required.

Do not ask a human to manually answer a fact that the assistant can still investigate from relevant available evidence.

## Unresolved blocker is not implementation scope
Discovering a missing fact or technical blocker does not prove the required implementation change.

Do not convert:
- "identifier not yet found" into "add/persist identifier";
- "ownership unclear" into "move ownership";
- "storage behavior unknown" into "create new storage";
- or similar unknowns into Scope/AC/DoD/API changes.

First establish the root cause and credible solution space. If a new implementation change is truly required, support that conclusion with evidence/analysis and pass the Scope Expansion and Decision Dependency gates as applicable.
