# FlipRate Adjudication Plan — Stage 2 Draft

## Material Passport

- Origin Skill: `ars-codex:academic-research-suite` → `experiment-agent` → `plan`
- Origin Date: 2026-11-15
- Verification Status: ANALYZED
- Version Label: `fliprate_adjudication_plan_v0.3`
- Authorization Scope: planning only; no model execution or final prompt lock

## Purpose

This plan operationalizes the item and evidence rubric in `protocol/scoring_rubric.md`. Its purpose is to establish that every accepted family has a determinate hidden world, an underdetermined displayed baseline, a valid/relevant/insufficient block `I`, and a valid/relevant/sufficient block `S` before any model sees the item.

Human ratings are process evidence, not a substitute for the required witness states and uniqueness derivations.

## Corpus and workload

- 24 accepted development/calibration families.
- 96 accepted confirmatory families.
- 120 accepted families total, plus a reserve pool of rejected or revised candidates.
- 240 single-block packages before duplication: one candidate `S` and one candidate `I` per family.
- 480 independent single-block ratings, followed by 240 reviewer-level pair-matching checks.
- Third adjudication occurs only for gating disagreements; changed text returns to both primary reviewers.

| Activity | Planning unit and assumption | Estimated hours |
|---|---|---:|
| Construction and formal proofs | 120 accepted families plus reserve/rework | 45–70 |
| Package preparation and S/I form matching | 120 paired packages | 18–30 |
| Reviewer calibration and training | two reviewers plus coordinator/C | 8–14 |
| Independent single-block ratings | 480 ratings at approximately 8–12 minutes | 64–96 |
| Independent pair-form checks | 240 checks at approximately 4–6 minutes | 16–24 |
| Third adjudication | planning case: up to 20% of families | 6–10 |
| Rerating after revisions | planning allowance, not guaranteed capacity | 12–24 |
| Stratified 10% re-audit | 12 families plus any reopened template set | 3–8 |
| Coordination, versioning and agreement reporting | roster control and quality reporting | 12–20 |
| **Total planning range** | excludes unexpected template-wide reopening | **184–296** |

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

Each family receives a stable internal `item_id` and each rating package a randomized `package_id`. Stage 1 is a single-block classification/proof review. The package initially shows:

1. the complete generating world;
2. the displayed baseline;
3. the substantive answer options and hidden-world target `B`;
4. one candidate evidence block;
5. the single-block scoring form.

The first-pass package does not show:

- whether the block is intended as `S` or `I`;
- the constructor's classification;
- Reviewer A or B's answer;
- any model response;
- any confirmatory outcome.

After the reviewer records an independent classification and rationale, the system reveals the constructor's witness/derivation appendix. The reviewer then rates the proof itself and may revise the classification with an audit note. Both pre-reveal and post-reveal records are preserved.

Stage 2 begins only after both reviewers have locked both single-block records for the family. It shows the paired `S/I` evidence blocks and the draft `N/P` wrappers, with intended evidence labels revealed, solely to evaluate length, structure, specificity, register, wrapper purity and target-position matching. Stage-2 pair ratings cannot retroactively alter a Stage-1 classification without opening a documented disagreement and fresh rating cycle.

## Calibration procedure

Calibration uses development families only and occurs before confirmatory ratings.

1. Adjudicator C and the coordinator prepare eight development families spanning both domains and the main construction templates.
2. A and B independently rate four families without discussion.
3. The group compares decisions against the formal witnesses and derivations, records misunderstood rubric language, and revises training notes only.
4. A and B independently rate the remaining four families.
5. Calibration passes only if there is no unresolved gating disagreement, both reviewers can produce valid witness/uniqueness checks, and raw agreement on the primary validity and sufficiency axes is at least 0.80.
6. If calibration fails, reviewers repeat training with unused development material. Confirmatory packages remain untouched.

The 0.80 rule is a process diagnostic; it does not prove correctness. Any rubric text change is versioned before the confirmatory rating round.

## Rating forms

Every axis is `PASS`, `FAIL`, `UNCERTAIN` or `NA` and requires a written locator or proof note. `NA` is permitted only for the nonapplicable condition-specific sufficiency axis after classification.

