# FlipRate Stage-2 Readiness Report

**Date:** 2026-11-15  
**Overall readiness:** **BLOCKED**  
**Design-audit state:** **PASS WITH LIMITATIONS**  
**Power disposition:** **OWNER ACCEPTED LOWER POWER; ORIGINAL TARGET REMAINS FAILED**  
**Study classification:** **LOWER-POWERED EXPLORATORY**  
**Execution authorization:** **NOT GRANTED**

> **Submission-preparation addendum (2026-11-16):** the owner later authorized documentation-only sprint submission preparation from existing artifacts. This does not alter any execution-readiness status below and does not authorize provider calls, prompt locking, experiments, completed adjudication or empirical results claims.

## Owner decision recorded

The owner formally accepts the current **72.24% ± 0.63% CR1/Holm power** as a documented limitation. The original 80% target is not met and is not waived or reclassified as passed.

The owner preserves:

- the research question, central constructs and hypotheses;
- the four-cell Turn-1 factorial comparison;
- the primary family-weighted complete-case estimand;
- the 0.05 SESOI;
- CR1/Holm multiplicity control and the registered claim gates;
- 15 calls per item-model tree;
- 96 confirmatory item families; and
- the 6,840-call planned envelope.

No further redesign or repeated optimization to reach 80% is authorized. Any eventual study must be described as lower-powered exploratory, despite retaining prospective confirmatory-style procedures.

## Eight owner requirements

| Owner requirement | Status | Evidence and consequence |
|---|---|---|
| **S2-DOC-001 — Formal protocol** | **PASS** | The design, replay rules, eligibility, claim gates and scope limits are specified. |
| **S2-STAT-001 — Raw-scale SESOI** | **PASS** | The prospective SESOI remains 0.05 support points. |
| **S2-STAT-002 — Multiplicity** | **PASS** | CR1/Holm difference and equivalence families, failed-gate p=1 handling and cluster-aware secondary families remain fixed. |
| **S2-SIM-001 — Power/completeness validation** | **FAIL** | The 80% criterion is not met: CR1/Holm power is 72.24% ± 0.63%. Owner acceptance records a limitation; it does not create a statistical PASS. |
| **S2-ADJ-001 — Adjudication operations plan** | **PASS** | The workflow and 184–296-hour planning range are specified. Actual operation remains blocked. |
| **S2-AUD-ARIS-R2 — ARIS protocol re-review** | **PASS** | Focused fallback review returned PASS WITH LIMITATIONS. |
| **S2-AUD-ARS-R2 — Blind ARS methodological re-challenge** | **PASS** | Focused blind fallback review returned PASS WITH LIMITATIONS. |
| **S2-READY-001 — Provider/budget/personnel readiness** | **BLOCKED** | Credentials, exact models, funded authority, personnel, accepted evidence packages and operational validation remain unresolved. |

Additional governance requirement:

| Requirement | Status | Basis |
|---|---|---|
| **S2-OWNER-POWER — Power disposition** | **PASS** | Lower power accepted, design preserved and exploratory classification mandated. |

## Execution-readiness prerequisites

| Prerequisite | Status | Current evidence | Evidence required to pass |
|---|---|---|---|
| Provider credentials | **BLOCKED** | `OPENAI_API_KEY`, `ANTHROPIC_API_KEY`, `GEMINI_API_KEY` and `GOOGLE_API_KEY` are absent. | Approved credentials available without exposing secret values. |
| Exact model availability | **BLOCKED** | No account-level access or snapshot IDs are confirmed. | Exact model IDs/snapshots, endpoint/API versions, regions and access dates. |
| Public pricing arithmetic | **PASS** | The locally preserved official-price check from 2026-11-15 places candidate and higher-price reference envelopes below the proposed USD 250 cap. | Recheck immediately before authorization because prices and billed-token rules can change. |
| Funded budget authority | **BLOCKED** | No funding commitment or payment authority is recorded. | Named budget owner and approved cap covering all billed token classes, taxes and retry contingency. |
| Rate limits and provider operations | **BLOCKED** | Account-level RPM/TPM, structured output, retention, safety, timeout and retry behavior are unverified. | Documented account settings or a separately authorized preflight/pilot. |
| Reviewer/adjudicator availability | **BLOCKED** | No named constructors, Reviewers A/B, Adjudicator C or coordinator are recorded. | Names/IDs, qualifications, conflicts, availability, compensation and schedule. |
| Timed calibration and adjudication capacity | **BLOCKED** | The 184–296-hour range is a planning estimate only. | Completed timed development calibration and a staffed calendar. |
| Evidence-package completion | **BLOCKED** | No completed accepted 24-development/96-confirmatory package set or frozen roster was found. | Versioned packages, proofs, A/B ratings, C adjudications and accepted/reserve/rejected rosters. |
| Institutional determination | **BLOCKED** | No applicable ethics/employment/data-protection record is present. | Owner/institutional documentation appropriate to the staffing arrangement. |
| Parser/schema validation | **BLOCKED** | Schema rules are specified, but implementation and synthetic-fixture tests are not authorized or complete. | Deterministic local validation after separate implementation authorization. |
| Parent replay and failure propagation | **BLOCKED** | Behavior is specified prospectively, not demonstrated against provider adapters. | Replay-capability tests and immutable raw-record checks after implementation authorization. |
| Randomization, storage and provenance pipeline | **BLOCKED** | Seeds and required records are specified; no operational pipeline exists. | Verified deterministic scheduling, raw-response storage, checksums and audit logs. |
| Final prompt/model lock | **BLOCKED** | Explicitly unauthorized. | Later versioned lock after all applicable readiness gates and owner approval. |
| Model-facing pilot/main execution | **BLOCKED** | Explicitly unauthorized. | Separate written owner authorization identifying scope, models, budget and stop rules. |

## What is ready

- Research question, constructs, hypotheses and anti-claims.
- Fixed 15-call/96-family/6,840-call design.
- Primary estimand, SESOI, CR1/Holm inference and claim gates.
- Missingness bounds, template sensitivities and validation-subset rules.
- Adjudication procedure and workload estimate.
- Synthetic simulation artifacts, provenance hashes and design audit.
- Owner disposition of the failed power target.

## What remains blocked

- Provider/account access and exact model snapshots.
- Funded execution budget.
- Named and available personnel.
- Completed evidence packages, ratings, adjudications and frozen rosters.
- Timed calibration and capacity confirmation.
- Institutional determination.
- Authorized implementation and deterministic operational/data-quality validation.
- Final prompt/model lock.
- Separate execution authorization.

## Readiness for an execution-authorization decision

**The project is not yet ready for an execution-authorization decision.** The statistical power disposition is resolved, but required external, corpus, staffing and operational evidence is still missing.

The next permitted phase is execution-readiness preparation only. No provider/model calls, API spending, pilot/main execution, confirmatory data collection, final prompt locking or paper writing may begin without a separate explicit owner authorization.
