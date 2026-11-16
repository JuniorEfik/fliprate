#!/usr/bin/env python3
"""Prospective power/completeness simulation for FlipRate Stage 2.

Uses only Python's standard library. No model outputs or external services.
The inferential approximation is a two-sided normal test with estimated-design
SD treated as known for planning. It is intentionally labeled a planning model,
not a substitute for the pre-execution analysis lock.
"""

from __future__ import annotations

import argparse
import bisect
import csv
import json
import math
import random
from pathlib import Path


ALPHA = 0.05
N_START = 96
N_GATE = 86
MODELS = 3
SESOI = 0.05
MODEL_CORRELATION = 0.30


def normal_cdf(x: float) -> float:
    return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))


def two_sided_p(z: float) -> float:
    return max(0.0, min(1.0, 2.0 * (1.0 - normal_cdf(abs(z)))))


def holm_rejections(p_values: list[float], alpha: float = ALPHA) -> list[bool]:
    order = sorted(range(len(p_values)), key=lambda idx: p_values[idx])
    rejected = [False] * len(p_values)
    for rank, idx in enumerate(order):
        threshold = alpha / (len(p_values) - rank)
        if p_values[idx] <= threshold:
            rejected[idx] = True
        else:
            break
    return rejected


def binomial_pmf(n: int, p: float) -> list[float]:
    probs = []
    for k in range(n + 1):
        probs.append(math.comb(n, k) * (p**k) * ((1.0 - p) ** (n - k)))
    total = sum(probs)
    return [value / total for value in probs]


def binomial_cdf_table(n: int, p: float) -> list[float]:
    running = 0.0
    cdf = []
    for value in binomial_pmf(n, p):
        running += value
        cdf.append(running)
    cdf[-1] = 1.0
    return cdf


def sample_binomial_from_cdf(rng: random.Random, cdf: list[float]) -> int:
    return bisect.bisect_left(cdf, rng.random())


def prob_at_least(n: int, p: float, threshold: int) -> float:
    probs = binomial_pmf(n, p)
    return sum(probs[threshold:])


def retention(shared_failure: float, per_cell_failure: float) -> float:
    return (1.0 - shared_failure) * ((1.0 - per_cell_failure) ** 4)


