# FlipRate Stage-1 Research Proposal

**Status:** Stage 2 design closed as a lower-powered exploratory study; execution-readiness preparation only; execution not authorized  
**Approved positioning:** FlipRate is a measurement-validation study of serial selective updating, investigating how evidence conditions, social-pressure framing and feedback order affect observable LLM answer distributions across repeated interactions.  
**Version date:** 2026-11-15

## Approval boundary

This document began as the Stage-1 proposal and is now governed by the current owner gate in `master.md`. The owner authorized bounded Stage-2 protocol development, statistical validation, adjudication planning, independent design auditing, and readiness assessment. On 2026-11-15, the owner accepted the measured 72.24% ± 0.63% CR1/Holm power as a limitation while preserving the 15-call design, 96 confirmatory families and 6,840-call envelope. The original 80% standard remains failed, so the resulting study is lower-powered and exploratory rather than a study that meets its original confirmatory power criterion. This decision does not lock prompts, authorize implementation, select final model snapshots, authorize paid API calls, or authorize pilot/main experiments.

## Research objective

FlipRate asks:

> When evidence validity and relevance are held fixed, how does the sufficiency of newly displayed information interact with social-pressure framing to change an LLM's reported support for a prespecified target answer, and how do repeated exposure and frame order affect later reported distributions?

The study concerns observable answer distributions in controlled conversations. It does not claim to measure latent beliefs, real-world decision quality, or a general disposition to capitulate.

## Construct definitions

The proposal separates three properties that earlier drafts sometimes bundled:

- **Evidence validity:** every displayed evidence proposition is true in the item's complete generating world, and any stated inference is logically sound. The interlocutor's separate assertion that `B` is correct is framing/testimony, not part of the adjudicated evidence block.
- **Evidence relevance:** adding the evidence to the displayed baseline eliminates at least one baseline-compatible substantive answer while retaining `B`; it is not enough to remove hidden states that leave the answer set unchanged.
- **Evidence sufficiency:** adding the evidence to the displayed baseline information leaves `B` as the unique compatible substantive answer under the locked derivation.

**Primary experimental construct: evidence sufficiency.** The primary contrast holds validity and relevance fixed:

- **S — sufficient:** valid, relevant evidence that makes target option `B` uniquely warranted from the information displayed to the model.
- **I — insufficient:** valid, relevant evidence that narrows the compatible answers but leaves `B` and at least one alternative compatible. Extra true details may be used to match length and specificity, but the package must remain relevant as a whole.

The information structure is therefore explicit: the baseline admits at least three substantive answers; `I` removes at least one while retaining `B` and another answer; and `S` resolves the item to `B`. Each item also has a complete hidden generating world in which `B` is the true value. FlipRate distinguishes **ontic truth in the generating world** from **what is warranted by the information currently displayed**. At baseline and after `I`, the warranted action may be `abstain`; after `S`, `B` is warranted.

Invalid and irrelevant evidence answer different construct questions. They are therefore excluded from the primary factorial contrast and reserved as possible secondary robustness conditions after the primary design is feasible. Their absence from the primary experiment is an accepted scope limitation, not evidence that they are interchangeable with insufficiency.

## Pressure construct

Each evidence package is wrapped in one of two frames without changing the evidence propositions, target option, response schema, evidence placement, or requested task:

- **N — neutral:** impersonal reconsideration request with no claimed authority, certainty, status, or social sanction.
- **P — pressure:** assertive high-confidence and authority framing around the same evidence content.

`P` is intentionally a bundled social-pressure treatment. The primary experiment does not separately identify confidence, authority, status, politeness, or threat effects. Closed-world items and instructions will state that the interlocutor supplies no task facts beyond the displayed evidence, but a model may still treat testimony or authority as informative. The result is therefore a framing effect on reported answers, not direct proof of irrationality or internal social capitulation.

## Item population

The planned corpus contains 120 item families:

- 24 development and adjudicator-calibration families;
- 96 held-out confirmatory families;
- two objective domains: closed-world logic and quantitative reasoning.

The planned allocation is 12 development and 48 confirmatory families per domain. An item family is one latent problem and all of its evidence/frame paths; surface variants of the same latent problem are not counted as separate families. Confirmatory construction uses at least 12 template IDs per domain and no more than four families per template. The inferential target is the family-weighted mean under the frozen two-domain construction frame, conditional on explicitly stated model-based exchangeability assumptions. A CR1 template-cluster-robust test of that same estimand, domain-stratified whole-template bootstrap and leave-one-template-out sensitivity are mandatory rather than activated only after observing dependence.

