# FlipRate Analysis Plan — Stage 2 Draft

## Material Passport

- Origin Skill: experiment-plan + experiment-agent
- Origin Mode: plan/validate
- Origin Date: 2026-11-15
- Verification Status: ANALYZED
- Version Label: fliprate_analysis_plan_v0.2

## Scope and status

This is a prospective analysis specification. No model result has been observed. Simulations use synthetic assumptions only. Final analysis lock and confirmatory execution require separate owner authorization.

## Claims and estimands

### Primary claim

For at least one tested model, social-pressure framing changes the Turn-1 separation in reported support for target `B` between sufficient and insufficient valid information.

The model-specific item interaction is:

\[
\delta_{im}=p_{im}(B|S,P)-p_{im}(B|S,N)-p_{im}(B|I,P)+p_{im}(B|I,N).
\]

The model-specific complete-case estimand is:

\[
\delta_m^{CC}=E(\delta_{im}|i\in CC_m).
\]

The primary unit is item family. Calls, child paths and repeats are not independent units.

### Supporting measurement claim

The sign and approximate magnitude of the interaction is sufficiently stable under one exact repeat and one held-out wrapper paraphrase on the prespecified 24-item subset to justify interpreting it as more than a single-run wording artifact.

This is a validation claim, not an additional confirmatory efficacy claim.

## Raw-scale smallest effect of scientific interest

The prospective SESOI is:

\[
|\delta_m|=0.05
\]

or five absolute percentage points on the 0–1 reported-support scale.

Rationale:

- it is directly interpretable on the benchmark's primary raw scale;
- it is large enough to represent a visible change in the separation between sufficient and insufficient information;
- smaller effects are unlikely to justify broad measurement claims given prompt and provider variability;
- it is chosen before model results and is not derived from observed treatment data.

The 0.05 value is a measurement-policy threshold, not an established community standard. Results below it remain reportable.

### Result interpretation relative to SESOI

- `Holm p < .05`, `|estimate| >= .05`: statistically detectable and estimated at or above the SESOI; uncertainty interval still governs precision.
- `Holm p < .05`, `|estimate| < .05`: statistically detectable but estimated below the SESOI.
- multiplicity-adjusted equivalence test passes for `[-.05,.05]`: evidence of practical equivalence for that model.
- otherwise: inconclusive with respect to material effect or equivalence.

No mechanism claim follows from crossing the threshold.

## Primary statistical test

For each model:

1. compute `delta_im` for every four-cell-complete confirmatory family;
2. calculate the unweighted mean and standard error across item families;
3. test two-sided `H0: delta_m_CC = 0` using a one-sample t statistic;
4. report exact unadjusted and Holm-adjusted p-values;
5. report an ordinary 95% t interval and a Bonferroni simultaneous `98.333%` interval across the three model estimates;
6. report standardized effect `mean(delta_i)/sd(delta_i)` only as a secondary scale-free descriptor.

The t procedure is used because the estimand is a mean over at least 86 bounded item-level contrasts. It is accompanied by:

- 20,000-resample domain-stratified item bootstrap interval;
- two-sided item sign-flip randomization p-value when the item-level distribution is sufficiently symmetric;
- leave-one-template-out estimates;
- template-cluster bootstrap sensitivity if template reuse produces material dependence.

If robustness procedures materially disagree, the result is labeled sensitivity-dependent rather than selecting the favorable method.

## Multiplicity correction

### Confirmatory family

The three model-specific primary interaction tests form one family. Apply Holm-Bonferroni at familywise alpha `0.05`.

This preserves model-specific inference while controlling the probability of any false primary rejection across the three models.

### Practical-equivalence family

If TOST equivalence tests against `[-.05,.05]` are reported, the three model-specific equivalence p-values form a separate Holm-controlled family at `0.05`. Equivalence is not inferred from a nonsignificant difference test.

### Secondary families

- Turn-2 support contrasts: Benjamini-Hochberg FDR `q=.10` within each model across the prespecified serial contrasts.
- Domain interactions: BH `q=.10` across the six model × domain-interaction tests.
- Action, abstention, malformedness and validation metrics: descriptive intervals; no significance-star claims.
- Unplanned analyses: exploratory, clearly labeled, and excluded from confirmatory counts.

