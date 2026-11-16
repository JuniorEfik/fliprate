# FlipRate Provider, Budget and Personnel Readiness Assessment

**Date checked:** 2026-11-15 15:44 WAT  
**Scope:** Stage-2 readiness assessment only  
**Execution status:** no model endpoint called; no paid API request made

## Executive assessment

The planned call and token envelope is economically plausible under the proposed USD 250 ceiling, but execution readiness is **BLOCKED**. Official pricing pages are reachable and candidate price points fit the per-model threshold. No relevant provider credential is configured, no funded budget is evidenced, exact model snapshots and rate limits are not confirmed, and the required adjudication personnel are unnamed.

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

Estimated labor remains 98–131 person-hours:

- construction/rework: 50–75 hours;
- double independent rating: 40–48 hours;
- adjudication: up to 8 hours.

A plausible non-sprint schedule is four to six weeks with parallel role coverage. For example, two constructors would each carry roughly 25–38 construction hours, two reviewers roughly 20–24 rating hours each, and C up to 8 adjudication hours. This is a workload scenario only; no person has accepted it.

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

No provider prerequisite in this assessment authorizes execution.
