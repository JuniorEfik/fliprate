# FlipRate — Round-2 Blind Methodological Verification

**Verdict: PASS WITH LIMITATIONS for design-audit readiness. Execution remains BLOCKED.**

This is a focused follow-up by the same blinded **GPT-6.1-sol same-family/provisional fallback reviewer** who produced the round-1 report. I read the current specified files and verified the two final local clarifications. I did not read any ARIS response, trace, or another reviewer's output. I made no edits and ran no simulation, model/provider call, implementation, prompt lock, or paper-writing task.

Verification consisted of source inspection and read-only comparisons of stored results, summary values, Monte Carlo standard errors, and file hashes. **This favorable design review does not authorize execution.**

## Round-1 issue dispositions

“RESOLVED” means the design correction is verified. It does not establish empirical provider compliance, adjudication performance, or model behavior.

| Round-1 finding | Status | Current evidence and judgment |
|---|---|---|
| Critical findings | **None established** | No new evidence establishes a fatal methodological flaw or fabricated model results. |
| **M1: Failed power target and unresolved owner decision** | **OPEN — owner decision required** | `experimental_protocol.md:222–232`, `simulation_report.md:118–141`, and `EXPERIMENT_TRACKER.md:15` preserve the FAIL. The current confirmatory CR1/Holm power is 72.24% ± 0.63 percentage points. No acceptance of lower power or authorized redesign is evidenced. |
| **M2: Undefined construction population/exchangeability** | **RESOLVED, conditionally** | `benchmark_specification.md:68–73` defines outcome-blind template freezing, candidate adjudication, seeded selection, independent-cluster assumptions, and model-based repeated-construction inference. `analysis_plan.md:20–22,90–107` makes CR1 target the family-weighted mean. Designed templates are explicitly distinguished from a probability sample of all reasoning templates. |
| **M3: Incomplete template protection for equivalence/secondary tests** | **RESOLVED** | `analysis_plan.md:127` specifies CR1 TOST and representation gates; lines 147 and 157 specify cluster-aware serial and domain tests. `experimental_protocol.md:130` and `analysis_plan.md:219` require 24 distinct validation templates and provide clustered inference if that allocation is violated. |
| **M4: Simulation omitted the complete rule and mismatched coverage targets** | **RESOLVED at the stated synthetic-validation level** | The simulator now applies family/template gates, CR1/Holm, leave-one-template-out, and same-direction simultaneous bootstrap intervals (`power_completeness_sim.py:1067–1097,1155–1161,1209–1224`). Coverage uses a separately recorded Monte Carlo complete-case target (`1268–1337`). A ceiling-heavy observed-scale-null scenario is included (`436–461`). Endpoint inference is restricted following failed coverage rather than promoted to a claim (`analysis_plan.md:196–205`). |
| **D1: Two-answer versus three-answer baseline gates** | **RESOLVED** | `benchmark_specification.md:79,92`, `scoring_rubric.md:45`, and `adjudication_plan.md:109` consistently require three compatible substantive answers. |
| **D2: UNCERTAIN confused agreement with referral** | **RESOLVED** | `scoring_rubric.md:60,84` and `adjudication_plan.md:156` distinguish categorical agreement, PASS/non-PASS agreement, and mandatory referral. The pause-rule coding is explicit. |
| **D3: Completeness threshold lacked its independence boundary** | **RESOLVED as specification; empirical uncertainty retained** | `experimental_protocol.md:92` and `simulation_report.md:165–185` state the binomial assumptions and their limits. The simulator adds template-correlated failures (`614–618,668–679`). |
| **D4: C's re-audit overstated blind independence** | **RESOLVED** | `adjudication_plan.md:165` excludes C's earlier cases where possible, discloses unavoidable overlap as a non-independent recheck, and prefers a fresh reviewer for overlapped cases. |
| Minor: Stale “Stage 2 must not start” sentence | **RESOLVED** | `research_proposal.md:240` now distinguishes active design/audit work from gated implementation and execution. |
| Minor: Unspecified sign-flip diagnostic | **RESOLVED** | `analysis_plan.md:101` specifies absolute sample skewness ≤1 and makes the result exploratory, unable to change confirmation. |
| Minor: Missing runtime/hashes | **RESOLVED for provenance specification** | `simulation_summary.json:3–4,151–155` and `simulation_report.md:6,80–86` record Python and hashes. The current hashes match the files inspected. Independent simulation reproduction remains unperformed in this review. |