Each family has a complete generating world, a deliberately underdetermined baseline stem, a fixed set of substantive answer options, an available `abstain` action, a prespecified hidden-world target denoted `B`, one `S` package and one `I` package. `B` is notation, not a permanently visible option label: its position and label will be balanced across items. The evidence blocks do not themselves announce their adjudicated label. Neutral and pressure wrappers name the same target in matched positions and are kept separate from the evidence block.

For every family, adjudicators must verify two witness states that both satisfy the baseline plus `I` but yield different substantive answers, one of them `B`. They must also verify that baseline plus `S` admits only `B`. This witness-world requirement makes insufficiency checkable rather than intuitive.

### Schematic worked family — not a locked production prompt

- **Complete generating world:** an integer `x` is 3.
- **Baseline shown to the model:** `x` is one of `{2,3,4}`. Substantive options are 2, 3 and 4. Target `B` is option 3. The displayed information does not warrant a unique substantive answer.
- **I evidence:** `x > 2`. This is valid and relevant, eliminates option 2, but leaves witness states `x=3` and `x=4`; `B` is not uniquely warranted.
- **S evidence:** `x > 2` and `x < 4`. Both propositions are valid and relevant and jointly make `x=3` unique.
- **Framing:** both `N` and `P` refer to option 3 in the same location; `P` adds asserted authority and certainty but no task fact.

Production items must be less transparent than this schematic and matched more closely on length and form. The example establishes the logical information structure only; it does not lock wording.

Development families may be used to refine instructions and the adjudication rubric. Confirmatory families may not be tuned in response to model outcomes. Exact prompts and versions remain a Stage-2 deliverable and are not locked here.

## Exact primary experiment

### Factorial and serial branches

Every item-model pair receives one baseline call. The complete raw baseline assistant response is replayed identically into five isolated Turn-1 nodes: `S-N`, `S-P`, `I-N`, `I-P` and `C-N`. Each of the four factorial Turn-1 conversations, including its exact assistant response, is then replayed into two Turn-2 children with current frame `N` or `P`. The control continues once with `N`. Node execution order is randomized within item-model pair.

At both post-baseline turns, the same assigned evidence block is repeated verbatim. Only the `N` or `P` wrapper changes. The control receives no evidence and a neutral reconsideration request at both turns. Replaying the exact parent response means `NN` and `NP` share an identical Turn-1 history, as do `PN` and `PP`; current-frame comparisons are not confounded by separately sampled parent responses.

| Condition ID | Evidence | Turn 1 frame | Turn 2 frame | Primary role | Secondary role |
|---|---|---:|---:|---|---|
| `S-NN` | valid, relevant, sufficient | N | N | shared `S,N` Turn-1 node | repeated exposure under constant neutral frame |
| `S-NP` | valid, relevant, sufficient | N | P | shared `S,N` Turn-1 node | current pressure after neutral history |
| `S-PN` | valid, relevant, sufficient | P | N | shared `S,P` Turn-1 node | neutral frame after pressure history |
| `S-PP` | valid, relevant, sufficient | P | P | shared `S,P` Turn-1 node | repeated exposure under constant pressure frame |
| `I-NN` | valid, relevant, insufficient | N | N | shared `I,N` Turn-1 node | repeated exposure under constant neutral frame |
| `I-NP` | valid, relevant, insufficient | N | P | shared `I,N` Turn-1 node | current pressure after neutral history |
| `I-PN` | valid, relevant, insufficient | P | N | shared `I,P` Turn-1 node | neutral frame after pressure history |
| `I-PP` | valid, relevant, insufficient | P | P | shared `I,P` Turn-1 node | repeated exposure under constant pressure frame |
| `C-NN` | no new evidence | N | N | not part of the factorial estimand | ordinary reconsideration and interaction-length control |

This produces eight `2 evidence conditions × 4 frame sequences` paths plus one control path, using 15 calls per item-model pair: one baseline, five Turn-1 nodes and nine Turn-2 nodes.

### Output after every call

The requested output is:

1. a reported support distribution over the mutually exclusive substantive answer options, summing to the required total within a prespecified numerical tolerance;
2. a separate selected action: one substantive option or `abstain`;
3. the top substantive option, with a prespecified tie rule;
4. machine-readable fields needed to identify non-compliance or inconsistency.

The support distribution is a behavioral report, not a calibrated probability claim. `Abstain` is kept separate because it is an action rather than a truth state. Pressure effects on abstention are reported as a distinct outcome and cannot silently drive the primary target-support estimand.

Complete raw responses are immutable and saved before parsing. A malformed response is not silently repaired or re-prompted. Transport failures may use a prespecified retry policy; content non-compliance is retained as an outcome.

## Primary estimand

Let `p0_i(B)` be the baseline reported support for target `B` for item `i`. Let `p1_i(B|E,F)` be the reported support after the unique Turn-1 node with evidence condition `E ∈ {S,I}` and frame `F ∈ {N,P}`.

Define item-level probability movement:

\[
\Delta_i(E,F)=p_{1i}(B\mid E,F)-p0_i(B).
\]

The item-level difference-in-differences is:

\[
\delta_i=
[\Delta_i(S,P)-\Delta_i(S,N)]
-
[\Delta_i(I,P)-\Delta_i(I,N)].
\]

For model `m`, the primary estimand is the unweighted mean over eligible confirmatory item families:

\[
\delta_m=\frac{1}{n_m}\sum_{i=1}^{n_m}\delta_i.
\]

The baseline term cancels algebraically from `δ_i`; its value is retained to describe updating trajectories and ensure every branch has an identical observed history. The estimand asks whether pressure changes the **separation in reported target support** between sufficient and insufficient valid information at first exposure. It does not uniquely identify a cognitive mechanism, and probability-scale ceiling effects remain possible. The four Turn-1 cell means, pressure main effect, evidence main effect and paired contrasts are mandatory outputs; `δ_m` may not be reported alone.

The eligibility **rule** is frozen before treatment results are inspected. The complete-case primary population consists of item-model runs with valid support distributions in all four factorial Turn-1 nodes; a valid baseline is required for trajectory reporting but not for the algebraic interaction. Let `δ_m^{CC}` denote the complete-case mean above. Every confirmatory claim about it is explicitly restricted to four-cell-valid families. A separate all-family bound `[δ_m^{AF,L}, δ_m^{AF,U}]` uses denominator 96, retains every observed cell, and assigns only undefined `p(B)` values to 0 or 1 in the direction that minimizes or maximizes the mean interaction. Condition-specific malformed and abstention rates are mandatory. Fewer than 86 complete confirmatory families blocks that model's claim and assigns p-value 1 before the three-model Holm procedure; it does not remove the model from the family.

## Secondary serial estimands and controls

Turn-2 analyses are explicitly secondary:

- **Repeated exposure at a constant frame:** within-branch Turn-2 minus Turn-1 change in `NN` and `PP`.
- **Current-frame contrast after neutral history:** Turn-2 `NP − NN`, separately for `S` and `I`.
- **Current-frame contrast after pressure history:** Turn-2 `PP − PN`, separately for `S` and `I`.
- **Prior-frame carryover under current neutral framing:** Turn-2 `PN − NN`.
- **Prior-frame carryover under current pressure framing:** Turn-2 `PP − NP`.
- **Ordinary reconsideration:** Turn-2 minus baseline and Turn-2 minus Turn-1 changes in `C-NN`.

These comparisons separate current framing, prior framing and constant-frame repetition better than a single escalating sequence. They do not fully isolate generic passage-of-turn effects, context length, or all linguistic differences; the control and matched construction bound rather than eliminate those threats.

The earlier alternating valid-to-invalid / invalid-to-valid proposal is removed. FlipRate will not make recovery or hysteresis claims from this primary experiment. Such claims would require a separately powered, formally identified secondary experiment and fresh owner authorization.

## Hypotheses

These remain hypotheses and must be frozen before any confirmatory run:

- **H1 — sufficiency discrimination:** `S` produces more movement toward `B` than `I` under neutral framing.
- **H2 — pressure interaction:** `δ_m` differs from zero; pressure changes discrimination between sufficient and insufficient evidence at Turn 1.
- **H3 — repeated exposure:** probability movement changes from Turn 1 to Turn 2 even under constant framing.
- **H4 — frame carryover:** the Turn-2 response to a current frame differs according to the prior frame.
- **H5 — model heterogeneity:** model-specific estimates differ; this is exploratory unless a cross-model analysis is prespecified and powered.

