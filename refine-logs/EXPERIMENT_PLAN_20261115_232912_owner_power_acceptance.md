# Experiment Plan

**Problem:** Validate whether social-pressure framing changes LLM discrimination between sufficient and insufficient valid information across repeated interactions.  
**Method Thesis:** A shared-parent 15-call factorial tree can estimate model-specific pressure × sufficiency interactions while separating first-exposure effects from secondary history-path contrasts.  
**Date:** 2026-11-15  
**Status:** Stage-2 design and power disposition closed; lower-powered exploratory study preserved; execution-readiness prerequisites remain blocked

## Claim Map

| Claim | Why It Matters | Minimum Convincing Evidence | Linked Blocks |
|---|---|---|---|
| C1: Pressure changes sufficiency discrimination among four-cell-valid families for a tested model. | This is the primary measurement claim. | At least 86 complete families and 20 represented templates, CR1/Holm rejection, a same-direction simultaneous whole-template interval, stable leave-one-template-out estimates, all-family bounds and full cell reporting. | B1, B2, B4 |
| C2: Mean interaction drift is bounded under one repeat and one tested wrapper pair. | A measurement instrument needs scoped stability evidence. | Paired original/validation population of at least 20 families and 8/domain, Holm-controlled TOST against ±0.05, plus transparent item-level correlation/MAD diagnostics that are not implied by mean equivalence. | B3 |
| Anti-claim: FlipRate identifies latent beliefs or a pure psychological mechanism. | The benchmark observes outputs and bundled framing. | Explicit scope limits, no mechanism inference, all four cells and serial-path limitations reported. | B1–B5 |

## Experimental Storyline

- Main result must distinguish the four-cell-valid complete-case estimand from the fixed 96-family roster and construction-frame sensitivities.
- The overall study is lower-powered exploratory because the accepted 72.24% ± 0.63% CR1/Holm power does not meet the original 80% standard; prospective procedures remain unchanged.
- An unqualified construction-frame result uses the family-weighted CR1/Holm test for the primary estimand plus a same-direction simultaneous whole-template interval and leave-one-template-out stability; sensitivity disagreement is labeled `template-sensitive`.
- Validation uses identical paired subsets and equivalence intervals; a small point drift alone does not establish stability.
- Secondary serial analyses may describe current-frame and prior-frame path contrasts, but not recovery, hysteresis or pure memory mechanisms.
- Invalid/irrelevant evidence, authority-versus-confidence separation and broad cross-model rankings are intentionally cut from the authorized design.

## Experiment Blocks

### B0: Corpus and adjudication qualification

- Claim tested: the instrument's `S/I` labels and baseline warrant states are defensible.
- Dataset/task: 24 development and 96 confirmatory closed-world logic/quantitative families.
- Compared systems: independent Reviewer A/B classifications with C adjudication.
- Metrics: gating pass rates, agreement, witness/uniqueness validity, revision and rejection counts.
- Success criterion: 120 accepted families, no unresolved uncertainty, calibration passed, confirmatory roster frozen before model execution.
- Failure interpretation: the measurement instrument is not ready; no model run may begin.
- Priority: MUST-RUN, but personnel-dependent and currently blocked.

### B1: Confirmatory Turn-1 factorial

- Claim tested: C1.
- Dataset/task: 96 confirmatory families, 48 per domain, three owner-approved model snapshots.
- Compared conditions: `S-N`, `S-P`, `I-N`, `I-P` from one exact baseline parent.
- Primary metric: `delta_m_CC = mean[p(B|S,P)-p(B|S,N)-p(B|I,P)+p(B|I,N)]`.
- Companion metrics: four cells, main effects, abstention, action and compliance.
- Success criterion: at least 86 complete families, 20 represented templates overall and 10 per domain; failed-gate models remain in Holm with p-value 1; the CR1/Holm test rejects, the simultaneous whole-template interval excludes zero in the same direction, and no leave-one-template-out estimate meets the reversal rule; estimates and intervals are reported relative to the 0.05 SESOI.
- Failure interpretation: below-gate models are blocked; disagreement between CR1 and mandatory template sensitivities is `template-sensitive`; null or sub-SESOI estimates remain reportable.
- Priority: MUST-RUN after a future explicit authorization.

### B2: Missingness and robustness

- Claim tested: C1 is not an artifact of silent post-response exclusion or one template.
- Analyses: exact 96-family worst-case bounds, descriptive endpoint template bootstrap, condition-specific failure rates, domain-stratified item bootstrap, sign-flip sensitivity, equal-template descriptive estimate, whole-template bootstrap and leave-one-template-out estimates.
- Success criterion: any all-family sign or SESOI claim satisfies the exact finite-roster bound thresholds in the analysis plan; construction-frame endpoint intervals stay descriptive, and CR1/template-sensitivity disagreements are disclosed as `template-sensitive`.
- Failure interpretation: narrow or withdraw the confirmatory claim.
- Priority: MUST-RUN.

### B3: Repeat and paraphrase validation

