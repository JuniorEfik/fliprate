# FlipRate Stage-1 Discovery Audit

**Audit date:** 2026-11-15  
**Stage:** Discover  
**Historical owner decision at this checkpoint:** conditional approval; Stage 2 had not yet been authorized  
**Historical verdict:** **Stage-1 design package ready for owner decision**  
**Current governance:** lower power accepted as an exploratory limitation; Stage-2 design closed; execution blocked and unauthorized

> This is the preserved Stage-1 discovery audit. Current authority and readiness are governed by `master.md`, `docs/project_state_report.md` and `docs/stage2_closure_decision.md`. The original 80% target remains failed at 72.24% ± 0.63%; no experiment has been run.

## Approved positioning

> FlipRate is a measurement-validation study of serial selective updating, investigating how evidence conditions, social-pressure framing and feedback order affect observable LLM answer distributions across repeated interactions.

The active study is limited to observable behavior under specified prompts. It does not infer latent beliefs, prove irrationality, or claim a general model tendency to capitulate.

## Fresh review execution and assurance

The conditionally approved revision received two separate reviews:

1. **ARIS `research-review`:** Round 1 returned `REVISE` with three major findings: an incoherent sufficiency information state, ambiguous probability/abstention and complete-case semantics, and unallocated validation/construction work. After revision, Round 2 returned **`READY FOR OWNER APPROVAL`** with no remaining Critical or Major design issue.
2. **ARS `deep-research` Devil's Advocate Checkpoint 1:** the independently executed first pass returned `REVISE` on the same central sufficiency ambiguity. After the explicit underdetermined-item repair, the rebuttal scored `5/5` and the updated verdict was **`PASS`**, with no unresolved Critical or Major issue.

The reviewers were fresh GPT-6 Astra workers, while the executor is also in the OpenAI model family. Assurance is therefore **same-family and provisional**, not cross-family acceptance. Neither review authorizes Stage 2.

Full review artifacts and the ARIS call trace are preserved under `audits/` and `.aris/traces/research-review/`.

## Source and novelty findings retained

- The checked source identities matched preserved primary metadata; checked raw-record hashes matched `research/raw/README.md`.
- No checked source was classified as fabricated.
- ELEPHANT is resolved as Cheng et al., arXiv:2505.13995.
- The closest corpus includes FlipFlop, SycEval, ELEPHANT, SYCON Bench, BASIL, Challenging the Evaluator, BeliefShift, PPT-Bench, MEDLEY-BENCH, Ma et al., the SycEval confound audit, SycoBench-600, Wavering Oracles and Big-Big-SycoBench.
- SycoBench-600 has an authoritative local ACL Anthology PDF and DOI. Several other venue statements remain author-supplied arXiv metadata.
- Warranted-versus-unwarranted revision, baseline-conditioned rates, correct/wrong suggestions, authority, repetition, multi-turn pressure, confidence revision and prompt-confound controls are precedents rather than FlipRate contributions.
- The residual gap is search-bounded: no inspected source was verified to run the exact underdetermined information-sufficiency × pressure factorial with the proposed serial shared-parent paths.

## Final Stage-1 design determination

The primary construct is **information sufficiency**. Both evidence conditions are valid and relevant:

- `S`: baseline plus displayed evidence uniquely warrants target `B`;
- `I`: baseline plus displayed evidence leaves `B` and at least one alternative compatible.

Items have a complete hidden generating world in which `B` is true, but their displayed baseline is deliberately underdetermined. Adjudicators must provide two witness states with different answers for `I` and prove uniqueness for `S`. This separates hidden-world truth from what the displayed information warrants.

Pressure has neutral `N` and bundled authority/confidence `P` frames. One baseline is replayed into five Turn-1 nodes (`S-N`, `S-P`, `I-N`, `I-P`, `C-N`). Exact Turn-1 conversations are then replayed into nine Turn-2 nodes, producing the paths `S-NN`, `S-NP`, `S-PN`, `S-PP`, `I-NN`, `I-NP`, `I-PN`, `I-PP` and `C-NN`. This requires 15 calls per item-model pair.

The primary outcome is reported support for substantive target `B`; abstention is a separate action. The model-specific Turn-1 interaction is:

\[
\delta_m^{CC}=\operatorname{mean}_{i\in CC}\{p_{1i}(B|S,P)-p_{1i}(B|S,N)-p_{1i}(B|I,P)+p_{1i}(B|I,N)\}.
\]

`CC` is the predeclared four-cell-complete population. An all-family sensitivity interval `[δ_m^{AF,L}, δ_m^{AF,U}]` uses denominator 96 and varies only undefined target-support values between 0 and 1. All four cell means, evidence and pressure main effects, malformed rates, abstention and denominators are mandatory.

Turn-2 repeated-exposure, current-frame and prior-frame comparisons are secondary. Recovery and hysteresis are excluded from the active experiment.

## Audit issue log

Statuses concern the Stage-1 proposal, not an implemented protocol.

| ID | Severity | Problem | Final disposition | Status |
|---|---|---|---|---|
| D-01 | Major | Original novelty framing duplicated close prior work. | Priority claims removed; closest work named jointly; gap explicitly search-bounded. | **Resolved** |
| D-02 | Major | Separate arms did not identify an evidence × pressure interaction. | Exact `S/I × N/P` Turn-1 factorial specified. | **Resolved at proposal level** |
| D-03 | Major | Force, round, repetition and context were collinear. | Turn 1 is primary; exact shared parents support current-frame comparisons; `NN/NP/PN/PP` histories and `C-NN` are explicit. Generic turn effects remain a limitation. | **Resolved for primary; accepted secondary limitation** |
| D-04 | Major | Changes could reflect copying, template recognition or spontaneous reconsideration. | Underdetermined baselines, same target placement, control path, balanced positions, held-out items and budgeted paraphrase run. Individual motivational attribution remains prohibited. | **Resolved with accepted limitation** |
| D-05 | Major | Testimony may be informative; pressure response is not automatically irrational. | Framing adds no task fact, but testimony may still affect the model. Interpretation is restricted to reported-support framing effects. | **Accepted construct limitation** |
| D-06 | Major | Small samples and baseline-conditioned subsets could be sparse or incomparable. | 96 confirmatory families, target ≥86 complete/model, within-model item contrasts, baseline abstention compliance only as a stratifier, multiplicity-aware simulation required. | **Resolved at planning level; simulation is a Stage-2 prerequisite** |
| D-07 | Major | Confidence referent, abstention and malformed states were ambiguous. | Support distribution covers substantive options only; action/abstention is separate; ties, inconsistencies and malformed outputs must be prespecified. | **Resolved at proposal level** |
| D-08 | Major | Close works and ELEPHANT were missing. | Register and comparison matrix expanded; raw sources preserved. | **Resolved** |
| D-09 | Major | MEDLEY has material disclosed pipeline limitations. | Used only as bounded protocol precedent unless corrected artifacts are audited. | **Accepted literature limitation** |
| D-10 | Major | BeliefShift metrics contain local definition/range inconsistencies. | Its metrics and numerical conclusions will not be adopted without reconciliation. | **Accepted literature limitation** |
| D-11 | Moderate | SycEval metadata versions disagree. | Version-specific discrepancy retained. | **Accepted metadata limitation** |
| D-12 | Moderate | PPT-Bench model counts differ across sections. | Protocol described without a single unsupported count. | **Resolved** |
| D-13 | Moderate | Venue/version provenance is self-reported for several works. | Status remains qualified; formatting and placeholder DOI are not treated as verification. | **Accepted metadata limitation** |
| D-14 | Moderate | Reproducibility was treated as novel. | Raw preservation is an integrity requirement, not a contribution. | **Resolved** |
| D-15 | Major | No realistic model access, budget or call plan. | Three-provider target; 4,320 main + 360 development + 1,080 exact repeat + 1,080 paraphrase = 6,840 calls; 7,800 ceiling; 4–6M input tokens; <1M output; USD 250 cap and ≤USD 60/provider preflight. | **Resolved as a plan; access and funding blocked** |
| D-16 | Major | Human adjudication and construction capacity were unspecified. | 240 packages, two reviewers, third adjudicator, reserve/replacement rule, 40–48 rating hours, up to 8 adjudication hours and 50–75 construction/rework hours. | **Resolved as a plan; personnel and schedule blocked** |
| D-17 | Major | Alternating feedback did not identify recovery/hysteresis. | Alternating experiment and related claims removed from active proposal and comparison synthesis. | **Resolved by scope removal** |
| D-18 | Moderate | Pressure bundles authority and confidence. | Bundling is explicit; no component-level claim allowed. | **Accepted design limitation** |
| D-19 | Moderate | Treatment-dependent malformed output could change the analyzed population. | Four-cell complete-case target, condition-specific failure rates and 96-family worst-case bounds are specified; no content retry. | **Resolved at proposal level** |
| D-20 | Major | Sufficiency was incompatible with an already solved objective baseline. | Baseline is now underdetermined; `I` requires two witness states and `S` uniqueness; schematic family demonstrates constructibility. | **Resolved; ARIS and ARS confirmed** |
| D-21 | Major | Abstention and target probability mixed truth states with actions. | Substantive-option support and selected action are separate outputs. | **Resolved; ARIS and ARS confirmed** |
| D-22 | Major | Development, paraphrase and construction work were outside the envelope. | Separate bounded allocations added; construction/rework labor included. | **Resolved as a plan; resources unconfirmed** |
| D-23 | Moderate | Probability-scale interaction may reflect ceilings rather than a unique mechanism. | Claim narrowed to support separation on the chosen scale; ceiling simulation and cell means required. | **Accepted measurement limitation** |
| D-24 | Moderate | Three model-specific tests and raw-scale importance were unspecified. | Stage-2 plan must define multiplicity and a smallest effect of scientific interest before simulation. | **Recorded Stage-2 prerequisite** |
| D-25 | Moderate | Original three-day sprint cannot accommodate 98–131 person-hours for one person. | Proposal explicitly requires a team or post-sprint schedule. | **External feasibility blocker** |

