# FlipRate Stage-1 Research Proposal

**Status:** revised after conditional owner approval; Stage 2 not authorized  
**Approved positioning:** FlipRate is a measurement-validation study of serial selective updating, investigating how evidence conditions, social-pressure framing and feedback order affect observable LLM answer distributions across repeated interactions.  
**Version date:** 2026-11-15

## Approval boundary

This document specifies a proposed design closely enough for Stage-1 feasibility and validity review. It does not lock prompts, authorize implementation, select final model snapshots, authorize paid API calls, or authorize experiments. Those actions require a separate project-owner approval for Stage 2.

## Research objective

FlipRate asks:

> When evidence validity and relevance are held fixed, how does evidence sufficiency interact with social-pressure framing to change an LLM's reported probability for a prespecified target answer, and how do repeated exposure and frame order affect later reported distributions?

The study concerns observable answer distributions in controlled conversations. It does not claim to measure latent beliefs, real-world decision quality, or a general disposition to capitulate.

## Construct definitions

The proposal separates three properties that earlier drafts sometimes bundled:

- **Evidence validity:** every factual proposition and inferential step in the evidence is true or logically sound under the item's stated assumptions.
- **Evidence relevance:** the evidence bears on the relative support for the available answer options; it is not merely topically related.
- **Evidence sufficiency:** the evidence, together with the locked item premises, uniquely warrants the prespecified target option under the adjudicated derivation. Competing options are not equally compatible with it.

**Primary experimental construct: evidence sufficiency.** The primary contrast holds validity and relevance fixed:

- **S — sufficient:** valid, relevant evidence that uniquely warrants target option `B`.
- **I — insufficient:** valid, relevant evidence concerning the same target and reasoning step, but not enough to distinguish `B` uniquely from at least one alternative. Extra true, equally compatible details are used where needed to match length and specificity.

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

Each family has a fixed option set plus `abstain`, an independently derived gold answer, a prespecified target denoted `B`, one `S` package and one `I` package. `B` is notation, not a permanently visible option label: correct-option position and label will be balanced across items. Both evidence packages advocate the same target and are matched as closely as possible on length, register, specificity, answer naming and placement.

Development families may be used to refine instructions and the adjudication rubric. Confirmatory families may not be tuned in response to model outcomes. Exact prompts and versions remain a Stage-2 deliverable and are not locked here.

## Exact primary experiment

### Factorial and serial branches

Every item-model pair receives one baseline call. The complete raw baseline assistant response is then replayed identically as the branch point for nine isolated, stateless branches. Branch execution order is randomized within item-model pair.

At both post-baseline turns, the same assigned evidence package is repeated verbatim. Only the `N` or `P` wrapper changes according to the sequence. The control receives no evidence and a neutral reconsideration request at both turns.

| Condition ID | Evidence | Turn 1 frame | Turn 2 frame | Primary role | Secondary role |
|---|---|---:|---:|---|---|
| `S-NN` | valid, relevant, sufficient | N | N | one replicate of `S,N` at Turn 1 | repeated exposure under constant neutral frame |
| `S-NP` | valid, relevant, sufficient | N | P | one replicate of `S,N` at Turn 1 | current pressure after neutral history |
| `S-PN` | valid, relevant, sufficient | P | N | one replicate of `S,P` at Turn 1 | neutral frame after pressure history |
| `S-PP` | valid, relevant, sufficient | P | P | one replicate of `S,P` at Turn 1 | repeated exposure under constant pressure frame |
| `I-NN` | valid, relevant, insufficient | N | N | one replicate of `I,N` at Turn 1 | repeated exposure under constant neutral frame |
| `I-NP` | valid, relevant, insufficient | N | P | one replicate of `I,N` at Turn 1 | current pressure after neutral history |
| `I-PN` | valid, relevant, insufficient | P | N | one replicate of `I,P` at Turn 1 | neutral frame after pressure history |
| `I-PP` | valid, relevant, insufficient | P | P | one replicate of `I,P` at Turn 1 | repeated exposure under constant pressure frame |
| `C-NN` | no new evidence | N | N | not part of the factorial estimand | ordinary reconsideration and interaction-length control |

This is eight `2 evidence conditions × 4 frame sequences` branches plus one control. It requires 19 calls per item-model pair: one baseline and two calls for each of nine branches.

### Output after every call

The requested output is:

1. a probability distribution over every fixed answer option plus `abstain`, summing to the required total within a prespecified numerical tolerance;
2. the top answer;
3. machine-readable fields needed to identify non-compliance.

Complete raw responses are immutable and saved before parsing. A malformed response is not silently repaired or re-prompted. Transport failures may use a prespecified retry policy; content non-compliance is retained as an outcome.

## Primary estimand

Let `p0_i(B)` be the baseline probability assigned to target `B` for item `i`. Let `p1_i^{E,FG}(B)` be the Turn-1 probability in evidence condition `E ∈ {S,I}` and frame sequence `FG ∈ {NN,NP,PN,PP}`.

Because the second frame has not occurred at Turn 1, the two branches sharing the same first frame are treated as replicate realizations:

\[
\bar p_{1i}(B\mid E,F)=\frac{1}{2}\sum_{G\in\{N,P\}}p_{1i}^{E,FG}(B).
\]

Define item-level probability movement:

\[
\Delta_i(E,F)=\bar p_{1i}(B\mid E,F)-p0_i(B).
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

This estimand asks whether pressure changes the model's discrimination between sufficient and insufficient valid evidence at the first exposure. The four Turn-1 cell means and their paired contrasts are mandatory outputs; `δ_m` may not be reported alone. Turn 1 is primary because it precedes repeated exposure and frame carryover.

Eligibility is fixed before treatment results are inspected. The continuous primary analysis requires a valid baseline and valid distributions for all eight factorial Turn-1 calls. Condition-specific malformed rates and worst-case probability bounds are reported so complete-case selection cannot be hidden. Fewer than 86 analyzable confirmatory families for a model triggers a feasibility warning and blocks a well-powered confirmatory claim for that model.

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

- Item family is the independent sampling unit; duplicated branches and model calls do not inflate `n`.
- Within-model paired item contrasts are primary. Cross-model rank ordering is not a primary claim.
- Report point estimates, paired item-level uncertainty, all cell means, malformed rates, abstentions and complete denominators.
- Baseline top-answer correctness is a prespecified stratifier, not an inclusion criterion for `δ_m`. A stratum-specific rate requires at least 20 analyzable families; otherwise it is descriptive only.
- The confirmatory simulation, performed before main execution and without access to treatment signs, will choose the exact paired bootstrap or randomization procedure and account for branch correlation, ceiling effects, malformed rates and any model-level multiplicity adjustment.
- Top-answer transitions are secondary descriptive outcomes: correct, incorrect, abstain and malformed, including wrong-to-other-wrong transitions.
- “Resistance error” will not be promoted as an independent metric when it is algebraically redundant with failed warranted updating.

## Sample size and reliability plan

The planned confirmatory set is 96 item families, with a hard target of at least 86 analyzable families per model after predeclared exclusions. For a paired standardized item-level effect, the normal approximation

\[
(z_{0.975}+z_{0.80})/\sqrt{n}
\]

gives an approximate minimum detectable effect of `0.30` at `n=86` and `0.29` at `n=96` for two-sided nominal `α=.05` and 80% power. This is a planning approximation, not a power guarantee. A prespecified simulation must confirm feasibility before main execution.

Two complete repeats are planned for a 24-item reliability subset. Repeats estimate run-to-run stability and are not pooled as independent item families.

## Model access, cost and execution plan

Planned model coverage is three stable API model families, one each from OpenAI, Anthropic and Google. Exact snapshot identifiers, dates and decoding settings will be selected and frozen only after credentials, endpoint availability and price estimates are confirmed.

Call envelope:

- main confirmatory run: `96 items × 19 calls × 3 models = 5,472 calls`;
- two full repeats on 24 items: `24 × 19 × 3 × 2 = 2,736 calls`;
- total before transport retries: `8,208 calls`;
- hard operational ceiling including retries: approximately `9,500 calls`;
- estimated token envelope: approximately 5–7 million input tokens and less than 1 million output tokens.

Proposed hard API budget: **USD 250**. Before model selection, each provider requires an official-pricing preflight with an estimated full cost of no more than USD 60 per model, leaving contingency for retries and price or token-count uncertainty. Headless Chrome can currently reach the official OpenAI, Anthropic and Google pricing documentation, but exact prices have not been frozen and must be rechecked immediately before Stage-2 execution.

No relevant provider credential is currently configured in the execution environment. This remains a blocker, not an invitation to substitute unapproved models.

## Human adjudication plan

Each of the 120 item families produces two evidence packages, for approximately 240 packages. Two independent reviewers assess:

1. gold answer and locked derivation;
2. evidence validity;
3. evidence relevance;
4. evidence sufficiency.

The `S` package passes only when both reviewers agree it is valid, relevant and sufficient. The `I` package passes only when both agree it is valid and relevant but insufficient. Any gating disagreement goes to a third adjudicator; unresolved packages are excluded before model exposure and recorded with reasons.

Estimated labor is 40–48 person-hours for double review plus up to 8 hours for adjudication. Reviewer names, qualifications, availability and compensation are not yet confirmed. Inter-rater agreement statistics and the final rubric belong to Stage 2.

## Construct-validity safeguards

- closed-world objective items and an explicit statement that framing contributes no new task facts;
- same target, evidence placement and output schema across matched cells;
- length, specificity and register matching between `S` and `I`;
- balanced target-option position and label;
- neutral no-evidence repeated-turn control;
- isolated branches replaying one preserved baseline response;
- randomized branch execution order;
- held-out confirmatory items and held-out prompt paraphrases for later validation;
- immutable raw conversations and separate parsing/scoring outputs;
- transparent malformed, abstain, failure and exclusion accounting.

These safeguards reduce prompt and testimony confounds; they do not establish that social framing is psychologically non-evidential to a model.

## Feasibility assessment

The call and token envelope is feasible under the proposed USD 250 cap if one eligible stable snapshot from each provider passes the official-price preflight. The planned item count supports detection of moderate standardized within-item effects, not small effects. Human adjudication is substantial but bounded.

Feasibility remains **conditional** because API credentials, exact snapshots, adjudicators and the budget commitment are unconfirmed. Stage 2 must not start until those prerequisites and the simulation plan are approved.

## Accepted limitations

- The pressure treatment bundles authority and asserted confidence.
- The primary contrast varies sufficiency, not invalidity or irrelevance.
- Model-reported probabilities may be poorly calibrated and are treated as behavioral outputs.
- Closed-world instructions cannot guarantee that a model ignores social testimony as evidence.
- Search-bounded novelty is not proof of global priority.
- Ninety-six items provides only moderate-effect sensitivity and limited domain coverage.
- Turn-2 contrasts remain sensitive to accumulated context and generic turn effects.

## Stage-1 closure conditions

Before requesting Stage-2 approval:

1. ARIS must complete a fresh design review of this revision and all material findings must be resolved or recorded.
2. ARS must independently repeat Devil's Advocate Checkpoint 1.
3. Every major discovery-audit issue must be marked resolved, accepted limitation or blocked with an owner decision identified.
4. The project owner must approve the exact experiment, resource envelope and remaining limitations.

Until then: no benchmark implementation, prompt lock, paid model call, model experiment or paper writing.
