# Experiment Plan

**Problem:** Validate whether social-pressure framing changes LLM discrimination between sufficient and insufficient valid information across repeated interactions.  
**Method Thesis:** A shared-parent 15-call factorial tree can estimate model-specific pressure × sufficiency interactions while separating first-exposure effects from secondary history-path contrasts.  
**Date:** 2026-11-15  
**Status:** design plan only; execution and final prompt lock are unauthorized

## Claim Map

| Claim | Why It Matters | Minimum Convincing Evidence | Linked Blocks |
|---|---|---|---|
| C1: Pressure changes sufficiency discrimination for a tested model. | This is the primary measurement claim. | Four Turn-1 cells on at least 86 of 96 families, model-specific interaction, Holm control, all-family bounds and full cell reporting. | B1, B2, B4 |
| C2: The measured interaction is not solely a one-run or one-wrapper artifact. | A measurement instrument needs stability evidence. | Prespecified 24-family exact repeat and held-out wrapper paraphrase with transparent sign/magnitude diagnostics. | B3 |
| Anti-claim: FlipRate identifies latent beliefs or a pure psychological mechanism. | The benchmark observes outputs and bundled framing. | Explicit scope limits, no mechanism inference, all four cells and serial-path limitations reported. | B1–B5 |

## Experimental Storyline

- Main result must establish the model-specific Turn-1 sufficiency × pressure interaction with complete-case and all-family sensitivity analyses.
- Validation must establish exact-repeat and wrapper-paraphrase stability on the prespecified subset.
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
- Success criterion: at least 86 complete families per model; multiplicity-adjusted estimate and interval reported relative to the 0.05 SESOI.
- Failure interpretation: below-gate models are limited/inconclusive; null or sub-SESOI estimates remain reportable.
- Priority: MUST-RUN after a future explicit authorization.

### B2: Missingness and robustness

- Claim tested: C1 is not an artifact of silent post-response exclusion or one template.
- Analyses: 96-family worst-case bounds, condition-specific failure rates, domain-stratified bootstrap, sign-flip sensitivity, template-cluster bootstrap and leave-one-template-out estimates.
- Success criterion: conclusions are not reversed by plausible prespecified sensitivity analyses; disagreements are disclosed as sensitivity-dependent.
- Failure interpretation: narrow or withdraw the confirmatory claim.
- Priority: MUST-RUN.

### B3: Repeat and paraphrase validation

- Claim tested: C2.
- Dataset/task: prespecified 24-family subset, one exact full repeat and one held-out wrapper paraphrase.
- Metrics: model interaction difference, sign, item correlation/MAD, cell MAD, action/abstention agreement and compliance change.
- Success criterion: no sign reversal or greater-than-0.05 model-level drift without explicit limitation/re-evaluation.
- Failure interpretation: the measurement is unstable or wrapper-sensitive; no selective deletion of the unfavorable run.
- Priority: MUST-RUN for the supporting measurement claim.

### B4: Secondary serial-path analysis

- Claim tested: repeated exposure and prior/current frame are associated with different output paths.
- Compared paths: `NN`, `NP`, `PN`, `PP` within `S` and `I`, plus `C-NN`.
- Metrics: prespecified Turn-2 path contrasts with BH FDR `q=.10` within family.
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
| M0 | Complete protocol/audit | Synthetic simulations and document review only | Owner approves Stage-2 readiness | No paid API | IN PROGRESS |
| M1 | Qualify corpus and personnel | Human construction/calibration/adjudication | 120 accepted families and named team | 98–131 person-hours | BLOCKED |
| M2 | Parser/synthetic sanity | Hand-built JSON fixtures only | Deterministic validation tests pass | Local compute | NOT AUTHORIZED FOR IMPLEMENTATION |
| M3 | Authorized 8-family pilot | 360 model calls | Compliance/variance/cost preflight passes | Paid API, later approval required | BLOCKED |
| M4 | Confirmatory main | 4,320 model calls | At least 86 complete families/model | Paid API, later approval required | BLOCKED |
| M5 | Repeat/paraphrase | 2,160 model calls | Stability diagnostics complete | Paid API, later approval required | BLOCKED |
| M6 | Locked analysis | Prespecified processing only | Independent results audit | Local compute | BLOCKED ON DATA |

## Compute, Data and Human Budget

- Planned logical calls: 6,840; hard ceiling approximately 7,800.
- Token envelope: 4–6M input and less than 1M output, subject to authorized pilot measurement.
- Proposed API ceiling: USD 250; observed public prices imply economic feasibility but funding is unconfirmed.
- Human work: approximately 98–131 person-hours.
- Biggest bottleneck: named adjudication personnel and empirical nuisance estimates, not local compute.

## Risks and Mitigations

- Empirical interaction SD may exceed 0.15: use the authorized development pilot, then request an owner decision if power falls below target.
- Per-cell validity may fall below about 98%: improve schema clarity before lock without content retries; retain all failures.
- Pressure bundles authority and confidence: keep the claim at bundled social-pressure framing.
- Social testimony can be treated as information: interpret effects behaviorally, not as proof of irrationality.
- Complete-case selection may bias estimates: report all-family bounds and condition-specific missingness.
- Human proof errors may survive agreement: retain formal witnesses, third adjudication and stratified re-audit.

## Final Checklist

- [x] Primary claim and anti-claim mapped.
- [x] SESOI and multiplicity specified.
- [x] Power and completeness simulated synthetically.
- [x] Adjudication workflow specified.
- [ ] Independent ARIS protocol review complete.
- [ ] Independent ARS methodological challenge complete.
- [ ] Named providers, budget authority and personnel confirmed.
- [ ] Owner authorizes any pilot/main execution.
