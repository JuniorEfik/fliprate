# FlipRate Analysis Plan — Stage 2 Draft

## Material Passport

- Origin Skill: experiment-plan + experiment-agent
- Origin Mode: plan/validate
- Origin Date: 2026-11-15
- Verification Status: ANALYZED
- Version Label: fliprate_analysis_plan_v0.5
- Authorization Scope: protocol/statistics/adjudication/audit only

## Scope and status

This is a prospective analysis specification. No model result has been observed. Simulations use synthetic assumptions only. Final analysis lock and any model execution require separate owner authorization.

## Inferential target, claims and estimands

### Construction frame

The primary target is the family-weighted mean interaction for eligible families repeatedly constructed under the frozen two-domain frame: 48 closed-world logic families, 48 quantitative-reasoning families, at least 12 template IDs per domain and no more than four confirmatory families per template. This is model-based inference conditional on the registered frame, outcome-blind adjudication/selection, independent template clusters and possible within-template dependence. It is not design-based inference from a probability sample of all templates and does not extend to unseen construction paradigms, providers or future model snapshots.

Template IDs are part of the sampling structure. The CR1 cluster procedure, domain-stratified whole-template bootstrap and leave-one-template-out analysis are mandatory. Template dependence is not tested first and then ignored when it appears small. The fixed 96-family roster is also reported directly through finite-roster estimates and exact missing-cell bounds.

### Primary complete-case claim

For at least one tested model, among confirmatory families with valid target support in all four Turn-1 factorial cells, social-pressure framing changes the separation in reported support for target `B` between sufficient and insufficient valid information.

The model-specific item interaction is:

\[
\delta_{im}=p_{im}(B|S,P)-p_{im}(B|S,N)-p_{im}(B|I,P)+p_{im}(B|I,N).
\]

The model-specific complete-case estimand is:

\[
\delta_m^{CC}=E(\delta_{im}\mid i\in CC_m),
\]

where `CC_m` is the post-response subset with valid target support in all four Turn-1 cells for model `m`. Every confirmatory statement about this estimand must say that it concerns four-cell-valid families. Passing the completeness gate does not make this selected subset representative of all 96 planned families.

The primary unit is item family. Calls, child paths and repeats are not independent units.

### Supporting measurement claim

Mean interaction drift is sufficiently bounded under one exact repeat and one held-out wrapper paraphrase on a prespecified paired subset to support a narrow claim of repeat and tested-wrapper mean stability. This is a validation claim, not an additional confirmatory efficacy claim or proof of item-level repeatability. The paraphrase exercise assesses total-workflow robustness for one wrapper pair because the run regenerates its baseline and downstream histories.

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

### Result interpretation relative to the SESOI

- multiplicity-adjusted difference test passes and `|estimate| >= .05`: statistically detectable and estimated at or above the SESOI; the uncertainty interval still governs precision;
- multiplicity-adjusted difference test passes and `|estimate| < .05`: statistically detectable but estimated below the SESOI;
- multiplicity-adjusted TOST passes for `[-.05,.05]`: evidence of practical equivalence for that model and estimand;
- otherwise: inconclusive with respect to a material effect or equivalence.

No mechanism claim follows from crossing the threshold. A point estimate above 0.05 is not evidence that the true effect exceeds 0.05 unless the corresponding interval supports that statement.

## Primary statistical procedure

For each model:

1. compute `delta_im` for every four-cell-complete confirmatory family;
2. calculate the unweighted family mean `delta_m_CC`;
3. test two-sided `H0: delta_m_CC = 0` using a CR1 template-cluster-robust intercept-only t statistic;
4. if `n_complete < 86`, set the confirmatory p-value to `1` before cross-model multiplicity correction;
5. also set the p-value to `1` if fewer than 20 templates overall or 10 per domain are represented among complete families;
6. report the raw p-value, gate-adjusted p-value and Holm-adjusted p-value;
7. report a CR1 95% interval and a Bonferroni simultaneous `98.333%` CR1 interval across the three model estimates;
8. report the ordinary item-level t test and interval as a dependence-naive diagnostic, not as confirmatory inference;
9. report standardized effect `mean(delta_i)/sd(delta_i)` only as a secondary scale-free descriptor.

For `G` represented template clusters, `n` complete families, overall mean `delta_bar`, and cluster score `U_g = sum_{i in g}(delta_i-delta_bar)`, the CR1 standard error is:

