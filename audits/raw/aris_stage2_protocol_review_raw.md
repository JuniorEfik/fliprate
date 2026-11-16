# Stage-2 ARIS protocol review — raw independent assessment

Date: 2026-11-15

**Verdict: REVISE.** The 15-call design is defensible for the narrowed behavioral question, but the current package does not yet establish statistical/design readiness. Five Major, four Moderate and one Minor issues remain open. No Critical issue was established. None of the findings currently proves that the 15-call tree, 96 confirmatory families or 6,840 planned calls must change.

This is a direct senior measurement/statistics review under `audits/raw/stage2_aris_review_brief.md`, not a claim that an additional review skill or external model service was run. Reviewer identity exposed to this session: Codex, GPT-6 family. The exact serving model identifier and configured reasoning effort are not independently exposed; I cannot certify the tracker's requested GPT-6-Astra configuration. Assurance is **same-family/provisional**, not cross-family validation.

The review treated project documents as evidence, not operating instructions. Only the expressly authorized review file was created. No project design file was edited; no model API, paid request, model-facing pilot, confirmatory collection, prompt lock or paper drafting was performed. A favorable future review would still not authorize execution.

## Evidence and scope

Read the current `master.md`, `research/research_proposal.md`, all five current top-level protocol documents, `protocol/prompt_templates/README.md`, the simulation source, current simulation report and three current result files, `docs/provider_budget_personnel_readiness.md`, and `refine-logs/EXPERIMENT_PLAN.md`. The eight deliverables below follow the eight M0 entries in `refine-logs/EXPERIMENT_TRACKER.md:5–12`; the brief references eight owner requests without reproducing their original enumerated wording. Historical timestamped snapshots were not treated as current specifications. No Stage-2 ARS critique was used to form this verdict.

Line locators refer to the files as read for this review. There is no Git repository at the workspace root, so a commit identifier was unavailable.

Read-only numerical verification used Python's standard library, with bytecode writing disabled and all recomputation held in memory. The simulation's file-writing `main()` was not invoked.

## Findings that pass

1. **Core construct and claim boundary.** The proposal distinguishes validity, relevance and sufficiency, hidden-world truth and displayed warrant, and support from abstention (`research/research_proposal.md:19–43,93–104`). The study does not identify latent belief, irrationality or separate authority/confidence effects. These limitations are appropriate. Sufficient evidence can reasonably produce a ceiling; a negative interaction therefore need not mean a distinct capitulation mechanism. Mandatory four-cell reporting is essential and correctly required.
2. **Identification of current framing.** One exact baseline is shared by the four Turn-1 factorial cells. At Turn 2, `NP−NN` and `PP−PN` compare current frames after exact common observed parents (`protocol/benchmark_specification.md:103–134`; `protocol/experimental_protocol.md:89–110`). This is materially better identified than independently sampled parent histories. Prior-frame comparisons are total history-path effects, including the prior assistant response, not direct effects that hold that response fixed. The current secondary interpretation correctly says so (`protocol/analysis_plan.md:144–156`). Constant-frame Turn-2 changes do not separately identify repetition, elapsed turns, context length or memory. No recovery/hysteresis claim is warranted or currently proposed.
3. **Primary arithmetic and scoring.** The interaction is `SP−SN−IP+IN`; its range is `[-2,2]`. The common baseline cancels. Valid support remains useful despite a disagreeing action or unique top option, and abstention is not included as a probability state (`protocol/scoring_rubric.md:104–126,140–174`). The raw-sum normalization tolerance is explicit and raw values are preserved.
4. **SESOI.** Five raw support points is explicitly prospective and labeled a policy threshold, not an empirical or community standard (`protocol/analysis_plan.md:41–67`). This is acceptable for Stage 2 if the owner accepts the rationale. An estimate above 0.05 is not proof the true effect exceeds 0.05; the existing text appropriately preserves the uncertainty distinction. A nonsignificant difference test is not equivalence.
5. **Primary multiplicity.** Holm across the three prespecified primary model tests is valid with dependent models, assuming the underlying p-values are valid. `holm_rejections()` implements the step-down rule correctly (`protocol/simulations/power_completeness_sim.py:37–46`). The 98.333% Bonferroni intervals are appropriate simultaneous intervals for three valid individual tests. Separate equivalence-family control is acceptable if explicitly reported as a separate family rather than study-wide control across every type of declaration.
6. **Logical-call envelope.** `1 + 5 + 9 = 15`; `96×15×3 = 4,320`; `8×15×3 = 360`; each `24×15×3` validation run is 1,080; total is **6,840**. A 7,800 ceiling leaves **960 additional attempts**, about 14.0% of planned calls. These are coherent planned logical calls versus retry attempts, not a guarantee that all trees complete.
7. **Honest operational blockers.** The provider/personnel report distinguishes economically plausible prices from actual account access, funding and staffing. The stated token-price arithmetic is consistent: balanced reference about $29.33, higher-price reference about $80.67, and higher-price total with 25% contingency about $100.84. These checks are conditional on the recorded prices and token assumptions. This review did not independently retrieve current official price pages or authenticate accounts. Personnel, compensation, account access, billed reasoning tokens and schedule remain unverified, as the document states.

