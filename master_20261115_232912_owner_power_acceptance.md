# FlipRate — Master Research & Agent Operating Manual

> **Project:** FlipRate  
> **Research sprint:** AI x Epistemics Research Sprint, 13–15 November 2026  
> **Track:** Track 1 — Model Epistemics & Decision-Making Evals  
> **Primary question:** Can we distinguish genuine evidence-based belief updating from social capitulation in large language models when they face increasingly forceful disagreement?

This file is the central operating manual for Codex and every agent or skill working on FlipRate. Read it before starting or continuing project work. It takes precedence over informal workflow suggestions, but it does not override the actual instructions or safety constraints of an installed skill.

## Current owner gate — 15 November 2026

Stage 1 is closed. The project owner approved this narrowed positioning:

> FlipRate is a measurement-validation study of serial selective updating, investigating how evidence conditions, social-pressure framing and feedback order affect observable LLM answer distributions across repeated interactions.

The owner authorized Stage 2 only for protocol development, statistical validation, adjudication planning, independent design auditing, and provider/budget/personnel readiness assessment. The approved targets are the 15-call design, 96 confirmatory items and 6,840-call planned envelope.

On 2026-11-15, the owner formally accepted the current **72.24% ± 0.63% CR1/Holm power** as a documented limitation. The original 80% target remains unmet and must not be represented as passed. The design is preserved without further power-driven redesign: 15 calls per item-model tree, 96 confirmatory families, 6,840 planned logical calls, the existing research question and constructs, the primary estimand, hypotheses, SESOI and CR1/Holm multiplicity rules. Any eventual study is classified as **lower-powered and exploratory**, despite retaining prospective confirmatory-style procedures.

Current restrictions: no provider/model API calls, paid requests, pilot or main-model execution, confirmatory data collection, final prompt locking or paper writing. A separate explicit owner authorization is required before implementation or any experiment.

This current owner gate supersedes legacy stage descriptions later in this manual wherever they conflict. Those sections remain as historical workflow guidance; they do not revoke the bounded Stage-2 authorization or authorize execution.

---

## 1. Mission and research objective

FlipRate is a **research benchmark and evaluation framework**, not primarily a chatbot or end-user application.

It investigates how language models change their answers and stated confidence across a sequence of increasingly forceful rebuttals. The central research problem is to distinguish:

1. **Good updating:** The model changes its position because the rebuttal supplies valid new evidence, corrects a factual error, or exposes a genuine reasoning flaw.
2. **Bad updating (social capitulation):** The model changes its position because the challenger sounds confident, claims authority, repeats disagreement, or applies social pressure without supplying adequate evidence.
3. **Bad resistance:** The model maintains an incorrect position despite compelling contradictory evidence.

A useful benchmark must measure all three. A benchmark that only rewards answer stability risks rewarding stubbornness; one that only rewards agreement with rebuttals risks rewarding sycophancy.

### Research objectives

- Design a reproducible, multi-turn benchmark for belief and confidence changes under rebuttal.
- Separate evidence sensitivity from sensitivity to rhetorical and social pressure.
- Measure both appropriate updating and inappropriate capitulation.
- Evaluate multiple models under consistent, documented conditions.
- Publish the dataset, methodology, evaluation code and results where feasible.
- State clearly what the evidence does and does not establish.

### Non-goals

Unless the research evidence makes a compelling case otherwise, do not let the project drift into:

- Building a general-purpose chatbot.
- Treating answer stability as an end in itself.
- Treating every answer change as a failure.
- Treating every refusal to change as a virtue.
- Making broad claims about a model's internal beliefs from text outputs alone.
- Claiming that a benchmark score proves real-world decision quality.

The interface is secondary. The benchmark, experimental design, analysis and defensible findings are the centrepiece.

---

## 2. Research question and hypotheses

### Primary research question

**Can we distinguish genuine evidence-based belief updating from social capitulation in large language models when they face increasingly forceful disagreement?**

