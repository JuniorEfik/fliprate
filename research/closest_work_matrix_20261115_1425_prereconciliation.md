# FlipRate Closest-Work Comparison Matrix

**Status:** Stage 1 working evidence; full-text methods checked where noted  
**Assessment date:** 2026-11-15  
**Purpose:** determine whether FlipRate has a defensible contribution before protocol lock

## Executive finding

The original contribution is not novel. Prior work already separates helpful correction from harmful yielding, conditions transition rates on initial correctness, tests doubt and authority, records multi-turn flips, elicits confidence or probabilities, audits target-answer naming and instruction placement, and releases raw logs.

The strongest direct overlaps are:

- **SycoBench-600**: correct suggestion versus doubt, authority, and wrong suggestion; initial-correctness-conditioned update and wrong-flip rates; a selectivity metric; fixed prompt variants; raw logs and regeneration code.
- **Big-Big-SycoBench**: matched valid and invalid arguments on the same artefacts and revision directions; human-reviewed validity labels; separate responsiveness and compliance; baseline-variability controls; a benchmark format supporting up to three challenge turns, although the reported experiment uses one.
- **Ma et al.**: Unsupported-Yielding versus Rational-Updating on initially correct and initially incorrect subsets, including identical evidence presented as a reference note or user claim.
- **SYCON Bench**: five-turn trajectories, repeated pressure, Turn-of-Flip, and Number-of-Flip.
- **Gupta et al.**: target-answer naming and output-instruction position can reverse benchmark conclusions.

A residual contribution may exist only as an **executed, controlled serial interaction study**: evidence validity or sufficiency crossed with pressure form on matched items, with counterbalanced turn schedules and answer plus fixed-proposition confidence collected after every turn. That is a proposed delta, not an established contribution.

## Comparison matrix

Abbreviations: `IC` = conditioned on initial correctness; `TP` = target answer or target direction named; `OI` = output-format or scoring instruction placement.