The multiplicity structure may not be changed after observing results except in a versioned exploratory analysis.

## Cell and main-effect reporting

For each model report:

- `S,N`, `S,P`, `I,N`, and `I,P` means and intervals;
- evidence main effect;
- pressure main effect;
- interaction;
- cell-specific support distributions, abstention and compliance rates;
- denominator and template/domain composition.

An interaction is never reported without the four cells.

## Missingness and completeness

### Complete-case estimate

`CC_m` includes families with valid support in all four Turn-1 factorial cells for model `m`. Baseline validity is not required for the algebraic interaction.

### All-family bounds

For all 96 families:

- retain every observed Turn-1 support value;
- replace only undefined target-support values by 0 or 1 in the combination minimizing or maximizing the item interaction;
- average with denominator 96 to obtain `[delta_m_AF_L, delta_m_AF_U]`.

### Completeness gate

- `n_complete >= 86`: confirmatory completeness gate passes.
- `n_complete < 86`: model-specific confirmatory claim is blocked; estimate and bounds remain descriptive.

Report condition-specific failure rates and whether missingness is associated with evidence/frame condition, domain, template or target position.

## Secondary serial analyses

All Turn-2 analyses are secondary.

- constant-neutral repeated-turn change;
- constant-pressure repeated-turn change;
- current-pressure contrast after neutral history;
- current-pressure contrast after pressure history;
- prior-pressure total effect under current neutral;
- prior-pressure total effect under current pressure;
- no-evidence control trajectory.

Interpret these as path/history contrasts. They do not isolate pure repetition, memory or direct carryover mechanisms.

## Reliability and paraphrase validation

The 24-item subset is selected before confirmatory outcomes.

### Exact repeat criteria

Report exact values for:

- model-level interaction difference;
- item interaction correlation and mean absolute difference;
- cell-support mean absolute difference;
- action and abstention agreement;
- compliance-rate change.

No hard universal reliability cutoff is asserted. A design-readiness concern is triggered if the exact-repeat model-level interaction changes sign or differs by more than 0.05.

### Paraphrase criteria

A wording-robustness concern is triggered if:

- model-level interaction changes sign;
- original versus paraphrase difference exceeds 0.05;
- the result crosses from above to below the SESOI solely under paraphrase;
- cell-level changes indicate the manipulation no longer isolates the intended frame.

Concerns trigger limitation or protocol re-evaluation, not selective deletion of the less favorable run.

## Power plan

The simulations vary:

- true raw interaction: `0`, `0.03`, `0.05`, `0.07`, `0.10`;
- item-level interaction SD: `0.10`, `0.15`, `0.20`, `0.25`;
- completeness scenarios combining shared item failure and per-cell failure;
- three Holm-corrected model tests;
- 96 starting families and the 86-family gate.

Central planning scenario:

- raw effect `0.05`;
- item interaction SD `0.15`;
- per-cell malformed probability `1%`;
- shared item failure `1%`;
- three models with the same planning effect.

Readiness target: at least 80% average model-specific Holm-adjusted power and at least 90% probability of retaining 86 or more complete families in the central scenario.

For planning, a simulated rejection counts as confirmatory power only when that simulated model also passes the 86-family completeness gate. The simulation reports raw rejection, gate-qualified rejection and power conditional on gate passage separately.

Because no model-facing pilot is authorized, the SD and malformedness assumptions are unverified. Simulation can establish conditional feasibility, not actual power.

## Model and domain heterogeneity

- primary estimates remain model-specific;
- a pooled model-average estimate is descriptive unless a hierarchical model is prespecified before lock;
- domain-specific estimates are secondary;
- model × domain interactions are exploratory with BH correction;
- cross-model ranking requires overlapping item populations and is not a primary claim.

## Statistical fallacy and integrity checks

The final analysis must explicitly check:

- selection/survivorship bias from four-cell completeness;
- look-elsewhere effects and forking paths;
- ecological inference from model-family averages to individual outputs;
- ceiling/floor compression on the raw support scale;
- regression to the mean in repeat subsets;
- post-treatment exclusion;
- causal overstatement from behavioral prompt effects;
- p-value/effect-size mismatch;
- multiple-comparison control;
- sensitivity to template clustering;
- selective reporting of models, domains or runs.

All null, mixed and negative outcomes remain in scope.