### Questions to operationalise

- How often does a model abandon a defensible answer without receiving sufficient new evidence?
- How often does it correctly revise an answer after receiving valid evidence?
- How much does stated confidence change under evidence, confidence, authority and repetition conditions?
- Does rebuttal intensity predict answer changes after controlling for evidence quality?
- Can the benchmark distinguish justified updating, unjustified flipping and unjustified resistance?

### Candidate hypotheses

Treat these as hypotheses to test, not findings to assume.

- **H1 — Evidence responsiveness:** Models should update more often when rebuttals contain valid, relevant evidence than when rebuttals contain only rhetorical pressure.
- **H2 — Pressure sensitivity:** Some models will change answers or confidence under assertive disagreement even when no meaningful new evidence is supplied.
- **H3 — Repetition effect:** Repeated disagreement may increase answer-change probability independently of evidence quality.
- **H4 — Authority effect:** Unsupported claims of expertise or authority may influence model responses.
- **H5 — Resistance failure:** Models will sometimes retain an incorrect answer even after receiving decisive, valid evidence.
- **H6 — Model variation:** These behaviours may differ across models and task categories.

Before testing, refine hypotheses and define measurable outcomes. Do not rewrite hypotheses after seeing results without labelling the change as exploratory.

---

## 3. Agent and skill responsibilities

Codex should use the installed skills as specialist capabilities. First inspect the installed skill instructions and identify their exact invocation names and requirements. Do not assume that a skill's repository name is necessarily its invocation name. Do not invent commands or claim a skill was used when it was not.

### ARIS — Discover, design and implement

**Primary responsibility:** Research development and execution.

Use ARIS for:

- Finding neglected or tractable research questions.
- Reviewing relevant literature and existing benchmarks.
- Assessing novelty and identifying overlap with prior work.
- Refining the research question and hypotheses.
- Designing the dataset, rebuttal conditions, scoring rubric and protocol.
- Implementing the benchmark and evaluation harness.
- Running experiments and collecting results.
- Producing experiment logs, analysis and reproducibility materials.

**Expected outputs:**

- Research proposal and novelty assessment.
- Related-work map and source register.
- Benchmark specification and dataset.
- Experimental protocol.
- Working implementation and tests.
- Raw experiment outputs and analysis.

ARIS is not the final authority on the validity of its own work. Its outputs must be independently audited.

### ARS — Independent audit and challenge

**Primary responsibility:** Research integrity, verification and adversarial review.

Use ARS to:

- Verify that citations exist and support the claims attached to them.
- Check whether sources are primary, reliable and relevant.
- Challenge novelty claims and identify overlooked related work.
- Audit the experimental design, controls, metrics and statistical reasoning.
- Check whether the implementation matches the stated protocol.
- Inspect raw results and reproduce calculations where possible.
- Identify unsupported conclusions, confounds, leakage and benchmark gaming.
- Review limitations, dual-use risks and ethical considerations.
- Conduct an independent challenge before publication.

**Expected outputs:**

- Citation and source-verification report.
- Novelty and related-work challenge.
- Methodology audit.
- Code and data audit.
- Results and statistical audit.
- Limitations and dual-use review.
- Final research-integrity report.

ARS must be allowed to disagree with ARIS. Do not instruct ARS to approve work merely because it has already been implemented.

### Best-Paper-Writing — Research communication and publication

**Primary responsibility:** Communicating verified work clearly and accurately.

Use Best-Paper-Writing to:

- Organise the report around the research question and contribution.
- Draft the abstract, introduction, related work, methodology, results and discussion.
- Produce clear tables, figures and captions from verified data.
- Improve structure, precision, readability and academic presentation.
- Ensure limitations and dual-use considerations are explicit.
- Check the report against the sprint's submission requirements.

**Expected outputs:**

- Report outline.
- Draft report.
- Revised report after audit.
- Final submission-ready PDF, subject to the official template and export requirements.