| Field | Required record |
|---|---|
| Hidden-world determinacy | Winning answer and derivation from the complete world. |
| Baseline underdetermination | At least three compatible substantive answers, including `B`, with explicit compatible states. |
| Proposition validity | Truth check for every displayed proposition. |
| Inference validity | Invalid step locator or confirmation that every explicit step follows. |
| Answer-level relevance | Baseline-compatible answer eliminated while `B` remains; for `I`, another answer also remains. |
| Information-state classification | `S`, `I`, `NEITHER`, or `UNCERTAIN`, recorded before proof reveal. |
| `I` insufficiency | Two explicit witness states with different answers, one `B`; otherwise `NA`. |
| `S` sufficiency | Uniqueness argument showing no alternative answer remains; otherwise `NA`. |
| Duplicate/template risk | Existing family/template IDs checked. |
| Overall disposition | `ACCEPT`, `REVISE`, `REJECT` or `UNCERTAIN`. |

Free-text rationale is mandatory for any `FAIL`, `UNCERTAIN`, or post-reveal decision change.

The Stage-2 pair form separately records:

- S/I word counts, absolute difference and ratio;
- sentence and proposition-count differences;
- register and numeric/symbolic-format match;
- wrapper purity and same-target/same-position checks;
- any prospectively documented tolerance exception;
- pair disposition: `PASS`, `REVISE`, `REJECT`, or `UNCERTAIN`.

## Acceptance and adjudication flow

1. Coordinator assigns each single-block package independently to A and B.
2. Both reviewers complete pre-reveal classification and post-reveal proof audit.
3. Once both blocks have locked records, A and B independently complete the pair-form review.
4. If all applicable single-block gates and pair gates pass and intended labels are recovered, the family is provisionally accepted.
5. Any `FAIL`, `UNCERTAIN`, label disagreement, proof disagreement or pair-gate disagreement goes to C.
6. C records the disputed axis, evidence examined, decision and rationale.
7. If C requires any item, evidence or wrapper text change, the revised package receives a new version and returns to both A and B for fresh blinded single-block rating and pair review as applicable.
8. A family enters the accepted roster only after all applicable gates pass with no unresolved uncertainty.
9. Rejected and replaced candidates remain in the audit log with their reason and versions.

Adjudicator C cannot waive a failed logical proof.

## Agreement and quality-control reporting

Before adjudication, report separately for pre-reveal classification, post-reveal proof audit and pair review:

- raw percent agreement;
- positive and negative agreement for binary pass/fail reductions;
- Cohen's kappa;
- Gwet's AC1;
- count and proportion sent to C;
- count changed after proof reveal;
- count revised, replaced and rejected.

For the pre-reveal information-state classification, retain `S`, `I`, `NEITHER`, and `UNCERTAIN` as categories. Two identical `UNCERTAIN` ratings count as categorical agreement. In binary PASS/non-PASS reductions, `UNCERTAIN` maps to non-PASS, so two such ratings agree on that reduction. Any `UNCERTAIN` from either reviewer nevertheless triggers referral to C and cannot pass. `NA` is excluded from the axis denominator and its count is shown. The 0.80 information-state pause rule uses four-category pre-reveal raw agreement; validity-axis pause rules use the applicable binary reduction. Headline independent agreement uses pre-reveal records. Post-reveal agreement is reported as proof-audit convergence, not independent label agreement.

Evaluate pause rules after calibration and after each non-overlapping batch of 20 families. Pause the rating process if:

- more than 20% of candidate families require C;
- proposition validity, inference validity or information-state classification agreement is below 0.80;
- a reviewer repeatedly cannot reproduce witness or uniqueness checks;
- a rubric ambiguity affects more than one package.

After provisional acceptance, C re-audits a stratified 10% sample across domains and template IDs with package IDs, prior dispositions and reviewer identities concealed. The coordinator first excludes families C previously adjudicated when enough eligible families remain. Any unavoidable overlap is disclosed and labeled a non-independent recheck; masking IDs is not claimed to erase prior knowledge. A fresh fourth reviewer is preferred for overlapped cases when available. A discovered gating failure reopens every family sharing the affected template or construction rule.

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
| Operational rubric | SPECIFIED; VALIDATION PENDING | Forms, applicability, tolerances and pair review are specified; timed calibration has not occurred. |
| Blinding and rerating rule | SPECIFIED; VALIDATION PENDING | Exact sequence specified above; no personnel have executed it. |
| Calibration plan | SPECIFIED; VALIDATION PENDING | Eight-family development calibration specified. |
| Agreement plan | SPECIFIED; VALIDATION PENDING | Metrics, denominators and batch pause thresholds specified. |
| Named Reviewers A/B/C | BLOCKED | Names, qualifications, availability and conflicts. |
| Compensation/funding | BLOCKED | Owner-confirmed arrangement. |
| Institutional determination | BLOCKED | Applicable ethics/employment/data-protection record. |
| Completed adjudication | BLOCKED | Cannot begin until personnel and later implementation authorization exist. |

This plan is ready for design re-audit. The adjudication operation is not ready to start.
