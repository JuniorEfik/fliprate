# FlipRate Adjudication Plan — Stage 2 Draft

## Material Passport

- Origin Skill: `ars-codex:academic-research-suite` → `experiment-agent` → `plan`
- Origin Date: 2026-11-15
- Verification Status: UNVERIFIED
- Version Label: `fliprate_adjudication_plan_v0.1`
- Authorization Scope: planning only; no model execution or final prompt lock

## Purpose

This plan operationalizes the item and evidence rubric in `protocol/scoring_rubric.md`. Its purpose is to establish that every accepted family has a determinate hidden world, an underdetermined displayed baseline, a valid/relevant/insufficient block `I`, and a valid/relevant/sufficient block `S` before any model sees the item.

Human ratings are process evidence, not a substitute for the required witness states and uniqueness derivations.

## Corpus and workload

- 24 accepted development/calibration families.
- 96 accepted confirmatory families.
- 120 accepted families total, plus a reserve pool of rejected or revised candidates.
- 240 evidence-block reviews before duplication: one candidate `S` and one candidate `I` per family.
- Two independent ratings per package, followed by third adjudication only for gating disagreements.
- Estimated rating labor: 40–48 person-hours.
- Estimated third-adjudication labor: up to 8 person-hours.
- Estimated construction, matching, revision and reserve replacement: 50–75 person-hours.
- Total planning estimate: 98–131 person-hours.

These are workload estimates, not confirmed personnel commitments.

## Roles and separation of duties

| Role | Responsibility | Independence rule |
|---|---|---|
| Constructor | Creates the hidden world, baseline, answer set, evidence blocks, witnesses and derivations. | May not rate or adjudicate an item they constructed. |
| Reviewer A | Independently rates the blinded package. | Does not see Reviewer B, the intended `S/I` label, model output or treatment outcomes. |
| Reviewer B | Independently rates the same blinded package. | Same restrictions as Reviewer A. |
| Adjudicator C | Resolves gating disagreement and audits the stated proof. | Does not replace fresh A/B ratings after any text change. |
| Study coordinator | Randomizes packages, controls versions and reports agreement. | Does not alter ratings or silently discard failed packages. |

The same person may fill more than one project role only when the item-level independence rule remains satisfied and the overlap is disclosed. Five distinct people is the lower-risk staffing pattern; no staffing level is currently confirmed.

## Minimum personnel criteria

Before rating begins, the project owner must record for each reviewer:

- name or stable internal identifier;
- relevant logic, quantitative-reasoning or benchmark-adjudication experience;
- availability for calibration and the planned workload;
- conflicts of interest and any constructor overlap;
- compensation or an explicit volunteer arrangement;
- confidentiality and data-access terms;
- confirmation that model outputs will not be shown during item adjudication.

No credential, qualification or availability may be inferred from a person's title alone.

## Package construction and blinding

Each family receives a stable internal `item_id` and each rating package a randomized `package_id`. The package initially shows:

1. the complete generating world;
2. the displayed baseline;
3. the substantive answer options and hidden-world target `B`;
4. one candidate evidence block;
5. draft neutral and pressure wrappers with condition labels removed;
6. the scoring form.

The first-pass package does not show:

- whether the block is intended as `S` or `I`;
- the constructor's classification;
- Reviewer A or B's answer;
- any model response;
- any confirmatory outcome.

After the reviewer records an independent classification and rationale, the system reveals the constructor's witness/derivation appendix. The reviewer then rates the proof itself and may revise the classification with an audit note. Both pre-reveal and post-reveal records are preserved.

## Calibration procedure

Calibration uses development families only and occurs before confirmatory ratings.

1. Adjudicator C and the coordinator prepare eight development families spanning both domains and the main construction templates.
2. A and B independently rate four families without discussion.
3. The group compares decisions against the formal witnesses and derivations, records misunderstood rubric language, and revises training notes only.
4. A and B independently rate the remaining four families.
5. Calibration passes only if there is no unresolved gating disagreement, both reviewers can produce valid witness/uniqueness checks, and raw agreement on the primary validity and sufficiency axes is at least 0.80.
6. If calibration fails, reviewers repeat training with unused development material. Confirmatory packages remain untouched.

