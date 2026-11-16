# Experiment Tracker

| Run ID | Milestone | Purpose | System / Variant | Split | Metrics | Priority | Status | Notes |
|---|---|---|---|---|---|---|---|---|
| S2-DOC-001 | M0 | Formal protocol | 15-call shared-parent design | design | completeness against owner requirements | MUST | PASS | Design-audit specification complete with documented limitations; no prompts locked. |
| S2-STAT-001 | M0 | Raw-scale SESOI | 0.05 support points | design | interpretability and sensitivity | MUST | DONE | Policy threshold, not community standard. |
| S2-STAT-002 | M0 | Multiplicity | CR1/Holm primary and equivalence families; BY secondary | design | FWER/FDR | MUST | DONE | Failed-gate tests remain in Holm with p=1; 13 serial and 3 domain tests use cluster-aware inference. |
| S2-SIM-001 | M0 | Power/completeness | 20,000 legacy + 5,000 item-level reps, seed 20261115 | synthetic | CR1/bootstrap calibration, power, coverage, bounds, gate probability | MUST | FAIL — OWNER-ACCEPTED LIMITATION | Single-active CR1/Holm power 72.24% ± 0.63%; original 80% target remains unmet; study classified lower-powered exploratory. |
| S2-ADJ-001 | M0 | Adjudication operations | staged A/B/C workflow | design | agreement, applicability, pair matching and workload | MUST | PASS — OPERATIONS BLOCKED | Planning requirement passes; personnel and timed calibration remain blocked. |
| S2-AUD-ARIS | M0 | First ARIS protocol review | independent same-family/provisional reviewer | Stage-2 files | adversarial design verdict | MUST | REVISE — INCORPORATED | Raw review saved; fresh blind re-review required. |
| S2-AUD-ARS | M0 | First ARS methodological challenge | blind to ARIS response | Stage-2 files | independent issue log | MUST | REVISE — INCORPORATED | Raw report must be preserved; fresh blind re-review required. |
| S2-AUD-ARIS-R2 | M0 | ARIS protocol re-review | focused GPT-6.1-sol fallback verification | revised Stage-2 files | independent readiness verdict | MUST | PASS WITH LIMITATIONS — PROVISIONAL | Requested Astra route failed before review with HTTP 402; report and trace preserved. |
| S2-AUD-ARS-R2 | M0 | ARS methodological re-challenge | focused blind GPT-6.1-sol fallback verification | revised Stage-2 files | independent issue log | MUST | PASS WITH LIMITATIONS — PROVISIONAL | Reviewer remained blind to ARIS responses; report and trace preserved. |
| S2-READY-001 | M0 | Provider/budget/personnel | public docs + environment presence | readiness | PASS/FAIL/BLOCKED | MUST | BLOCKED | Economic plausibility passes; credentials, funding, snapshots, staffing and schedule remain blocked. |
| S2-OWNER-POWER | M0 | Resolve power tradeoff | current 96-family design | decision | accept lower power or authorize scoped redesign | MUST | PASS — LOWER POWER ACCEPTED | Owner preserved 15 calls, 96 confirmatory families, 6,840 calls, SESOI, estimand and CR1/Holm; no further power optimization authorized. |
| S2-CORPUS-001 | M1 | Construct/adjudicate corpus | 24 development + 96 confirmatory | item families | rubric gates and agreement | MUST | BLOCKED | Named personnel/funding absent. |
| S2-PARSER-001 | M2 | Synthetic schema tests | hand-built JSON only | development | parser compliance | MUST | NOT AUTHORIZED | Implementation outside current scope. |
| S2-PILOT-001 | M3 | Estimate SD/compliance/cost | 8 development families × 3 models | development | SD, validity, tokens, latency | MUST | BLOCKED | Requires explicit owner authorization and credentials. |
| S2-MAIN-001 | M4 | Primary interaction | 96 families × 3 models | confirmatory | `delta_m_CC`, cells, bounds | MUST | BLOCKED | Main execution prohibited. |
| S2-VAL-REP | M5 | Exact repeat | 24 families × 3 models | validation | repeat stability | MUST | BLOCKED | Depends on main authorization. |
| S2-VAL-PAR | M5 | Wrapper paraphrase | 24 families × 3 models | validation | wording robustness | MUST | BLOCKED | Depends on main authorization. |
| S2-PROVIDER-ACCESS | readiness | Credentials and model availability | OpenAI / Anthropic / Google | accounts | credential presence, exact snapshots, limits | MUST | BLOCKED | Checked credential variables are absent; account-level availability is unverified. |
| S2-BUDGET-AUTH | readiness | Funded execution budget | USD 250 proposed ceiling | finance | funding and payment authority | MUST | BLOCKED | Price arithmetic is plausible; no funded authority is evidenced. |
| S2-PERSONNEL | readiness | Staff adjudication workflow | constructor(s), A/B, C, coordinator | personnel | commitments, qualifications, schedule | MUST | BLOCKED | No named or committed team and no timed calibration. |
| S2-EVIDENCE-PACKAGES | readiness | Complete accepted packages and rosters | 24 development + 96 confirmatory | corpus | proofs, ratings, adjudications, frozen roster | MUST | BLOCKED | No completed accepted roster or rating package set found. |
| S2-OPS-QA | readiness | Operational/data-quality validation | parser, replay, storage, randomization | synthetic fixtures | deterministic checks | MUST | BLOCKED | Specified prospectively but implementation and validation remain unauthorized. |
| S2-EXEC-AUTH | readiness | Separate execution authorization | owner decision | governance | explicit scope and caps | MUST | BLOCKED | Current decision is not execution authorization. |
