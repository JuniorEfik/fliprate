# FlipRate Power and Completeness Simulation Report

**Date:** 2026-11-15  
**Status:** synthetic planning validation only  
**Seed:** 20261115  
**Python:** 3.12.3  
**Historical approximation:** 20,000 replications per scenario  
**Item-level validation:** 5,000 replications per scenario  
**Bootstrap validation:** first 200 datasets per scenario, 499 resamples each  
**No model outputs or paid APIs were used.**

## Executive result

The expanded validation supports the CR1 template-cluster procedure as the confirmatory test for the family-weighted complete-case estimand, but it does **not** support an overall statistical-readiness PASS.

- Global-null CR1/Holm familywise rejection is 4.34% with ICC 0, 4.72% with ICC 0.10, and 4.34% in a calibrated ceiling-heavy observed-scale null.
- The ordinary item t/Holm procedure remains anti-conservative at ICC 0.10: 9.68% familywise rejection.
- In the single-active-model 0.05 anchor, affected-model CR1/Holm power is **72.24% ± 0.63%**, below the 80% target. Any stricter full claim gate cannot have greater power.
- The exact full gate on the 200-dataset bootstrap subset passes in 75.0% ± 3.1% of affected-model datasets. This smaller-subset estimate is imprecise and does not override the 5,000-replication estimate of the necessary CR1 component.
- With 1% shared family failure, equal per-cell validity must be 98.3347% for a 90% chance of retaining at least 86 families under the specified independent-binomial model.
- Simultaneous bootstrap intervals for all-family bound endpoints under-cover under template-correlated failure. All-family sign and SESOI claims are therefore restricted to exact finite-roster bounds; construction-frame endpoint intervals remain descriptive.

No result proves that the 15-call tree, 96-family roster or 6,840-call envelope must change. On 2026-11-15, the owner accepted the failed power target as a documented limitation, preserved the current design and classified any resulting study as lower-powered exploratory. The statistical target remains failed.

## Prospective procedure represented

Each item-level dataset contains:

- 96 families in two domains;
- 12 templates per domain and four families per template;
- three correlated models;
- four bounded support cells per family;
- family, template and cell missingness states;
- a fixed three-model Holm family, with failed family/template gates entered as p-value 1.

The confirmatory point estimate is the unweighted mean over four-cell-complete families. Its confirmatory standard error is CR1 template-cluster robust:

\[
SE_{CR1}=
\sqrt{\frac{G}{G-1}\frac{\sum_g U_g^2}{n^2}},
\qquad
U_g=\sum_{i\in g}(\delta_i-\bar\delta),
\]

using G−1 reference degrees of freedom. It targets the same family-weighted estimand as the point estimate while allowing arbitrary within-template dependence.

An unqualified claim additionally requires:

- at least 86 complete families;
- at least 20 represented templates and 10 per domain;
- CR1/Holm rejection;
- a simultaneous 98.333% whole-template bootstrap interval excluding zero in the same direction;
- no leave-one-template-out reversal with an absolute shift greater than 0.05.

The simulation also evaluates ordinary item t inference, equal-template t sensitivity, exact all-family identification bounds, complete-case coverage, ceiling/floor mass, condition-dependent and informative missingness, template-correlated failures, and descriptive simultaneous endpoint intervals.

## Scenario coverage

The item-level suite includes:

- global null, three equal 0.05 effects, one active 0.05 model, and heterogeneous model effects;
- ICC 0 and ICC 0.10;
- a zero-mean heterogeneous-template null with ±0.08 template shifts;
- interior and ceiling-heavy outcomes;
- a calibrated ceiling-heavy observed-scale null;
- independent, condition-dependent, outcome-informative and template-correlated failures.

The historical known-SD Gaussian approximation remains in the output for audit continuity. It is not the readiness validation.

## Numerical and reproducibility checks

The standard-library Student t implementation reproduces:

- t(.975, 10) = 2.228138852;
- t(.975, 95) = 1.985251004;
- two-sided p(t=2, df=10) = 0.073388035.

All exact all-family bounds contained their corresponding fully observed 96-family interaction in every simulated dataset.

Reproduction identifiers:

