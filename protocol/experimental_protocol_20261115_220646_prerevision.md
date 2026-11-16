# FlipRate Experimental Protocol — Stage 2 Draft

## Material Passport

- Origin Skill: experiment-plan + experiment-agent
- Origin Mode: plan
- Origin Date: 2026-11-15
- Verification Status: UNVERIFIED
- Version Label: fliprate_experimental_protocol_v0.2

## Authorization boundary

This protocol is for design validation only. No paid API call, main model execution, confirmatory data collection, or final prompt lock is authorized.

## Objectives

### Primary objective

Estimate, separately for each model, whether pressure changes the Turn-1 separation in reported support for target `B` between sufficient and insufficient valid information.

### Secondary objectives

- estimate repeated-turn changes under constant neutral and constant pressure framing;
- estimate current-frame contrasts with exact shared parent histories;
- estimate total prior-frame carryover effects;
- quantify abstention, malformed output and provider failure;
- estimate exact-repeat stability and wrapper-paraphrase robustness.

No recovery or hysteresis objective is included.

## Planned study population

- 24 development/calibration families;
- 96 confirmatory families;
- 48 confirmatory families per domain;
- one model family each from OpenAI, Anthropic and Google, subject to owner-approved snapshots and access.

Model-specific conclusions are primary. Cross-model rankings are not primary.

## Pre-execution gates

All gates must pass before a future main run:

| Gate | Required evidence |
|---|---|
| Owner authorization | explicit authorization for main model execution |
| Corpus | 96 accepted confirmatory families and 24 accepted development families |
| Adjudication | double review complete; disagreements resolved; agreement reported |
| Prompts | versioned and explicitly locked after owner approval |
| Models | exact snapshot IDs, parameters, access and dates recorded |
| Budget | official-price estimate ≤ USD 60/model and total approved cap ≤ USD 250 |
| Statistics | SESOI, multiplicity, simulation and missingness plan frozen |
| Parser | deterministic schema validation tests pass |
| Audit | no unresolved Critical design issue; Major issues resolved or owner-accepted |

## Development sequence

### D0 — Item and rubric construction

- construct candidate baseline worlds, `S` blocks and `I` blocks;
- assign template IDs and domain/difficulty strata;
- run independent adjudication without model outputs;
- revise or replace failed candidates;
- freeze the 120 accepted-family roster only after the rubric passes.

### D1 — Parser-only synthetic checks

Use manually constructed synthetic JSON examples, not model outputs, to test:

- normalization tolerance;
- range checks;
- tie handling;
- action/support consistency;
- malformed classification;
- missing-cell bounds.

### D2 — Authorized model-facing development pilot

Only after a later execution authorization, use 8 development families per the approved 360-call allocation. The pilot may diagnose:

- schema compliance;
- gross ceiling/floor behavior;
- token/cost estimates;
- evidence/wrapper distinguishability;
- failure and latency rates.

Pilot results may trigger a documented protocol revision. They may not be combined with confirmatory results.

## Confirmatory execution tree

For each accepted item-model pair:

1. Send the baseline prompt once and preserve the complete raw response.
2. Create exact replay contexts for `S-N`, `S-P`, `I-N`, `I-P`, and `C-N`.
3. Execute the five Turn-1 nodes in a deterministic randomized order generated from `run_seed`, model ID and item ID.
4. Preserve every Turn-1 raw response before parsing.
5. Replay each exact factorial parent into its Turn-2 `N` and `P` children.
6. Continue the control into `C-NN`.
7. Execute Turn-2 nodes in a separately generated deterministic randomized order.
8. Preserve raw responses, errors, timestamps, parameters and parser results.

No branch may inherit another branch's response except through its specified exact parent.

## Randomization and balancing

- Correct-option labels are balanced across substantive positions within domain.
- Branch execution order is randomized within item-model pair.
- Provider/model run order is blocked by item batches so time drift is not perfectly confounded with one provider.
- The exact-repeat/paraphrase validation subset of 24 confirmatory families is selected before confirmatory outcomes are inspected: 12 per domain, balanced across template IDs and target positions.
- Seeds and selection code are preserved.

## Model settings

The following must be fixed for each model snapshot before execution:

- provider and exact model ID/snapshot;
- endpoint and API version;
- temperature and any top-p/top-k controls;
- maximum output tokens;
- system/developer message content;
- structured-output mechanism, if supported;
- safety settings and region;
- retry/timeout policy.

Settings need not be numerically identical across providers when APIs differ, but the intended sampling regime must be comparable and deviations documented.

The design targets a low-variance deployment evaluation. Exact-repeat runs quantify residual provider/model nondeterminism. Repeats are not independent item families.

## Retry policy

The future locked protocol must distinguish:

- **transport retry:** allowed only for timeout, connection or provider server error; same request bytes and parameters; maximum retry count fixed before execution;
- **rate-limit retry:** allowed after provider-directed backoff; logged as the same logical call;
- **content retry:** prohibited for malformed, inconsistent, refusal or undesirable substantive answers.

All attempts are retained. A retry never overwrites the first attempt.

## Data record requirements

Each logical call records:

- unique run and call IDs;
- parent call ID;
- item, domain and template IDs;
- condition/path and turn;
- prompt/evidence/wrapper/schema versions;
- exact messages sent;
- raw provider response;
- provider request/response metadata where available;
- parsed support, action and top option;
- compliance state;
- timestamps, latency, errors and retries;
- model snapshot and sampling parameters;
- code/version identifier.

Raw and processed records remain separate. Raw records are immutable.

## Confirmatory exclusions

### Pre-treatment exclusions

Only adjudication failures identified before model execution may remove an item from the confirmatory roster. Replacement occurs before model calls.

### Post-response missingness

No treatment-response content causes an item to disappear silently.

- `delta_m_CC` uses families with valid support in all four Turn-1 factorial cells.
- all 96 families enter the worst-case bound analysis;
- malformedness, refusal and transport failure are reported per cell;
- exclusions and logical-call retries are enumerated.

If fewer than 86 families are complete for a model, the model fails the confirmatory completeness gate. Its estimate remains reportable as limited/inconclusive, not silently reclassified as confirmatory.

## Validation runs

### Exact repeat

- 24 prespecified confirmatory families;
- same snapshot, prompt version and parameters;
- one complete 15-call tree per item/model;
- outcome: item-level interaction stability, cell-support absolute differences and action agreement.

### Wrapper paraphrase

- same 24-family subset;
- semantically matched but held-out `N/P` wrapper version;
- evidence blocks and answer options unchanged;
- outcome: sign and magnitude stability of the primary interaction and cell means.

The paraphrase run tests wording robustness; it is not treated as a second exact repeat.

## Stop/go rules

Stop and request owner direction if:

- a review requires a material change to the 15-call design, 96 items or 6,840 planned-call target;
- official-price preflight exceeds USD 60 for any model or USD 250 overall;
- fewer than 96 items pass adjudication without expanding the planned human workload materially;
- named adjudicators or credentials remain unavailable when execution authorization is requested;
- simulation shows <80% power for the SESOI under the owner-approved planning variance and no in-scope remedy exists;
- an unresolved Critical design issue is found.

## Prohibited actions under current authorization

- final prompt lock;
- any paid API request;
- any main or pilot model execution;
- collection of confirmatory model outputs;
- paper drafting.
