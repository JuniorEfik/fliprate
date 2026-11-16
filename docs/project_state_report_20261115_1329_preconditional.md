# FlipRate Project State Report

**Updated:** 2026-11-15  
**Governing manual:** `master.md`  
**Current stage:** Stage 1 — Discover  
**Gate:** **OPEN / REVISE**

## Executive state

Stage 0 is complete. Stage 1 now has a full-text closest-work matrix, expanded source register, revised proposal, ARIS novelty review, and ARS source-verification and Devil's Advocate audits.

The evidence invalidates the original novelty framing. SycoBench-600, Big-Big-SycoBench, Ma et al., BASIL, SYCON Bench, and other work already cover the core distinction and most proposed mechanics. The only remaining candidate is a narrow serial measurement-validation study that crosses evidence sufficiency with pressure framing and counterbalances feedback order.

Stage 1 does not yet pass because the project owner has not accepted this rescope, several design-validity issues remain open, and model access, cost, sample size, and adjudication resources are unknown.

## Skill status

| Capability | Installed invocation | Use in this stage |
|---|---|---|
| ARIS end-to-end | `research-pipeline` | Inspected; not launched because master gates forbid automatic advancement |
| ARIS literature | `research-lit` | Used for discovery and primary-source comparison |
| ARIS novelty | `novelty-check` | Fresh GPT-6 Astra review plus addendum; trace saved under `.aris/traces/novelty-check/` |
| ARS | `ars-codex:academic-research-suite`, routed to `deep-research` roles | Source verification and Checkpoint-1 Devil's Advocate audit completed |
| Best-Paper-Writing | `bestpaper-writing` | Inspected only; drafting remains prohibited |

## Completed

- Read `master.md` and the relevant skill instructions.
- Preserved original and newly retrieved raw research files with checksums.
- Resolved ELEPHANT as arXiv:2505.13995.
- Retrieved and read the closest comparator corpus, including SycoBench-600 and Big-Big-SycoBench.
- Created `research/closest_work_matrix.md`.
- Updated the related-work review, source register, novelty assessment, and proposal.
- Ran a fresh ARIS novelty review and bounded follow-up after newer close work was found.
- Ran ARS source verification and Checkpoint-1 Devil's Advocate review.
- Created `audits/discovery_audit.md` with severity, evidence, recommendations, and status.

## Pending

- Project-owner decision on the narrowed serial measurement-validation contribution.
- One worked item family demonstrating the proposed crossed cells and counterbalanced schedules.
- Exact primary estimand and minimum usable denominator rule.
- Formal treatment of neutral reconsideration, invalid/irrelevant evidence, abstention, malformed outputs, and shared-baseline branching.
- Execution budget, approved model list, credentials/access path, and cost cap.
- Human or expert evidence-sufficiency adjudication plan.
- Independent venue/version reconciliation for sources with arXiv-only status.
- Stage 2 protocol, scoring rubric, prompt templates, analysis plan, and design audit.

## Unverified

- Global novelty of the serial evidence-sufficiency × pressure interaction; the current finding is search-bounded.
- Whether another recent or non-arXiv work executes the same serial design.
- Whether the `FlipRate` name conflicts with another project.
- Code/data completeness or reproducibility of comparator repositories.
- Numerical results reported by prior papers; none were reproduced.
- Official sprint portal status, exact deadline time, report template, authors, and affiliations.
- Availability and permitted use of provider APIs or remote compute.

## Blocked

- Stage 2: blocked on scope approval and unresolved design issues.
- Model experiments: blocked on model selection, credentials/access, budget, and sample-size plan.
- Local open-weight experiments: blocked by unavailable GPU access.
- Paper drafting: blocked by research, implementation, experiment, and audit gates.
- Final PDF/submission: blocked by official template, author details, toolchain, and portal-status uncertainty.

## Principal risks

1. **Novelty compression:** the candidate may be judged as a combination of SycoBench-600, Big-Big-SycoBench, Ma et al., SYCON, and Gupta et al.
2. **Factorial-design failure:** separate arms do not estimate evidence × pressure interactions.
3. **Turn confounding:** force, repetition, round number, and accumulated context can move together.
4. **Template gaming:** a model may follow reference style or named options without evaluating evidence.
5. **Sparse denominators:** strong models may produce too few initial errors for correction estimates.
6. **Changing confidence referent:** scalar confidence is misleading after answer changes.
7. **Resource infeasibility:** no execution budget or provider access is established.

## Highest-value next action

Obtain the project owner's approval or rejection of the narrowed contribution in `research/research_proposal.md`. If accepted, the next justified work is a Stage-1 worked item and estimand proof that resolves the open major audit issues before Stage 2 begins.

## Gate status

- **Stage 0:** PASS.
- **Stage 1:** OPEN / REVISE.
- **Stage 2 onward:** NOT AUTHORIZED.
