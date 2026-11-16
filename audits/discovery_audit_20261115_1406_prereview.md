# FlipRate Stage-1 Discovery Audit

**Audit date:** 2026-11-15  
**Stage:** Discover  
**Owner decision:** conditional approval of the narrowed research direction; Stage 2 not authorized  
**Current verdict:** **REVISED; awaiting fresh ARIS and ARS review**

## Approved positioning under review

> FlipRate is a measurement-validation study of serial selective updating, investigating how evidence conditions, social-pressure framing and feedback order affect observable LLM answer distributions across repeated interactions.

This wording supersedes the earlier broad benchmark and priority claims. It is limited to observable outputs and does not infer latent beliefs.

## Prior audit assurance

The pre-conditional audit used three fresh read-only reviewers:

1. ARIS `novelty-check`: `PROCEED WITH CAUTION`, 5/10, with a recent-work addendum;
2. ARS `source_verification_agent`: no fabricated source found, with provenance and read-scope caveats;
3. ARS `devils_advocate_agent`, Checkpoint 1: `REVISE`, no critical issue and seven major issues.

Those reviewers were requested as GPT-6 Astra workers from the same model family as the executor. The reviews are therefore same-family and provisional. The revised design requires a new ARIS design review and a separate new ARS Checkpoint-1 challenge before this audit can close.

## Source and novelty findings retained

- The original registered source identities matched the preserved arXiv records; raw-record hashes checked by the verifier matched `research/raw/README.md`.
- No checked source was classified as fabricated.
- ELEPHANT is resolved as Cheng et al., arXiv:2505.13995.
- The closest corpus includes FlipFlop, SycEval, ELEPHANT, SYCON Bench, BASIL, Challenging the Evaluator, BeliefShift, PPT-Bench, MEDLEY-BENCH, Ma et al., the SycEval confound audit, SycoBench-600, Wavering Oracles and Big-Big-SycoBench.
- SycoBench-600 has an authoritative local ACL Anthology PDF and DOI. Several other venue statements remain author-supplied arXiv metadata.
- Warranted-versus-unwarranted revision, initial-correctness-conditioned rates, correct/wrong suggestions, authority, repetition, multi-turn pressure, confidence revision and prompt-confound controls are precedents, not FlipRate contributions.
- The residual gap is search-bounded: no inspected source was verified to run the exact sufficiency-by-pressure serial design now proposed.

## Revised design determination

The primary construct is now **evidence sufficiency**, not a mixture of validity, relevance and correctness. Both primary evidence conditions must be valid and relevant:

- `S`: sufficient to uniquely warrant target `B`;
- `I`: insufficient to uniquely warrant the same target.

Pressure has two frames, neutral `N` and bundled authority/confidence pressure `P`. Every item branches from one preserved baseline into `S-NN`, `S-NP`, `S-PN`, `S-PP`, `I-NN`, `I-NP`, `I-PN`, `I-PP` and the no-evidence `C-NN` control.

The primary estimand is the model-specific Turn-1 difference-in-differences:

\[
\delta_m=\operatorname{mean}_i\{[\Delta_i(S,P)-\Delta_i(S,N)]-[\Delta_i(I,P)-\Delta_i(I,N)]\},
\]

where `Δ` is change in reported probability for target `B` from the shared baseline. Turn-2 order, repeated-exposure and carryover comparisons are secondary. Recovery and hysteresis claims have been removed.

## Audit issue log

Statuses in this table concern the Stage-1 proposal, not implemented protocol validity.