**DA decisions:** M1 remains held because no owner decision is evidenced. The remaining concessions are based on direct source changes addressing the original findings, rather than assurances that they were fixed.

## Complete prospective decision rule

The current unqualified primary claim requires:

1. At least 86 four-cell-complete families.
2. At least 20 represented templates overall and 10 per domain.
3. CR1/Holm rejection.
4. A simultaneous 98.333% whole-template bootstrap interval excluding zero in the same direction.
5. No leave-one-template-out reversal accompanied by an absolute shift exceeding 0.05.

These requirements are stated at `analysis_plan.md:109–115` and represented in the simulator's gate logic.

The final clarification at `analysis_plan.md:117` resolves an ambiguity found during this round: an ordinary item result blocks an unqualified claim when it rejects but CR1/Holm does not. A merely smaller ordinary-item p-value or narrower interval does not create an additional gate when the five requirements pass.

The summary's power-PASS flag now requires both the CR1 component and full-gate subset estimates to reach 0.80 (`power_completeness_sim.py:1869–1872`). The current flag remains **false**. A noisy bootstrap-subset estimate can no longer override a failed required component.

No unresolved Critical or Major implementation/specification mismatch was established in this rule.

## Numerical and provenance checks

The current item-level CSV contains **51 rows covering 17 scenarios and three models**, with 92 columns. Every field in the summary's single-active anchor matches its CSV row. The checked rejection-rate standard errors reproduce the stated binomial Monte Carlo calculations.

| Check | Stored result | Judgment |
|---|---:|---|
| Independent-null CR1/Holm FWER | 4.34% | Compatible with 5% in the tested generator. |
| ICC 0.10 null CR1/Holm FWER | 4.72% | Compatible with 5% in the tested generator. |
| Calibrated ceiling-null CR1/Holm FWER | 4.34% | Addresses the earlier observed-scale-null gap. |
| Heterogeneous-template null CR1/Holm FWER | 0.24% | Strong conservatism; not exact calibration. |
| ICC 0.10 ordinary item/Holm FWER | 9.68% | Correctly retained as a failed dependence-naive diagnostic. |
| Single-active CR1/Holm power | 72.24% ± 0.63 points | **FAIL versus 80%.** |
| Full gate on 200-dataset subset | 75.0% ± 3.06 points | Imprecise; does not overturn the power FAIL. |
| Single-active CR1/Holm power, ICC 0.10 | 59.12% | Material sensitivity limit. |
| Single-active CR1/Holm power, template-correlated failure | 55.64% | Material sensitivity limit. |
| Central fixed-roster bounds crossing zero | 34.08% | Completeness does not identify the all-family sign. |
| Template-correlated endpoint coverage | 78.57% / 79.59% | Supports restricting these intervals to descriptive use. |

The 75% subset estimate exceeding the 72.24% component estimate is not a logical contradiction: they use different replication denominators. Within any dataset, full-gate passage necessarily implies CR1/Holm rejection.

Strictly, the mathematical relationship is **P(full gate) ≤ P(CR1 rejection)**. The 72.24% value estimates the latter probability; it is not an uncertainty-free population bound. Its approximate 95% Monte Carlo interval is **71.00%–73.48%**, still comfortably below 80%. This wording refinement does not change the decision.

I verified the current simulator SHA-256:

`a44a49916f575b050d0f9c4087c45fe5f4462e2d97d2dc159f96992bcc219873`

It matches both summary and report. The recorded output hashes also match; the item-level CSV remains:

