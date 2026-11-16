# FlipRate Preliminary Research Proposal

**Status:** Stage 1 working draft; not approved for implementation  
**Evidence level:** primary metadata and abstracts only  
**Date:** 2026-11-15

## Problem statement

Large language models sometimes revise an answer after a user objects. The same observable change can represent at least three different outcomes:

1. warranted updating after valid, relevant evidence;
2. unsupported yielding to confidence, authority, repetition, or social pressure;
3. unwarranted resistance despite decisive corrective evidence.

**Observed:** prior work already distinguishes versions of these outcomes. SycEval separates progressive from regressive sycophancy; Ma et al. distinguish Unsupported-Yielding from Rational-Updating; MEDLEY-BENCH measures prompted belief revision under social disagreement; PPT-Bench uses multi-turn pressure escalation.

**Interpreted:** FlipRate is only defensible if it improves causal isolation, measurement validity, or reproducibility beyond these benchmarks.

## Preliminary research question

Can a matched, multi-turn evaluation distinguish warranted evidence-responsive updating, unsupported social yielding, and unwarranted resistance when evidence quality, pressure form, escalation, repetition, target-answer naming, output-format placement, and interaction order are explicitly controlled?

## Candidate hypotheses

These are preregistration candidates, not findings.

- **H1 — Evidence responsiveness:** valid, sufficient evidence increases correct revision more than matched unsupported pressure.
- **H2 — Residual pressure sensitivity:** pressure intensity predicts answer or confidence change after controlling evidence content and template features.
- **H3 — Repetition effect:** repeated evidence-free disagreement increases unsupported yielding relative to a matched no-rebuttal interaction.
- **H4 — Authority effect:** unsupported authority framing increases yielding relative to content-matched disagreement without authority cues.
- **H5 — Resistance failure:** some initially incorrect answers persist after decisive corrective evidence.
- **H6 — Model variation:** conditional rates and confidence trajectories vary across models.

Hypotheses and scoring rules must be frozen before main experiments. Any later analysis must be labelled exploratory.

## Candidate contribution

The current candidate contribution is a **confound-resistant matched factorial protocol**, not the general idea of measuring sycophancy or rational updating.

Potential differentiators to verify by full-text comparison:

- multi-turn trajectories rather than only a final two-turn change;
- crossed manipulation of evidence quality and social-pressure form on matched underlying items;
- separate escalation and repetition factors;
- explicit controls for target-answer naming and output-format placement;
- metrics conditioned on initial correctness and adjudicated evidence sufficiency;
- simultaneous reporting of warranted update, unsupported yielding, resistance error, and confidence drift;
- immutable raw conversations plus versioned prompt, item, scorer, and run metadata.

No priority or novelty claim is made yet.

## Smallest defensible initial scope

### Tasks

- Start with objective questions whose ground truth and corrective evidence can be independently verified.
- Prefer two domains with distinct reasoning demands rather than broad coverage.
- Exclude ambiguous, subjective, time-sensitive, or adversarially under-specified items from the confirmatory pilot.

### Conditions

Use matched item families, with wording held constant where possible:

1. no rebuttal / interaction-length control;
2. valid corrective evidence;
3. confident disagreement without evidence;
4. unsupported authority claim;
5. repeated disagreement without new evidence.

Evidence strength and pressure intensity must not change in the same manipulation unless the interaction is explicitly exploratory.

### Sequence

1. initial answer and confidence;
2. first condition message;
3. second message that either adds prespecified evidence or increases prespecified pressure;
4. third message following the assigned condition;
5. final answer, confidence, and concise justification.

### Pilot size

**Hypothesised plan:** 20–30 validated item families across the selected domains and all core conditions, using deterministic or low-temperature settings plus limited repeated trials. The final sample size must follow an analysis and cost plan; this number is not yet approved.

## Preliminary outcome definitions

- **Warranted update:** an initially incorrect or incomplete response becomes correct after sufficient valid evidence.
- **Unsupported yielding:** an initially defensible response becomes incorrect or less defensible without sufficient new evidence.
- **Resistance error:** an initially incorrect response remains incorrect after sufficient valid evidence.
- **Confidence drift:** change in elicited confidence at each stage, reported separately by outcome and condition.

Every denominator must be conditional on the relevant initial state. Ambiguous items and malformed responses require prespecified handling.

## Adjudication requirements

- Ground-truth citation or derivation per item.
- Evidence sufficiency label independent of the model response.
- Review for accidental answer leakage, target-answer naming, and unequal specificity.
- Human double-rating for genuinely judgment-dependent cases, with disagreement retained and inter-rater agreement reported.
- A locked rubric and versioned item schema before main experiments.

## Analysis outline

- Report raw conditional proportions with denominators and uncertainty intervals.
- Model answer change with evidence, pressure, round, initial correctness, task domain, and model as explicit factors where sample size permits.
- Keep answer accuracy and confidence outcomes separate.
- Do not collapse the benchmark into one headline score without a defensible weighting and sensitivity analysis.
- Separate confirmatory from exploratory comparisons.

## Feasibility constraints

- No model API credentials, model list, cost budget, or usable local GPU currently exists.
- A dataset and protocol can be designed locally, but model experiments cannot begin until those prerequisites are resolved.
- The stated sprint ends on the current date; the official submission deadline and portal status are unverified.

## Stop/go criteria before Stage 2

Proceed to design only if:

- full-text comparison identifies a specific non-duplicative contribution;
- the scope is feasible under available model access and time;
- the unresolved `ELEPHANT` reference is identified or explicitly documented as unavailable;
- ARS independently challenges and does not identify an unresolved critical flaw in the discovery case;
- the project owner accepts any major novelty limitation or rescoping decision.

## Current recommendation

Continue Stage 1. Do not lock prompts, metrics, or claims until the closest-work comparison matrix is complete.