- simulator SHA-256: a44a49916f575b050d0f9c4087c45fe5f4462e2d97d2dc159f96992bcc219873;
- item-level CSV SHA-256: 059955b367b052794a24a15ffbbd9aa2aad111d57bd1e56809a6c3f9db3374b6;
- legacy power CSV SHA-256: f7075dedbd49a65d7ffd507893d618a35b061e8848c6fe82e67028d319028bca.

The full output hashes are recorded in simulation_summary.json.

After the seeded run, the summary pass flag was tightened to require both the 5,000-replication CR1/Holm component and the 200-dataset full-gate subset estimate to reach 80%. The stored flag remains `false`; no simulated draw, CSV value or substantive verdict changed.

## Historical approximation

Under the old three-equal-effect central scenario:

| Quantity | Result |
|---|---:|
| Expected complete families | 91.30 |
| Exact probability of at least 86 complete | 99.258% |
| Historical gate-qualified average Holm rejection | 85.307% |
| Current p=1-before-Holm policy rejection | 85.258% |
| Probability at least one policy-qualified rejection | 96.540% |

This is a reproducible conditional calculation for three equally affected models. It is not the single-active or CR1 power result.

The old 0.03-effect table mixed gated and ungated columns:

- gate-qualified Holm rejection: 36.155%, reported as **36.2%**;
- ungated Holm rejection: 36.383%, reported as **36.4%**.

## Null calibration

| Observed-scale global null | Any-model item t/Holm | Any-model CR1/Holm | Full gate, bootstrap subset |
|---|---:|---:|---:|
| Interior, ICC 0 | 4.42% ± 0.29% | 4.34% ± 0.29% | 6.5% ± 1.7% |
| Interior, ICC 0.10 | 9.68% ± 0.42% | 4.72% ± 0.30% | 4.0% ± 1.4% |
| Ceiling-heavy calibrated null, ICC 0.10 | 8.34% ± 0.39% | 4.34% ± 0.29% | 3.5% ± 1.3% |
| Heterogeneous-template null, ICC 0.10 | 4.50% ± 0.29% | 0.24% ± 0.07% | 0% in 200 |

The CR1 procedure controls or conservatively controls familywise error in these selected nulls. The heterogeneous-template row shows strong conservatism, not exact calibration. The bootstrap-subset estimates have wide uncertainty and are additional gates, not a replacement for CR1 calibration.

## Single-active-model power

### Central interior, independent missingness, ICC 0

| Quantity | Result |
|---|---:|
| Complete-case population interaction | 0.05036 |
| Family gate passage | 99.32% |
| Ordinary item t/Holm power | 77.46% ± 0.59% |
| Confirmatory CR1/Holm power | **72.24% ± 0.63%** |
| Claim gate without bootstrap | 72.24% ± 0.63% |
| Exact full gate on bootstrap subset | 75.0% ± 3.1% |
| Any-model CR1/Holm rejection | 73.16% |
| Any-model full-gate passage on subset | 75.0% |

The 80% target **FAILS**. Because the full gate contains CR1/Holm rejection, true full-gate power cannot exceed true CR1/Holm component power. That necessary component is estimated at 72.24% ± 0.63%, regardless of the noisier 200-dataset full-gate estimate.

### Stress sensitivities

| Scenario | Affected-model CR1/Holm | Full gate, bootstrap subset | Family gate |
|---|---:|---:|---:|
| ICC 0.10 | 59.12% | 58.0% | 99.18% |
| Template-correlated failures, ICC 0.10 | 55.64% | 51.5% | 95.78% |
| Ceiling-heavy informative missingness, ICC 0.10 | 30.46% | 26.0% | 96.10% |

Ceiling compression reduces the complete-case observed interaction from a latent 0.05 input to about 0.0308, with about 18.5% of support cells at 1.

## Equal-effect sensitivity

| Scenario | Average CR1/Holm power | Average full-gate subset power | Any-model full-gate subset |
|---|---:|---:|---:|
| Interior, ICC 0 | 81.33% | 79.67% | 96.0% |
| Interior, ICC 0.10 | 68.42% | 65.17% | 84.0% |

The equal-effect scenario can look favorable because later Holm steps become easier when all three models are affected. It cannot substitute for the single-active readiness criterion.

## Coverage

In the central single-active anchor:

- ordinary item 95% coverage for the complete-case target: 95.41%;
- CR1 95% coverage: 95.27%;
- CR1 simultaneous 98.333% coverage: 98.49%;
- whole-template 98.333% bootstrap coverage on eligible subset datasets: 97.97%.