Best-Paper-Writing must not invent results, citations, methods, datasets, author details or claims to make the paper sound stronger.

### Responsibility boundaries

| Work | Lead | Independent check |
|---|---|---|
| Research direction and novelty | ARIS | ARS |
| Literature and source collection | ARIS | ARS |
| Benchmark design | ARIS | ARS |
| Implementation | ARIS | ARS |
| Experiment execution | ARIS | ARS |
| Statistical analysis | ARIS | ARS |
| Citation verification | ARS | ARIS resolves issues |
| Adversarial challenge | ARS | ARIS responds with evidence |
| Paper drafting | Best-Paper-Writing | ARS verifies claims; ARIS verifies technical details |
| Final release | Project owner | All three provide their required sign-offs |

The project owner makes final scope and submission decisions. Agents must report uncertainty and unresolved disagreements rather than silently deciding disputed matters.

---

## 4. Required research workflow

Follow these stages in order. A stage is not complete because an agent says it is complete; it is complete when its exit criteria are met and the evidence is recorded.

### Stage 0 — Environment and source inspection

**Lead:** Codex, with ARIS as needed.

1. Inspect the project directory and existing work before creating or overwriting files.
2. Read the installed skill instructions for ARIS, ARS and Best-Paper-Writing.
3. Record the exact skill names, locations and invocation method.
4. Identify available models, APIs, datasets, compute and execution constraints.
5. Create the project structure described in Section 5.
6. Record missing prerequisites and ask the project owner only when a decision or credential is genuinely required.

**Exit criteria:**

- Skills and their instructions have been inspected.
- Existing project assets are preserved.
- The environment and constraints are documented.
- No skill invocation or tool capability has been fabricated.

### Stage 1 — Discover

**Lead:** ARIS  
**Audit:** ARS

1. Review the sprint brief and the Track 1 framing.
2. Study relevant work, especially MASK, DarkBench, SycEval, ELEPHANT, ForecastBench and other directly relevant work identified during research.
3. Search for work that already measures multi-turn answer changes, confidence changes, social pressure, evidence sensitivity and resistance to correction.
4. Identify what is genuinely new in FlipRate and what is an adaptation or replication.
5. Define the intended contribution and the smallest defensible research scope.
6. Build a research proposal with hypotheses, candidate tasks, conditions, metrics and risks.
7. Ask ARS to challenge the novelty assessment before locking the design.

**Required deliverables:**

- `research/research_proposal.md`
- `research/related_work.md`
- `research/novelty_assessment.md`
- `research/source_register.csv` or an equivalent structured source register
- `audits/discovery_audit.md`

**Exit criteria:**

- The research question is precise and measurable.
- Related work has been reviewed sufficiently to describe the gap accurately.
- Novelty language is qualified and supported.
- The project scope is feasible within the available time and resources.
- Major objections from ARS are resolved or explicitly recorded.

### Stage 2 — Design

**Lead:** ARIS  
**Audit:** ARS

Develop a protocol that tests answer and confidence changes across rebuttal sequences.

#### Core interaction sequence

1. **Initial question:** Elicit the model's answer, reasoning or explanation, and confidence.
2. **First rebuttal:** Present a counterargument under a defined condition.
3. **Second rebuttal:** Increase disagreement intensity or introduce additional evidence, according to the assigned condition.
4. **Third rebuttal:** Apply stronger social pressure, authority framing or repeated disagreement, as appropriate to the condition.
5. **Final evaluation:** Record the final answer, confidence and justification; score whether any changes were warranted.

The sequence should be controlled and documented. Do not accidentally mix evidence quality and social pressure in a way that makes their effects impossible to distinguish.

#### Conditions to investigate

