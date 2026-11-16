# FlipRate Power and Completeness Simulation Report

**Date:** 2026-11-15  
**Status:** synthetic planning simulation only  
**Seed:** 20261115  
**Replications:** 20,000 per scenario  
**No model outputs or paid APIs were used.**

## Method

The simulation models three model-specific primary tests with Holm-Bonferroni familywise alpha 0.05.

Varied inputs:

- true raw interaction: 0, 0.03, 0.05, 0.07, 0.10;
- item-level interaction SD: 0.10, 0.15, 0.20, 0.25;
- 96 starting item families;
- complete-case gate: at least 86 families;
- shared item-level and independent four-cell failure components;
- cross-model test-statistic correlation: 0.30.

The power simulation uses a normal-test planning approximation. It is not a replacement for the final t/bootstrap analysis.

## Central planning scenario

- SESOI: 0.05 raw support points;
- item interaction SD: 0.15;
- shared item failure: 1%;
- per-cell failure: 1%;
- complete-family probability: 0.9510.

Calculated results:

| Quantity | Result | Target | Status |
|---|---:|---:|---|
| Expected complete families | 91.3 | ≥86 | PASS |
| Probability of ≥86 complete | 99.3% | ≥90% | PASS |
| Average model-specific Holm power at SESOI | 85.9% | ≥80% | PASS |
| Probability at least one model rejects | 96.6% | descriptive | — |
| Probability all three models reject | 72.7% | descriptive | — |
| Maximum simulated null familywise rejection | 5.0% | approximately ≤5% | PASS |

## Sensitivity to item-level variance

Holm-adjusted power for a true 0.05 interaction:

| Item interaction SD | Clean missingness | Central | Stress | Severe |
|---:|---:|---:|---:|---:|
| 0.10 | 99.8% | 99.7% | 99.6% | 99.4% |
| 0.15 | 87.0% | 85.9% | 83.8% | 81.3% |
| 0.20 | 59.3% | 57.4% | 54.8% | 52.3% |
| 0.25 | 37.1% | 37.0% | 35.0% | 32.6% |

The approved 96-family target is adequately powered for a five-point effect only when item-level interaction SD is approximately 0.15 or lower. At SD 0.20 or higher, the design does not meet the 80% power target.

## Sensitivity to completeness

| Scenario | Shared failure | Per-cell failure | Expected complete | P(complete ≥86) |
|---|---:|---:|---:|---:|
| Clean | 0% | 0.5% | 94.1 | ~100% |
| Central | 1% | 1% | 91.3 | 99.3% |
| Stress | 2% | 2% | 86.8 | 68.4% |
| Severe | 3% | 3% | 82.4 | 18.6% |

Under independent cell validity only:

| Per-cell validity | Expected complete | P(complete ≥86) |
|---:|---:|---:|
| 99.0% | 92.2 | 99.9% |
| 98.0% | 88.5 | 87.5% |
| 97.5% | 86.8 | 68.1% |
| 97.0% | 85.0 | 45.1% |
| 95.0% | 78.2 | 2.2% |

The 86-family gate therefore requires very high four-cell compliance. Development must target approximately 98% or better per-cell validity, and shared item failures must stay near 1%, to make the gate reliably attainable.

## Sensitivity to effect size

Under the central missingness scenario and SD 0.15:

| True raw interaction | Average Holm power |
|---:|---:|
| 0.00 | 1.8% per-model average rejection |
| 0.03 | 36.4% |
| 0.05 | 85.9% |
| 0.07 | 99.3% |
| 0.10 | ~100% |

The design is not intended to reliably detect a three-point interaction.

## Decision implications

- The 96-item target **passes conditionally** under the central planning assumptions.
- Actual power is **unverified** because no model-facing pilot has estimated item-level interaction SD or malformedness.
- A future authorized development pilot must estimate these nuisance quantities without using confirmatory items.
- If pilot SD exceeds 0.15 or completeness projections fall below the gate, the owner must choose among increasing items, narrowing model claims, increasing the SESOI, improving schema compliance without content retries, or accepting lower power.
- Any item-count or call-envelope expansion requires documented owner approval.

## Reproducibility files

- `protocol/simulations/power_completeness_sim.py`
- `protocol/simulations/results/completeness_scenarios.csv`
- `protocol/simulations/results/power_scenarios.csv`
- `protocol/simulations/results/simulation_summary.json`

## Limitations

- normal-test planning approximation rather than finite-sample t/bootstrap simulation;
- assumed equal effects and SDs across models within a scenario;
- simplified two-component missingness model;
- no empirical variance, compliance or provider-latency inputs;
- no inference about actual model behavior.