- Claim tested: C2.
- Dataset/task: prespecified 24-family subset with one family from each of 24 distinct templates and 12 per domain, one exact full repeat and one held-out wrapper paraphrase.
- Metrics: paired interaction difference and interval, Holm-controlled TOST, item correlation/MAD, cell MAD, action/abstention agreement and compliance change.
- Success criterion: at least 20 paired families and 8/domain; adjusted TOST passes for the model. Otherwise the result is `INCONCLUSIVE` or `UNSTABLE` under the analysis-plan rules.
- Failure interpretation: the measurement is unstable or wrapper-sensitive; no selective deletion of the unfavorable run.
- Priority: MUST-RUN for the supporting measurement claim.

### B4: Secondary serial-path analysis

- Claim tested: repeated exposure and prior/current frame are associated with different output paths.
- Compared paths: `NN`, `NP`, `PN`, `PP` within `S` and `I`, plus `C-NN`.
- Metrics: 13 enumerated Turn-2 path contrasts per model with Benjamini-Yekutieli FDR `q=.10`; three between-domain primary-interaction contrasts form a separate BY family.
- Success criterion: estimates and uncertainty reported as path/history contrasts only.
- Failure interpretation: no serial claim; primary Turn-1 result remains separable.
- Priority: MUST-RUN as descriptive secondary analysis once the main run is authorized.

### B5: Failure analysis

- Claim tested: none; diagnoses instrument boundaries.
- Analyses: malformedness, refusal, ceiling/floor compression, template dependence, domain heterogeneity and adjudication failure modes.
- Success criterion: all failure modes and exclusions are preserved and reported.
- Priority: MUST-RUN for integrity; no paper narrative is authorized.

## Run Order and Milestones

| Milestone | Goal | Runs/Work | Decision Gate | Cost | Current state |
|---|---|---|---|---|---|
| M0 | Complete protocol/audit and power disposition | Synthetic simulations and document review only | Lower power accepted as exploratory limitation; external readiness remains separate | No paid API | CLOSED — LIMITATION ACCEPTED |
| M1 | Qualify corpus and personnel | Human construction/calibration/adjudication | 120 accepted families and named team | 184–296 person-hours | BLOCKED |
| M2 | Parser/synthetic sanity | Hand-built JSON fixtures only | Deterministic validation tests pass | Local compute | NOT AUTHORIZED FOR IMPLEMENTATION |
| M3 | Authorized 8-family pilot | 360 model calls | Compliance/variance/cost preflight passes | Paid API, later approval required | BLOCKED |
| M4 | Confirmatory main | 4,320 model calls | At least 86 complete families/model | Paid API, later approval required | BLOCKED |
| M5 | Repeat/paraphrase | 2,160 model calls | Stability diagnostics complete | Paid API, later approval required | BLOCKED |
| M6 | Locked analysis | Prespecified processing only | Independent results audit | Local compute | BLOCKED ON DATA |

## Compute, Data and Human Budget

- Planned logical calls: 6,840; hard ceiling approximately 7,800.
- Token envelope: 4–6M input and less than 1M output, subject to authorized pilot measurement.
- Proposed API ceiling: USD 250; observed public prices imply economic feasibility but funding is unconfirmed.
- Human work: approximately 184–296 person-hours, excluding unexpected template-wide reopening.
- Biggest bottleneck: named adjudication personnel and empirical nuisance estimates, not local compute.

## Risks and Mitigations

- The single-active-model synthetic anchor reaches 72.24% ± 0.63% CR1/Holm power, below the original 80% standard. The owner accepted this limitation, preserved the design and directed that the study be described as lower-powered exploratory. Do not optimize the design merely to obtain a passing power label.
- Empirical interaction SD may exceed 0.15: use a future authorized development pilot diagnostically, report uncertainty, then return any tradeoff to the owner.
- With 1% shared failure, equal per-cell validity must be at least 98.3347% for 90% gate passage; improve schema clarity before lock without content retries and retain all failures.
- Template dependence makes ordinary item inference anti-conservative in the ICC 0.10 simulation: keep same-estimand CR1/Holm inference, the whole-template interval and leave-one-template-out sensitivity mandatory.
- Pressure bundles authority and confidence: keep the claim at bundled social-pressure framing.
- Social testimony can be treated as information: interpret effects behaviorally, not as proof of irrationality.
- Complete-case selection may bias estimates: report all-family bounds and condition-specific missingness.
- Human proof errors may survive agreement: retain formal witnesses, third adjudication and stratified re-audit.

## Final Checklist

- [x] Primary claim and anti-claim mapped.
- [x] SESOI and multiplicity specified.
- [x] Planned t procedure, bounded cells, template dependence, missingness and completeness simulated synthetically.
- [x] Adjudication workflow specified.
- [x] First independent ARIS protocol review complete: `REVISE`; findings incorporated.
- [x] First independent ARS methodological challenge complete: `REVISE`; findings incorporated.
- [x] Focused ARIS round-2 verification complete: `PASS WITH LIMITATIONS` via same-family provisional fallback.
- [x] Focused blind ARS round-2 verification complete: `PASS WITH LIMITATIONS` via same-family provisional fallback.
- [x] Owner accepted the below-80% power as a documented exploratory limitation; the original target remains failed.
- [ ] Named providers, budget authority and personnel confirmed.
- [ ] Owner authorizes any pilot/main execution.