| Condition | What it tests |
|---|---|
| Evidence-based | Does the model update when valid, relevant evidence is supplied? |
| Confidence-based | Does assertive disagreement influence the model without adding evidence? |
| Authority-based | Does a claimed expert or authority influence the model without adequate supporting evidence? |
| Repeated pressure | Does persistent disagreement cause capitulation? |
| No rebuttal | Baseline answer and confidence stability over the same interaction structure, where appropriate |

Consider matched scenarios: the same underlying question should appear in comparable conditions so that condition effects can be analysed. Define how questions, rebuttals and evidence are generated, reviewed and balanced.

#### Essential design decisions to document

- Task domains and inclusion/exclusion criteria.
- Ground-truth or adjudication procedure.
- How an initial answer is classified as correct, incorrect or ambiguous.
- What qualifies as valid, relevant and sufficient evidence.
- How confidence is elicited and represented.
- How rebuttal strength and social pressure are operationalised.
- Whether rebuttal order is fixed, randomised or counterbalanced.
- How repeated trials and model stochasticity are handled.
- Prompt templates and exact conversation transcripts.
- Model versions, dates, settings and API parameters.
- Human or expert review requirements.
- Missing, malformed or non-compliant model responses.
- Scoring procedures and inter-rater agreement where human judgement is used.

#### Candidate metrics

These are proposed metrics, not validated instruments. Refine definitions before running the main experiment.

1. **Unwarranted Flip Rate:** Frequency with which a model abandons a defensible position without sufficient new evidence.
2. **Warranted Update Rate:** Frequency with which a model correctly updates when presented with valid evidence.
3. **Confidence Drift:** Magnitude and direction of stated confidence change across rebuttal stages.
4. **Pressure Sensitivity:** Degree to which answer or confidence changes as rebuttal intensity increases, especially without new evidence.
5. **Evidence Responsiveness:** Ability to distinguish useful evidence from rhetorical or social pressure.
6. **Resistance Error Rate:** Frequency with which a model maintains an incorrect position despite compelling contradictory evidence.

For every metric, define:

- Unit of analysis and denominator.
- Exact numerator and scoring rule.
- Treatment of uncertain or ambiguous cases.
- Whether higher or lower values are desirable.
- Required human judgement, if any.
- Known failure modes and possible gaming strategies.

Do not combine metrics into a single headline score unless there is a defensible rationale, transparent weighting and analysis showing what the aggregate hides.

**Required deliverables:**

- `protocol/benchmark_specification.md`
- `protocol/experimental_protocol.md`
- `protocol/scoring_rubric.md`
- `protocol/prompt_templates/`
- `protocol/analysis_plan.md`
- `audits/design_audit.md`

**Exit criteria:**

- Conditions are distinguishable and operationalised.
- Metrics have explicit scoring definitions.
- The protocol includes appropriate controls and a ground-truth/adjudication plan.
- ARS has reviewed the design.
- Any unresolved validity risks are documented before implementation.

### Stage 3 — Implement

**Lead:** ARIS  
**Audit:** ARS

Build the smallest working implementation that faithfully executes the approved protocol.

Implementation priorities:

1. Versioned benchmark item format.
2. Dataset validation and quality checks.
3. Prompt and conversation runner.
4. Model adapter layer, where multiple providers or models are available.
5. Structured response capture.
6. Scoring and adjudication pipeline.
7. Analysis scripts and visualisations.
8. Reproducibility documentation.

The implementation must preserve the exact prompts and complete interaction history used in each run. Store model outputs as received before normalisation or scoring.

**Required deliverables:**

- `src/` — implementation.
- `data/` — dataset and documented data versions.
- `tests/` — automated tests.
- `experiments/` — run configurations and logs.
- `docs/reproduction.md`
- `audits/implementation_audit.md`

**Exit criteria:**

- The benchmark runs end-to-end on a small pilot.
- Tests validate data formats, stage ordering and scoring logic.
- Raw outputs are preserved.
- The implementation matches the approved protocol.
- ARS has checked for material implementation/protocol mismatches.

### Stage 4 — Pilot and experiment

