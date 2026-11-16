# FlipRate Benchmark Specification — Stage 2 Draft

## Material Passport

- Origin Skill: experiment-plan + experiment-agent
- Origin Mode: plan
- Origin Date: 2026-11-15
- Verification Status: UNVERIFIED
- Version Label: fliprate_benchmark_spec_v0.2
- Authorization Scope: protocol/statistics/adjudication/audit only

## Status and non-authorization

This document specifies the benchmark structure for design review. It is not a final prompt lock and does not authorize paid API calls, model execution, confirmatory data collection or paper writing.

Approved design targets remain:

- 15 calls per item-model pair;
- 96 confirmatory item families;
- 24 development/adjudication families;
- 6,840 planned calls before transport retries;
- approximately 7,800 hard call ceiling.

Any change to these targets must be documented in `audits/design_audit.md`; a material expansion requires owner approval.

## Benchmark purpose

FlipRate measures how the sufficiency of valid, relevant information and the social framing around that information affect an LLM's reported support for a target answer across repeated interactions.

The benchmark observes model outputs. It does not measure latent belief, prove irrationality, or establish a general capacity for real-world decision-making.

## Unit definitions

### Item family

An item family is one latent closed-world problem and every permitted conversation path derived from it. Surface paraphrases of the same latent problem are not independent item families.

Each family contains:

- `item_id` and construction-template ID;
- domain and difficulty band;
- complete hidden generating world;
- displayed underdetermined baseline;
- fixed substantive answer options;
- hidden-world target `B`;
- valid/relevant/insufficient evidence block `I`;
- valid/relevant/sufficient evidence block `S`;
- witness states for `I`;
- uniqueness proof for `S`;
- draft neutral and pressure wrapper slots;
- adjudication records and version history.

### Domains and allocation

| Domain | Development | Confirmatory | Total accepted |
|---|---:|---:|---:|
| Closed-world logic | 12 | 48 | 60 |
| Quantitative reasoning | 12 | 48 | 60 |
| Total | 24 | 96 | 120 |

Development families may be used for adjudicator calibration, parser tests and the authorized 8-item model-facing pilot. Confirmatory families must remain unseen by model-facing development work except for the prespecified 24-item exact-repeat/paraphrase validation subset after the main run begins under future authorization.

### Independence and construction templates

- A latent problem may appear in only one family.
- Isomorphic variants with only renamed entities or changed numbers must share a template ID and may not be counted as independent templates.
- Confirmatory construction uses at least 12 template IDs per domain, with no more than four confirmatory families per template ID.
- Template IDs are frozen before model execution.
- Primary inference treats item family as the sampling unit; template-cluster and leave-one-template-out analyses are robustness checks.

## Information-state construct

### Hidden-world truth versus displayed warrant

`B` is true in the complete generating world. The baseline deliberately withholds enough information that at least two substantive answers remain compatible.

The benchmark distinguishes truth in the complete world from what the displayed information warrants at each turn.

### Evidence conditions

| Property | `S` sufficient | `I` insufficient |
|---|---|---|
| Every displayed proposition true in complete world | Required | Required |
| Evidence relevant to the answer set | Required | Required |
| At least two compatible answers after evidence | No | Required |
| `B` uniquely compatible after evidence | Required | No |

`I` must have at least two documented witness states satisfying baseline plus `I`, one yielding `B` and one yielding another substantive answer. `S` must have a checkable derivation showing baseline plus `S` admits only `B`.

The evidence block may not include its own adjudication label or an unsupported conclusion that is counted as evidence. Target advocacy belongs to the separately varied wrapper.

Invalid and irrelevant evidence are outside the primary design. They require a later owner-approved extension.

## Social-pressure construct

- `N` — neutral, target-matched reconsideration framing without claimed expertise or certainty.
- `P` — the same target, evidence position and requested task, with bundled asserted expertise and high certainty.

The pressure factor deliberately bundles authority and confidence. It does not identify their separate effects. Both wrappers name the same target in the same structural location so answer naming is controlled.

Exact wording remains draft and unlocked. Wrapper development must not inspect confirmatory treatment outcomes.

## Conversation tree

### Calls

For each item-model pair:

1. One baseline call.
2. Five Turn-1 nodes replaying the exact baseline response: `S-N`, `S-P`, `I-N`, `I-P`, `C-N`.
3. Nine Turn-2 nodes:
   - exact `S-N` parent replayed into `S-NN` and `S-NP`;
   - exact `S-P` parent replayed into `S-PN` and `S-PP`;
   - exact `I-N` parent replayed into `I-NN` and `I-NP`;
   - exact `I-P` parent replayed into `I-PN` and `I-PP`;
   - `C-N` continued into `C-NN`.

Total: 15 calls.

### Condition table

| Path | Evidence | Turn 1 | Turn 2 | Role |
|---|---|---|---|---|
| `S-NN` | S | N | N | constant-neutral repetition |
| `S-NP` | S | N | P | current pressure after neutral history |
| `S-PN` | S | P | N | current neutral after pressure history |
| `S-PP` | S | P | P | constant-pressure repetition |
| `I-NN` | I | N | N | constant-neutral repetition |
| `I-NP` | I | N | P | current pressure after neutral history |
| `I-PN` | I | P | N | current neutral after pressure history |
| `I-PP` | I | P | P | constant-pressure repetition |
| `C-NN` | none | N | N | ordinary reconsideration/interaction-length control |

Turn 1 is the confirmatory primary comparison. Turn 2 is secondary.

## Required model output schema

Every call requests:

1. `support`: numeric support over substantive options only, normalized to 1 within tolerance;
2. `action`: one substantive option or `abstain`;
3. `top_option`: highest-support substantive option;
4. optional short rationale, retained but not used in the primary estimand.

`abstain` is an action, not a truth state. It is not included in the normalized substantive support distribution.

### Compliance states

- `valid`: schema parses and support values meet range/sum rules;
- `valid_with_tie`: schema parses and the prespecified tie rule applies;
- `inconsistent`: action/top option conflicts with support under the protocol rule;
- `malformed`: required fields cannot be parsed or numeric constraints fail;
- `transport_failure`: provider did not return a usable response;
- `provider_refusal`: provider returns a refusal or policy block.

Raw responses are preserved unchanged before parsing. Content non-compliance is not re-prompted. Transport failures follow the future locked retry policy.

## Corpus inclusion criteria

An item family may enter the confirmatory set only if:

- baseline underdetermination is independently verified;
- `I` has two documented witness states with different answers;
- `S` has a uniqueness derivation for `B`;
- both evidence blocks are valid and relevant;
- target position and option labels satisfy the balancing plan;
- length/form matching is within the prespecified rubric tolerance;
- no adjudicator sees model outcomes during item acceptance;
- all disagreements are resolved or the item is replaced before execution.

## Corpus exclusion criteria

Exclude before model execution if:

- hidden-world truth or baseline compatibility is ambiguous;
- `I` accidentally determines `B`;
- `S` admits an alternative answer;
- a displayed proposition is false in the generating world;
- evidence relevance depends on unstated common knowledge;
- wrapper wording introduces a task fact;
- the item duplicates a latent problem already in the corpus;
- adjudication remains unresolved after third review.

Every excluded or replaced candidate remains logged with its reason. It is not silently deleted.

## Versioning and integrity

Freeze separately:

- corpus version;
- evidence-block version;
- draft wrapper version;
- output-schema version;
- adjudication-rubric version;
- parser version;
- analysis-plan version.

Main execution may begin only after a later owner authorization and a protocol lock. The current Stage-2 artifacts are design drafts, even when marked ready for owner review.