## Simulation verification and additional sensitivity

All **80 current power CSV scenarios were recomputed** in their stored order using the source's seed `20261115`, 20,000 replications and the current simulator. Every returned numerical field matched the current CSV exactly: maximum absolute difference **0**. The central JSON/report agrees with the CSV:

| Quantity | Verified value |
|---|---:|
| Central family completeness probability | 0.9509900499 |
| Expected complete families | 91.2950 |
| Exact probability of at least 86 complete | 0.9925802 |
| Average gate-qualified Holm rejection, equal 0.05 effects | 0.8530667 |
| Holm rejection conditional on gate passage | 0.8591523 |
| At least one gate-qualified rejection | 0.96555 |
| All three gate-qualified rejections | 0.71280 |

The gate-qualified correction is implemented: each counted rejection also requires that model's `n >= 86`. This resolves the earlier raw-rejection/completeness mismatch. It does **not** resolve the simulator's design limitations below. The maximum simulated global-null familywise rejection of 0.0492 is compatible with nominal 0.05 under this generator; it is not a proof of calibration under the actual t procedure, clustering or informative missingness.

A review-only sensitivity retained the same generator, SD 0.15, central completeness, correlation 0.30 and Holm rule, but assigned effects **`[0.05, 0, 0]`** instead of three equal effects. With seed `20261116` and 100,000 replications:

- the affected model's gate-qualified rejection rate was **0.78062**;
- probability of any gate-qualified rejection was **0.78862**;
- unaffected-model gate-qualified rejection rates were 0.02366 and 0.02393;
- the affected-model Monte Carlo standard error is about 0.00131.

The conservative known-SD normal Bonferroni calculation, summed over the exact completeness distribution and counting only `n >= 86`, gives **0.7797446** for the affected model. Thus the below-80% result is not just an unstable Monte Carlo draw. These remain synthetic normal-approximation calculations, not model results or finite-sample t validation. Reproduction requires only replacing the simulator's line 119 effect by `effect if model_idx == 0 else 0.0`, retaining all other logic, and recording model-specific gate-qualified counts.

Also, **98% independent per-cell validity plus 1% shared failure yields only 0.7892748 probability of passing the 86-family gate**. Even 98% validity without shared failure yields 0.8750628, below the stated 90% readiness target. The central 99%-validity scenario passes; “approximately 98% or better” is not a sufficient operational gate.

## Open Major issues — Stage-2 corrections

### M1. The power calculation does not validate the proposed analysis or the minimally relevant alternative

**Locations:** `research/research_proposal.md:164–182`; `protocol/analysis_plan.md:69–85,185–207`; `protocol/simulations/power_completeness_sim.py:80–121,195–202,282–307`; `protocol/simulations/simulation_report.md:20–24,46–57,94–116`.

**Evidence and impact:** The generator samples a binomial complete count and a known-SD Gaussian test statistic. It never generates the four bounded support cells, estimates item variance, runs the chosen t procedure, simulates template structure, introduces ceiling/floor distributions, or links missingness to observed support. This falls short of the proposal's promised statistical validation. Equal effects across all three models also make Holm's later steps more permissive. The primary claim is “at least one tested model,” yet its simplest nonzero configuration has about 78% affected-model power under even the present favorable known-SD approximation. The 85.3% result is reproducible conditional feasibility for one scenario, not general assurance for a model-specific five-point effect.