**Lead:** ARIS  
**Audit:** ARS

Run a pilot before the main experiment.

#### Pilot

- Use a small, documented subset of benchmark items.
- Check whether prompts elicit interpretable answers and confidence.
- Check whether rebuttal conditions are actually distinct.
- Inspect ambiguous scoring cases.
- Estimate execution cost, latency and failure rates.
- Revise the protocol only when there is a documented reason.
- Version all changes and keep pilot results separate from main results.

#### Main experiment

- Select models and record exact model identifiers or versions.
- Use consistent settings wherever comparisons require them.
- Record timestamps, parameters, prompt versions and dataset versions.
- Run all approved conditions and baselines.
- Preserve raw responses, errors and incomplete runs.
- Repeat runs where required by the analysis plan.
- Report exclusions and missing data transparently.
- Do not stop, extend or selectively rerun experiments merely because results look favourable or unfavourable.

**Required deliverables:**

- `experiments/pilot/`
- `experiments/main/`
- `results/raw/`
- `results/processed/`
- `results/analysis/`
- `results/figures/`
- `results/results_summary.md`

**Exit criteria:**

- The run set matches the registered or versioned analysis plan.
- Raw outputs and run metadata are complete enough to audit.
- Exclusions and failures are accounted for.
- Results can be regenerated from preserved inputs and code.
- No result has been fabricated, silently edited or selectively omitted.

### Stage 5 — Audit

**Lead:** ARS  
**Response owner:** ARIS

ARS must conduct an independent audit of the actual project artefacts, not just review the team's descriptions.

Audit at least:

1. **Sources:** Do cited works exist? Are titles, authors, dates and links accurate? Do they support the attached claims?
2. **Novelty:** Does the report overstate what is new? Are closely related benchmarks or methods missing?
3. **Dataset:** Are items valid, balanced and suitable for the claims? Is there leakage or contamination?
4. **Protocol:** Do the conditions isolate the effects they claim to test?
5. **Implementation:** Does the code execute the documented protocol?
6. **Scoring:** Are rubrics clear, consistent and applied correctly?
7. **Statistics:** Are denominators, uncertainty, variance, baselines and comparisons reported appropriately?
8. **Interpretation:** Do conclusions follow from the observed data?
9. **Reproducibility:** Can another researcher understand and rerun the work?
10. **Ethics and dual use:** Could the benchmark or findings enable manipulation, and are personal data handled appropriately?

Every issue must be recorded with:

- Severity: critical, major, moderate or minor.
- Exact file, section, item or result affected.
- Why it is a problem.
- Evidence supporting the objection.
- A recommended correction or a statement that the issue cannot be resolved with current evidence.
- Status: open, resolved, accepted limitation or disputed.

**Required deliverables:**

- `audits/citation_audit.md`
- `audits/methodology_audit.md`
- `audits/results_audit.md`
- `audits/reproducibility_audit.md`
- `audits/ethics_audit.md`
- `audits/audit_issue_log.md`

**Exit criteria:**

- No critical issue remains unresolved.
- Major issues are fixed or explicitly accepted by the project owner with a clear explanation.
- All changes are traceable.
- ARS does not certify claims it could not verify.

### Stage 6 — Challenge

**Lead:** ARS, with ARIS responding

Conduct an adversarial review. Assume a sceptical reviewer wants to find reasons not to trust the results.

Challenge questions include:

- Could the benchmark reward stubbornness rather than good epistemics?
- Could it reward agreement with the most recent speaker?
- Are evidence quality and social pressure confounded?
- Could the model infer the expected behaviour from the prompt structure?
- Are ground-truth labels reliable?
- Do the metrics measure the stated constructs?
- Could one or two task categories dominate the result?
- Are apparent differences within ordinary run-to-run variation?
- Could the same findings be explained by prompt wording or model formatting?
- Does the paper claim more than the benchmark demonstrates?
- Is the novelty real when compared with existing work?

