# FlipRate Stage 1 Closure Report

**Date:** 2026-11-15  
**Decision requested:** project-owner approval or rejection of the final Stage-1 design package  
**Owner decision recorded:** Stage 1 closed; limited Stage 2 protocol/statistics/audit work authorized on 2026-11-15
**Historical status:** preserved Stage-1 closure record; current authority and readiness state are governed by `master.md` and `docs/project_state_report.md`.

> **Current-status addendum (2026-11-16):** Stage-2 design has since closed. The owner accepted 72.24% ± 0.63% CR1/Holm power as a lower-powered exploratory limitation while retaining the failed 80% criterion. Execution remains blocked and no empirical model study or completed adjudication exists. The historical requests and blockers below are preserved as the Stage-1 record.

## Closure conclusion

The revised Stage-1 scientific design is **ready for owner approval**.

- ARIS `research-review`: **READY FOR OWNER APPROVAL** after one corrective round.
- ARS Devil's Advocate Checkpoint 1: **PASS** after a 5/5 rebuttal on the central construct issue.
- No unresolved Critical or Major design issue remains at Stage-1 scope.
- Both reviews are same-family/provisional, not cross-family acceptance.

This conclusion means the design is sufficiently specified for the owner to decide whether Stage 2 should begin. It does not authorize implementation, prompt lock, paid calls, model experiments or paper writing.

## Exact proposed primary experiment

### Item structure

Each item family has:

- a complete hidden generating world in which target `B` is true;
- a deliberately underdetermined displayed baseline;
- `I`: valid, relevant information that leaves `B` and at least one other answer compatible;
- `S`: valid, relevant information that makes `B` uniquely warranted;
- a neutral frame `N` and bundled authority/confidence pressure frame `P`, both naming the same target in the same position;
- substantive answer options plus a separate `abstain` action.

Adjudicators must document two witness states with different answers for `I` and prove uniqueness for `S`.

### Interaction tree

For each item-model pair:

1. Run one baseline call.
2. Replay the exact baseline into five Turn-1 nodes: `S-N`, `S-P`, `I-N`, `I-P`, `C-N`.
3. Replay each exact factorial Turn-1 conversation into neutral and pressure Turn-2 children.
4. Continue the control once under neutral reconsideration.

The resulting paths are `S-NN`, `S-NP`, `S-PN`, `S-PP`, `I-NN`, `I-NP`, `I-PN`, `I-PP`, and `C-NN`. Total: 15 calls per item-model pair.

### Primary estimand

For model `m`, on the four-cell-complete item-model population:

\[
\delta_m^{CC}=\operatorname{mean}_{i\in CC}
[p_{1i}(B|S,P)-p_{1i}(B|S,N)-p_{1i}(B|I,P)+p_{1i}(B|I,N)].
\]

This estimates whether pressure changes the separation in reported target support between sufficient and insufficient valid information at first exposure. It does not identify an internal mechanism.

Mandatory reporting includes all four cell means, evidence and pressure main effects, the interaction, complete denominators, malformed rates and abstention. A separate all-family interval uses denominator 96 and assigns only undefined target-support values to 0 or 1. Turn-2 repetition and carryover contrasts are secondary.

## Resolved issues

- Validity, relevance and sufficiency are separately defined; information sufficiency is primary.
- The `S/I × N/P` first-turn factorial and exact serial condition table are explicit.
- The primary estimand, unit of analysis and calculation are explicit.
- Exact baseline and Turn-1 response replay control branch history; Turn 1 avoids serial carryover.
- Recovery and hysteresis claims are removed.
- Abstention is separated from the substantive support distribution.
- Complete-case selection and all-family missing-output bounds are explicit.
- Development, exact-repeat and paraphrase validation calls are budgeted.
- Construction, rating, adjudication and rework labor are estimated.
- Previous discovery-audit major issues have been resolved, accepted as limitations or identified as external blockers.
- Stale nonfactorial and recovery/hysteresis descriptions were reconciled across current artifacts.

## Accepted limitations

- `P` bundles authority and asserted confidence.
- A model may treat social testimony as information even when it adds no task fact.
- `I` can rationally increase support for `B` without making `B` unique.
- Reported support is behavioral and may be poorly calibrated.
- The interaction is scale-specific and can be influenced by ceiling effects.
- Turn-2 effects include accumulated context, generic turn effects and mediation through prior assistant responses.
- Invalid and irrelevant evidence are not primary conditions.
- The 96-item, two-domain sample targets moderate effects and limited generality.
- The residual novelty claim is search-bounded and may be viewed as a controlled combination of prior methods.
- Same-family review provides provisional assurance only.

## Remaining blockers

These do not invalidate the Stage-1 design, but they block execution:

- explicit owner authorization for Stage 2;
- funded USD 250 API budget;
- OpenAI, Anthropic and Google credentials or approved alternative scope;
- eligible stable snapshots, rate limits and official-price preflight;
- two named independent reviewers and a third adjudicator;
- a team or post-sprint schedule for approximately 98–131 human hours;
- prespecified raw-scale meaningful-effect threshold, multiplicity rule and power/completeness simulation;
- later protocol, scoring and design-audit deliverables.

## Feasibility assessment

### API plan

- Main: `96 × 15 × 3 = 4,320` calls.
- Development pilot: `8 × 15 × 3 = 360` calls.
- Exact 24-item repeat: `1,080` calls.
- 24-item held-out wrapper paraphrase: `1,080` calls.
- Planned total before transport retries: `6,840` calls.
- Hard operational ceiling: approximately `7,800` calls.
- Token envelope: approximately 4–6M input and <1M output.
- Proposed budget: USD 250, with ≤USD 60 full-run preflight per model.

### Sample plan

- 24 development/calibration families and 96 held-out confirmatory families.
- Equal confirmatory allocation across closed-world logic and quantitative reasoning.
- Target at least 86 complete confirmatory families per model.
- Nominal standardized MDE: approximately 0.30 at 86 families and 0.29 at 96; this is not a power guarantee.
- Multiplicity-aware, ceiling-aware and joint-malformedness simulation remains required before execution.

### Human plan

- Approximately 240 evidence packages.
- Two independent ratings per package; third adjudicator for gating disagreements.
- 40–48 rating hours, up to 8 adjudication hours, and 50–75 construction/rework hours.
- Estimated total: approximately 98–131 person-hours.

The plan is operationally bounded and scientifically plausible, but execution feasibility is **conditional** on money, access and people. It is not feasible for one person within the original three-day sprint.

## Owner decision requested

The revised proposal is ready for owner approval of the design direction. If the owner approves Stage 2, that approval should explicitly state:

1. whether the 15-call, 120-family plan is accepted;
2. whether the USD 250 cap and three-provider target are authorized;
3. whether the project has the required adjudication personnel and post-sprint schedule;
4. that Stage 2 begins with protocol, simulation and design audit—not main model execution.

The owner subsequently granted limited Stage-2 authorization for protocol development, statistical validation, adjudication planning, independent design auditing and readiness assessment. Main execution remains unauthorized.

## Evidence and artifacts

- `research/research_proposal.md`
- `research/novelty_assessment.md`
- `research/related_work.md`
- `research/closest_work_matrix.md`
- `research/source_register.csv`
- `audits/discovery_audit.md`
- `audits/aris_stage1_design_review_20261115.md`
- `audits/ars_stage1_checkpoint1_20261115.md`
- `audits/raw/ars_stage1_checkpoint1_round1.md`
- `audits/raw/ars_stage1_checkpoint1_round2.md`
- `.aris/traces/research-review/2026-11-15_run01/`
- `docs/project_state_report.md`
