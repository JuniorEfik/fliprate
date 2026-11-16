# FlipRate

FlipRate is a planned behavioral evaluation protocol for measuring how evidence sufficiency and social-pressure framing affect language-model answer support. It was developed for Track 1, Model Epistemics and Decision-Making Evals, during the Apart Research AI x Epistemics Research Sprint.

The project has not run empirical model experiments. The repository contains the research protocol, analysis and adjudication plans, independent design audits, a standard-library Python simulator, and stored synthetic operating-characteristic results.

## Current status

- Author: Junior Efik
- Affiliation: not yet confirmed
- Design: 15 calls per item-model tree, 96 confirmatory item families, 6,840 planned calls
- Stored CR1/Holm power: **72.24% +/- 0.63%**
- Prespecified 80% target: **FAIL**
- Classification: lower-powered exploratory
- Experiment execution: blocked and unauthorized

No provider calls, empirical experiments, confirmatory data collection, completed human adjudication, or final prompt lock are claimed.

## Start here

- [Final report PDF](output/pdf/FlipRate_Final_Report.pdf)
- [Master project record](master.md)
- [Research proposal](research/research_proposal.md)
- [Experimental protocol](protocol/experimental_protocol.md)
- [Analysis plan](protocol/analysis_plan.md)
- [Simulation report](protocol/simulations/simulation_report.md)
- [Design audit](audits/design_audit.md)

## Reproduce the synthetic simulation

Python 3.12 or later is recommended. The simulator uses only the Python standard library and does not contact external services.

```bash
python3 protocol/simulations/power_completeness_sim.py \
  --output-dir /tmp/fliprate-simulation
```

The preserved run used seed `20261115`, 20,000 legacy replications per scenario, 5,000 item-level replications per scenario, 200 bootstrap outer replications, and 499 bootstrap resamples. Stored outputs and their provenance are under `protocol/simulations/results/`.

For a quick smoke test:

```bash
python3 protocol/simulations/power_completeness_sim.py \
  --reps 20 \
  --item-reps 10 \
  --bootstrap-outer-reps 2 \
  --bootstrap-resamples 9 \
  --output-dir /tmp/fliprate-smoke
```

## Repository scope

Downloaded third-party full texts, source archives, temporary render files, and local agent traces are intentionally excluded from Git. Bibliographic metadata and the source register remain available under `research/`.