ARIS must respond point by point with evidence, code, analysis or a documented limitation. Do not dismiss an objection because it is inconvenient.

**Change policy:**

- Fix only issues that can be resolved with actual evidence or a defensible methodological change.
- Do not manufacture supporting data.
- Do not alter raw results.
- Do not quietly change the hypothesis or scoring rule after observing results.
- If a change affects the protocol, version it and explain whether results must be rerun.
- If an issue cannot be resolved within the sprint, disclose it.

**Exit criteria:**

- Every challenge has a recorded response.
- Material corrections are complete or disclosed.
- The final claims are proportionate to the evidence.
- The project owner approves the final scope.

### Stage 7 — Publish

**Lead:** Best-Paper-Writing  
**Technical verification:** ARIS  
**Independent verification:** ARS

Write the paper only from the verified project record.

#### Required report structure

1. **Title and abstract** — abstract must be 150–250 words.
2. **Introduction** — research question, motivation and contribution.
3. **Related Work** — relevant prior work and precise distinction from FlipRate.
4. **Methodology** — models, prompts, dataset, conditions, rubrics, metrics and analysis.
5. **Results** — quantitative findings where possible; baselines, variance and uncertainty where appropriate.
6. **Discussion** — interpretation, implications and future work.
7. **Limitations and Dual-Use / Ethical Considerations** — required section or appendix.
8. **References.**
9. **Appendices** — supplementary methods, prompts, rubrics or results as needed.

#### Sprint submission constraints from the supplied brief

- Research report in PDF using the official template.
- Maximum 8 pages, excluding references and appendices.
- Project title and abstract of 150–250 words.
- Author names and affiliations.
- A required “Limitations and Dual-Use / Ethical Considerations” appendix.
- Public GitHub repository and 3–5 minute demo video are optional.

Verify the current official submission template and submission instructions before export. Do not invent author names, affiliations or template requirements.

#### Required ethical and limitations discussion

State:

- What the results establish.
- What they do not establish.
- Limits of the dataset, models, sample size and task domains.
- Limits of confidence elicitation and behavioural interpretation.
- Risks of using the benchmark to train models to appear stable rather than reason well.
- Risks of using pressure-sensitivity findings to manipulate models or users.
- How personal data were avoided, minimised or handled.
- Any safeguards and responsible-use considerations.

**Exit criteria:**

- The report follows the official template and page limit.
- Abstract is 150–250 words.
- All claims and citations are verified.
- Results match the preserved analysis outputs.
- Required limitations and dual-use material is present.
- ARIS and ARS have completed their final checks.
- The PDF opens and has been visually inspected.

---

## 5. Suggested project structure

Use this structure unless an existing repository already has a sensible equivalent. Preserve existing files and document any structural deviation.

```text
fliprate/
├── master.md
├── README.md
├── research/
│   ├── research_proposal.md
│   ├── related_work.md
│   ├── novelty_assessment.md
│   └── source_register.csv
├── protocol/
│   ├── benchmark_specification.md
│   ├── experimental_protocol.md
│   ├── scoring_rubric.md
│   ├── analysis_plan.md
│   └── prompt_templates/
├── data/
│   ├── README.md
│   ├── raw/
│   └── processed/
├── src/
├── tests/
├── experiments/
│   ├── pilot/
│   └── main/
├── results/
│   ├── raw/
│   ├── processed/
│   ├── analysis/
│   ├── figures/
│   └── results_summary.md
├── audits/
│   ├── audit_issue_log.md
│   ├── discovery_audit.md
│   ├── design_audit.md
│   ├── implementation_audit.md
│   ├── citation_audit.md
│   ├── methodology_audit.md
│   ├── results_audit.md
│   ├── reproducibility_audit.md
│   └── ethics_audit.md
├── paper/
│   ├── outline.md
│   ├── draft.md
│   ├── references.bib
│   └── figures/
└── submission/
    ├── final_report.pdf
    └── submission_checklist.md
```

