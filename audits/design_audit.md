# FlipRate Stage-2 Design Audit

**Date:** 2026-11-15  
**Scope:** protocol, statistical validation, adjudication planning and readiness evidence only  
**Design-audit verdict:** **PASS WITH LIMITATIONS**  
**Owner power disposition:** **ACCEPTED AS A LOWER-POWERED EXPLORATORY LIMITATION**  
**Execution status:** **BLOCKED and unauthorized**

## Executive conclusion

The corrected Stage-2 package is coherent enough to close the bounded design-audit cycle. Both focused round-2 reviewers returned **PASS WITH LIMITATIONS**, found no Critical or Major defect, and agreed that no evidence proves a need to alter the 15-call tree, 96-family roster or 6,840-call envelope.

The prespecified 80% single-active-model power target fails. On 2026-11-15, the owner accepted the measured 72.24% ± 0.63% CR1/Holm power as a documented limitation while preserving the research question, constructs, primary estimand, hypotheses, SESOI, CR1/Holm rules, 15-call tree, 96-family roster and 6,840-call envelope. This resolves the owner-decision gate but does not convert the statistical FAIL to PASS. The resulting study is lower-powered exploratory.

The audit still does not support execution readiness. Provider access, funded authority, exact snapshots, replay capability, named personnel, evidence-package completion, timed calibration and a feasible schedule remain unverified. A favorable design audit and accepted limitation are not execution authorization.

The requested GPT-6-Astra reviews failed before substantive review with HTTP 402. Both completed reviews used GPT-6.1-sol as same-family, provisional fallbacks. The ARS follow-up remained blind to every ARIS response and research-review trace.

## Audited package

- `protocol/benchmark_specification.md` v0.5
- `protocol/experimental_protocol.md` v0.5
- `protocol/scoring_rubric.md` v0.5
- `protocol/analysis_plan.md` v0.5
- `protocol/adjudication_plan.md` v0.3
- `protocol/simulations/power_completeness_sim.py`
- stored simulation CSV/JSON outputs and `protocol/simulations/simulation_report.md`
- `research/research_proposal.md`
- `docs/provider_budget_personnel_readiness.md`
- `refine-logs/EXPERIMENT_PLAN.md`
- `refine-logs/EXPERIMENT_TRACKER.md`

The current simulator SHA-256 is `a44a49916f575b050d0f9c4087c45fe5f4462e2d97d2dc159f96992bcc219873`. The item-level CSV SHA-256 is `059955b367b052794a24a15ffbbd9aa2aad111d57bd1e56809a6c3f9db3374b6`. All recorded output hashes match the current files.

## Core design judgment

The study supports a narrow behavioral measurement claim: among four-cell-valid families constructed under the registered two-domain frame, test whether bundled social-pressure framing changes the separation in reported support between sufficient and insufficient valid information.

The confirmatory estimator is the family-weighted complete-case interaction. Its test uses CR1 template-cluster-robust uncertainty for the same estimand. An unqualified claim additionally requires:

1. at least 86 four-cell-complete families;
2. at least 20 represented templates overall and 10 per domain;
3. CR1/Holm rejection;
4. a simultaneous 98.333% whole-template bootstrap interval excluding zero in the same direction; and
5. no leave-one-template-out reversal with an absolute shift greater than 0.05.

The equal-template estimate and ordinary item test are sensitivity diagnostics, not alternative confirmatory methods. Exact all-family sign and SESOI claims are limited to finite-roster identification bounds. Construction-frame endpoint intervals remain descriptive because their stress coverage failed.

## Round-1 issue disposition

| Issue | Disposition | Evidence |
|---|---|---|
| Different-estimand template co-gate | **RESOLVED** | CR1 now targets the family-weighted complete-case mean directly; equal-template weighting is descriptive (`protocol/analysis_plan.md:80–107`). |
| Template dependence in primary equivalence | **RESOLVED** | TOST uses CR1 uncertainty, template gates and cluster degrees of freedom (`protocol/analysis_plan.md:125–127`). |
| Repeat/paraphrase dependence | **RESOLVED** | The subset contains one family from each of 24 distinct templates; clustered inference is required if execution deviates (`protocol/analysis_plan.md:217–234`). |
| Construction population and exchangeability | **RESOLVED conditionally** | The frame, outcome-blind selection and model-based independent-template assumptions are explicit; no probability-sample claim is made (`protocol/analysis_plan.md:18–22`). |
| Secondary serial and domain test specification | **RESOLVED** | Formal tests use CR1 template clustering with fixed eligibility and multiplicity rules (`protocol/analysis_plan.md:129–157`). |
| Full prospective claim rule absent from simulation | **RESOLVED** | Stored code implements completeness/template gates, CR1/Holm, whole-template direction and leave-one-template-out stability. |
| Coverage targeted the wrong population | **RESOLVED conditionally** | Coverage now uses a separately recorded Monte Carlo complete-case target and reports CR1 95% and 98.333% coverage. It remains synthetic evidence. |
| Construction-frame bound-endpoint claims | **RESOLVED by restriction** | Exact finite-roster bounds remain inferential; construction-frame endpoint intervals are descriptive only (`protocol/analysis_plan.md:187–205`). |
| Two-answer versus three-answer baseline | **RESOLVED** | Benchmark, rubric and adjudication form consistently require at least three compatible substantive answers. |
| `UNCERTAIN` agreement versus referral | **RESOLVED** | Categorical agreement, binary reduction and mandatory referral are distinct (`protocol/adjudication_plan.md:144–165`). |
| Completeness-threshold independence assumptions | **RESOLVED as specification** | The 98.3347% threshold is explicitly conditional on its binomial assumptions; correlated failures are a separate sensitivity (`protocol/experimental_protocol.md:92`). |
| Adjudicator C re-audit independence | **RESOLVED** | Prior cases are excluded where possible; unavoidable overlap is disclosed as non-independent (`protocol/adjudication_plan.md:165`). |
| Sign-flip diagnostic | **RESOLVED** | Absolute skewness ≤1 is specified and the analysis cannot change confirmation (`protocol/analysis_plan.md:98–103`). |
| Failed 80% power requirement | **OWNER DISPOSITION RECORDED; STATISTICAL FAIL RETAINED** | The owner accepted lower power as a limitation and prohibited further optimization merely to reach 80%. The study is exploratory; the criterion is not reclassified as passed. |
| Monte Carlo uncertainty fields | **PARTIAL, Minor** | Most rate uncertainties are present. Raw-t rejection and retained same-roster coverage still lack explicit MC-SE fields. This does not change the current power verdict. |