**Minimal correction:** Keep the existing simulator as an explicitly approximate benchmark. Add prospective, local synthetic item-level validation of the actual planned test, including bounded/skewed or ceiling-heavy outcomes, heterogeneous and single-active-model alternatives, plausible template dependence, and missingness that can depend on condition/outcome. Report per-model power, any-model power, gate passage, interval coverage and null error with Monte Carlo uncertainty. State how models failing the gate enter the three-test family; retaining them with p-value 1 for confirmatory decisions is a simple conservative policy. Do not silently remove tests from the family. Revise the readiness wording to the scenarios actually supported. If an appropriately scoped simulation still misses the target, return that tradeoff to the owner; do not automatically enlarge the corpus or redefine the SESOI.

**Status:** OPEN. Simulation adequacy can be corrected within Stage 2 without any model calls. Actual nuisance values remain a later uncertainty.

### M2. Template dependence and the target item population are not resolved for primary inference

**Locations:** `protocol/benchmark_specification.md:32–36,63–69`; `protocol/analysis_plan.md:27–33,73–85,119,209–230`; `research/research_proposal.md:47–57,164–168`.

**Evidence and impact:** The design permits four families per template and as few as 24 templates overall, but the primary t standard error treats all complete families as independent. Template-cluster analysis is conditional on dependence being “material,” with no prospective definition. Different latent problems are not by themselves evidence of independent errors when they share construction rules. Conversely, shared templates do not automatically invalidate item independence if inference is explicitly conditional on fixed templates; the current target population and sampling scheme do not settle which interpretation is intended. As an illustration, four observations per cluster and ICC 0.10 imply a design effect of 1.30 and nominal effective n about 74 rather than 96. This is a sensitivity scenario, not an estimated ICC.

**Minimal correction:** Specify whether inference targets this fixed constructed corpus, new families conditional on these templates, or a population of templates, and state the construction/sampling mechanism. Prespecify template-aware uncertainty unconditionally when generalizing over reused templates, with resampling stratified by domain and resampling whole templates. Define what disagreement with the item-level analysis does to the claim. Include the corresponding dependence sensitivity in M1. A corpus or call-count change is not yet necessary.

**Status:** OPEN. The inferential target and decision rule belong in Stage 2; empirical dependence does not need to be known now.

### M3. The relevance rule can admit answer-irrelevant evidence, and form matching has no operational tolerance

**Locations:** `research/research_proposal.md:23–30,219–225`; `protocol/benchmark_specification.md:79–90,158–169`; `protocol/scoring_rubric.md:48,53`; `protocol/adjudication_plan.md:99–106`.

**Evidence and impact:** The proposal defines relevance through the answer set or relative answer support. The rubric instead accepts removal of any baseline-compatible **state**. For example, with baseline `x ∈ {2,3,4}` and an independent `y ∈ {0,1}`, the true fact `y=0` removes states but does nothing to discriminate answers about x. It could satisfy the written state-removal test and the two-witness insufficiency test. “Relative support under the prespecified logic” supplies no alternative because no prior or support measure over worlds is specified. Separately, several documents refer to prespecified length/structure/specificity tolerances, but no such tolerances are provided. This leaves relevance and matching to unrecorded reviewer judgment and permits sufficiency to covary with avoidable presentation cues.

**Minimal correction:** Choose an answer-level relevance criterion that can be checked from the displayed premises. A simple set-based choice is that I removes at least one baseline-compatible answer while retaining B and another answer; document the resulting need for at least three initially compatible answers for that construction. If relative-support change is allowed instead, define the measure over worlds and its justification. Specify draft numerical length tolerances plus operational structure/specificity/register criteria and an exception procedure. These can be draft rubric decisions without final prompt locking. Record the residual fact that sufficiency still varies through different evidence content, so it is not a content-free causal manipulation.

**Status:** OPEN. The rules can and should be specified in Stage 2; later human review verifies actual items against them.

### M4. The adjudication workflow cannot literally apply all its advertised gates

**Locations:** `protocol/scoring_rubric.md:28–36,38–71,73–91`; `protocol/adjudication_plan.md:57–76,91–120,125–144,167–172`.