| Work | Interaction and tasks | Evidence manipulation | Pressure / social manipulation | Trajectory or confidence | IC scoring and controls | Artifacts / residual relation to FlipRate |
|---|---|---|---|---|---|---|
| **FlipFlop** (Laban et al., 2023; arXiv:2311.08596) | Initial classification answer followed by a challenge; seven classification tasks | No independently validated corrective-evidence factor | “Are you sure?” challengers, including teacher and PhD authority personas | Answer flips; no explicit probability trajectory | Correct-to-Flip and Wrong-to-Flip; filters low-accuracy model-task pairs | Direct precedent for conditional flips and authority. Does not execute a valid-evidence × pressure factorial. |
| **SycEval** (Fanous et al., 2025; arXiv:2502.08177) | Math and medical QA; in-context and preemptive rebuttals | Correct or incorrect target support is embedded in rebuttals | Nested simple, ethos, justification, citation/abstract rebuttals | Progressive/regressive response changes; no explicit confidence | Initial response judged correct/incorrect/erroneous; rhetoric and evidence strength are bundled | Direct precedent for progressive/regressive changes. Later audit shows material TP/OI confounds. |
| **ELEPHANT** (Cheng et al., 2025; arXiv:2505.13995) | Open-ended advice, wrongdoing, and paired moral perspectives | No objective corrective-evidence factor | User face and adopted perspective | Paired response reversals; human comparison | Measures face preservation and mutually inconsistent affirmation | Adjacent construct: social sycophancy beyond factual QA, not the target objective-answer revision estimand. |
| **SYCON Bench** (Hong et al., 2025; arXiv:2505.23840) | Five-turn free-form dialogues; debate, stereotype, false-presupposition scenarios | No matched valid-correction arm | Sustained and escalating strategies; debate condition includes repeated identical disagreement | Turn-of-Flip and Number-of-Flip across five turns | Tracks stance transitions; no valid-evidence selectivity denominator | Direct precedent for multi-turn trajectories and repetition. Residual gap is mixed valid/invalid feedback in controlled serial branches. |
| **BASIL** (Atwell et al., 2025/2026; arXiv:2508.16846) | Three uncertainty-driven tasks; elicited probability estimates | Common task evidence; Bayesian-rational posterior derived from model-elicited quantities | Abstract, third-party-belief, and user-belief frames | Verbalized probabilities; direct, hybrid, and repeated-sample elicitation | Descriptive log-odds shift and normative Bayesian-error change | Direct precedent for distinguishing evidence-sensitive updating from user-driven shifts and for confidence-like outputs. Not a serial objective-answer benchmark. |
| **Challenging the Evaluator** (Kim & Khashabi, 2025; arXiv:2509.16533) | MCQ disagreement pairs; conversational follow-up versus neutral judge presentation | Rebuttals vary reasoning amount and quality, including flawed reasoning | Formal and casual styles; “Are you sure,” divergence, and assertive sure rebuttals | Final response adoption; no explicit confidence trajectory | Persuasion rates overall and conditional on initially correct/incorrect; Correction Rate | Direct precedent for framing, reasoning quantity, style, and IC adoption. Two-turn rather than a serial crossed design. |
| **BeliefShift** (Myakala et al., 2026; arXiv:2603.23848) | Multi-session health, politics, values, and product-preference trajectories | Evidence-driven revision is one track | Opinion drift and contradiction contexts | Longitudinal user-belief-state tracking | BRA, DCS, CRR, ESI; local audit found unresolved metric-definition inconsistencies | Adjacent: mainly tests tracking the user's changing beliefs, not revising the evaluated model's own objective answer. |
| **PPT-Bench** (Au & Noronha, 2026; arXiv:2604.07749) | Baseline, single-turn pressure, and multi-turn Socratic escalation on philosophical positions | No independently varied valid evidence | Four pressure types and escalating sequence | Recovery, persistence, worsening and capitulation across rounds | Judge-dependent stance scoring; escalation is tied to turn history | Direct precedent for multi-turn pressure. Residual gap is causal isolation of evidence from pressure. |
| **MEDLEY-BENCH** (Abtahi et al., 2026; arXiv:2604.16009) | Solo baseline with parallel private-revision and social-revision branches | Analyst arguments and manipulated consensus labels | Social consensus versus private reconsideration | Ordinal confidence per claim across branches | Rubric-based, direction-aware scores; consensus-label inversion control | Direct precedent for confidence and social revision. Branches are parallel, not a serial rebuttal chain; disclosed pipeline and judge limitations constrain result use. |
| **Ma et al.** (2026; arXiv:2608.26511) | Initial answer plus one feedback turn on TruthfulQA, PopQA, EX-FEVER, and AQuA | Golden supporting evidence; same evidence as reference note or user statement | Unsupported message naming a wrong answer | Final answer; no round-by-round confidence | Unsupported-Yielding on initially correct cases; Rational-Updating on initially incorrect cases | Closest conceptual comparator. FlipRate cannot claim the construct distinction or IC metrics as new. |
| **SycEval confound audit** (Gupta et al., 2026; arXiv:2609.32867) | Controlled reanalysis of SycEval templates | Not an evidence benchmark | Manipulates target naming and OI placement | Direction-specific follow rates | Requires separate progressive/regressive reporting; shows 14.1–49.5 point naming effects and sign reversals in some timing comparisons | Direct precedent for the proposed confound controls. Applying the checklist is necessary, not itself a contribution. |
| **SycoBench-600** (Sinha, 2026; ACL Findings DOI 10.18653/v1/2026.findings-acl.1759) | Baseline plus doubt, authority, wrong suggestion, and correct suggestion on 600 MCQs / 272 stems | Explicit correct suggestion paired with misleading conditions | Doubt, trusted authority, explicit wrong suggestion; three fixed variants each | One perturbation per branch; example traces combine conditions descriptively; no confidence | WrongFlip on baseline-correct, Update/Stubness on baseline-wrong, Selectivity = Update − WrongFlip; raw responses retained | Very high overlap. Already provides correction selectivity, authority, prompt variants, conditional denominators, raw logs, and artifact regeneration. |
| **Wavering Oracles** (Nee et al., 2026; arXiv:2609.11428) | Reuses SycoBench-600 across 17,055 trajectories and scientific-workflow analyses | Correct versus wrong explicit suggestions | Matched doubt, authority, and explicit-advice contrasts | Phrasing stability; no primary elicited-confidence trajectory | Selectivity and pressure contrasts with clustered bootstrap intervals | Reinforces that “selective updating” and matched authority/doubt/advice effects are occupied terminology and territory. |
| **Big-Big-SycoBench** (Ballon et al., 2026; arXiv:2610.15634) | Numerical quality ratings for 450 artefacts; 20 baselines then branched rescoring | Human-reviewed valid versus invalid arguments matched by artefact and revision direction | Invalid arguments include authority, consensus, emotion, bare assertions, and unsupported claims; persuasive register matched | Baseline score distributions; main experiment uses one challenge; format supports up to three | Separate follow/stable/contrarian probabilities for valid and invalid arguments; baseline-SD threshold; neutral control absent | Strongest recent overlap. It already operationalizes warranted responsiveness versus invalid-pressure compliance and includes rigorous construction controls. A serial mixed-sequence experiment remains unexecuted in the paper. |
| **SycoEval-EM** (Peng et al., 2026; arXiv:2601.16529) | Multi-agent, multi-turn simulated emergency encounters across three scenarios | Guideline-concordant target, not a matched valid-correction arm | Five patient persuasion tactics under sustained pressure | Encounter-level acquiescence | Physician-validated judge on a matched subset | Domain-specific precedent for sustained pressure; adjacent to, not a replacement for, a matched evidence-pressure study. |

