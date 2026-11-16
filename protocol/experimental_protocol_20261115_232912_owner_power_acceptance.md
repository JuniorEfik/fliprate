# FlipRate Experimental Protocol — Stage 2 Draft

## Material Passport

- Origin Skill: experiment-plan + experiment-agent
- Origin Mode: plan
- Origin Date: 2026-11-15
- Verification Status: ANALYZED
- Version Label: fliprate_experimental_protocol_v0.5

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
| Power disposition | owner acceptance of the observed sub-80% power is recorded; the original 80% criterion remains failed and the study is classified as lower-powered exploratory |
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

The eight-family pilot is diagnostic, not a certification of 1–2% failure rates or `SD <= 0.15`. Report exact binomial uncertainty for compliance and uncertainty for the interaction SD. Zero observed failures does not establish high compliance. A favorable point estimate may not convert an inconclusive nuisance estimate into a readiness PASS; any larger pilot, item-count change, or sensitivity tradeoff returns to the owner.

The synthetic 98.3347% per-cell threshold at 1% shared failure assumes independent family retention and equal, conditionally independent cell validity after the shared failure component. It does not apply unchanged to provider-wide batches, template-correlated formatting failures or concentrated outages. Those mechanisms are reported separately and remain empirical uncertainties; the development pilot cannot certify their absence.

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

## Parent-state and replay policy

The runner must classify every parent before scheduling descendants. It may never invent assistant text, omit a failed turn from history, or resample a parent to obtain a more convenient response.

| Parent state | Replayable assistant content? | Descendant policy | Primary record |
|---|---|---|---|
| Schema-valid response | Yes | Run specified children with exact assistant content. | Parsed fields plus immutable raw response. |
| Malformed but textual response | Yes | Run specified children with exact assistant content; parent support may be missing. | `malformed_*` flags plus immutable raw response. |
| Textual refusal returned as assistant content | Yes | Run specified children with the exact refusal text. | `refusal_text` flag; any valid structured fields remain separately eligible. |
| Provider refusal with metadata only and no assistant content | No | Do not run descendants; mark each `ancestor_unavailable`. | Provider metadata and all attempts. |
| Exhausted transport/rate-limit failure with no assistant content | No | Do not run descendants; mark each `ancestor_unavailable`. | Terminal error and all attempts. |

For retries, the first transport-successful response is the logical-call response even if its content is malformed or undesirable. All attempts are retained. If no attempt returns replayable assistant content, the terminal state propagates deterministically to descendants. Skipped descendants are not replacement calls and do not free budget for selective reruns.

Replayable content is the exact provider-visible assistant message content used by the next request. Request IDs, token accounting, safety annotations, hidden reasoning and other provider metadata are stored but are not inserted into the conversation unless the provider's documented API requires a replayable public field. Provider adapters must demonstrate this capability before execution readiness.

## Randomization and balancing

- Correct-option labels are balanced across substantive positions within domain.
- Branch execution order is randomized within item-model pair.
- Provider/model run order is blocked by item batches so time drift is not perfectly confounded with one provider.
- The exact-repeat/paraphrase validation subset of 24 confirmatory families is selected before confirmatory outcomes are inspected: one family from each of 24 distinct templates, 12 per domain. If the frozen frame contains more than 12 templates in a domain, 12 templates and then one eligible family within each are chosen by recorded seeded random selection while preserving target-position balance.
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

Models failing the completeness gate remain in the three-model Holm family with confirmatory p-value fixed to `1`; they are not removed to make the remaining tests easier to reject. Ancestor-unavailable states, cell-level failures and replayable malformed parents are reported separately.

## Validation runs

### Exact repeat

- 24 prespecified confirmatory families;
- same snapshot, prompt version and parameters;
- one complete 15-call tree per item/model;
- comparison population: the same prespecified 24 main-run families with valid paired cells in both runs;
- minimum interpretable denominator: at least 20 paired complete families overall and at least 8 per domain; otherwise the validation result is inconclusive;
- outcome: paired item-level interaction stability, cell-support absolute differences, action agreement and uncertainty for the run difference.
- decision: Holm-controlled paired TOST against `[-0.05,0.05]`, with `EQUIVALENT`, `INCONCLUSIVE`, or `UNSTABLE` status under the analysis plan.

### Wrapper paraphrase

- same 24-family subset;
- semantically matched but held-out `N/P` wrapper version;
- evidence blocks and answer options unchanged;
- comparison population and denominator: the same paired eligibility rule as the exact repeat;
- outcome: sign and magnitude stability of the primary interaction and cell means, interpreted as total workflow robustness to one held-out wrapper pair.
- decision: a separate three-model Holm-controlled paired TOST family against `[-0.05,0.05]`.

The paraphrase run regenerates the branch histories under the held-out wrappers. It tests total workflow robustness to that specific wrapper pair; it is not treated as a second exact repeat or broad evidence of wording invariance.

Affected-model CR1/Holm power is estimated at **72.24% ± 0.63%** in the 5,000-replication single-active 0.05 anchor. Because CR1/Holm rejection is required by the full claim rule, true full-rule power cannot exceed true CR1/Holm component power; the more precise component estimate is below 80%. The exact full gate passed in **75.0% ± 3.1%** of the smaller 200-dataset bootstrap subset; that imprecise estimate does not override the component result. On 2026-11-15, the owner accepted this lower power as a documented limitation and preserved the corpus, SESOI, estimand, CR1/Holm procedure and call envelope. The 80% criterion remains failed, the study is lower-powered exploratory, and this disposition does not authorize implementation or execution.

## Stop/go rules

Stop and request owner direction if:

- a review requires a material change to the 15-call design, 96 items or 6,840 planned-call target;
- official-price preflight exceeds USD 60 for any model or USD 250 overall;
- fewer than 96 items pass adjudication without expanding the planned human workload materially;
- named adjudicators or credentials remain unavailable when execution authorization is requested;
- later evidence materially worsens the accepted sensitivity assumptions or would require changing the frozen 15/96/6,840 design, SESOI, estimand or multiplicity rules;
- an unresolved Critical design issue is found.

## Prohibited actions under current authorization

- final prompt lock;
- any paid API request;
- any main or pilot model execution;
- collection of confirmatory model outputs;
- paper drafting.