Do not create empty folders or placeholder artefacts merely to make the tree look complete. Create them when the corresponding stage begins.

---

## 6. Research integrity rules — non-negotiable

These rules apply to every agent, script, analysis and report.

### 6.1 No fabricated evidence

Never fabricate:

- Experimental results, measurements or sample sizes.
- Model outputs or conversation transcripts.
- Citations, papers, authors, publication dates or URLs.
- Dataset contents, labels or expert judgements.
- Statistical tests, confidence intervals or significance claims.
- Implementation status, tests or reproducibility claims.
- Novelty claims or claims of priority.

If something has not been checked, label it **unverified**. If something is unknown, say **unknown**.

### 6.2 Preserve raw data

- Raw model responses are immutable after capture.
- Never overwrite raw logs with cleaned or scored versions.
- Keep raw, processed and analysed data separate.
- Record transformations in code or documented procedures.
- Keep failed runs and exclusions, with reasons.
- Use version control for code, prompts, rubrics and protocol changes.
- Do not place API keys, passwords or private credentials in the repository.

### 6.3 Citation discipline

For every substantive research claim:

- Locate the original source where possible.
- Verify bibliographic details.
- Read enough of the source to confirm the claim.
- Prefer primary sources for technical and empirical claims.
- Record a DOI or stable URL where available.
- Distinguish what the source says from the team's interpretation.
- Never cite a search-result snippet as if the full paper had been read.
- Never attach a citation to a claim the source does not support.

A reference appearing in a related paper does not automatically verify the original claim.

### 6.4 Separate evidence from interpretation

Use explicit labels in working documents:

- **Observed:** directly present in data or source material.
- **Calculated:** derived using a documented procedure.
- **Interpreted:** an explanation of observed or calculated evidence.
- **Hypothesised:** a proposition to test.
- **Unverified:** not yet checked.
- **Limitation:** a known boundary on the conclusion.

Do not turn a hypothesis into a finding through repeated wording.

### 6.5 No result-driven methodological manipulation

Do not change scoring rules, inclusion criteria, model selection or analysis methods after seeing results simply to improve the outcome. If a change is necessary:

1. Record the reason.
2. Version the protocol.
3. Identify whether the change was made before or after observing results.
4. Preserve the original analysis.
5. Report exploratory and confirmatory analyses separately.
6. Rerun affected experiments when required.

### 6.6 Honest reporting

Report null, mixed and negative results. Disclose missing data, failures, exclusions, limitations and uncertainty. Do not claim that a model has an internal belief state when the experiment only observes its expressed answers and confidence.

---

## 7. Experiment record requirements

Every experiment run must have a unique identifier and enough metadata for an independent researcher to understand what happened.

Record at minimum:

- Run ID.
- Date and time (UTC where practical).
- Model provider and exact model identifier/version.
- Dataset version and item IDs.
- Prompt-template version.
- Condition and rebuttal stage.
- Sampling parameters and other relevant settings.
- Full conversation input and raw model response.
- Parsed answer and confidence, if successfully extracted.
- Scoring result and scorer/version.
- Errors, retries and exclusions.
- Code commit or version identifier.

Do not rely on screenshots or manually copied summaries as the only record of an experiment.

---

## 8. Decision-making and escalation rules

When agents disagree:

1. State the exact disputed claim or decision.
2. Identify the evidence each position relies on.
3. Ask ARS to assess the dispute independently when it concerns validity, sources, methods or interpretation.
4. Prefer the position best supported by verifiable evidence, not the most confident agent.
5. If evidence is insufficient, preserve the uncertainty and narrow the claim.
6. Escalate scope, resource or final-submission decisions to the project owner.

### Severity and escalation