## Feasibility assessment

### Bounded plan

- 120 families: 24 development/calibration and 96 confirmatory, split evenly between logic and quantitative reasoning.
- 6,840 planned calls before transport retries; 7,800 hard operational ceiling.
- 4–6 million estimated input tokens and less than 1 million output tokens.
- USD 250 proposed cap with an official-price preflight of no more than USD 60 per model.
- 98–131 estimated human hours including construction, double review, adjudication and rework.
- Nominal standardized MDE approximately 0.30 at 86 families and 0.29 at 96, before multiplicity and simulation adjustments.

### Remaining external blockers

- No relevant provider API credential is configured.
- Exact eligible snapshots, rate limits, decoding controls and current prices are unselected.
- The USD 250 budget is not approved or funded.
- Two named independent reviewers and a third adjudicator are not confirmed.
- A team or post-sprint schedule is not confirmed.
- The multiplicity-aware simulation and raw-scale meaningful-effect threshold are not authorized before Stage 2.

Feasibility is **plausible but conditional, not demonstrated**. Headless Chrome reached official OpenAI, Anthropic and Google pricing documentation on 2026-11-15; this confirms an access route for preflight, not affordability.

## Strongest remaining counter-argument

> FlipRate may validate a response pattern for particular information packages and wrappers without revealing a new epistemic mechanism. Its value depends on construction quality, repeatability and paraphrase robustness; a statistically significant interaction alone would not prove irrationality, social capitulation or broad generality.

The revised positioning accepts this boundary. Null, mixed and negative results remain reportable.

## Stage-1 exit assessment

| Exit criterion | Assessment |
|---|---|
| Research question precise and measurable | **Pass at proposal level.** Information state, construct, outcome and estimand are explicit. |
| Related work sufficient to describe the gap | **Pass with search-bounded limitation.** Global absence is unproved. |
| Novelty language qualified and supported | **Pass.** The contribution is measurement validation, not priority over the core construct. |
| Scope feasible within available resources | **Conditional.** The envelope is realistic; access, people, schedule and funding remain unconfirmed. |
| Major ARS objections resolved or recorded | **Pass.** ARS Checkpoint 1 returned `PASS`; ARIS returned `READY FOR OWNER APPROVAL`. |

## Historical gate decision

**The Stage-1 design package is ready for the project owner's approval decision. Stage 2 remains unauthorized until the owner explicitly approves the exact experiment, accepted limitations and resource commitments.** No benchmark implementation, prompt locking, model experiment or paper drafting may begin from this audit.

The owner later authorized and closed bounded Stage-2 design work, accepted the lower-power exploratory classification, and continued to block implementation and execution. This historical audit does not supersede that later decision.
