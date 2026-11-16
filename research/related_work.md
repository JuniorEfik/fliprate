# FlipRate Related-Work Review

**Status:** Stage 1 full-text comparison complete for the closest local corpus; broader absence claims remain unverified  
**Search date:** 2026-11-15

## Search and read boundary

Primary metadata came from arXiv, Crossref, and the ACL Anthology. Source archives or authoritative PDFs were preserved under `research/raw/`, with extracted working copies under `research/working/fulltext/`. The dedicated browser-control host was unavailable and Google challenged headless Chrome with a CAPTCHA, which was not bypassed. Direct primary-source retrieval remained available.

The closest-work comparison is recorded in `research/closest_work_matrix.md`. Full-text methods were inspected for FlipFlop, SycEval, ELEPHANT, SYCON Bench, BASIL, Challenging the Evaluator, BeliefShift, PPT-Bench, MEDLEY-BENCH, Ma et al., the SycEval confound audit, SycoBench-600, Wavering Oracles, and Big-Big-SycoBench. SycoEval-EM was assessed from its arXiv abstract.

## Direct conceptual and metric precedents

**Ma et al. (2026)** explicitly separate Unsupported-Yielding from Rational-Updating and define rates on initially correct and initially incorrect subsets. Their Evidence and User-Evidence conditions present the same supporting content under different source framings. This defeats any priority claim for the central distinction or the conditional denominators.

**SycoBench-600 (Sinha, 2026)** is the closest objective-task protocol. It pairs a correct suggestion with doubt, authority, and explicit wrong-suggestion conditions; uses three fixed prompt variants; reports WrongFlip, Update, stubbornness, and Selectivity; and releases raw responses plus regeneration tooling. It does not supply independent supporting evidence beyond naming the correct option and is not a serial crossed experiment.

**Big-Big-SycoBench (Ballon et al., 2026)** is the strongest recent valid-versus-invalid feedback comparator. It matches valid and invalid arguments on the same artefacts and revision directions, matches persuasive register, uses human-reviewed labels, models baseline score variability, and reports separate responsiveness and compliance. The reported experiment uses one challenge, although the format supports up to three. Its subjective rating tasks do not provide objective answer correctness.

**BASIL (Atwell et al., 2025/2026)** formalizes inappropriate updating using elicited probabilities and Bayesian consistency. It compares abstract, third-party-belief, and user-belief frames around task evidence and explicitly treats outputs as behavioral commitments rather than latent beliefs.

## Multi-turn and pressure precedents

**SYCON Bench (Hong et al., 2025)** evaluates five-turn, free-form pressure sequences and reports Turn-of-Flip and Number-of-Flip. Its debate condition includes repeated evidence-free disagreement. It lacks a matched valid-correction arm.

**PPT-Bench (Au & Noronha, 2026)** includes baseline, single-turn pressure, and multi-turn Socratic escalation across four pressure types, with recovery, persistence, worsening, and capitulation outcomes. Evidence quality is not independently manipulated.

**SycoEval-EM (Peng et al., 2026)** uses sustained patient persuasion in simulated emergency encounters and validates its primary judge against physicians. It is a domain-specific pressure benchmark rather than a matched selective-updating design.

**FlipFlop (Laban et al., 2023)** provides the foundational two-round “Are you sure?” paradigm, initial-correctness-conditioned flips, and authority challengers.

## Confidence, framing, and construct precedents

**MEDLEY-BENCH (Abtahi et al., 2026)** records claim-level confidence under private and social revision. Its branches are parallel from a solo baseline, not serial. The manuscript discloses material pipeline and judge limitations, so it is strongest as a protocol precedent rather than a reliable leaderboard.

**Challenging the Evaluator (Kim & Khashabi, 2025)** compares follow-up user rebuttals with neutral joint evaluation, varies reasoning depth and casual/formal style, and reports persuasion conditional on initial correctness.

**SycEval (Fanous et al., 2025)** distinguishes progressive from regressive changes and uses simple, ethos, justification, and citation-based rebuttals. Evidence and rhetoric are bundled.

**Gupta et al. (2026)** show that target-answer naming and output-instruction placement can materially change or reverse SycEval conclusions. These controls are mandatory for FlipRate but cannot be claimed as novel.

**ELEPHANT (Cheng et al., 2025)** measures social face preservation and paired moral-perspective reversal. It expands the construct beyond factual answer changes but does not measure the same objective revision outcome.

**BeliefShift (Myakala et al., 2026)** is longitudinal but principally evaluates tracking a user's evolving beliefs, not changing the evaluated model's own objective answer. The local source audit found unresolved inconsistencies in several metric definitions, so its numerical claims should not be reused without clarification.

## Broader adjacent work

MASK distinguishes honesty from accuracy; DarkBench places sycophancy within a broader dark-pattern taxonomy; ForecastBench and EvolveCast provide dynamic forecasting and confidence-updating context. These works reinforce construct-validity and calibration concerns but are not the closest design competitors.

## Synthesis

The literature already contains every original FlipRate component either directly or in close combination:

- warranted correction versus harmful yielding;
- initial-correctness-conditioned transition metrics;
- correct versus wrong suggestions;
- doubt, authority, repetition, and multi-turn escalation;
- confidence or probability revision;
- target-naming and instruction-position controls;
- raw logs and reproducibility tooling.

The remaining search-bounded gap is narrower: no inspected work was verified to **independently cross adjudicated evidence sufficiency with pressure framing on objectively decidable matched items and execute counterbalanced serial trajectories with a fixed answer distribution after every turn**. Big-Big-SycoBench comes closest and already supports multiple turns, so the contribution must be an identified interaction or carryover finding, not the presence of additional turns.

## Design implications

1. Use an actual crossed design; separate condition buckets are insufficient.
2. Start from a deliberately underdetermined baseline, branch from a shared baseline response and replay exact Turn-1 parents into counterbalanced Turn-2 frames.
3. Use neutral reconsideration as the primary no-evidence control. Invalid and irrelevant evidence are deferred robustness conditions, not substitutes for the primary sufficient-versus-insufficient information factor.
4. Elicit reported support over fixed substantive options and keep abstention as a separate action rather than mixing it into a scalar confidence or truth distribution.
5. Report all four sufficient/insufficient × neutral/pressure cell means, not only the interaction aggregate.
6. Treat resistance as redundant with failed correction when the scoring space is exhaustive and binary.
7. Make within-model contrasts primary and disclose initial-state denominators.
8. Preserve raw responses, parser failures, shared-parent dependencies and all exclusions.

## Coverage limitations

- The search is not a systematic review and cannot establish global absence.
- Venue status remains self-reported from arXiv for several papers; SycoBench-600 is independently represented by its ACL Anthology PDF and DOI.
- Numerical findings were not reproduced.
- Code and released datasets were not independently audited.
- General web search coverage was constrained, but recent arXiv searches and direct primary-source retrieval identified the strongest new overlaps.