The 0.80 rule is a process diagnostic; it does not prove correctness. Any rubric text change is versioned before the confirmatory rating round.

## Rating form

Every axis is `PASS`, `FAIL` or `UNCERTAIN` and requires a written locator or proof note.

| Field | Required record |
|---|---|
| Hidden-world determinacy | Winning answer and derivation from the complete world. |
| Baseline underdetermination | At least two compatible states/answers, including `B`. |
| Proposition validity | Truth check for every displayed proposition. |
| Inference validity | Invalid step locator or confirmation that every explicit step follows. |
| Relevance | State or answer eliminated, or a prespecified relative-support change. |
| `I` insufficiency | Two explicit witness states with different answers, one `B`. |
| `S` sufficiency | Uniqueness argument showing no alternative answer remains. |
| Wrapper purity | Confirmation that no task fact is introduced. |
| Target-position match | Locator showing the same target in the same structural position. |
| Form match | Length, structure, specificity and register comparison. |
| Duplicate/template risk | Existing family/template IDs checked. |
| Overall disposition | `ACCEPT`, `REVISE`, `REJECT` or `UNCERTAIN`. |

Free-text rationale is mandatory for any `FAIL`, `UNCERTAIN`, or post-reveal decision change.

## Acceptance and adjudication flow

1. Coordinator assigns the same package independently to A and B.
2. Both reviewers complete pre-reveal classification and post-reveal proof audit.
3. If all gating axes pass and intended labels are recovered, the family is provisionally accepted.
4. Any `FAIL`, `UNCERTAIN`, label disagreement or proof disagreement goes to C.
5. C records the disputed axis, evidence examined, decision and rationale.
6. If C requires any item, evidence or wrapper text change, the revised package receives a new version and returns to both A and B for fresh blinded rating.
7. A family enters the accepted roster only after all gating axes pass with no unresolved uncertainty.
8. Rejected and replaced candidates remain in the audit log with their reason and versions.

Adjudicator C cannot waive a failed logical proof.

## Agreement and quality-control reporting

Before adjudication, report per axis and overall:

- raw percent agreement;
- positive and negative agreement for binary pass/fail reductions;
- Cohen's kappa;
- Gwet's AC1;
- count and proportion sent to C;
- count changed after proof reveal;
- count revised, replaced and rejected.

Pause the rating process if:

- more than 20% of candidate families require C;
- either primary validity axis has pre-adjudication agreement below 0.80;
- a reviewer repeatedly cannot reproduce witness or uniqueness checks;
- a rubric ambiguity affects more than one package.

After provisional acceptance, C blindly re-audits a stratified 10% sample across domains and template IDs. A discovered gating failure reopens every family sharing the affected template or construction rule.

## Data and version records

Store separately and preserve:

- immutable package versions;
- constructor proofs and witness states;
- A and B pre-reveal forms;
- A and B post-reveal forms;
- C decisions;
- change requests and revised versions;
- agreement-analysis code and outputs;
- accepted, reserve, rejected and replaced rosters.

No rating is overwritten. Corrections append a new record linked to the superseded record.

## Ethics and institutional boundary

The planned reviewers evaluate constructed benchmark items as research personnel; no participant recruitment or personal-response dataset is currently planned. This does not itself establish exemption from institutional ethics, employment, contractor or data-protection requirements. The project owner or relevant institution must document the applicable determination before external raters are engaged.

## Readiness gates

| Requirement | Current status | Evidence needed to pass |
|---|---|---|
| Operational rubric | PASS | `protocol/scoring_rubric.md` and this plan specify the workflow. |
| Blinding and rerating rule | PASS | Exact sequence specified above. |
| Calibration plan | PASS | Eight-family development calibration specified. |
| Agreement plan | PASS | Metrics and pause thresholds specified. |
| Named Reviewers A/B/C | BLOCKED | Names, qualifications, availability and conflicts. |
| Compensation/funding | BLOCKED | Owner-confirmed arrangement. |
| Institutional determination | BLOCKED | Applicable ethics/employment/data-protection record. |
| Completed adjudication | BLOCKED | Cannot begin until personnel and later implementation authorization exist. |

This plan is ready for design audit. The adjudication operation is not ready to start.