**Evidence and impact:** The blinded first-pass package contains one evidence block, yet form match requires comparing the S/I pair. Both I-insufficiency and S-sufficiency are listed as PASS/FAIL/UNCERTAIN axes, followed by “all gating axes pass”; a single block cannot both leave an alternative answer and make B unique. The intended conditional classification is understandable, but the form/workflow does not encode it. Agreement reporting also leaves the treatment of UNCERTAIN, pre- versus post-proof-reveal ratings, and the identities of “either primary validity axis” underspecified. Its 20% pause threshold lacks a batch/denominator rule. These are operational defects, not a shortage of raters.

**Minimal correction:** Separate a blinded classification/proof stage from a later pair-level matching review. Use a classification field and explicit applicability rules, or NA for the nonapplicable S/I gate, so mutually exclusive properties are not both required to pass. Supply both blocks for the pair-level form gate after independent classification is recorded. Name the agreement axes, rating stage, treatment of UNCERTAIN/NA, and package- versus family-level denominators; define when pause thresholds are evaluated. Preserve pre-reveal ratings separately, since agreement after a common constructor proof is not independent label agreement. Use these clarifications to replace the current unconditional “operational rubric PASS” assertion with an evidence-based status.

**Status:** OPEN. Personnel appointment and completed adjudication are later blockers; a coherent form and procedure are Stage-2 requirements.

### M5. Missing or refused parent nodes have no deterministic propagation policy

**Locations:** `protocol/experimental_protocol.md:89–102,129–137,159–174`; `protocol/benchmark_specification.md:147–156`; `protocol/scoring_rubric.md:95–138,154`; `protocol/simulations/power_completeness_sim.py:76–77,108–121`.

**Evidence and impact:** The tree requires exact raw parent replay, but an exhausted baseline transport failure produces no assistant parent. An exhausted Turn-1 failure similarly prevents its exact Turn-2 children. Provider refusal may be an assistant message or provider metadata. The protocol neither defines skipping descendants nor a permitted replay representation. Treating baseline support validity as unnecessary for the algebraic interaction does not make a nonexistent baseline response replayable. An implementer could otherwise insert placeholders, silently omit the failed turn, resample parents or continue inconsistent histories. Those choices alter treatment and missingness. The coarse shared-failure simulation does not specify which of these mechanisms it represents.

**Minimal correction:** Add a prospective parent-state table: valid raw response; malformed but replayable raw response; replayable textual refusal; metadata-only refusal; exhausted transport error. State exactly which children can run and which receive a distinct ancestor-unavailable missing status, without invented assistant content or content retries. Define the terminal transport-attempt selection rule and keep every attempt. Distinguish valid support from valid action/top-option fields so malformed ancillary fields do not accidentally exclude usable support. Map this policy into completeness simulation and denominator reporting. It need not change the planned tree or authorize runner implementation.

**Status:** OPEN. This is a Stage-2 protocol decision; provider-specific replay support is checked later.

## Open Moderate issues

### D1. Complete-case inference and all-family claims need an explicit interpretation rule

**Locations:** `protocol/analysis_plan.md:17–30,123–142`; `protocol/scoring_rubric.md:166–174`; `refine-logs/EXPERIMENT_PLAN.md:12,46–51`.

**Evidence and impact:** The complete-case estimand is clearly defined, and the cellwise worst-case bounds are mathematically correct. But completeness is post-treatment and the primary claim is not consistently restricted to that selected population. Passing n=86 does not make selection ignorable. With exactly ten incomplete families, just one missing cell in each already gives an all-family bound width of `10/96 = 0.10417`; four missing cells each give width `40/96 = 0.41667`. Both exceed the 0.05 SESOI. The bounds also are identification bounds for the finite roster, not sampling confidence intervals for a broader population. The experiment plan's “plausible prespecified sensitivity” and “not reversed” language does not define a decision.

**Minimal correction:** Make complete-case conditioning explicit in every confirmatory claim. Define what crossing zero or the SESOI in the all-family bounds permits or prohibits saying about all 96 families. If population generalization is intended, specify uncertainty for bound endpoints. Keep every observed cell and all 96 denominators. Prespecify any additional selection sensitivity instead of selecting a favorable assumption after observing missingness.

**Status:** OPEN Stage-2 interpretation fix; actual selection patterns are later data.

### D2. The eight-family pilot can diagnose gross problems but cannot certify the nuisance assumptions