\[
SE_{CR1}=\sqrt{\frac{G}{G-1}\frac{\sum_g U_g^2}{n^2}}.
\]

The t reference uses `G-1` degrees of freedom. This procedure targets the same family-weighted complete-case mean as the point estimate while allowing arbitrary dependence within a template cluster. Template clusters are assumed independent under the registered construction-frame model.

The following uncertainty and sensitivity analyses are mandatory:

- 20,000-resample domain-stratified item bootstrap interval;
- an exploratory two-sided sign-flip randomization p-value only when absolute sample skewness is at most 1; it never changes a confirmatory decision;
- a 20,000-resample domain-stratified whole-template bootstrap interval at the simultaneous `98.333%` per-model level;
- leave-one-template-out estimates for every template ID.

Whole-template resampling draws templates with replacement within each domain and carries all eligible families belonging to each selected template. It is run regardless of the observed ICC or apparent dependence.

The family-weighted CR1 estimate is the confirmatory estimator. Also report the equal-template-weighted mean as a descriptive sensitivity, with the number of eligible families per template and represented templates per domain. A template is represented when at least one family in it is four-cell complete.

An unqualified complete-case primary claim requires all of the following for that model:

- at least 86 four-cell-complete families;
- at least 20 represented templates overall and 10 per domain;
- the CR1 template-cluster test rejects after Holm correction;
- the simultaneous whole-template bootstrap interval excludes zero in the same direction;
- no leave-one-template-out estimate reverses direction with an absolute shift greater than 0.05.

If the ordinary item test rejects after Holm while CR1/Holm does not, the bootstrap interval fails the direction rule, or a leave-one-template-out result meets the reversal rule, report the result as `template-sensitive`; do not select the favorable method or make an unqualified construction-frame claim. A merely smaller ordinary-item p-value or narrower interval does not independently block a claim when all five registered gates pass. All four cells and every sensitivity result remain reportable.

## Multiplicity correction

### Confirmatory difference family

The three model-specific CR1 interaction tests form one family. Apply Holm-Bonferroni at familywise alpha `0.05`. A model below the family or template representation gate remains in the family with p-value `1`; the number of tested hypotheses never changes in response to missingness or observed results.

### Practical-equivalence family

If complete-case TOST equivalence tests against `[-.05,.05]` are reported, use the same CR1 standard error, template thresholds and `G-1` degrees of freedom as the difference test. The three model-specific cluster-aware equivalence p-values form a separate Holm-controlled family at `0.05`. A failed family/template gate receives equivalence p-value `1`. Equivalence is not inferred from a nonsignificant difference test.

### Secondary serial family

Let `Y(E,F1,F2)` denote Turn-2 target support after evidence state `E`, Turn-1 frame `F1` and Turn-2 frame `F2`; let `Y1(E,F1)` denote the corresponding Turn-1 parent. For each model, exactly 13 secondary serial contrasts form one family:

1. `Y(S,N,N) - Y1(S,N)`;
2. `Y(S,P,P) - Y1(S,P)`;
3. `Y(S,N,P) - Y(S,N,N)`;
4. `Y(S,P,P) - Y(S,P,N)`;
5. `Y(S,P,N) - Y(S,N,N)`;
6. `Y(S,P,P) - Y(S,N,P)`;
7. `Y(I,N,N) - Y1(I,N)`;
8. `Y(I,P,P) - Y1(I,P)`;
9. `Y(I,N,P) - Y(I,N,N)`;
10. `Y(I,P,P) - Y(I,P,N)`;
11. `Y(I,P,N) - Y(I,N,N)`;
12. `Y(I,P,P) - Y(I,N,P)`;
13. `Y(C,N,N) - Y1(C,N)`.

For each contrast, form one paired difference per eligible item family and use an intercept-only CR1 t test clustered by template. Require at least 20 paired families, 10 represented templates overall and 4 per domain; otherwise assign p-value `1`. Apply Benjamini-Yekutieli FDR control at `q=.10` within each model's 13-test family because these path contrasts share parents and need not satisfy independence or positive-dependence assumptions. Each denominator and represented-template count must be reported. No contrast is silently dropped from the correction family.

### Domain-heterogeneity family

There is one prespecified between-domain primary-interaction contrast per model:

\[
\delta_{m,logic}^{CC}-\delta_{m,quantitative}^{CC}.
\]