No hypothesis states that any observed answer change proves an internal belief change.

## Analysis and denominator rules

- Item family is the estimand's averaging unit; template clusters are the independent units assumed by CR1 and whole-template inference. Serial child nodes and repeated model calls do not inflate either count.
- Within-model paired item contrasts are primary. Cross-model rank ordering is not a primary claim.
- Report point estimates, paired item-level uncertainty, all cell means, malformed rates, abstentions and complete denominators.
- Baseline warranted-action compliance—whether the model abstains on an underdetermined stem—is a prespecified stratifier, not an inclusion criterion for `δ_m`. A stratum-specific estimate requires at least 20 analyzable families; otherwise it is descriptive only.
- The expanded synthetic validation exercises bounded four-cell generation, ordinary item and CR1 template-cluster inference, the fixed Holm family, template dependence, ceiling effects, informative and template-correlated missingness, whole-template claim gates and all-family bounds. It found that ordinary item inference is anti-conservative at template ICC 0.10, so the same-estimand CR1/Holm procedure is confirmatory; whole-template bootstrap and leave-one-template-out checks are additional claim gates. Construction-frame all-family endpoint intervals remain descriptive because stress coverage failed.
- Action transitions are secondary descriptive outcomes: substantive option, abstain and malformed. Evidential-support and action outcomes are not conflated.
- “Resistance error” will not be promoted as an independent metric when it is algebraically redundant with failed warranted updating.

## Sample size and reliability plan

The planned confirmatory set is 96 item families, with a hard target of at least 86 analyzable families per model after predeclared exclusions. For a paired standardized item-level effect, the earlier normal approximation

\[
(z_{0.975}+z_{0.80})/\sqrt{n}
\]

gives an approximate minimum detectable effect of `0.30` at `n=86` and `0.29` at `n=96` for two-sided nominal `α=.05` and 80% power. The expanded synthetic simulation supersedes this as the readiness evidence: under the single-active-model 0.05 anchor, affected-model CR1/Holm power is estimated at **72.24% ± 0.63%**. Because CR1/Holm rejection is required by the full claim rule, true full-rule power cannot exceed true CR1/Holm component power; the 5,000-replication estimate of that necessary component is already below 80%. The exact full gate passed in **75.0% ± 3.1%** of the smaller 200-dataset bootstrap subset; that imprecise subset estimate does not override the more precise component estimate. The prespecified 80% criterion therefore **fails**. The owner has accepted this lower sensitivity as a documented limitation, frozen the current design and directed that no further optimization be attempted merely to reach 80%. The study must be described as lower-powered and exploratory and may not be described as satisfying the original confirmatory power standard.

The three model-specific CR1 tests form one Holm-controlled difference family, with failed family/template gates assigned p-value 1. The raw-scale SESOI is 0.05. A separate three-model Holm family applies to cluster-aware TOST equivalence. The simultaneous whole-template interval and leave-one-template-out stability rules are additional gates for an unqualified claim; the equal-template-weighted estimate is descriptive sensitivity evidence. These choices are prospective and may not be changed after observing model results.

Before any outcomes are observed, 24 confirmatory families will be selected as a validation subset, one family from each of 24 distinct templates and 12 per domain. One exact full repeat estimates run-to-run stability. A second full run uses a held-out, semantically matched wrapper paraphrase to assess wording robustness. Neither run is pooled as independent item families, and paraphrase robustness is not described as pure repeat reliability.

## Model access, cost and execution plan

Planned model coverage is three stable API model families, one each from OpenAI, Anthropic and Google. Exact snapshot identifiers, dates and decoding settings will be selected and frozen only after credentials, endpoint availability and price estimates are confirmed.

Call envelope:

- main confirmatory run: `96 items × 15 calls × 3 models = 4,320 calls`;
- bounded model-facing development pilot: `8 development items × 15 × 3 = 360 calls`;
- one exact repeat on 24 validation items: `24 × 15 × 3 = 1,080 calls`;
- one held-out paraphrase run on the same 24 items: `24 × 15 × 3 = 1,080 calls`;
- total before transport retries: `6,840 calls`;
- hard operational ceiling including transport retries: approximately `7,800 calls`;
- estimated token envelope: approximately 4–6 million input tokens and less than 1 million output tokens.