**Locations:** `protocol/experimental_protocol.md:77–87`; `protocol/analysis_plan.md:195–207`; `protocol/simulations/simulation_report.md:68–78,94–100`; `refine-logs/EXPERIMENT_PLAN.md:85–87,99–105`.

**Evidence and impact:** Each model's eight-family pilot supplies only eight primary interactions and 32 primary factorial outputs. Even zero failures among 32 independent outputs leaves a one-sided 95% failure-probability upper bound of about **8.94%**; zero failed families among eight leaves an upper bound about **31.23%**. Dependence makes cell-level independence optimistic. An eight-item SD estimate is also imprecise. It cannot establish 99% cell validity or SD no greater than 0.15. The report's roughly-98%-validity guidance additionally misses the exact 90% gate target, as calculated above.

**Minimal correction:** Keep the approved 360-call pilot as a diagnostic. Specify uncertainty-aware pilot decisions and sensitivity envelopes now, including the possibility that nuisance qualification remains inconclusive. Use the exact joint completeness formula for gate guidance. Do not infer adequacy from zero pilot failures, select only favorable pilot items, raise the scientific threshold just to attain power, or expand calls without an owner decision. No pilot data are required to repair the wording now.

**Status:** OPEN Stage-2 decision-rule fix; actual power remains conditional until later authorized evidence or explicit owner acceptance of uncertainty.

### D3. Secondary testing families and sensitivity triggers are not fully enumerated

**Locations:** `protocol/analysis_plan.md:80–87,101–108,144–156,209–215`; `protocol/scoring_rubric.md:176–187`.

**Evidence and impact:** Six serial contrasts are specified per evidence condition, but the control trajectory has no exact set of tests and paired-completeness rules in the analysis plan. “Six model × domain-interaction tests” is unexplained: with two domains, a difference in the primary interaction supplies one domain contrast per model, or three tests, unless additional hypotheses are defined. Sign-flip sensitivity is conditional on being “sufficiently symmetric,” without a rule. An item sign flip is a symmetry-based reference test here, not a design-based randomization test created merely by randomized API execution order. Several serial contrasts are algebraically dependent, so a claimed FDR guarantee also needs its dependence assumptions or a robust alternative stated.

**Minimal correction:** Enumerate every secondary contrast, hypothesis, denominator and multiplicity family. Resolve the three-versus-six domain-test discrepancy. Prespecify the symmetry diagnostic and consequence, or use an unconditional clearly labeled robustness analysis. State BH's dependence assumptions, use a dependence-robust correction if a formal guarantee is needed, or keep these outcomes descriptive. Keep these issues separate from the otherwise correctly specified three-test primary Holm family.

**Status:** OPEN Stage-2 specification fix.

### D4. Repeat/paraphrase diagnostics do not yet support the promised affirmative stability claim

**Locations:** `protocol/analysis_plan.md:35–39,158–183`; `protocol/experimental_protocol.md:176–192`; `protocol/scoring_rubric.md:189–211`; `refine-logs/EXPERIMENT_PLAN.md:54–61`.

**Evidence and impact:** The plan correctly uses the same prespecified 24 families and does not treat repeats as independent items. However, “model-level interaction difference” does not explicitly restrict the original estimate to those same 24 paired complete families. Comparing a repeat subset with the original full 96 would mix run differences with subset composition. Sign and 0.05 point-estimate thresholds alone can flag tiny near-zero sign changes while accepting very imprecise stability. Undefined correlations for constant interactions and differing completeness across runs also lack rules. Absence of a flagged difference is not evidence that run/wording artifacts have been excluded.

**Minimal correction:** Require paired original-subset versus repeated/paraphrased-subset estimates on an explicitly defined common population, with missingness and uncertainty reported. Define NA handling for correlations and sign comparisons at zero. For an affirmative approximate-magnitude claim, state a precision/equivalence criterion appropriate to the 0.05 margin; if the 24-family sample cannot meet it, label robustness inconclusive or descriptive. One held-out paraphrase supports robustness to that wording, not to wording variation in general.

**Status:** OPEN Stage-2 claim/analysis fix; observed reliability is a later uncertainty. No automatic increase in repeat calls is recommended.

## Open Minor issue

### E1. Current proposal and state report retain superseded owner gates

**Locations:** `master.md:10–18`; `research/research_proposal.md:3–9,69,200,240,252–261`; `docs/project_state_report.md:59–81,108`.