| ID | Severity | Problem | Disposition in revised proposal | Status |
|---|---|---|---|---|
| D-01 | Major | Original novelty framing duplicated Ma et al., BASIL, SycoBench-600 and Big-Big-SycoBench. | Priority claims removed; closest work named jointly; residual gap explicitly search-bounded. | **Resolved** |
| D-02 | Major | Separate arms did not form an identifiable factorial design. | Exact `S/I × N/P` Turn-1 factorial embedded in four two-turn frame sequences per evidence condition. | **Resolved at proposal level; implementation unverified** |
| D-03 | Major | Force, round, repetition and accumulated context were collinear. | Turn 1 is primary; all `NN/NP/PN/PP` histories are executed; branch order randomized; constant-frame and no-evidence controls added. Turn-2 context effects remain bounded rather than eliminated. | **Resolved for primary; accepted limitation for secondary turns** |
| D-04 | Major | Wrong-to-right change could reflect copying, template recognition or spontaneous reconsideration. | Same target and placement across cells; no-evidence control; balanced option positions; matched `S/I`; held-out confirmatory items and later paraphrase checks; raw malformed outcomes retained. Invalid/irrelevant evidence is outside the primary scope. | **Resolved with accepted scope limitation** |
| D-05 | Major | Testimony and confidence can themselves be informative, so pressure-induced change is not automatically irrational. | Closed-world objective tasks and an explicit no-new-facts role for framing; interpretation narrowed to a framing effect on reported answers. Social testimony may still function as evidence to a model. | **Accepted construct limitation** |
| D-06 | Major | Small samples risk sparse initial-error denominators and incomparable cross-model item populations. | 96 confirmatory families, target ≥86 analyzable; item-family unit; within-model estimand; initial correctness is a stratifier with a minimum 20-family reporting rule; simulation required. | **Resolved at planning level; simulation blocked until Stage 2** |
| D-07 | Major | Scalar confidence changes referent after answer flips; abstain and malformed states were undefined. | Fixed-option distribution plus abstain after every turn; top-answer and malformed status retained; full transition categories specified. | **Resolved at proposal level; implementation unverified** |
| D-08 | Major | Close works and ELEPHANT resolution were missing. | Source register and closest-work matrix expanded; raw sources preserved. | **Resolved** |
| D-09 | Major | MEDLEY has disclosed rendering, aggregation and judge limitations. | Used only as bounded protocol precedent unless its corrected artifacts are separately audited. | **Accepted literature limitation** |
| D-10 | Major | BeliefShift metric definitions and ranges were inconsistent in the local source. | Metrics and numerical conclusions will not be adopted without reconciliation. | **Accepted literature limitation** |
| D-11 | Moderate | SycEval cached metadata and local author block disagree. | Version-specific discrepancy retained; no unsupported canonical author claim made. | **Accepted metadata limitation** |
| D-12 | Moderate | PPT-Bench model-count descriptions differed across sections. | Only bounded protocol description retained; no single model-count claim used. | **Resolved** |
| D-13 | Moderate | Venue/version provenance is self-reported for several works; BASIL contains a placeholder DOI. | Venue status remains qualified; formatting or arXiv comments are not treated as independent venue verification. | **Accepted metadata limitation** |
| D-14 | Moderate | Raw logs and reproducibility were incorrectly treated as novel. | Preservation is now an integrity requirement, not a scientific contribution. | **Resolved** |
| D-15 | Major | No exact model access, cost or call plan. | Three-provider target, 8,208 planned calls, approximately 9,500 ceiling, 5–7M input tokens, <1M output tokens, USD 250 cap and ≤USD 60/provider preflight. | **Resolved as a plan; credentials and budget approval blocked** |
| D-16 | Major | Human adjudication capacity and gating rules were unspecified. | 240 packages, two independent reviewers, third-adjudicator rule, 40–48 hours plus up to 8 hours adjudication. | **Resolved as a plan; named personnel blocked** |
| D-17 | Major | Alternating valid/invalid sequences did not yet identify recovery or hysteresis. | Alternating experiment and all recovery/hysteresis claims removed from the proposed study. | **Resolved by scope removal** |
| D-18 | Moderate | Pressure combines authority and asserted confidence. | Bundling is explicit; no component-level causal claim allowed. | **Accepted design limitation** |
| D-19 | Moderate | Complete-case probability analysis could hide treatment-dependent malformed outputs. | Condition-specific malformed rates and worst-case bounds are mandatory; content non-compliance is not retried. | **Resolved at proposal level; analysis details require Stage 2** |

## Feasibility review

### Evidence supporting feasibility

- The design has a finite call envelope: 5,472 main calls plus 2,736 reliability calls before retries.
- Headless Chrome reached the official OpenAI, Anthropic and Google pricing documentation on 2026-11-15, enabling a future official-price preflight.
- The nominal paired-effect planning calculation gives standardized MDE approximately 0.30 at 86 items and 0.29 at 96 items.
- Human adjudication workload is bounded and explicitly estimated.

### Unverified or blocked prerequisites

- No OpenAI, Anthropic, Gemini or Google API credential is configured in the current environment.
- Exact eligible model snapshots, rate limits and decoding controls are unselected.
- The USD 250 cap has not been approved or funded.
- Two named independent adjudicators and a third tie-breaker are not confirmed.
- The pre-execution power/correlation simulation has not run and is not authorized in Stage 1.

Feasibility is therefore **conditional, not demonstrated**.

## Strongest remaining counter-argument

> The proposed study may still be a carefully controlled recombination of established selective-updating and multi-turn methods. Its pressure manipulation bundles authority and confidence, its insufficient evidence may still rationally shift probability toward a correct target, and its serial contrasts cannot remove all accumulated-context effects. Without reliable human construction and a visible interaction beyond ordinary prompt sensitivity, the work may validate a measurement procedure rather than establish a broad model-epistemics contribution.

This objection is proportionate. The project must keep the contribution at measurement validation and report null or mixed findings.

## Stage-1 exit assessment before fresh reviews

| Exit criterion | Current assessment |
|---|---|
| Research question precise and measurable | **Pass at proposal level.** Constructs, conditions and estimand are explicit. |
| Related work sufficient to describe the gap | **Pass with search-bounded limitation.** Exhaustive absence is not established. |
| Novelty language qualified and supported | **Pass.** No priority claim remains. |
| Scope feasible within available resources | **Conditional.** Quantified plan exists; access, people and budget remain unconfirmed. |
| Major ARS objections resolved or explicitly recorded | **Pending fresh review.** Prior issues now have dispositions, but ARS must challenge the revision. |

## Current gate decision

**Stage 1 remains open pending the required fresh ARIS and ARS reviews and owner approval. Stage 2 is not authorized.** No benchmark implementation, prompt locking, model experiment or paper drafting may begin from this document.