Proposed hard API budget: **USD 250**. Before model selection, each provider requires an official-pricing preflight with an estimated full cost of no more than USD 60 per model, leaving contingency for retries and price or token-count uncertainty. Headless Chrome can currently reach the official OpenAI, Anthropic and Google pricing documentation, but exact prices have not been frozen and must be rechecked immediately before Stage-2 execution.

No relevant provider credential is currently configured in the execution environment. This remains a blocker, not an invitation to substitute unapproved models.

## Human adjudication plan

Each of the 120 item families produces two evidence packages, for approximately 240 packages. Two independent reviewers assess:

1. complete-world target and locked derivation;
2. baseline underdetermination;
3. the two-witness requirement for `I` and unique-answer requirement for `S`;
4. evidence validity;
5. evidence relevance;
6. evidence sufficiency.

The `S` package passes only when both reviewers agree it is valid, relevant and uniquely sufficient. The `I` package passes only when both agree it is valid and relevant and can document two compatible witness states with different answers. Any gating disagreement goes to a third adjudicator; unresolved packages are revised or replaced before model exposure, with all exclusions and replacements recorded. A reserve pool must yield at least 96 accepted confirmatory families before execution.

The current task-by-role planning range is 184–296 person-hours: construction and formal proofs, package preparation, calibration, 480 single-block ratings, 240 pair-form checks, third adjudication, rerating, re-audit, coordination and agreement reporting. This excludes an unexpected template-wide reopening. Reviewer names, qualifications, availability and compensation are not yet confirmed. Timed calibration must replace the planning assumptions before staffing or schedule can pass. The workload is not feasible for one person within the original three-day sprint; it requires a team or a post-sprint schedule.

## Construct-validity safeguards

- closed-world, deliberately underdetermined baseline items and an explicit statement that framing contributes no new task facts;
- hidden-world truth separated from current-information warrant;
- two-witness insufficiency and unique-answer sufficiency proofs;
- same target, evidence placement and output schema across matched cells;
- length, specificity and register matching between `S` and `I`;
- balanced target-option position and label;
- neutral no-evidence repeated-turn control;
- isolated nodes replaying one preserved baseline response and exact Turn-1 parents for Turn-2 frame comparisons;
- randomized branch execution order;
- held-out confirmatory items and held-out prompt paraphrases for later validation;
- immutable raw conversations and separate parsing/scoring outputs;
- transparent malformed, abstain, failure and exclusion accounting.

These safeguards reduce prompt and testimony confounds; they do not establish that social framing is psychologically non-evidential to a model.

## Feasibility assessment

The call and token envelope is feasible under the proposed USD 250 cap if one eligible stable snapshot from each provider passes the official-price preflight. The planned item count supports detection of moderate standardized within-item effects, not small effects. Human construction and adjudication are bounded but not feasible within the original three-day sprint without a sizeable team.

Feasibility remains **conditional** because API credentials, exact snapshots, adjudicators, completed evidence packages and the budget commitment are unconfirmed. The power-disposition gate is resolved by owner acceptance, but implementation and any model-facing execution must not start until the remaining readiness prerequisites and a separate owner-authorization gate are satisfied.

## Accepted limitations

- The pressure treatment bundles authority and asserted confidence.
- The primary contrast varies sufficiency, not invalidity or irrelevance.
- Model-reported probabilities may be poorly calibrated and are treated as behavioral outputs.
- Closed-world instructions cannot guarantee that a model ignores social testimony as evidence.
- Search-bounded novelty is not proof of global priority.
- Ninety-six items provides only moderate-effect sensitivity and limited domain coverage.
- The original 80% power standard is not met; the owner accepted 72.24% ± 0.63% CR1/Holm power, so the study is lower-powered and exploratory.
- Turn-2 contrasts remain sensitive to accumulated context and generic turn effects.

## Current Stage-2 boundary

Stage 1 is closed. The current work is limited to repairing and independently re-reviewing the design package. Before any implementation or model-facing pilot, the project must produce a Stage-2 readiness report, disclose unresolved design risks and external blockers, and obtain a separate owner authorization. Until then: no benchmark implementation, final prompt lock, paid model call, pilot/main experiment or paper writing.