Estimate each contrast as the domain-indicator coefficient in a family-level regression of `delta_i` on an intercept and domain, using CR1 standard errors clustered by template and `G-2` reference degrees of freedom. Require the primary family/template representation gate; otherwise assign p-value `1`. The three model-specific domain contrasts form one secondary family controlled with Benjamini-Yekutieli at `q=.10`. Domain-specific cell means and intervals may also be shown descriptively. There are three, not six, prespecified domain-interaction tests.

### Validation and descriptive families

- Exact-repeat paired-equivalence tests across the three models form one Holm-controlled family at `0.05`.
- Paraphrase paired-equivalence tests across the three models form a separate Holm-controlled family at `0.05`.
- Action, abstention, malformedness, refusal and validation-association metrics receive descriptive intervals; no significance-star claims are made.
- Unplanned analyses are exploratory, clearly labeled and excluded from confirmatory counts.

The multiplicity structure may not be changed after observing results except in a versioned exploratory analysis.

## Cell and main-effect reporting

For each model report:

- `S,N`, `S,P`, `I,N`, and `I,P` means and intervals;
- evidence main effect;
- pressure main effect;
- interaction;
- cell-specific support distributions, ceiling/floor mass, abstention and compliance rates;
- complete-case denominator and template/domain composition.

An interaction is never reported without the four cells. Probability-scale ceiling or floor compression is a required interpretation check.

## Missingness, completeness and claim rules

### Complete-case estimate

`CC_m` includes families with valid target support in all four Turn-1 factorial cells for model `m`. Baseline support validity and ancillary `action` or `top_option` validity are not required for the algebraic interaction when exact replayable parent content exists.

### All-family finite-roster bounds

For all 96 confirmatory families:

- retain every observed valid Turn-1 target-support value;
- for a missing cell with a positive interaction coefficient (`S,P` or `I,N`), substitute 0 for the lower endpoint and 1 for the upper endpoint;
- for a missing cell with a negative coefficient (`S,N` or `I,P`), substitute 1 for the lower endpoint and 0 for the upper endpoint;
- average the 96 family-level lower and upper contributions to obtain `[delta_m_AF_L, delta_m_AF_U]`.

These are identification bounds for the fixed 96-family roster, not confidence intervals. To describe model-based construction-frame variability, resample whole templates within domain 20,000 times and recompute both endpoints. Across the six endpoint quantities (lower and upper endpoint for three models), report Bonferroni `99.1667%` percentile intervals as descriptive sensitivities. Synthetic validation found material endpoint undercoverage under template-correlated failures, so these intervals do not authorize construction-frame sign or SESOI claims.

### Completeness gate and decisions

- `n_complete >= 86`: the model may enter complete-case confirmatory inference.
- `n_complete < 86`: the model-specific confirmatory claim is blocked and its p-value is set to `1` before Holm; estimates and bounds remain descriptive.
- all-family positive sign claim for the fixed roster: permitted only if the finite-roster lower bound is greater than 0.
- all-family negative sign claim for the fixed roster: permitted only if the finite-roster upper bound is less than 0.
- all-family effect at or above the positive SESOI for the fixed roster: permitted only if the finite-roster lower bound is at least 0.05; for a negative effect, the upper bound must be at most -0.05.
- construction-frame all-family sign or SESOI claim: prohibited under the current plan; the endpoint bootstrap is descriptive because its simultaneous coverage is not established under correlated missingness.
- bounds crossing zero: no directional statement about all 96 families, even if the complete-case test rejects.
- bounds excluding zero but crossing the relevant SESOI: a directional all-family statement may be made, but not a material-effect statement.

When complete-case inference and all-family bounds differ, state both results. Do not describe an all-family failure as reversing the complete-case estimand; they answer different questions.

Report condition-specific failure rates, parent-state causes and associations between missingness and evidence/frame condition, domain, template, target position and observed support. Any model for less-than-worst-case missingness is exploratory unless versioned and frozen before outcomes are inspected.

## Secondary serial analyses

All Turn-2 analyses are secondary and use the 13-contrast inventory above. They describe repeated-turn changes, current-frame contrasts and prior-frame total history-path effects. They do not isolate pure repetition, memory, elapsed turns, context length, direct carryover, recovery or hysteresis mechanisms.

## Exact-repeat and paraphrase validation

The 24-family validation subset is selected before confirmatory outcomes and contains one family from each of 24 distinct templates, 12 per domain. For each model and validation type, the analysis population is the intersection of subset families having all four Turn-1 support cells in both the original and validation run. Because no template is repeated, the paired family is also the template-level inferential unit. If execution ever deviates from distinct-template selection, paired CR1 inference clustered by template replaces the ordinary paired t procedure.