## Control coverage summary

| Candidate FlipRate feature | Prior coverage | Current status |
|---|---|---|
| Warranted versus unwarranted updating | Ma, BASIL, SycoBench-600, Big-Big-SycoBench | **Not novel** |
| Initial-correctness denominators | FlipFlop, SycEval, Ma, Challenging the Evaluator, SycoBench-600 | **Not novel** |
| Multi-turn flips / escalation | SYCON, PPT-Bench, SycoEval-EM | **Not novel** |
| Authority and repetition | FlipFlop, SYCON, SycoBench-600, Wavering Oracles | **Not novel** |
| Confidence / probability revision | BASIL, MEDLEY, Big-Big-SycoBench baseline distributions | **Not novel as a component** |
| Target naming and OI controls | Gupta et al. | **Not novel** |
| Raw logs and regeneration | SycoBench-600 and other released benchmarks | **Research requirement, not a contribution** |
| Fully crossed evidence validity × pressure in serial, counterbalanced trajectories with confidence after every turn | No inspected work executes the full combination; Big-Big-SycoBench supports but does not report up to three turns | **Possible narrow delta; unverified absence outside searched corpus** |
| Order, carryover, recovery, and hysteresis after alternating valid and invalid feedback | Partial trajectory precedents only | **Most promising candidate estimand** |

## Stage-1 implication

The smallest defensible scope is no longer “a benchmark that distinguishes good updating from capitulation.” It is a **measurement-validation pilot of serial selective updating**. The primary question should be whether the same model treats the same adjudicated evidence differently when pressure framing and feedback order change, after controlling target naming, response format, turn count, and baseline variability.

Before Stage 2, the project owner must accept this narrower positioning or choose a different contribution. The design must also show an actual crossed condition table; the five independent arms in the current proposal are not a factorial design.

## Evidence and verification limits

- Full-text methods were checked for the locally extracted comparison set and the newly retrieved SycoBench-600 and Big-Big-SycoBench sources.
- Numerical results are recorded only where needed to document a methodological warning or direct overlap; they were not reproduced.
- Venue status is independently supported for SycoBench-600 by the ACL Anthology PDF/DOI. Other venue claims remain arXiv self-reports unless separately stated.
- Absence from this matrix is not proof that no further overlapping work exists.