## Statistical validation

| Check | Stored result | Audit judgment |
|---|---:|---|
| CR1/Holm global-null FWER, ICC 0 | 4.34% | Compatible with 5% in the tested generator. |
| CR1/Holm global-null FWER, ICC 0.10 | 4.72% | Compatible with 5% in the tested generator. |
| CR1/Holm calibrated ceiling-null FWER | 4.34% | Compatible with 5% in the tested generator. |
| Heterogeneous-template null FWER | 0.24% | Conservative; not universal calibration evidence. |
| Ordinary item/Holm FWER, ICC 0.10 | 9.68% | Anti-conservative; diagnostic only. |
| Single-active CR1/Holm power | **72.24% ± 0.63%** | **FAIL versus 80%.** |
| Exact full gate on 200-dataset subset | **75.0% ± 3.1%** | Imprecise; cannot overturn the failed necessary component. |
| CR1 95% complete-case coverage, central anchor | 95.27% | Acceptable conditional synthetic evidence. |
| CR1 98.333% coverage, central anchor | 98.49% | Acceptable conditional synthetic evidence. |
| Bounds crossing zero, central anchor | 34.08% | Complete-case significance need not identify the all-family sign. |
| Endpoint coverage, template-correlated failure | 78.57% / 79.59% | Fails for construction-frame endpoint claims. |
| Required per-cell validity with 1% shared failure | 98.334655% | Correct under stated independence assumptions. |

Mathematically, `P(full gate) ≤ P(CR1 rejection)` because CR1 rejection is a necessary gate. The 72.24% value estimates the component probability; it is not an uncertainty-free bound. Its Monte Carlo uncertainty still places it well below 80%.

## Design arithmetic and feasibility

- Calls per item-model tree: `1 baseline + 5 Turn-1 + 9 Turn-2 = 15`.
- Main confirmatory calls: `96 × 15 × 3 = 4,320`.
- Authorized future pilot allocation: `8 × 15 × 3 = 360`.
- Exact-repeat allocation: `24 × 15 × 3 = 1,080`.
- Wrapper-paraphrase allocation: `24 × 15 × 3 = 1,080`.
- Planned total: `6,840` logical calls; approximate hard operational ceiling `7,800`.
- Human workload: `184–296` person-hours before unexpected template-wide reopening.

The arithmetic is internally consistent. Economic plausibility under public price assumptions does not establish funding, account access or operational feasibility.

## Remaining limitations

- Inference is model-based and conditional on independent template clusters and the registered construction frame.
- The full-gate operating characteristic uses 200 outer bootstrap datasets and 499 resamples, so its Monte Carlo uncertainty is material.
- Synthetic variance, ceiling and missingness assumptions are not empirical model/provider measurements.
- Endpoint-bootstrap undercoverage prohibits construction-frame all-family sign or SESOI claims.
- Repeat/paraphrase TOST concerns mean interaction drift; it does not establish item-level repeatability or general wording invariance.
- The completed external reviews are same-family provisional fallbacks, not the originally requested Astra assurance.
- Exact prompts, provider adapters, model snapshots and parser behavior remain intentionally unlocked and unimplemented.

## Final audit disposition

The Stage-2 design package receives **PASS WITH LIMITATIONS for design-audit readiness**. The owner has accepted the power limitation, so the protocol/audit and power-disposition cycle is closed. The original power criterion remains failed and the study-level classification is lower-powered exploratory.

Execution remains **BLOCKED** pending:

1. provider credentials, exact snapshots, replay-capability evidence and rate-limit checks;
2. funded budget authority;
3. named, qualified and committed adjudication personnel, timed calibration and a feasible schedule;
4. completed and accepted evidence packages and frozen development/confirmatory rosters;
5. applicable institutional/ethics/employment/data-protection determinations;
6. deterministic parser, replay, storage and data-quality validation after implementation is separately authorized; and
7. a separate explicit owner authorization for implementation and any model-facing pilot or main run.

No implementation, prompt lock, provider call, pilot/main execution, confirmatory collection or paper writing is authorized by this audit.
