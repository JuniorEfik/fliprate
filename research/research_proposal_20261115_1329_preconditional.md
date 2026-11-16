# FlipRate Stage-1 Research Proposal

**Status:** rescope candidate; not approved for Stage 2  
**Evidence basis:** full-text closest-work comparison plus provisional independent reviews  
**Date:** 2026-11-15

## Decision forced by prior work

FlipRate cannot claim to introduce selective updating, warranted-versus-unwarranted revision, initial-correctness-conditioned flip rates, multi-turn pressure, authority tests, confidence revision, prompt-confound controls, or auditable raw logs. Those components already appear in Ma et al., BASIL, FlipFlop, SycEval, SYCON Bench, MEDLEY-BENCH, SycoBench-600, Wavering Oracles, Big-Big-SycoBench, and related work.

The project is defensible only if it becomes a narrow **measurement-validation study of serial selective updating**, rather than a broad new benchmark.

## Revised research question

When the substantive evidence is held fixed, how do social-pressure framing and feedback order change an LLM's answer distribution across repeated interactions, and can those effects be separated from ordinary reconsideration, answer naming, and response-format artifacts?

This question concerns observable responses. It does not claim access to latent beliefs.

## Candidate contribution

The candidate delta is an executed, counterbalanced serial design that:

1. crosses feedback validity or sufficiency with social-pressure framing on matched item families;
2. branches conditions from the same preserved baseline response;
3. reverses feedback order to estimate carryover, recovery, and hysteresis;
4. elicits an answer distribution over fixed options after every turn, avoiding a changing confidence referent;
5. holds target-answer naming, response instructions, turn count, information quantity, and lexical intensity constant where the comparison requires it;
6. reports the full transition matrix, malformed responses, abstentions, denominators, and raw conversations.

No inspected paper was verified to execute this complete serial combination. Big-Big-SycoBench supports up to three challenge turns but reports a single-challenge experiment; SYCON provides serial pressure without matched valid correction; SycoBench-600 provides selectivity and authority without a serial crossed experiment. This residual gap remains search-bounded and unproven.

## Candidate hypotheses

These must be frozen before any confirmatory run.

- **H1 — Validity effect:** valid, sufficient feedback produces more movement toward the correct answer than matched unsupported or invalid feedback.
- **H2 — Pressure interaction:** pressure framing changes response to the same substantive feedback, producing a feedback-validity × pressure interaction.
- **H3 — Order effect:** the effect of a valid correction differs when it follows invalid pressure compared with when it appears first.
- **H4 — Persistence and recovery:** some models retain a pressure-induced error after subsequent valid evidence, while others recover.
- **H5 — Distributional change:** pressure can change probability mass over fixed answer options even when the top answer does not change.
- **H6 — Model variation:** the above effects differ by model; within-model contrasts are primary.

## Minimal crossed protocol candidate

For each objective item, create one valid/sufficient argument and one invalid or unsupported argument advocating a prespecified direction. Match length, register, specificity, and target naming. Add neutral and pressure wrappers without changing the argument content.

Branch from one initial response into counterbalanced schedules:

| Schedule | Turn 1 | Turn 2 | Purpose |
|---|---|---|---|
| A | valid feedback, neutral frame | same valid feedback, pressure frame | pressure effect after valid evidence |
| B | valid feedback, pressure frame | same valid feedback, neutral frame | order and carryover for valid evidence |
| C | invalid/unsupported feedback, neutral frame | same invalid feedback, pressure frame | pressure effect without adequate support |
| D | invalid/unsupported feedback, pressure frame | same invalid feedback, neutral frame | order and carryover for invalid feedback |
| E | neutral reconsideration | neutral reconsideration | interaction-length and spontaneous-change control |

An additional alternating valid→invalid / invalid→valid experiment is desirable for recovery and hysteresis but should remain secondary unless the execution budget supports it.

## Outcomes

At baseline and after every turn, require a structured distribution over the fixed answer options plus an abstain state. Preserve the raw response before parsing.

Primary outcomes:

- probability-mass movement toward the correct option;
- top-answer transitions: correct, incorrect, abstain, malformed;
- following rate for valid and invalid feedback;
- selectivity contrast: valid-following minus invalid-following, with both components shown;
- feedback-validity × pressure interaction at a fixed turn;
- carryover, recovery, and persistence under reversed schedules.

Initial correctness remains a required stratifier. “Resistance error” may be reported descriptively, but under exhaustive binary scoring it is algebraically redundant with one minus warranted-update rate and must not be marketed as an independent metric.

## Validation requirements

- Independent ground-truth and evidence-sufficiency adjudication per item.
- Matched invalid, irrelevant, and neutral-reconsideration controls.
- Checks for answer leakage, target naming, output-instruction position, length, politeness, authority wording, and information quantity.
- Unseen prompt paraphrases reserved for validation rather than tuned on pilot outcomes.
- Minimum usable denominators for initially correct and initially incorrect strata.
- Clustered uncertainty by item family and correct handling of shared-baseline branches.
- Exact model identifiers, dates, parameters, prompt versions, and provider metadata.
- Immutable raw conversations; processed outputs and scores stored separately.

## Smallest feasible scope

Treat the first study as a feasibility and construct-validation pilot, not a leaderboard.

- One or two objective domains with independently checkable evidence.
- One primary evidence-validity × pressure contrast.
- A small model set selected only after access and cost are known.
- Enough item families to produce usable initially correct and initially incorrect denominators for every selected model; 20–30 items is not automatically adequate.
- Within-model contrasts as primary; cross-model comparisons accompanied by baseline accuracy and item-population information.

## Feasibility blockers

- No approved model providers, exact models, credentials, or cost budget.
- No accessible local GPU.
- No confirmed human adjudication capacity.
- No official sprint template, portal status, author details, or verified deadline time.

## Stage-1 stop/go rule

Stage 2 may begin only after the project owner accepts the narrower serial measurement-validation positioning and the discovery audit's major issues are either resolved in the proposal or explicitly accepted as limitations. Until then, prompt locking, implementation, experiments, and paper drafting remain prohibited.
