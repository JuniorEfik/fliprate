# FlipRate Provider, Budget and Personnel Readiness Assessment

**Date checked:** 2026-11-15; credentials rechecked during owner-decision closure  
**Scope:** Stage-2 readiness assessment only  
**Execution status:** no model endpoint called; no paid API request made

## Executive assessment

The planned call and token envelope remains economically plausible under the proposed USD 250 ceiling, but execution readiness is **BLOCKED**. The latest locally preserved official-price check is from 2026-11-15 15:44 WAT; it was not refreshed through provider calls during this closure. No relevant provider credential is configured, no funded budget is evidenced, exact model snapshots and rate limits are not confirmed, accepted evidence-package rosters are absent, and the required adjudication personnel are unnamed.

Affected-model CR1/Holm power is estimated at **72.24% ± 0.63%** in the 5,000-replication single-active 0.05 anchor, below the prespecified 80% target. The owner has accepted this as a documented lower-powered exploratory limitation and preserved the 15/96/6,840 design. The statistical target remains failed; the owner-decision gate is resolved. This decision does not improve provider, budget, personnel, evidence-package or operational readiness.

## Provider checks

Headless Chrome was used only to read official documentation.

| Provider | Official source | Observed candidate pricing per 1M tokens | Access state |
|---|---|---|---|
| OpenAI | <https://developers.openai.com/api/docs/pricing> | `gpt-6.1-sol`: USD 2 input / USD 10 output; `gpt-6-astra`: USD 10 input / USD 50 output. | Documentation reachable; account/model access unverified. |
| Anthropic | <https://platform.claude.com/docs/en/about-claude/pricing> | Claude Sonnet 5.5: USD 2 input / USD 10 output; Claude Fable 5.2: USD 8 input / USD 40 output. | Documentation reachable; account/model access unverified. |
| Google | <https://ai.google.dev/gemini-api/docs/pricing> | Gemini 4 Argon/Carbon: USD 2 input / USD 10 output through 2026-11-30, then USD 4 input / USD 20 output from 2026-12-01. | Documentation reachable; account/model access unverified. |

Prices are observations on the check date, not a lock. Google explicitly publishes a scheduled increase. Exact model IDs, snapshots, regions, safety settings, structured-output support, context limits and reasoning-token behavior must be rechecked immediately before any later execution authorization.

## Credential presence

Only variable presence was checked; no secret value was printed or stored.

| Environment variable | State |
|---|---|
| `OPENAI_API_KEY` | not configured |
| `ANTHROPIC_API_KEY` | not configured |
| `GEMINI_API_KEY` | not configured |
| `GOOGLE_API_KEY` | not configured |

Credential readiness is therefore **BLOCKED**.

## Budget calculation

Approved planning envelope:

- 6,840 logical calls before transport retries;
- approximately 7,800 hard operational ceiling;
- 4–6 million aggregate input tokens;
- less than 1 million aggregate output tokens;
- three providers/models with approximately equal call counts.

For a conservative per-model calculation, allocate 2.0M input tokens and 0.333M output tokens to each model.

| Reference selection | Input cost | Output cost | Estimated model total |
|---|---:|---:|---:|
| OpenAI `gpt-6.1-sol` at 2/10 | USD 4.00 | USD 3.33 | USD 7.33 |
| Anthropic Claude Sonnet 5.5 at 2/10 | USD 4.00 | USD 3.33 | USD 7.33 |
| Google Gemini 4 Argon after scheduled increase at 4/20 | USD 8.00 | USD 6.67 | USD 14.67 |
| **Balanced candidate total** |  |  | **USD 29.33** |

A higher-price reference envelope also remains below the proposed thresholds:

| Higher-price reference | Estimated model total |
|---|---:|
| OpenAI `gpt-6-astra` at 10/50 | USD 36.67 |
| Anthropic Claude Fable 5.2 at 8/40 | USD 29.33 |
| Google Gemini 4 Carbon after scheduled increase at 4/20 | USD 14.67 |
| **Higher-price total** | **USD 80.67** |