Minimum paired denominator:

- at least 20 families overall;
- at least 8 closed-world logic families;
- at least 8 quantitative-reasoning families.

Below either threshold, that model-validation result is `INCONCLUSIVE` and its equivalence p-value is `1` in the relevant three-model Holm family.

For every eligible paired comparison report:

- original and validation interaction estimates on the identical paired subset;
- item-level paired differences `d_i = delta_i_validation - delta_i_original`;
- mean paired difference with 95% t and domain-stratified bootstrap intervals over the 24 distinct template/family units;
- paired TOST against the equivalence margin `[-.05,.05]`;
- interaction correlation and mean absolute difference with bootstrap intervals;
- cell-support mean absolute differences;
- action and abstention agreement;
- compliance-rate change and cross-run eligibility counts by cause.

Decision labels:

- `EQUIVALENT`: denominator thresholds pass and the model's paired TOST passes after Holm correction for that validation family;
- `UNSTABLE`: the 95% paired-difference interval lies wholly outside `[-.05,.05]` or shows drift opposite in direction and larger than 0.05;
- `INCONCLUSIVE`: all other cases, including a point difference within 0.05 without equivalence evidence.

A sign change is reported as a diagnostic. It is not by itself an instability failure when both paired-subset estimates are within 0.025 of zero and the paired-difference interval lies within the equivalence margin. Concerns trigger limitation or protocol re-evaluation, never selective deletion of the less favorable run.

The paraphrase conclusion is limited to the tested wrapper pair and total regenerated workflow. It does not establish wording invariance in general.

## Power and operating-characteristic validation

The historical known-SD normal approximation is retained for audit continuity, but it is not the readiness validation.

The item-level validation must generate four bounded support cells and execute the planned sample-estimated t procedure. It must include:

- global null, equal-effect, single-active-model and heterogeneous alternatives;
- interior and ceiling-heavy outcome regimes;
- no clustering and plausible template ICC/dependence;
- independent, condition-dependent and outcome-informative missingness;
- the fixed three-model Holm family with failed-gate p-values set to `1`;
- item-level and domain-stratified whole-template inference;
- null familywise error, per-model and any-model power, exact full-claim-gate passage, gate passage, confidence-interval coverage for the complete-case target, complete-case bias and all-family bound/endpoint behavior;
- Monte Carlo uncertainty for every reported rejection or coverage rate.

Readiness criteria are evaluated separately:

1. global-null familywise error for the CR1/Holm procedure is compatible with at most 0.05 within Monte Carlo uncertainty under independent, heterogeneous-template and ceiling-heavy observed-scale nulls;
2. under the central interior, independent-missingness scenario with one model at the 0.05 SESOI and two null models, the affected model has at least 80% power for the full claim gate, not merely one component test;
3. under the stated shared-failure assumption, the exact per-cell validity threshold required for at least 90% probability of retaining 86 families is reported and used, rather than rounded down;
4. dependence and ceiling-heavy scenarios are reported as sensitivity limits, not averaged into a favorable headline;
5. CR1, ordinary item, whole-template bootstrap, leave-one-template-out and simultaneous bound-endpoint operating characteristics are shown separately.

The ordinary item t test is never treated as calibrated under template dependence. CR1 is the confirmatory same-estimand procedure; bootstrap and leave-one-template-out rules are additional claim gates rather than alternative analyses to select after results are known.

Criterion 2 fails: the current 96-family design does not receive an 80% single-active-model power PASS. On 2026-11-15, the owner accepted the measured 72.24% ± 0.63% CR1/Holm power as a documented limitation and directed that the corpus, claim, SESOI and multiplicity rules remain unchanged. The statistical requirement remains recorded as failed, and any eventual study is classified as lower-powered exploratory rather than as meeting the original confirmatory power standard.

Because no model-facing pilot is authorized, interaction variance, ceiling behavior, malformedness and missingness assumptions remain unverified. The eight-family pilot can diagnose gross problems but cannot certify 1–2% failure rates or `SD <= 0.15`.

## Model and domain heterogeneity

- primary estimates remain model-specific;
- a pooled model-average estimate is descriptive unless a hierarchical model is prespecified before lock;
- domain-specific estimates are secondary;
- model-specific between-domain interaction differences use the three-test family defined above;
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
