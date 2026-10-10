# PO Assistant Core — Pre-distribution Consistency Review
Review date: 2026-10-10
Scope: GitHub feature snapshot `feat/log-intelligence-core-20261009` at pre-review SHA `96fbee4e19a15b66193588783b72d7872202f83f`.
Method: reviewed repository tree and selected governing source files; this is a DOCUMENT/STRUCTURE review, not an exhaustive behavioral test or security certification.

## Findings and resolutions
1. **README baseline vs branch contents**: README calls core baseline v1.0.9; feature branch also has Log Intelligence documents/tools. Resolution: README and START_HERE now explicitly separate stable Core baseline from optional experimental log pilot. No claim of a new Core release.
2. **Distribution onboarding missing**: No single install/use guide for other POs. Resolution: START_HERE added with product-pack setup, example prompt, access requirements and safety boundaries.
3. **Cross-product evidence risk**: A Chat-specific Log pack is held in a separate Chat repository, while generic rules and experimental tools are in PO Core. Resolution: onboarding explicitly forbids treating a Chat pack as reusable product evidence. Each PO supplies a validated Product Pack.
4. **Log pilot evidence version conflict**: `core/log-analysis-pilot-v0.1.md` mentions an earlier 8/8 local pilot while `core/log-step5-integration-regression-v1.0.md` records a later 12/12 local reproduction. These are **different reported runs**, not an aggregate 20/20, and neither is CI proof. Resolution: make the distinction explicit in distribution notes; do not claim a verified release test.
5. **Log catalog identity inconsistency**: `templates/log-discovery-template.md` had a shorthand key `commit+file+line+logger API`; `core/log-catalog-extraction-contract-v1.0.md` requires `repository+commit+path+method+line+invocation`. Resolution: align template to canonical contract.
6. **Partial coverage and source authority**: The experimental scanner emits regex candidates, not fully validated emitter inventory; Chat Catalog is incomplete. Resolution: log pilot remains explicitly experimental; no production readiness or repository-wide coverage claim.
7. **Missing deployment integration**: Repository defines instructions and offline Python tools, not an automatically installed agent, direct Jira integration, or scheduled service. Resolution: document manual setup and permissions clearly.

## Review outcomes
- Cross-file core rules inspected: evidence-first, source-access gate, requirement isolation, external research gate, human decision gate, adaptive Jira routing: no direct contradiction identified in reviewed passages.
- No live Jira, deployed source, runtime logs or GitHub Actions CI run inspected.
- No code modifications to Chat Server or production systems.
- Remaining uncertainty: unreviewed sections and actual assistant adherence require cold-start tests by recipient POs.
- **Distribution decision:** suitable to share as a labeled **starter framework / preview**; NOT a validated autonomous PO Agent release.
