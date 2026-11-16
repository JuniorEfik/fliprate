# FlipRate Novelty Assessment

**Current verdict:** **PROCEED WITH CAUTION — narrow measurement-validation contribution only**  
**Owner status:** Stage-2 design closed with lower power accepted as an exploratory limitation; execution remains blocked and unauthorized  
**Assurance:** Stage-1 reviews passed after revision; focused Stage-2 ARIS and blind ARS fallback re-reviews both concluded `PASS WITH LIMITATIONS` with same-family/provisional assurance  
**Updated:** 2026-11-16

## Approved positioning

> FlipRate is a measurement-validation study of serial selective updating, investigating how evidence conditions, social-pressure framing and feedback order affect observable LLM answer distributions across repeated interactions.

The positioning is deliberately narrower than a claim to introduce selective updating or to detect internal capitulation.

## Rejected novelty claims

FlipRate must not claim to be the first work to:

- distinguish warranted correction from harmful or unsupported following;
- condition answer changes on baseline correctness;
- compare correct and incorrect suggestions;
- test doubt, authority, confidence, repetition or multi-turn pressure;
- elicit confidence or probability changes;
- control target-answer naming or output-instruction position;
- preserve raw logs or regenerate scores.

Those components appear in Ma et al., BASIL, FlipFlop, SycEval, SYCON Bench, SycoBench-600, Wavering Oracles, Big-Big-SycoBench and related work recorded in `research/closest_work_matrix.md`.

## Closest work

The closest work must be named jointly:

- **SycoBench-600:** correct suggestion versus doubt, authority and wrong suggestion; baseline-correct and baseline-wrong metrics; selectivity; prompt variants and raw-log reproducibility.
- **Big-Big-SycoBench:** same-artefact, same-direction valid versus invalid arguments; register matching; human review; baseline variability; separate responsiveness and compliance.
- **Ma et al.:** Unsupported-Yielding and Rational-Updating; same substantive evidence under different source framing.
- **SYCON Bench and PPT-Bench:** serial pressure trajectories and order-dependent states without a matched sufficiency factorial.
- **BASIL and MEDLEY-BENCH:** behavioral probability/confidence revision and social framing.
- **Gupta et al.:** target-naming and instruction-placement confounds.

## Search-bounded residual delta

The proposed residual contribution is:

> an executed measurement-validation study that starts from deliberately underdetermined closed-world items, holds evidence validity and relevance fixed, crosses information sufficiency with a matched neutral-versus-pressure frame at first exposure, and uses counterbalanced `NN`, `NP`, `PN` and `PP` paths to estimate repeated-exposure and prior-frame carryover effects on reported answer support.

No inspected source was verified to execute that exact combination. This is a bounded absence statement over the preserved corpus, not proof of global priority.

The primary scientific delta is the identified Turn-1 sufficiency-by-pressure interaction. Serial order and carryover are secondary measurement-validation analyses. Merely having multiple turns, eliciting probabilities, adding authority language, or preserving logs is not novel.

## Construct distinction

The proposed primary factor is **sufficiency**, not generic “good versus bad evidence”:

| Property | S condition | I condition | Held fixed? |
|---|---:|---:|---:|
| Validity | valid | valid | yes |
| Relevance | relevant | relevant | yes |
| Sufficiency for target `B` | sufficient | insufficient | no; primary manipulation |

Invalid and irrelevant evidence remain potentially useful robustness conditions, but they are outside the primary experiment. This makes the claim smaller and more interpretable than a mixed valid/invalid treatment.

The revised item structure separates hidden-world truth from current-information warrant. Baseline plus `I` must admit at least two witness states with different answers; baseline plus `S` must admit only `B`. This repair makes “sufficiency” a checkable information property rather than the completeness of an explanation for an already solved item.

## Claim-by-claim assessment

| Candidate component | Assessment |
|---|---|
| Warranted versus unsupported updating | Established precedent; not novel |
| Correct versus wrong suggestions | Established precedent; not novel |
| Valid versus invalid arguments | Established precedent; not novel |
| Initial-correctness-conditioned rates | Established precedent; not novel |
| Doubt, authority, confidence and repetition | Established precedent; not novel |
| Multi-turn trajectories | Established precedent; not novel |
| Confidence or probability change | Established precedent; not novel as a component |
| Target naming and output-instruction controls | Established precedent; required control only |
| Raw logs and reproducible scoring | Integrity requirement, not contribution |
| Valid-and-relevant sufficient versus insufficient evidence crossed with matched pressure at Turn 1 | Possible residual measurement contribution; exact precedent not found in inspected corpus |
| Counterbalanced `NN/NP/PN/PP` carryover analysis using the same evidence | Possible secondary delta; serial confounding remains |
| Recovery or hysteresis under alternating valid/invalid feedback | Removed; not supported by the proposed experiment |

## Allowed claims if the study is executed successfully

Potentially allowed, subject to results and audits:

- FlipRate operationalizes a specific information-sufficiency-by-pressure interaction on underdetermined closed-world objective items.
- The study estimates how pressure framing changes reported target support under sufficient versus insufficient valid information.
- The serial branches describe repeated-exposure and prior-frame carryover effects under the prespecified prompts.
- The work validates or falsifies the usefulness of this measurement design across the tested models and domains.

Not allowed:

- “first to distinguish rational updating from sycophancy”;
- “first selective-updating benchmark”;
- “first multi-turn pressure benchmark”;
- “first valid-versus-invalid evidence benchmark”;
- claims that output changes reveal internal beliefs;
- component-level authority or confidence effects from the bundled pressure treatment;
- recovery or hysteresis claims from the current design;
- generalization beyond the tested tasks, prompts, models and dates.

## Novelty risks

1. **Combination risk:** reviewers may see the design as SycoBench-600 or Big-Big-SycoBench combined with SYCON-style serial turns.
2. **Measurement-not-phenomenon risk:** the main contribution may be a cleaner measurement procedure, not a new behavioral phenomenon.
3. **Prompt-sensitivity risk:** a nonzero interaction may be specific to one pressure wrapper or probability format.
4. **Recent-work risk:** another 2026 work may already run the exact factorial outside the searched corpus.
5. **Null-result risk:** no pressure interaction may occur; that outcome must still be reported as a validation result.

## Conditions for defensibility

- Human adjudication must verify validity, relevance and sufficiency separately, including two witness states for `I` and uniqueness for `S`.
- Exact matched cells and the primary estimand must be frozen before confirmatory execution.
- Turn 1 must remain primary; later serial contrasts must be labeled secondary.
- All four primary cell means, malformed rates and denominators must accompany the interaction estimate.
- Held-out items and the budgeted 24-item wrapper-paraphrase run must test whether the result is a template artifact.
- Claims must remain behavioral and model/task bounded.
- The fresh ARIS and ARS reviews must find no unresolved critical issue; major limitations must be visible to the owner.

## Decision

- **Retain the narrow measurement-validation positioning:** yes.
- **Treat the 72.24% ± 0.63% power result as meeting the original 80% target:** no; the target remains failed.
- **Classify the preserved design as lower-powered exploratory:** yes, by owner decision.
- **Use this assessment to claim global priority or empirical findings:** no.
- **Implement, lock prompts, run models or claim completed results:** no; separate owner authorization is still required.