`059955b367b052794a24a15ffbbd9aa2aad111d57bd1e56809a6c3f9db3374b6`

## Remaining limitations

- **Model-based inference remains assumption-dependent.** Independent template clusters and the registered construction process are explicit assumptions, not empirically established facts.
- **Full-gate simulation precision remains limited.** It uses 200 outer datasets and 499 bootstrap resamples, whereas the prospective analysis specifies 20,000 resamples. The code represents the rule, but the stored operating characteristics approximate the eventual bootstrap procedure.
- **Coverage targets are Monte Carlo estimates from the simulated ensemble.** This is stronger than using the full-roster mean for selected-case coverage, but it remains synthetic validation rather than a general coverage proof.
- **Endpoint-bootstrap coverage failed.** The resulting restriction to exact finite-roster sign/SESOI claims is appropriate. Construction-frame all-family endpoint claims remain prohibited.
- **Repeat/paraphrase equivalence concerns mean interaction drift on paired eligible families.** It does not establish individual-item agreement, general wording invariance, or stability across future snapshots.
- **Operational prerequisites remain absent.** Public-price arithmetic does not establish funded access, replay-capable adapters, personnel commitments, or a feasible calendar.

These limitations do not require reopening the basic design. They must remain visible through later locking, implementation, and results interpretation.

## Eight M0 owner requirements

| Requirement | Judgment | Basis |
|---|---|---|
| Formal protocol — S2-DOC-001 | **PASS WITH LIMITATIONS** | The reviewed specification is coherent for design audit; its model-based assumptions and later lock requirements remain explicit. |
| Raw-scale SESOI — S2-STAT-001 | **PASS** | 0.05 is prospective, interpretable, and labeled a policy threshold rather than a community standard. |
| Multiplicity — S2-STAT-002 | **PASS** | CR1/Holm difference and equivalence families, failed-gate p=1 rules, and cluster-aware BY secondary families are specified. |
| Power/completeness — S2-SIM-001 | **FAIL for the power target** | Synthetic validation is completed sufficiently to expose the failure. Completeness arithmetic passes conditionally; 80% single-active full-gate power does not. |
| Adjudication operations — S2-ADJ-001 | **PASS for planning; operationally BLOCKED** | Gates, agreement coding, blinding, rechecks and workload are specified. Named personnel and timed calibration are absent. |
| ARIS protocol review — S2-AUD-ARIS / R2 | **BLOCKED for this reviewer's attestation** | Strict blinding prevents verification of the ARIS verdict. The owner must reconcile that separate review; this is not a finding that it failed. |
| ARS methodological challenge — S2-AUD-ARS / R2 | **PASS WITH LIMITATIONS** | This focused blind verification is completed; no unresolved Critical or Major design correction was established. |
| Provider/budget/personnel — S2-READY-001 | **BLOCKED** | Access, exact snapshots, rate limits, funding, staffing and schedule remain unconfirmed. |

## Stress-test conclusion

| Stress test | Outcome |
|---|---|
| Remove optimistic equal-effect results | The single-active power target still fails. |
| Introduce template dependence | CR1 protects the same estimand in tested nulls; power declines substantially. |
| Require every prospective claim gate | No favorable component can substitute for full passage. |
| Introduce correlated failures | Completeness and endpoint behavior deteriorate; explicit limitations remain necessary. |
| Retain all 96 families | Exact bounds remain valid, but sign/material-size identification often fails. |
| Replace the wrapper pair | Validation supports only the tested regenerated workflow. |
| Generalize to unseen templates/providers/snapshots | Unsupported under the registered scope. |

**Final disposition: PASS WITH LIMITATIONS for design-audit readiness.** The owner must still decide whether to accept the failed 80% power target or authorize a scoped tradeoff, and resolve provider, funding, personnel and schedule prerequisites. No necessity to change the **15-call tree, 96-family roster, or 6,840-call envelope** has been proved.

**Implementation, prompt locking, pilot/main execution, and paper writing remain unauthorized.**