- **Critical:** Fabricated evidence, corrupted raw data, invalid core methodology, or a result that cannot be reproduced. Stop dependent work until addressed.
- **Major:** A problem that could materially change the main result or conclusion. Resolve or prominently disclose before publication.
- **Moderate:** A limitation or defect that affects interpretation but does not invalidate the central result. Document and address where feasible.
- **Minor:** Editorial, formatting or low-impact implementation issue. Fix during normal revision.

No agent may mark its own critical or major issue as resolved without recording the evidence for resolution.

---

## 9. Communication and progress reporting

At the end of each substantial task, the responsible agent must provide a concise report containing:

1. **Completed:** What was actually done.
2. **Evidence:** Files, outputs, logs, tests or sources supporting completion.
3. **Findings:** What the work establishes so far.
4. **Uncertainties:** What remains unknown or unverified.
5. **Issues:** Blockers, risks and audit objections.
6. **Next action:** The next concrete task and its owner.
7. **Gate status:** Whether the stage exit criteria are met.

Do not report a task as complete merely because a draft or plan exists. Distinguish planned, in progress, executed, verified and approved.

---

## 10. Final submission checklist

### Research

- [ ] Research question and contribution are explicit.
- [ ] Related work is accurate and sufficiently complete for the scope.
- [ ] Novelty claims are qualified and independently challenged.
- [ ] Hypotheses and metrics were defined clearly.
- [ ] Evidence and social-pressure conditions are distinguishable.
- [ ] Appropriate baselines and controls are included.
- [ ] Limitations of ground truth and confidence elicitation are discussed.

### Implementation and experiments

- [ ] Dataset and prompts are versioned.
- [ ] Evaluation code has tests.
- [ ] Model identifiers and settings are recorded.
- [ ] Raw outputs are preserved.
- [ ] Experiment failures and exclusions are disclosed.
- [ ] Results can be regenerated from recorded artefacts.
- [ ] Figures and tables are generated from verified data.

### Audit and integrity

- [ ] Citations have been checked against their sources.
- [ ] Methodology and scoring have been independently audited.
- [ ] Statistical claims have been checked.
- [ ] No fabricated or selectively omitted results remain.
- [ ] Major audit issues are resolved or explicitly disclosed.
- [ ] Dual-use and ethical considerations are addressed.

### Report and delivery

- [ ] Official report template is used.
- [ ] PDF is no more than 8 pages excluding references and appendices.
- [ ] Abstract is 150–250 words.
- [ ] Author names and affiliations are accurate.
- [ ] Required limitations and dual-use appendix is included.
- [ ] References and appendices are complete.
- [ ] Final PDF has been opened and visually inspected.
- [ ] Optional repository and demo are accurately described, if provided.

---

## 11. How Codex should start

When this file is first loaded, do not immediately write the paper or run a large experiment.

Proceed in this order:

1. Read this `master.md` completely.
2. Inspect the repository and preserve existing work.
3. Locate and read the installed ARIS, ARS and Best-Paper-Writing skill instructions.
4. Report the exact skill names and how Codex can invoke them.
5. Identify which research and implementation artefacts already exist.
6. Compare existing work against the stage exit criteria in this manual.
7. Produce a short **project state report** listing completed, missing, unverified and blocked items.
8. Recommend the single highest-value next action.
9. Begin only the next justified stage, using the assigned skill and recording outputs in the project structure.

If a skill is unavailable, report that clearly and continue only with capabilities that are actually available. Do not pretend that a missing skill ran.

If the sprint deadline or submission portal has passed, do not imply that submission is still possible. Confirm the current official status before making time-sensitive claims.

---

## 12. Governing principle

**FlipRate must reward good epistemics, not mere consistency.**

A model should be willing to change its answer when the evidence warrants it and should be able to resist pressure when the evidence does not. The research must apply the same standard to itself: update when reliable evidence exposes an error, resist unsupported claims, preserve uncertainty and never defend a conclusion simply because the team has already invested in it.

The quality of this project is determined by the strength of its evidence and the honesty of its conclusions—not by how impressive its prototype or paper sounds.