At ICC 0.10, affected-model CR1 95% coverage is 94.78% and simultaneous coverage is 98.43%. These checks directly target the Monte Carlo complete-case population, while full-roster means and complete-case bias are reported separately.

## Completeness and dependence boundary

The exact equal per-cell validity needed for 90% probability of retaining at least 86 families is:

| Shared family failure | Required per-cell validity |
|---:|---:|
| 0% | 98.0879% |
| 0.5% | 98.2109% |
| 1% | **98.3347%** |
| 2% | 98.5846% |
| 3% | 98.8377% |

This calculation assumes independent family retention, one shared family-failure component, and equal conditionally independent cell validity. It is not a guarantee under provider-wide batches, template-related formatting failures or concentrated outages.

The template-correlated-failure sensitivity has a similar high marginal-compliance regime but only 95.78% family-gate passage for the affected model and much poorer endpoint-bootstrap behavior. The eight-family pilot cannot certify that correlated failure modes are absent.

For comparison:

- 99% cell validity plus 1% shared failure gives 99.258% gate passage under the binomial model;
- 98% cell validity plus 1% shared failure gives approximately 78.93%;
- 98% cell validity with no shared failure gives approximately 87.51%.

## Exact all-family bounds

In the central single-active anchor:

| Quantity | Result |
|---|---:|
| Average complete families | 91.34 |
| Mean complete-case bias versus same full roster | -0.00001 |
| Average bound width | 0.0795 |
| Bounds cross zero | 34.08% ± 0.67% |
| Positive sign identified for fixed 96-family roster | 65.92% |
| Positive effect at least 0.05 identified for fixed roster | 6.02% ± 0.34% |

A model can therefore pass completeness and complete-case inference while the sign or material size for the fixed 96-family roster remains unidentified. The two claims are reported separately.

### Endpoint-bootstrap limitation

The planned Bonferroni 99.1667% percentile intervals for the lower and upper bound endpoints achieved only about 96.4% and 94.9% coverage in the central anchor. Under template-correlated failures, coverage fell to about 78.6% and 79.6%.

These intervals are retained as descriptive construction-frame sensitivities. They cannot support a construction-frame all-family sign or SESOI claim under the current plan. Exact finite-roster identification bounds remain valid.

## Readiness decisions

| Requirement | Verdict | Basis |
|---|---|---|
| Historical reproducibility | PASS | Central values reproduce and the 36.4/36.2 mismatch is corrected. |
| Bounded-cell, sample-estimated procedure | PASS | Four support cells, estimated variance and missingness are generated directly. |
| Same-estimand template protection | PASS conditionally | CR1 targets the family-weighted mean and is calibrated in the tested nulls under independent-cluster assumptions. |
| 80% single-active-model full-gate power | **FAIL** | The necessary CR1 component is estimated at 72.24% ± 0.63%; true full-gate power cannot exceed true component power. |
| Central independent-binomial completeness | PASS conditionally | 99.258% at 99% cell validity and 1% shared failure. |
| Correlated-failure robustness | LIMITATION | Gate passage and endpoint coverage deteriorate; empirical prevalence is unknown. |
| Construction-frame bound-endpoint inference | DESCRIPTIVE ONLY | Simultaneous percentile intervals under-cover in stress scenarios. |
| Empirical nuisance assumptions | BLOCKED | No authorized model-facing pilot or provider evidence exists. |

## Reproducibility files

- protocol/simulations/power_completeness_sim.py
- protocol/simulations/results/completeness_scenarios.csv
- protocol/simulations/results/gate_validity_thresholds.csv
- protocol/simulations/results/power_scenarios.csv
- protocol/simulations/results/item_level_validation.csv
- protocol/simulations/results/simulation_summary.json

## Limitations

- Results are conditional on a synthetic generator, not observed model behavior.
- CR1 relies on independent template clusters and model-based exchangeability under the registered construction frame.
- ICC, ceiling mass, interaction SD and missingness remain assumptions.
- The heterogeneous-template null is conservative and does not exhaust partial-null configurations.
- Bootstrap operating characteristics use 200 outer datasets and have wider Monte Carlo error.
- Endpoint percentile intervals require a better method before any construction-frame bound claim could be considered.
- No provider compliance, cost, latency or model-behavior inference is available.