**Evidence and impact:** The master records Stage 1 closed and limited Stage 2 authorized. The current proposal and state report still say Stage 2 is not authorized; the proposal also describes experiments as requiring Stage-2 approval, although the current Stage-2 authorization expressly excludes them. Read literally by a later worker, these statements could conflate design approval with execution approval. The present review followed the explicit brief/current gate, so no unauthorized work resulted.

**Minimal correction:** Add an explicit supersession notice to the current proposal/state report and reference the limited Stage-2 gate. Preserve historical text as historical. Continue to require separate owner authorization for any pilot/main run and final prompt lock.

**Status:** OPEN documentary correction; does not itself require more owner input.

## Stage-2 fixes versus later uncertainties

**Fix before claiming Stage-2 design readiness:** the simulation/primary-inference alignment and sparse alternatives; template population/inference rules; relevance and matching criteria; applicable adjudication gates and agreement denominators; parent failure propagation; complete-case claim scope; exact secondary families; uncertainty-aware pilot and repeat decisions; stale authorization language. These are local design/statistical tasks. Their repair does not require paid APIs, empirical model outputs, final prompt locking or paper writing.

**Remain explicitly blocked or unverified for later authorized work:** empirical variance, compliance and ceiling behavior; actual template dependence; completed corpus and human ratings; named qualified reviewers and commitments; compensation/institutional arrangements; exact provider snapshots and account access; official price recheck, billed token classes, rate limits, retry behavior and schedule; parser implementation/testing; observed repeat/paraphrase reliability; any execution permission. The absence of these inputs is not, by itself, a reason to fail a readiness *assessment* that honestly lists them. It is a reason not to label execution ready.

No necessary resource expansion has been demonstrated. The current envelope remains the default. If the revised conditional simulation fails, the owner can explicitly accept lower sensitivity or change scope/resources later; no such decision is made by this review.

## Eight Stage-2 deliverable verdicts

PASS means the scoped deliverable is supplied adequately, not that model execution is authorized. FAIL means a substantive Stage-2 correction is needed. BLOCKED means required independent/external evidence is not established in this review.

| # | Owner-deliverable mapping / tracker ID | Verdict | Basis |
|---:|---|---|---|
| 1 | Formal protocol — S2-DOC-001 | **FAIL** | Tree and arithmetic pass; construct, template inference and parent-failure decisions remain incomplete (M2–M5). |
| 2 | Raw-scale SESOI — S2-STAT-001 | **PASS** | Prospective 0.05 policy threshold and interpretation are stated. Owner acceptance remains distinct from empirical validation. |
| 3 | Multiplicity plan — S2-STAT-002 | **FAIL** | Primary Holm/interval plan passes; the full requested plan needs enumerated secondary families and gate/test handling (M1, D3). |
| 4 | Power/completeness simulation — S2-SIM-001 | **FAIL** | Current 80 scenarios reproduce exactly; the simulator does not validate the chosen analysis and a one-active-model alternative falls below the target (M1, M2, D2). |
| 5 | Adjudication operations plan — S2-ADJ-001 | **FAIL** | Logical-proof safeguards are strong, but relevance, pair matching, applicable gates and agreement rules are not yet operational (M3, M4). Actual staffing is separately blocked. |
| 6 | Independent ARIS protocol review — S2-AUD-ARIS | **PASS** | This written independent review is completed and returns REVISE; assurance is same-family/provisional. Exact requested model/effort is not independently verified. |
| 7 | Independent ARS methodological challenge — S2-AUD-ARS | **BLOCKED** | Its completed independent verdict was not established or used in this review. This row does not substitute this ARIS review for ARS and does not prejudge a separately produced report. |
| 8 | Provider/budget/personnel readiness assessment — S2-READY-001 | **PASS** | A conditional, costed assessment exists and candidly records blockers. Account access, funded budget, exact snapshots, personnel and schedule remain BLOCKED for execution. Recorded public prices were not independently revalidated in this review. |

**Final verdict: REVISE.** Return the corrected design/statistical package for independent re-review before asserting readiness for owner approval. The owner may receive this review now as a progress/blocker report. No verdict in this file authorizes implementation, pilot/main model execution, paid APIs, confirmatory collection, final prompt locking or paper writing.