The higher-price total with 25% contingency is approximately USD 100.84, below the proposed USD 250 ceiling and below USD 60 per model. This arithmetic does not establish that the budget is funded or that hidden reasoning tokens, provider retries, taxes or currency charges fit the envelope. A future preflight must use measured token counts from an authorized development pilot and include all billed token classes.

## Rate-limit and operational readiness

Unverified items:

- exact model/snapshot availability to the eventual accounts;
- requests-per-minute and tokens-per-minute limits;
- regional endpoint availability;
- structured-output behavior and support for fixed low-variance settings;
- provider retention/privacy settings;
- safety-filter and refusal behavior;
- treatment of hidden reasoning tokens;
- timeout, retry and batch constraints.

These checks require credentials or owner/account evidence and cannot be inferred from public pricing pages.

## Personnel plan

Required role coverage:

- constructor(s) for 120 accepted families plus reserve candidates;
- two independent reviewers;
- a third adjudicator;
- a coordinator for randomization, version control and agreement reporting.

The current planning range is **184–296 person-hours**, excluding an unexpected template-wide reopening:

| Activity | Estimated hours |
|---|---:|
| Construction and formal proofs | 45–70 |
| Package preparation and S/I form matching | 18–30 |
| Reviewer calibration and training | 8–14 |
| Independent single-block ratings | 64–96 |
| Independent pair-form checks | 16–24 |
| Third adjudication | 6–10 |
| Rerating after revisions | 12–24 |
| Stratified re-audit | 3–8 |
| Coordination, versioning and agreement reporting | 12–20 |

The 480 single-block ratings assume approximately 8–12 minutes each; the 240 pair-form checks assume approximately 4–6 minutes each. Timed calibration must replace these planning assumptions before staffing or schedule receives a PASS.

A four-to-six-week schedule remains only a possible planning scenario with parallel role coverage. No person or calendar has committed to it.

The following are unconfirmed:

- names and qualifications;
- availability and schedule;
- compensation or volunteer status;
- conflict-of-interest separation;
- institutional ethics/employment/data-protection determination;
- ownership of coordination and quality control.

Personnel readiness is therefore **BLOCKED**.

## Readiness verdicts

| Requirement | Verdict | Basis |
|---|---|---|
| Official pricing documentation reachable | PASS | All three official pages retrieved by headless Chrome. |
| 6,840-call envelope economically plausible | PASS | Both candidate and higher-price reference calculations fit proposed caps. |
| Exact model snapshots selected and accessible | BLOCKED | No account access or model IDs confirmed; prompt/model lock prohibited. |
| Provider credentials configured | BLOCKED | All checked variables absent. |
| Funded API budget | BLOCKED | No funding commitment or payment authority evidenced. |
| Rate limits and operational settings | BLOCKED | Require account-level checks or an authorized pilot. |
| Named adjudication personnel | BLOCKED | No names, qualifications or commitments recorded. |
| Feasible schedule | BLOCKED | Workload is bounded but no team/calendar is committed. |
| 80% single-active-model power target | FAIL | The CR1/Holm component is estimated at 72.24% ± 0.63%; the owner accepted the failure as an exploratory limitation, not as a PASS. |
| Owner power disposition | PASS | Lower power accepted; design frozen at 15 calls, 96 confirmatory families and 6,840 planned logical calls. |
| Completeness planning threshold | SPECIFIED; EMPIRICAL VALIDATION BLOCKED | At 1% shared failure, at least 98.3347% equal per-cell validity is required for 90% gate passage; actual provider compliance is unknown. |
| Evidence-package and accepted-roster completion | BLOCKED | No completed 24-development/96-confirmatory accepted roster or A/B/C rating records were found in the workspace. |
| Parser/replay/storage data-quality validation | BLOCKED | Procedures are specified, but implementation and deterministic validation are not authorized or completed. |
| Separate execution-authorization readiness | BLOCKED | Multiple external and operational prerequisites remain unresolved. |

No provider prerequisite in this assessment authorizes execution.