def simulate_scenario(
    *,
    rng: random.Random,
    reps: int,
    effect: float,
    item_sd: float,
    complete_prob: float,
) -> dict[str, float]:
    cdf = binomial_cdf_table(N_START, complete_prob)
    adjusted_rejects = [0] * MODELS
    unadjusted_rejects = [0] * MODELS
    gate_qualified_adjusted_rejects = [0] * MODELS
    gate_qualified_unadjusted_rejects = [0] * MODELS
    any_reject = 0
    all_reject = 0
    any_gate_qualified_reject = 0
    all_gate_qualified_reject = 0
    gate_passes = [0] * MODELS
    n_sums = [0] * MODELS

    rho_sqrt = math.sqrt(MODEL_CORRELATION)
    indep_sqrt = math.sqrt(1.0 - MODEL_CORRELATION)

    for _ in range(reps):
        common_z = rng.gauss(0.0, 1.0)
        p_values = []
        n_values = []
        for model_idx in range(MODELS):
            n_complete = sample_binomial_from_cdf(rng, cdf)
            n_values.append(n_complete)
            n_sums[model_idx] += n_complete
            if n_complete >= N_GATE:
                gate_passes[model_idx] += 1

            if n_complete < 2 or item_sd <= 0:
                p_values.append(1.0)
                continue

            noise_z = rho_sqrt * common_z + indep_sqrt * rng.gauss(0.0, 1.0)
            noncentrality = effect * math.sqrt(n_complete) / item_sd
            z_stat = noncentrality + noise_z
            p_values.append(two_sided_p(z_stat))

        unadjusted = [p <= ALPHA for p in p_values]
        adjusted = holm_rejections(p_values)
        gate_qualified_adjusted = [
            adjusted[model_idx] and n_values[model_idx] >= N_GATE
            for model_idx in range(MODELS)
        ]
        gate_qualified_unadjusted = [
            unadjusted[model_idx] and n_values[model_idx] >= N_GATE
            for model_idx in range(MODELS)
        ]
        for model_idx in range(MODELS):
            unadjusted_rejects[model_idx] += int(unadjusted[model_idx])
            adjusted_rejects[model_idx] += int(adjusted[model_idx])
            gate_qualified_unadjusted_rejects[model_idx] += int(
                gate_qualified_unadjusted[model_idx]
            )
            gate_qualified_adjusted_rejects[model_idx] += int(
                gate_qualified_adjusted[model_idx]
            )
        any_reject += int(any(adjusted))
        all_reject += int(all(adjusted))
        any_gate_qualified_reject += int(any(gate_qualified_adjusted))
        all_gate_qualified_reject += int(all(gate_qualified_adjusted))

    total_gate_passes = sum(gate_passes)
    conditional_holm_power = (
        sum(gate_qualified_adjusted_rejects) / total_gate_passes
        if total_gate_passes
        else 0.0
    )

    return {
        # Confirmatory power requires both statistical rejection and the
        # prespecified completeness gate. Keep raw rejection rates separately.
        "average_holm_power": sum(gate_qualified_adjusted_rejects)
        / (MODELS * reps),
        "average_gate_qualified_holm_power": sum(
            gate_qualified_adjusted_rejects
        )
        / (MODELS * reps),
        "average_holm_rejection_unconditional": sum(adjusted_rejects)
        / (MODELS * reps),
        "average_holm_power_given_gate": conditional_holm_power,
        "average_gate_qualified_unadjusted_power": sum(
            gate_qualified_unadjusted_rejects
        )
        / (MODELS * reps),
        "average_unadjusted_rejection_unconditional": sum(unadjusted_rejects)
        / (MODELS * reps),
        "any_model_rejection_unconditional": any_reject / reps,
        "all_models_rejection_unconditional": all_reject / reps,
        "any_model_gate_qualified_rejection": any_gate_qualified_reject / reps,
        "all_models_gate_qualified_rejection": all_gate_qualified_reject / reps,
        "average_gate_pass_probability": sum(gate_passes) / (MODELS * reps),
        "average_n_complete": sum(n_sums) / (MODELS * reps),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--reps", type=int, default=20000)
    parser.add_argument("--seed", type=int, default=20261115)
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("protocol/simulations/results"),
    )
    args = parser.parse_args()

    args.output_dir.mkdir(parents=True, exist_ok=True)
    rng = random.Random(args.seed)

    missingness = {
        "clean": (0.00, 0.005),
        "central": (0.01, 0.01),
        "stress": (0.02, 0.02),
        "severe": (0.03, 0.03),
    }
    effects = [0.00, 0.03, 0.05, 0.07, 0.10]
    item_sds = [0.10, 0.15, 0.20, 0.25]

    completeness_rows = []
    for name, (shared_failure, per_cell_failure) in missingness.items():
        complete_prob = retention(shared_failure, per_cell_failure)
        completeness_rows.append(
            {
                "scenario": name,
                "shared_item_failure": shared_failure,
                "per_cell_failure": per_cell_failure,
                "family_complete_probability": complete_prob,
                "expected_complete_of_96": N_START * complete_prob,
                "probability_at_least_86": prob_at_least(
                    N_START, complete_prob, N_GATE
                ),
            }
        )

    for per_cell_validity in [0.99, 0.98, 0.975, 0.97, 0.95]:
        complete_prob = per_cell_validity**4
        completeness_rows.append(
            {
                "scenario": f"independent_cell_validity_{per_cell_validity:.3f}",
                "shared_item_failure": 0.0,
                "per_cell_failure": 1.0 - per_cell_validity,
                "family_complete_probability": complete_prob,
                "expected_complete_of_96": N_START * complete_prob,
                "probability_at_least_86": prob_at_least(
                    N_START, complete_prob, N_GATE
                ),
            }
        )

    completeness_path = args.output_dir / "completeness_scenarios.csv"
    with completeness_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(completeness_rows[0]))
        writer.writeheader()
        writer.writerows(completeness_rows)

    power_rows = []
    for scenario_name, (shared_failure, per_cell_failure) in missingness.items():
        complete_prob = retention(shared_failure, per_cell_failure)
        exact_gate_probability = prob_at_least(N_START, complete_prob, N_GATE)
        for item_sd in item_sds:
            for effect in effects:
                result = simulate_scenario(
                    rng=rng,
                    reps=args.reps,
                    effect=effect,
                    item_sd=item_sd,
                    complete_prob=complete_prob,
                )
                power_rows.append(
                    {
                        "missingness_scenario": scenario_name,
                        "shared_item_failure": shared_failure,
                        "per_cell_failure": per_cell_failure,
                        "family_complete_probability": complete_prob,
                        "exact_probability_at_least_86": exact_gate_probability,
                        "true_raw_interaction": effect,
                        "item_interaction_sd": item_sd,
                        "standardized_effect": effect / item_sd,
                        "reps": args.reps,
                        **result,
                    }
                )

    power_path = args.output_dir / "power_scenarios.csv"
    with power_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(power_rows[0]))
        writer.writeheader()
        writer.writerows(power_rows)

    central = next(
        row
        for row in power_rows
        if row["missingness_scenario"] == "central"
        and row["true_raw_interaction"] == SESOI
        and row["item_interaction_sd"] == 0.15
    )
    null_rows = [row for row in power_rows if row["true_raw_interaction"] == 0.0]
    max_null_any_rejection = max(
        row["any_model_gate_qualified_rejection"] for row in null_rows
    )

    summary = {
        "status": "SYNTHETIC_PLANNING_SIMULATION_ONLY",
        "seed": args.seed,
        "reps_per_scenario": args.reps,
        "starting_families": N_START,
        "completeness_gate": N_GATE,
        "models": MODELS,
        "alpha_familywise": ALPHA,
        "multiplicity": "Holm-Bonferroni across three model-specific tests",
        "sesoi_raw": SESOI,
        "model_test_correlation": MODEL_CORRELATION,
        "central_scenario": central,
        "central_power_pass": central["average_holm_power"] >= 0.80,
        "central_completeness_pass": central["exact_probability_at_least_86"]
        >= 0.90,
        "max_simulated_null_any_model_rejection": max_null_any_rejection,
        "limitations": [
            "Normal-test planning approximation, not finite-sample t/bootstrap execution.",
            "Item-level SD and malformedness are assumptions because model-facing pilot data are unavailable.",
            "Same effect and SD assumed across the three models within each scenario.",
            "Missingness is represented by shared-item and independent per-cell components only.",
        ],
        "outputs": [str(completeness_path), str(power_path)],
    }
    summary_path = args.output_dir / "simulation_summary.json"
    summary_path.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")

    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
