#!/usr/bin/env python3
"""Prospective operating-characteristic validation for FlipRate Stage 2.

Uses only Python's standard library and synthetic data. The script preserves
the historical known-SD normal approximation for audit continuity, then adds
item-level validation of the planned sample-estimated t procedure, bounded
four-cell outcomes, template dependence, missingness, bootstrap intervals and
the fixed three-model Holm family.

No model outputs or external services are used.
"""

from __future__ import annotations

import argparse
import bisect
import csv
import functools
import hashlib
import json
import math
import platform
import random
from pathlib import Path
from typing import Any


ALPHA = 0.05
N_START = 96
N_GATE = 86
MODELS = 3
SESOI = 0.05
MODEL_CORRELATION = 0.30
DOMAINS = 2
TEMPLATES_PER_DOMAIN = 12
ITEMS_PER_TEMPLATE = 4
ITEM_INTERACTION_SD = 0.15

CELL_CODING = {
    "SN": (0.5, -0.5),
    "SP": (0.5, 0.5),
    "IN": (-0.5, -0.5),
    "IP": (-0.5, 0.5),
}
INTERACTION_COEFFICIENT = {"SN": -1.0, "SP": 1.0, "IN": 1.0, "IP": -1.0}


def normal_cdf(x: float) -> float:
    return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))


def normal_two_sided_p(z: float) -> float:
    return max(0.0, min(1.0, 2.0 * (1.0 - normal_cdf(abs(z)))))


def beta_continued_fraction(a: float, b: float, x: float) -> float:
    """Continued fraction for the regularized incomplete beta function."""

    max_iterations = 300
    epsilon = 3.0e-14
    tiny = 1.0e-300
    qab = a + b
    qap = a + 1.0
    qam = a - 1.0
    c = 1.0
    d = 1.0 - qab * x / qap
    if abs(d) < tiny:
        d = tiny
    d = 1.0 / d
    h = d

    for iteration in range(1, max_iterations + 1):
        m2 = 2 * iteration
        aa = (
            iteration
            * (b - iteration)
            * x
            / ((qam + m2) * (a + m2))
        )
        d = 1.0 + aa * d
        if abs(d) < tiny:
            d = tiny
        c = 1.0 + aa / c
        if abs(c) < tiny:
            c = tiny
        d = 1.0 / d
        h *= d * c

        aa = -(
            (a + iteration)
            * (qab + iteration)
            * x
            / ((a + m2) * (qap + m2))
        )
        d = 1.0 + aa * d
        if abs(d) < tiny:
            d = tiny
        c = 1.0 + aa / c
        if abs(c) < tiny:
            c = tiny
        d = 1.0 / d
        delta = d * c
        h *= delta
        if abs(delta - 1.0) <= epsilon:
            return h

    raise RuntimeError("incomplete beta continued fraction did not converge")


def regularized_beta(x: float, a: float, b: float) -> float:
    if x <= 0.0:
        return 0.0
    if x >= 1.0:
        return 1.0
    log_term = (
        math.lgamma(a + b)
        - math.lgamma(a)
        - math.lgamma(b)
        + a * math.log(x)
        + b * math.log1p(-x)
    )
    front = math.exp(log_term)
    if x < (a + 1.0) / (a + b + 2.0):
        value = front * beta_continued_fraction(a, b, x) / a
    else:
        value = 1.0 - front * beta_continued_fraction(b, a, 1.0 - x) / b
    return min(1.0, max(0.0, value))


def student_t_cdf(t_value: float, degrees_freedom: int) -> float:
    if degrees_freedom <= 0:
        raise ValueError("degrees_freedom must be positive")
    if not math.isfinite(t_value):
        return 1.0 if t_value > 0 else 0.0
    x = degrees_freedom / (degrees_freedom + t_value * t_value)
    tail = regularized_beta(x, degrees_freedom / 2.0, 0.5)
    return 1.0 - 0.5 * tail if t_value >= 0.0 else 0.5 * tail


def student_t_two_sided_p(t_value: float, degrees_freedom: int) -> float:
    if not math.isfinite(t_value):
        return 0.0
    x = degrees_freedom / (degrees_freedom + t_value * t_value)
    return regularized_beta(x, degrees_freedom / 2.0, 0.5)


@functools.lru_cache(maxsize=None)
def student_t_critical(probability: float, degrees_freedom: int) -> float:
    if not 0.5 < probability < 1.0:
        raise ValueError("probability must lie between 0.5 and 1")
    low = 0.0
    high = 1.0
    while student_t_cdf(high, degrees_freedom) < probability:
        high *= 2.0
        if high > 1.0e6:
            raise RuntimeError("failed to bracket Student-t critical value")
    for _ in range(80):
        midpoint = (low + high) / 2.0
        if student_t_cdf(midpoint, degrees_freedom) < probability:
            low = midpoint
        else:
            high = midpoint
    return (low + high) / 2.0


def mean_and_sample_sd(values: list[float]) -> tuple[float, float]:
    mean_value = sum(values) / len(values)
    if len(values) < 2:
        return mean_value, math.nan
    variance = sum((value - mean_value) ** 2 for value in values) / (
        len(values) - 1
    )
    return mean_value, math.sqrt(max(0.0, variance))


def one_sample_t(values: list[float], null_mean: float = 0.0) -> dict[str, float]:
    if len(values) < 2:
        return {
            "n": float(len(values)),
            "mean": sum(values) / len(values) if values else math.nan,
            "sd": math.nan,
            "se": math.nan,
            "t": math.nan,
            "p": 1.0,
            "ci_low": math.nan,
            "ci_high": math.nan,
            "sim_ci_low": math.nan,
            "sim_ci_high": math.nan,
        }
    mean_value, sample_sd = mean_and_sample_sd(values)
    standard_error = sample_sd / math.sqrt(len(values))
    if standard_error == 0.0:
        if mean_value == null_mean:
            t_value = 0.0
            p_value = 1.0
        else:
            t_value = math.copysign(math.inf, mean_value - null_mean)
            p_value = 0.0
    else:
        t_value = (mean_value - null_mean) / standard_error
        p_value = student_t_two_sided_p(t_value, len(values) - 1)
    critical = student_t_critical(0.975, len(values) - 1)
    return {
        "n": float(len(values)),
        "mean": mean_value,
        "sd": sample_sd,
        "se": standard_error,
        "t": t_value,
        "p": p_value,
        "ci_low": mean_value - critical * standard_error,
        "ci_high": mean_value + critical * standard_error,
    }


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
    probs = [
        math.comb(n, k) * (p**k) * ((1.0 - p) ** (n - k))
        for k in range(n + 1)
    ]
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
    return sum(binomial_pmf(n, p)[threshold:])


def retention(shared_failure: float, per_cell_failure: float) -> float:
    return (1.0 - shared_failure) * ((1.0 - per_cell_failure) ** 4)


def required_cell_validity(
    shared_failure: float,
    target_gate_probability: float = 0.90,
) -> float:
    """Equal per-cell validity needed to reach the exact binomial gate target."""

    if prob_at_least(N_START, 1.0 - shared_failure, N_GATE) < target_gate_probability:
        return math.nan
    low = 0.0
    high = 1.0
    for _ in range(70):
        midpoint = (low + high) / 2.0
        complete_probability = (1.0 - shared_failure) * midpoint**4
        if (
            prob_at_least(N_START, complete_probability, N_GATE)
            >= target_gate_probability
        ):
            high = midpoint
        else:
            low = midpoint
    return high


def mc_standard_error(rate: float, reps: int) -> float:
    if reps <= 0 or not math.isfinite(rate):
        return math.nan
    return math.sqrt(max(0.0, rate * (1.0 - rate) / reps))


def percentile(sorted_values: list[float], probability: float) -> float:
    if not sorted_values:
        return math.nan
    if len(sorted_values) == 1:
        return sorted_values[0]
    position = probability * (len(sorted_values) - 1)
    lower = int(math.floor(position))
    upper = int(math.ceil(position))
    if lower == upper:
        return sorted_values[lower]
    weight = position - lower
    return sorted_values[lower] * (1.0 - weight) + sorted_values[upper] * weight


def clamp_support(value: float) -> float:
    return min(1.0, max(0.0, value))


# ---------------------------------------------------------------------------
# Historical known-SD planning approximation
# ---------------------------------------------------------------------------


def simulate_legacy_scenario(
    *,
    rng: random.Random,
    reps: int,
    effect: float,
    item_sd: float,
    complete_prob: float,
) -> dict[str, float]:
    """Preserve prior columns while adding the current p=1 gate policy."""

    cdf = binomial_cdf_table(N_START, complete_prob)
    adjusted_rejects = [0] * MODELS
    unadjusted_rejects = [0] * MODELS
    gate_qualified_adjusted_rejects = [0] * MODELS
    gate_qualified_unadjusted_rejects = [0] * MODELS
    policy_adjusted_rejects = [0] * MODELS
    any_reject = 0
    all_reject = 0
    any_gate_qualified_reject = 0
    all_gate_qualified_reject = 0
    any_policy_reject = 0
    all_policy_reject = 0
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

            noise_z = (
                rho_sqrt * common_z
                + indep_sqrt * rng.gauss(0.0, 1.0)
            )
            noncentrality = effect * math.sqrt(n_complete) / item_sd
            z_stat = noncentrality + noise_z
            p_values.append(normal_two_sided_p(z_stat))

        unadjusted = [p <= ALPHA for p in p_values]
        adjusted = holm_rejections(p_values)
        gate_policy_p_values = [
            p_values[model_idx] if n_values[model_idx] >= N_GATE else 1.0
            for model_idx in range(MODELS)
        ]
        policy_adjusted = holm_rejections(gate_policy_p_values)
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
            policy_adjusted_rejects[model_idx] += int(policy_adjusted[model_idx])
        any_reject += int(any(adjusted))
        all_reject += int(all(adjusted))
        any_gate_qualified_reject += int(any(gate_qualified_adjusted))
        all_gate_qualified_reject += int(all(gate_qualified_adjusted))
        any_policy_reject += int(any(policy_adjusted))
        all_policy_reject += int(all(policy_adjusted))

    total_gate_passes = sum(gate_passes)
    conditional_holm_power = (
        sum(gate_qualified_adjusted_rejects) / total_gate_passes
        if total_gate_passes
        else 0.0
    )

    return {
        # Historical fields are retained so the earlier report is reproducible.
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
        # Current policy fields set failed-gate p-values to 1 before Holm.
        "average_policy_holm_rejection": sum(policy_adjusted_rejects)
        / (MODELS * reps),
        "any_model_policy_holm_rejection": any_policy_reject / reps,
        "all_models_policy_holm_rejection": all_policy_reject / reps,
    }


# ---------------------------------------------------------------------------
# Item-level bounded-cell validation
# ---------------------------------------------------------------------------


def item_scenarios() -> list[dict[str, Any]]:
    alternatives = {
        "null": (0.0, 0.0, 0.0),
        "ceiling_observed_null": (0.0132, 0.0132, 0.0132),
        "equal": (0.05, 0.05, 0.05),
        "single_active": (0.05, 0.0, 0.0),
        "heterogeneous": (0.08, 0.03, -0.02),
    }
    specifications = [
        ("null_interior_independent_icc00", "null", "interior", 0.00, "independent"),
        ("null_interior_independent_icc10", "null", "interior", 0.10, "independent"),
        (
            "null_interior_template_heterogeneous_icc10",
            "null",
            "interior",
            0.10,
            "independent",
        ),
        ("null_ceiling_informative_icc10", "null", "ceiling", 0.10, "informative"),
        (
            "observed_null_ceiling_informative_icc10",
            "ceiling_observed_null",
            "ceiling",
            0.10,
            "informative",
        ),
        ("equal_interior_independent_icc00", "equal", "interior", 0.00, "independent"),
        ("equal_interior_independent_icc10", "equal", "interior", 0.10, "independent"),
        ("equal_ceiling_independent_icc10", "equal", "ceiling", 0.10, "independent"),
        (
            "equal_interior_condition_dependent_icc10",
            "equal",
            "interior",
            0.10,
            "condition_dependent",
        ),
        ("equal_ceiling_informative_icc10", "equal", "ceiling", 0.10, "informative"),
        (
            "single_interior_independent_icc00",
            "single_active",
            "interior",
            0.00,
            "independent",
        ),
        (
            "single_interior_independent_icc10",
            "single_active",
            "interior",
            0.10,
            "independent",
        ),
        (
            "single_interior_condition_dependent_icc10",
            "single_active",
            "interior",
            0.10,
            "condition_dependent",
        ),
        (
            "single_ceiling_informative_icc10",
            "single_active",
            "ceiling",
            0.10,
            "informative",
        ),
        (
            "single_interior_template_correlated_failure_icc10",
            "single_active",
            "interior",
            0.10,
            "template_correlated",
        ),
        (
            "heterogeneous_interior_independent_icc10",
            "heterogeneous",
            "interior",
            0.10,
            "independent",
        ),
        (
            "heterogeneous_ceiling_condition_dependent_icc10",
            "heterogeneous",
            "ceiling",
            0.10,
            "condition_dependent",
        ),
    ]
    scenarios = [
        {
            "scenario": name,
            "alternative": alternative,
            "effects": alternatives[alternative],
            "outcome_regime": outcome,
            "template_icc": icc,
            "missingness": missingness,
            "template_effect_shift": (
                0.08
                if name == "null_interior_template_heterogeneous_icc10"
                else 0.0
            ),
        }
        for name, alternative, outcome, icc, missingness in specifications
    ]
    return scenarios


def outcome_parameters(regime: str) -> dict[str, float]:
    if regime == "interior":
        return {
            "base_mean": 0.50,
            "base_sd": 0.05,
            "evidence_mean": 0.24,
            "evidence_sd": 0.03,
            "pressure_mean": 0.02,
            "pressure_sd": 0.02,
        }
    if regime == "ceiling":
        return {
            "base_mean": 0.87,
            "base_sd": 0.07,
            "evidence_mean": 0.20,
            "evidence_sd": 0.04,
            "pressure_mean": 0.03,
            "pressure_sd": 0.02,
        }
    raise ValueError(f"unknown outcome regime: {regime}")


def per_cell_failure_probability(
    missingness: str,
    cell: str,
    support: float,
) -> float:
    if missingness == "independent":
        return 0.01
    if missingness == "condition_dependent":
        return {"SN": 0.005, "SP": 0.008, "IN": 0.008, "IP": 0.025}[cell]
    if missingness == "informative":
        probability = 0.003 + 0.008 * support
        if cell == "IP":
            probability += 0.025 * support
        if cell == "SP":
            probability += 0.008 * (1.0 - support)
        return min(0.20, probability)
    if missingness == "template_correlated":
        return 0.005
    raise ValueError(f"unknown missingness mechanism: {missingness}")


def shared_failure_probability(missingness: str) -> float:
    if missingness == "independent":
        return 0.01
    if missingness in {"condition_dependent", "informative", "template_correlated"}:
        return 0.005
    raise ValueError(f"unknown missingness mechanism: {missingness}")


def generate_item_data(
    *,
    rng: random.Random,
    scenario: dict[str, Any],
) -> list[list[dict[str, Any]]]:
    """Generate 96 families jointly for three correlated synthetic models."""

    parameters = outcome_parameters(scenario["outcome_regime"])
    template_icc = float(scenario["template_icc"])
    effects = scenario["effects"]
    rho_sqrt = math.sqrt(MODEL_CORRELATION)
    rho_independent = math.sqrt(1.0 - MODEL_CORRELATION)
    template_sqrt = math.sqrt(template_icc)
    item_sqrt = math.sqrt(1.0 - template_icc)
    model_items: list[list[dict[str, Any]]] = [[] for _ in range(MODELS)]

    for domain in range(DOMAINS):
        for template_within_domain in range(TEMPLATES_PER_DOMAIN):
            template_id = domain * TEMPLATES_PER_DOMAIN + template_within_domain
            common_template_z = rng.gauss(0.0, 1.0)
            model_template_z = [rng.gauss(0.0, 1.0) for _ in range(MODELS)]
            template_outage = [
                scenario["missingness"] == "template_correlated"
                and rng.random() < 0.02
                for _ in range(MODELS)
            ]
            signed_template_shift = float(
                scenario.get("template_effect_shift", 0.0)
            ) * (1.0 if template_within_domain < TEMPLATES_PER_DOMAIN / 2 else -1.0)
            for item_within_template in range(ITEMS_PER_TEMPLATE):
                common_item_z = rng.gauss(0.0, 1.0)
                model_item_z = [rng.gauss(0.0, 1.0) for _ in range(MODELS)]
                common_base_z = rng.gauss(0.0, 1.0)
                model_base_z = [rng.gauss(0.0, 1.0) for _ in range(MODELS)]

                for model_idx in range(MODELS):
                    correlated_template_z = (
                        rho_sqrt * common_template_z
                        + rho_independent * model_template_z[model_idx]
                    )
                    correlated_item_z = (
                        rho_sqrt * common_item_z
                        + rho_independent * model_item_z[model_idx]
                    )
                    item_interaction = (
                        effects[model_idx]
                        + signed_template_shift
                        + ITEM_INTERACTION_SD
                        * (
                            template_sqrt * correlated_template_z
                            + item_sqrt * correlated_item_z
                        )
                    )
                    base = parameters["base_mean"] + parameters["base_sd"] * (
                        rho_sqrt * common_base_z
                        + rho_independent * model_base_z[model_idx]
                    )
                    evidence_effect = (
                        parameters["evidence_mean"]
                        + parameters["evidence_sd"] * rng.gauss(0.0, 1.0)
                    )
                    pressure_effect = (
                        parameters["pressure_mean"]
                        + parameters["pressure_sd"] * rng.gauss(0.0, 1.0)
                    )
                    cells = {}
                    for cell, (evidence_code, pressure_code) in CELL_CODING.items():
                        value = (
                            base
                            + evidence_effect * evidence_code
                            + pressure_effect * pressure_code
                            + item_interaction * evidence_code * pressure_code
                        )
                        cells[cell] = clamp_support(value)

                    shared_failure = template_outage[model_idx] or (
                        rng.random()
                        < shared_failure_probability(scenario["missingness"])
                    )
                    observed = {}
                    for cell, value in cells.items():
                        observed[cell] = (
                            not shared_failure
                            and rng.random()
                            >= per_cell_failure_probability(
                                scenario["missingness"], cell, value
                            )
                        )

                    model_items[model_idx].append(
                        {
                            "domain": domain,
                            "template": template_id,
                            "item": item_within_template,
                            "cells": cells,
                            "observed": observed,
                        }
                    )

    if any(len(items) != N_START for items in model_items):
        raise AssertionError("item generator did not create 96 families per model")
    return model_items


def item_interaction(cells: dict[str, float]) -> float:
    return cells["SP"] - cells["SN"] - cells["IP"] + cells["IN"]


def all_family_bounds(items: list[dict[str, Any]]) -> tuple[float, float]:
    lower_total = 0.0
    upper_total = 0.0
    for item in items:
        lower, upper = item_bound_contributions(item)
        lower_total += lower
        upper_total += upper
    return lower_total / N_START, upper_total / N_START


def complete_item_records(
    items: list[dict[str, Any]],
) -> list[tuple[int, int, float]]:
    records = []
    for item in items:
        if all(item["observed"].values()):
            records.append(
                (
                    int(item["domain"]),
                    int(item["template"]),
                    item_interaction(item["cells"]),
                )
            )
    return records


def template_means(records: list[tuple[int, int, float]]) -> list[float]:
    grouped: dict[int, list[float]] = {}
    for _, template, value in records:
        grouped.setdefault(template, []).append(value)
    return [sum(values) / len(values) for values in grouped.values()]


def template_representation(
    records: list[tuple[int, int, float]],
) -> tuple[int, list[int]]:
    templates_by_domain = [set() for _ in range(DOMAINS)]
    for domain, template, _ in records:
        templates_by_domain[domain].add(template)
    counts = [len(templates) for templates in templates_by_domain]
    return sum(counts), counts


def cluster_robust_t(
    records: list[tuple[int, int, float]],
    null_mean: float = 0.0,
) -> dict[str, float]:
    """CR1 intercept-only t test clustered by construction template."""

    if len(records) < 2:
        return {
            "n": float(len(records)),
            "clusters": 0.0,
            "mean": math.nan,
            "se": math.nan,
            "t": math.nan,
            "p": 1.0,
            "ci_low": math.nan,
            "ci_high": math.nan,
            "sim_ci_low": math.nan,
            "sim_ci_high": math.nan,
        }
    values = [record[2] for record in records]
    mean_value = sum(values) / len(values)
    grouped_scores: dict[int, float] = {}
    for _, template, value in records:
        grouped_scores[template] = grouped_scores.get(template, 0.0) + (
            value - mean_value
        )
    clusters = len(grouped_scores)
    if clusters < 2:
        return {
            "n": float(len(records)),
            "clusters": float(clusters),
            "mean": mean_value,
            "se": math.nan,
            "t": math.nan,
            "p": 1.0,
            "ci_low": math.nan,
            "ci_high": math.nan,
        }
    variance = (
        clusters
        / (clusters - 1.0)
        * sum(score * score for score in grouped_scores.values())
        / (len(records) ** 2)
    )
    standard_error = math.sqrt(max(0.0, variance))
    if standard_error == 0.0:
        if mean_value == null_mean:
            t_value = 0.0
            p_value = 1.0
        else:
            t_value = math.copysign(math.inf, mean_value - null_mean)
            p_value = 0.0
    else:
        t_value = (mean_value - null_mean) / standard_error
        p_value = student_t_two_sided_p(t_value, clusters - 1)
    critical = student_t_critical(0.975, clusters - 1)
    simultaneous_critical = student_t_critical(
        1.0 - ALPHA / (2.0 * MODELS), clusters - 1
    )
    return {
        "n": float(len(records)),
        "clusters": float(clusters),
        "mean": mean_value,
        "se": standard_error,
        "t": t_value,
        "p": p_value,
        "ci_low": mean_value - critical * standard_error,
        "ci_high": mean_value + critical * standard_error,
        "sim_ci_low": mean_value - simultaneous_critical * standard_error,
        "sim_ci_high": mean_value + simultaneous_critical * standard_error,
    }


def leave_one_template_out_stable(
    records: list[tuple[int, int, float]],
    shift_limit: float = SESOI,
) -> bool:
    if not records:
        return False
    full_mean = sum(record[2] for record in records) / len(records)
    templates = sorted({record[1] for record in records})
    for omitted in templates:
        retained = [record[2] for record in records if record[1] != omitted]
        if not retained:
            return False
        omitted_mean = sum(retained) / len(retained)
        reverses = full_mean * omitted_mean < 0.0
        if reverses and abs(omitted_mean - full_mean) > shift_limit:
            return False
    return True


def item_bound_contributions(item: dict[str, Any]) -> tuple[float, float]:
    lower = 0.0
    upper = 0.0
    for cell, coefficient in INTERACTION_COEFFICIENT.items():
        if item["observed"][cell]:
            contribution = coefficient * item["cells"][cell]
            lower += contribution
            upper += contribution
        elif coefficient > 0.0:
            upper += 1.0
        else:
            lower -= 1.0
    return lower, upper


def bootstrap_inference(
    *,
    records: list[tuple[int, int, float]],
    items: list[dict[str, Any]],
    rng: random.Random,
    resamples: int,
) -> dict[str, float]:
    """Domain-stratified item/template inference and bound endpoints."""

    observed_mean = sum(record[2] for record in records) / len(records)
    values_by_domain: list[list[float]] = [[] for _ in range(DOMAINS)]
    template_groups: list[list[tuple[float, int, float, float, int]]] = [
        [] for _ in range(DOMAINS)
    ]
    values_by_template: dict[tuple[int, int], list[float]] = {}
    bounds_by_template: dict[tuple[int, int], list[tuple[float, float]]] = {}

    for domain, template, value in records:
        values_by_domain[domain].append(value)
        values_by_template.setdefault((domain, template), []).append(value)

    for item in items:
        key = (int(item["domain"]), int(item["template"]))
        bounds_by_template.setdefault(key, []).append(
            item_bound_contributions(item)
        )

    for domain in range(DOMAINS):
        for template_within_domain in range(TEMPLATES_PER_DOMAIN):
            template = domain * TEMPLATES_PER_DOMAIN + template_within_domain
            values = values_by_template.get((domain, template), [])
            bounds = bounds_by_template[(domain, template)]
            template_groups[domain].append(
                (
                    sum(values),
                    len(values),
                    sum(bound[0] for bound in bounds),
                    sum(bound[1] for bound in bounds),
                    len(bounds),
                )
            )

    item_bootstrap_means = []
    template_bootstrap_means = []
    lower_bound_bootstrap_means = []
    upper_bound_bootstrap_means = []
    for _ in range(resamples):
        item_total = 0.0
        item_count = 0
        for domain_values in values_by_domain:
            if not domain_values:
                continue
            sampled = rng.choices(domain_values, k=len(domain_values))
            item_total += sum(sampled)
            item_count += len(sampled)
        if item_count:
            item_bootstrap_means.append(item_total / item_count)

        template_total = 0.0
        template_count = 0
        lower_bound_total = 0.0
        upper_bound_total = 0.0
        bound_count = 0
        for groups in template_groups:
            sampled_groups = rng.choices(groups, k=len(groups))
            template_total += sum(group[0] for group in sampled_groups)
            template_count += sum(group[1] for group in sampled_groups)
            lower_bound_total += sum(group[2] for group in sampled_groups)
            upper_bound_total += sum(group[3] for group in sampled_groups)
            bound_count += sum(group[4] for group in sampled_groups)
        if template_count:
            template_bootstrap_means.append(template_total / template_count)
        if bound_count:
            lower_bound_bootstrap_means.append(lower_bound_total / bound_count)
            upper_bound_bootstrap_means.append(upper_bound_total / bound_count)

    item_bootstrap_means.sort()
    template_bootstrap_means.sort()
    lower_bound_bootstrap_means.sort()
    upper_bound_bootstrap_means.sort()

    def bootstrap_summary(
        values: list[float], lower_probability: float, upper_probability: float
    ) -> tuple[float, float, float]:
        if not values:
            return math.nan, math.nan, 1.0
        low = percentile(values, lower_probability)
        high = percentile(values, upper_probability)
        exceedances = sum(
            abs(value - observed_mean) >= abs(observed_mean)
            for value in values
        )
        p_value = (exceedances + 1.0) / (len(values) + 1.0)
        return low, high, p_value

    item_low, item_high, item_p = bootstrap_summary(
        item_bootstrap_means, 0.025, 0.975
    )
    template_tail = ALPHA / (2.0 * MODELS)
    template_low, template_high, template_p = bootstrap_summary(
        template_bootstrap_means, template_tail, 1.0 - template_tail
    )
    endpoint_tail = ALPHA / (2.0 * MODELS * 2.0)
    lower_endpoint_low = percentile(lower_bound_bootstrap_means, endpoint_tail)
    lower_endpoint_high = percentile(
        lower_bound_bootstrap_means, 1.0 - endpoint_tail
    )
    upper_endpoint_low = percentile(upper_bound_bootstrap_means, endpoint_tail)
    upper_endpoint_high = percentile(
        upper_bound_bootstrap_means, 1.0 - endpoint_tail
    )
    return {
        "item_ci_low": item_low,
        "item_ci_high": item_high,
        "item_p": item_p,
        "template_ci_low": template_low,
        "template_ci_high": template_high,
        "template_p": template_p,
        "bound_lower_ci_low": lower_endpoint_low,
        "bound_lower_ci_high": lower_endpoint_high,
        "bound_upper_ci_low": upper_endpoint_low,
        "bound_upper_ci_high": upper_endpoint_high,
    }


def new_model_accumulator() -> dict[str, Any]:
    return {
        "gate_passes": 0,
        "template_gate_passes": 0,
        "n_complete_sum": 0.0,
        "represented_templates_sum": 0.0,
        "full_mean_sum": 0.0,
        "full_mean_square_sum": 0.0,
        "cc_estimate_sum": 0.0,
        "cc_estimate_count": 0,
        "cc_minus_roster_sum": 0.0,
        "cc_minus_roster_count": 0,
        "item_raw_rejects": 0,
        "item_holm_rejects": 0,
        "template_mean_holm_rejects": 0,
        "cluster_holm_rejects": 0,
        "claim_gate_no_bootstrap_rejects": 0,
        "loto_stable_count": 0,
        "t_intervals": [],
        "cluster_intervals": [],
        "cluster_simultaneous_intervals": [],
        "t_same_roster_cover": 0,
        "cluster_same_roster_cover": 0,
        "t_interval_count": 0,
        "cluster_interval_count": 0,
        "cluster_simultaneous_interval_count": 0,
        "bound_contains_roster": 0,
        "bound_crosses_zero": 0,
        "bound_positive": 0,
        "bound_negative": 0,
        "bound_positive_sesoi": 0,
        "bound_negative_sesoi": 0,
        "bound_width_sum": 0.0,
        "bound_lower_sum": 0.0,
        "bound_upper_sum": 0.0,
        "ceiling_cells": 0,
        "floor_cells": 0,
        "cell_count": 0,
        "bootstrap_item_intervals": [],
        "bootstrap_template_intervals": [],
        "bootstrap_bound_lower_intervals": [],
        "bootstrap_bound_upper_intervals": [],
        "bootstrap_item_holm_rejects": 0,
        "bootstrap_template_holm_rejects": 0,
        "bootstrap_full_claim_gate_rejects": 0,
        "bootstrap_evaluated": 0,
    }


def simulate_item_scenario(
    *,
    scenario: dict[str, Any],
    data_seed: int,
    bootstrap_seed: int,
    reps: int,
    bootstrap_outer_reps: int,
    bootstrap_resamples: int,
) -> list[dict[str, Any]]:
    data_rng = random.Random(data_seed)
    bootstrap_rng = random.Random(bootstrap_seed)
    accumulators = [new_model_accumulator() for _ in range(MODELS)]
    any_item_rejects = 0
    any_template_mean_rejects = 0
    any_cluster_rejects = 0
    any_claim_gate_no_bootstrap_rejects = 0
    all_item_rejects = 0
    bootstrap_any_item_rejects = 0
    bootstrap_any_template_rejects = 0
    bootstrap_any_full_claim_gate_rejects = 0
    bootstrap_family_reps = 0

    for rep_idx in range(reps):
        model_items = generate_item_data(rng=data_rng, scenario=scenario)
        item_p_values = []
        template_mean_p_values = []
        cluster_p_values = []
        records_by_model = []
        model_gate_by_model = []
        loto_by_model = []
        cluster_tests = []

        for model_idx, items in enumerate(model_items):
            accumulator = accumulators[model_idx]
            full_values = [item_interaction(item["cells"]) for item in items]
            full_mean = sum(full_values) / N_START
            accumulator["full_mean_sum"] += full_mean
            accumulator["full_mean_square_sum"] += full_mean * full_mean

            records = complete_item_records(items)
            records_by_model.append(records)
            complete_values = [record[2] for record in records]
            n_complete = len(complete_values)
            represented_templates, represented_by_domain = template_representation(
                records
            )
            family_gate_pass = n_complete >= N_GATE
            template_gate_pass = (
                represented_templates >= 20
                and all(count >= 10 for count in represented_by_domain)
            )
            model_gate_pass = family_gate_pass and template_gate_pass
            model_gate_by_model.append(model_gate_pass)
            accumulator["n_complete_sum"] += n_complete
            accumulator["represented_templates_sum"] += represented_templates
            accumulator["gate_passes"] += int(family_gate_pass)
            accumulator["template_gate_passes"] += int(template_gate_pass)

            item_test = one_sample_t(complete_values)
            template_mean_test = one_sample_t(template_means(records))
            cluster_test = cluster_robust_t(records)
            cluster_tests.append(cluster_test)
            item_gate_p = item_test["p"] if model_gate_pass else 1.0
            template_mean_gate_p = (
                template_mean_test["p"] if model_gate_pass else 1.0
            )
            cluster_gate_p = cluster_test["p"] if model_gate_pass else 1.0
            item_p_values.append(item_gate_p)
            template_mean_p_values.append(template_mean_gate_p)
            cluster_p_values.append(cluster_gate_p)
            accumulator["item_raw_rejects"] += int(item_gate_p <= ALPHA)
            loto_stable = model_gate_pass and leave_one_template_out_stable(records)
            loto_by_model.append(loto_stable)
            accumulator["loto_stable_count"] += int(loto_stable)

            if complete_values:
                cc_estimate = sum(complete_values) / n_complete
                accumulator["cc_estimate_sum"] += cc_estimate
                accumulator["cc_estimate_count"] += 1
                accumulator["cc_minus_roster_sum"] += cc_estimate - full_mean
                accumulator["cc_minus_roster_count"] += 1

            if model_gate_pass and math.isfinite(item_test["ci_low"]):
                interval = (item_test["ci_low"], item_test["ci_high"])
                accumulator["t_intervals"].append(interval)
                accumulator["t_same_roster_cover"] += int(
                    interval[0] <= full_mean <= interval[1]
                )
                accumulator["t_interval_count"] += 1

            if model_gate_pass and math.isfinite(cluster_test["ci_low"]):
                cluster_interval = (
                    cluster_test["ci_low"],
                    cluster_test["ci_high"],
                )
                accumulator["cluster_intervals"].append(cluster_interval)
                accumulator["cluster_simultaneous_intervals"].append(
                    (
                        cluster_test["sim_ci_low"],
                        cluster_test["sim_ci_high"],
                    )
                )
                accumulator["cluster_same_roster_cover"] += int(
                    cluster_interval[0] <= full_mean <= cluster_interval[1]
                )
                accumulator["cluster_interval_count"] += 1
                accumulator["cluster_simultaneous_interval_count"] += 1

            lower_bound, upper_bound = all_family_bounds(items)
            tolerance = 1.0e-12
            accumulator["bound_contains_roster"] += int(
                lower_bound - tolerance <= full_mean <= upper_bound + tolerance
            )
            accumulator["bound_crosses_zero"] += int(
                lower_bound <= 0.0 <= upper_bound
            )
            accumulator["bound_positive"] += int(lower_bound > 0.0)
            accumulator["bound_negative"] += int(upper_bound < 0.0)
            accumulator["bound_positive_sesoi"] += int(lower_bound >= SESOI)
            accumulator["bound_negative_sesoi"] += int(upper_bound <= -SESOI)
            accumulator["bound_width_sum"] += upper_bound - lower_bound
            accumulator["bound_lower_sum"] += lower_bound
            accumulator["bound_upper_sum"] += upper_bound

            for item in items:
                for value in item["cells"].values():
                    accumulator["cell_count"] += 1
                    accumulator["ceiling_cells"] += int(value >= 1.0 - 1.0e-12)
                    accumulator["floor_cells"] += int(value <= 1.0e-12)

        item_rejections = holm_rejections(item_p_values)
        template_mean_rejections = holm_rejections(template_mean_p_values)
        cluster_rejections = holm_rejections(cluster_p_values)
        claim_gate_no_bootstrap = [
            cluster_rejections[idx] and loto_by_model[idx]
            for idx in range(MODELS)
        ]
        for model_idx in range(MODELS):
            accumulators[model_idx]["item_holm_rejects"] += int(
                item_rejections[model_idx]
            )
            accumulators[model_idx]["template_mean_holm_rejects"] += int(
                template_mean_rejections[model_idx]
            )
            accumulators[model_idx]["cluster_holm_rejects"] += int(
                cluster_rejections[model_idx]
            )
            accumulators[model_idx]["claim_gate_no_bootstrap_rejects"] += int(
                claim_gate_no_bootstrap[model_idx]
            )
        any_item_rejects += int(any(item_rejections))
        any_template_mean_rejects += int(any(template_mean_rejections))
        any_cluster_rejects += int(any(cluster_rejections))
        any_claim_gate_no_bootstrap_rejects += int(
            any(claim_gate_no_bootstrap)
        )
        all_item_rejects += int(all(item_rejections))

        if rep_idx < bootstrap_outer_reps:
            item_bootstrap_p_values = []
            template_bootstrap_p_values = []
            bootstrap_results: list[dict[str, float] | None] = []
            for model_idx, records in enumerate(records_by_model):
                if not model_gate_by_model[model_idx]:
                    bootstrap_results.append(None)
                    item_bootstrap_p_values.append(1.0)
                    template_bootstrap_p_values.append(1.0)
                    continue
                result = bootstrap_inference(
                    records=records,
                    items=model_items[model_idx],
                    rng=bootstrap_rng,
                    resamples=bootstrap_resamples,
                )
                bootstrap_results.append(result)
                item_bootstrap_p_values.append(result["item_p"])
                template_bootstrap_p_values.append(result["template_p"])

            item_bootstrap_rejections = holm_rejections(
                item_bootstrap_p_values
            )
            template_bootstrap_rejections = holm_rejections(
                template_bootstrap_p_values
            )
            bootstrap_full_claim_gate = []
            for model_idx, result in enumerate(bootstrap_results):
                if result is None:
                    bootstrap_full_claim_gate.append(False)
                    continue
                mean_value = cluster_tests[model_idx]["mean"]
                bootstrap_supports_direction = (
                    result["template_ci_low"] > 0.0
                    if mean_value > 0.0
                    else result["template_ci_high"] < 0.0
                )
                bootstrap_full_claim_gate.append(
                    cluster_rejections[model_idx]
                    and loto_by_model[model_idx]
                    and bootstrap_supports_direction
                )
            for model_idx, result in enumerate(bootstrap_results):
                if result is None:
                    continue
                accumulator = accumulators[model_idx]
                accumulator["bootstrap_evaluated"] += 1
                accumulator["bootstrap_item_intervals"].append(
                    (result["item_ci_low"], result["item_ci_high"])
                )
                accumulator["bootstrap_template_intervals"].append(
                    (result["template_ci_low"], result["template_ci_high"])
                )
                accumulator["bootstrap_bound_lower_intervals"].append(
                    (
                        result["bound_lower_ci_low"],
                        result["bound_lower_ci_high"],
                    )
                )
                accumulator["bootstrap_bound_upper_intervals"].append(
                    (
                        result["bound_upper_ci_low"],
                        result["bound_upper_ci_high"],
                    )
                )
                accumulator["bootstrap_item_holm_rejects"] += int(
                    item_bootstrap_rejections[model_idx]
                )
                accumulator["bootstrap_template_holm_rejects"] += int(
                    template_bootstrap_rejections[model_idx]
                )
                accumulator["bootstrap_full_claim_gate_rejects"] += int(
                    bootstrap_full_claim_gate[model_idx]
                )
            bootstrap_any_item_rejects += int(any(item_bootstrap_rejections))
            bootstrap_any_template_rejects += int(
                any(template_bootstrap_rejections)
            )
            bootstrap_any_full_claim_gate_rejects += int(
                any(bootstrap_full_claim_gate)
            )
            bootstrap_family_reps += 1

    rows = []
    for model_idx, accumulator in enumerate(accumulators):
        population_effect = accumulator["full_mean_sum"] / reps
        complete_case_population_effect = (
            accumulator["cc_estimate_sum"] / accumulator["cc_estimate_count"]
            if accumulator["cc_estimate_count"]
            else math.nan
        )
        lower_endpoint_population = accumulator["bound_lower_sum"] / reps
        upper_endpoint_population = accumulator["bound_upper_sum"] / reps
        if reps > 1:
            variance = (
                accumulator["full_mean_square_sum"]
                - reps * population_effect * population_effect
            ) / (reps - 1)
            population_effect_mc_se = math.sqrt(max(0.0, variance) / reps)
        else:
            population_effect_mc_se = math.nan

        t_intervals = accumulator["t_intervals"]
        t_complete_case_coverage = (
            sum(
                low <= complete_case_population_effect <= high
                for low, high in t_intervals
            )
            / len(t_intervals)
            if t_intervals
            else math.nan
        )
        cluster_intervals = accumulator["cluster_intervals"]
        cluster_complete_case_coverage = (
            sum(
                low <= complete_case_population_effect <= high
                for low, high in cluster_intervals
            )
            / len(cluster_intervals)
            if cluster_intervals
            else math.nan
        )
        cluster_simultaneous_intervals = accumulator[
            "cluster_simultaneous_intervals"
        ]
        cluster_simultaneous_complete_case_coverage = (
            sum(
                low <= complete_case_population_effect <= high
                for low, high in cluster_simultaneous_intervals
            )
            / len(cluster_simultaneous_intervals)
            if cluster_simultaneous_intervals
            else math.nan
        )
        item_bootstrap_intervals = accumulator["bootstrap_item_intervals"]
        template_bootstrap_intervals = accumulator[
            "bootstrap_template_intervals"
        ]
        item_bootstrap_coverage = (
            sum(
                low <= complete_case_population_effect <= high
                for low, high in item_bootstrap_intervals
            )
            / len(item_bootstrap_intervals)
            if item_bootstrap_intervals
            else math.nan
        )
        template_bootstrap_coverage = (
            sum(
                low <= complete_case_population_effect <= high
                for low, high in template_bootstrap_intervals
            )
            / len(template_bootstrap_intervals)
            if template_bootstrap_intervals
            else math.nan
        )
        lower_endpoint_intervals = accumulator[
            "bootstrap_bound_lower_intervals"
        ]
        upper_endpoint_intervals = accumulator[
            "bootstrap_bound_upper_intervals"
        ]
        lower_endpoint_coverage = (
            sum(
                low <= lower_endpoint_population <= high
                for low, high in lower_endpoint_intervals
            )
            / len(lower_endpoint_intervals)
            if lower_endpoint_intervals
            else math.nan
        )
        upper_endpoint_coverage = (
            sum(
                low <= upper_endpoint_population <= high
                for low, high in upper_endpoint_intervals
            )
            / len(upper_endpoint_intervals)
            if upper_endpoint_intervals
            else math.nan
        )
        gate_rate = accumulator["gate_passes"] / reps
        template_gate_rate = accumulator["template_gate_passes"] / reps
        item_holm_rate = accumulator["item_holm_rejects"] / reps
        template_mean_holm_rate = (
            accumulator["template_mean_holm_rejects"] / reps
        )
        cluster_holm_rate = accumulator["cluster_holm_rejects"] / reps
        claim_gate_no_bootstrap_rate = (
            accumulator["claim_gate_no_bootstrap_rejects"] / reps
        )
        bootstrap_evaluated = accumulator["bootstrap_evaluated"]
        bootstrap_item_rate = (
            accumulator["bootstrap_item_holm_rejects"] / bootstrap_family_reps
            if bootstrap_family_reps
            else math.nan
        )
        bootstrap_template_rate = (
            accumulator["bootstrap_template_holm_rejects"]
            / bootstrap_family_reps
            if bootstrap_family_reps
            else math.nan
        )
        bootstrap_full_claim_rate = (
            accumulator["bootstrap_full_claim_gate_rejects"]
            / bootstrap_family_reps
            if bootstrap_family_reps
            else math.nan
        )
        t_count = accumulator["t_interval_count"]

        rows.append(
            {
                "scenario": scenario["scenario"],
                "alternative": scenario["alternative"],
                "model_index": model_idx + 1,
                "input_latent_interaction": scenario["effects"][model_idx],
                "outcome_regime": scenario["outcome_regime"],
                "template_icc": scenario["template_icc"],
                "template_effect_shift": scenario.get(
                    "template_effect_shift", 0.0
                ),
                "missingness": scenario["missingness"],
                "item_interaction_sd_before_clipping": ITEM_INTERACTION_SD,
                "reps": reps,
                "bootstrap_family_reps": bootstrap_family_reps,
                "bootstrap_resamples": bootstrap_resamples,
                "population_interaction_mc": population_effect,
                "population_interaction_mc_se": population_effect_mc_se,
                "complete_case_population_interaction_mc": (
                    complete_case_population_effect
                ),
                "average_complete_case_estimate": complete_case_population_effect,
                "complete_case_bias_vs_same_roster": (
                    accumulator["cc_minus_roster_sum"]
                    / accumulator["cc_minus_roster_count"]
                    if accumulator["cc_minus_roster_count"]
                    else math.nan
                ),
                "average_n_complete": accumulator["n_complete_sum"] / reps,
                "average_represented_templates": (
                    accumulator["represented_templates_sum"] / reps
                ),
                "gate_pass_probability": gate_rate,
                "gate_pass_mc_se": mc_standard_error(gate_rate, reps),
                "template_gate_pass_probability": template_gate_rate,
                "template_gate_pass_mc_se": mc_standard_error(
                    template_gate_rate, reps
                ),
                "gate_qualified_raw_t_rejection": (
                    accumulator["item_raw_rejects"] / reps
                ),
                "item_t_holm_rejection": item_holm_rate,
                "item_t_holm_mc_se": mc_standard_error(item_holm_rate, reps),
                "template_mean_t_holm_rejection": template_mean_holm_rate,
                "template_mean_t_holm_mc_se": mc_standard_error(
                    template_mean_holm_rate, reps
                ),
                "cluster_cr1_holm_rejection": cluster_holm_rate,
                "cluster_cr1_holm_mc_se": mc_standard_error(
                    cluster_holm_rate, reps
                ),
                "claim_gate_without_bootstrap_rejection": (
                    claim_gate_no_bootstrap_rate
                ),
                "claim_gate_without_bootstrap_mc_se": mc_standard_error(
                    claim_gate_no_bootstrap_rate, reps
                ),
                "any_model_item_t_holm_rejection": any_item_rejects / reps,
                "any_model_item_t_holm_mc_se": mc_standard_error(
                    any_item_rejects / reps, reps
                ),
                "any_model_template_mean_t_holm_rejection": (
                    any_template_mean_rejects / reps
                ),
                "any_model_template_mean_t_holm_mc_se": mc_standard_error(
                    any_template_mean_rejects / reps, reps
                ),
                "any_model_cluster_cr1_holm_rejection": (
                    any_cluster_rejects / reps
                ),
                "any_model_cluster_cr1_holm_mc_se": mc_standard_error(
                    any_cluster_rejects / reps, reps
                ),
                "any_model_claim_gate_without_bootstrap": (
                    any_claim_gate_no_bootstrap_rejects / reps
                ),
                "any_model_claim_gate_without_bootstrap_mc_se": (
                    mc_standard_error(
                        any_claim_gate_no_bootstrap_rejects / reps, reps
                    )
                ),
                "all_models_item_t_holm_rejection": all_item_rejects / reps,
                "all_models_item_t_holm_mc_se": mc_standard_error(
                    all_item_rejects / reps, reps
                ),
                "leave_one_template_out_stable_rate": (
                    accumulator["loto_stable_count"] / reps
                ),
                "leave_one_template_out_stable_mc_se": mc_standard_error(
                    accumulator["loto_stable_count"] / reps, reps
                ),
                "t95_complete_case_population_coverage": (
                    t_complete_case_coverage
                ),
                "t95_complete_case_coverage_mc_se": mc_standard_error(
                    t_complete_case_coverage, len(t_intervals)
                ),
                "cluster_cr1_95_complete_case_population_coverage": (
                    cluster_complete_case_coverage
                ),
                "cluster_cr1_95_coverage_mc_se": mc_standard_error(
                    cluster_complete_case_coverage, len(cluster_intervals)
                ),
                "cluster_cr1_98333_complete_case_population_coverage": (
                    cluster_simultaneous_complete_case_coverage
                ),
                "cluster_cr1_98333_coverage_mc_se": mc_standard_error(
                    cluster_simultaneous_complete_case_coverage,
                    len(cluster_simultaneous_intervals),
                ),
                "t95_same_roster_coverage": (
                    accumulator["t_same_roster_cover"] / t_count
                    if t_count
                    else math.nan
                ),
                "t95_interval_reps": t_count,
                "cluster_cr1_interval_reps": accumulator[
                    "cluster_interval_count"
                ],
                "cluster_cr1_simultaneous_interval_reps": accumulator[
                    "cluster_simultaneous_interval_count"
                ],
                "item_bootstrap_holm_rejection": bootstrap_item_rate,
                "item_bootstrap_holm_mc_se": mc_standard_error(
                    bootstrap_item_rate, bootstrap_family_reps
                ),
                "template_bootstrap_holm_rejection": bootstrap_template_rate,
                "template_bootstrap_holm_mc_se": mc_standard_error(
                    bootstrap_template_rate, bootstrap_family_reps
                ),
                "full_claim_gate_bootstrap_subset": bootstrap_full_claim_rate,
                "full_claim_gate_bootstrap_subset_mc_se": mc_standard_error(
                    bootstrap_full_claim_rate, bootstrap_family_reps
                ),
                "any_model_item_bootstrap_holm_rejection": (
                    bootstrap_any_item_rejects / bootstrap_family_reps
                    if bootstrap_family_reps
                    else math.nan
                ),
                "any_model_item_bootstrap_holm_mc_se": mc_standard_error(
                    bootstrap_any_item_rejects / bootstrap_family_reps
                    if bootstrap_family_reps
                    else math.nan,
                    bootstrap_family_reps,
                ),
                "any_model_template_bootstrap_holm_rejection": (
                    bootstrap_any_template_rejects / bootstrap_family_reps
                    if bootstrap_family_reps
                    else math.nan
                ),
                "any_model_template_bootstrap_holm_mc_se": mc_standard_error(
                    bootstrap_any_template_rejects / bootstrap_family_reps
                    if bootstrap_family_reps
                    else math.nan,
                    bootstrap_family_reps,
                ),
                "any_model_full_claim_gate_bootstrap_subset": (
                    bootstrap_any_full_claim_gate_rejects
                    / bootstrap_family_reps
                    if bootstrap_family_reps
                    else math.nan
                ),
                "any_model_full_claim_gate_bootstrap_mc_se": mc_standard_error(
                    bootstrap_any_full_claim_gate_rejects
                    / bootstrap_family_reps
                    if bootstrap_family_reps
                    else math.nan,
                    bootstrap_family_reps,
                ),
                "item_bootstrap_population_coverage": item_bootstrap_coverage,
                "item_bootstrap_coverage_mc_se": mc_standard_error(
                    item_bootstrap_coverage, len(item_bootstrap_intervals)
                ),
                "template_bootstrap_population_coverage": (
                    template_bootstrap_coverage
                ),
                "template_bootstrap_coverage_mc_se": mc_standard_error(
                    template_bootstrap_coverage,
                    len(template_bootstrap_intervals),
                ),
                "bound_lower_endpoint_population_mc": lower_endpoint_population,
                "bound_upper_endpoint_population_mc": upper_endpoint_population,
                "bound_lower_endpoint_simultaneous_coverage": (
                    lower_endpoint_coverage
                ),
                "bound_lower_endpoint_coverage_mc_se": mc_standard_error(
                    lower_endpoint_coverage, len(lower_endpoint_intervals)
                ),
                "bound_upper_endpoint_simultaneous_coverage": (
                    upper_endpoint_coverage
                ),
                "bound_upper_endpoint_coverage_mc_se": mc_standard_error(
                    upper_endpoint_coverage, len(upper_endpoint_intervals)
                ),
                "bootstrap_evaluated_reps": bootstrap_evaluated,
                "all_family_bounds_contain_same_roster": (
                    accumulator["bound_contains_roster"] / reps
                ),
                "all_family_bounds_contain_mc_se": mc_standard_error(
                    accumulator["bound_contains_roster"] / reps, reps
                ),
                "all_family_bounds_cross_zero": (
                    accumulator["bound_crosses_zero"] / reps
                ),
                "all_family_bounds_cross_zero_mc_se": mc_standard_error(
                    accumulator["bound_crosses_zero"] / reps, reps
                ),
                "all_family_positive_sign_identified": (
                    accumulator["bound_positive"] / reps
                ),
                "all_family_positive_sign_mc_se": mc_standard_error(
                    accumulator["bound_positive"] / reps, reps
                ),
                "all_family_negative_sign_identified": (
                    accumulator["bound_negative"] / reps
                ),
                "all_family_negative_sign_mc_se": mc_standard_error(
                    accumulator["bound_negative"] / reps, reps
                ),
                "all_family_positive_sesoi_identified": (
                    accumulator["bound_positive_sesoi"] / reps
                ),
                "all_family_positive_sesoi_mc_se": mc_standard_error(
                    accumulator["bound_positive_sesoi"] / reps, reps
                ),
                "all_family_negative_sesoi_identified": (
                    accumulator["bound_negative_sesoi"] / reps
                ),
                "all_family_negative_sesoi_mc_se": mc_standard_error(
                    accumulator["bound_negative_sesoi"] / reps, reps
                ),
                "average_all_family_bound_width": (
                    accumulator["bound_width_sum"] / reps
                ),
                "ceiling_cell_fraction": (
                    accumulator["ceiling_cells"] / accumulator["cell_count"]
                ),
                "floor_cell_fraction": (
                    accumulator["floor_cells"] / accumulator["cell_count"]
                ),
            }
        )
    return rows


def write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--reps", type=int, default=20000)
    parser.add_argument("--item-reps", type=int, default=5000)
    parser.add_argument("--bootstrap-outer-reps", type=int, default=200)
    parser.add_argument("--bootstrap-resamples", type=int, default=499)
    parser.add_argument("--seed", type=int, default=20261115)
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("protocol/simulations/results"),
    )
    args = parser.parse_args()

    if args.reps <= 0 or args.item_reps <= 0:
        raise ValueError("replication counts must be positive")
    if args.bootstrap_outer_reps < 0 or args.bootstrap_resamples <= 0:
        raise ValueError("bootstrap counts are invalid")

    args.output_dir.mkdir(parents=True, exist_ok=True)
    legacy_rng = random.Random(args.seed)

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
    write_csv(completeness_path, completeness_rows)

    threshold_rows = []
    for shared_failure in [0.0, 0.005, 0.01, 0.02, 0.03]:
        validity = required_cell_validity(shared_failure)
        complete_probability = (1.0 - shared_failure) * validity**4
        threshold_rows.append(
            {
                "shared_item_failure": shared_failure,
                "target_probability_at_least_86": 0.90,
                "required_equal_per_cell_validity": validity,
                "implied_family_complete_probability": complete_probability,
                "exact_probability_at_least_86": prob_at_least(
                    N_START, complete_probability, N_GATE
                ),
            }
        )
    threshold_path = args.output_dir / "gate_validity_thresholds.csv"
    write_csv(threshold_path, threshold_rows)

    power_rows = []
    for scenario_name, (shared_failure, per_cell_failure) in missingness.items():
        complete_prob = retention(shared_failure, per_cell_failure)
        exact_gate_probability = prob_at_least(N_START, complete_prob, N_GATE)
        for item_sd in item_sds:
            for effect in effects:
                result = simulate_legacy_scenario(
                    rng=legacy_rng,
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
    write_csv(power_path, power_rows)

    item_rows = []
    scenarios = item_scenarios()
    for scenario_index, scenario in enumerate(scenarios):
        item_rows.extend(
            simulate_item_scenario(
                scenario=scenario,
                data_seed=args.seed + 100_000 + scenario_index * 10_007,
                bootstrap_seed=args.seed + 900_000 + scenario_index * 20_011,
                reps=args.item_reps,
                bootstrap_outer_reps=min(
                    args.bootstrap_outer_reps, args.item_reps
                ),
                bootstrap_resamples=args.bootstrap_resamples,
            )
        )
    item_path = args.output_dir / "item_level_validation.csv"
    write_csv(item_path, item_rows)

    central_legacy = next(
        row
        for row in power_rows
        if row["missingness_scenario"] == "central"
        and row["true_raw_interaction"] == SESOI
        and row["item_interaction_sd"] == 0.15
    )
    null_legacy_rows = [
        row for row in power_rows if row["true_raw_interaction"] == 0.0
    ]
    central_single_item = next(
        row
        for row in item_rows
        if row["scenario"] == "single_interior_independent_icc00"
        and row["model_index"] == 1
    )
    item_null_anchor = next(
        row
        for row in item_rows
        if row["scenario"] == "null_interior_independent_icc00"
        and row["model_index"] == 1
    )
    clustered_null_anchor = next(
        row
        for row in item_rows
        if row["scenario"] == "null_interior_independent_icc10"
        and row["model_index"] == 1
    )
    ceiling_observed_null_anchor = next(
        row
        for row in item_rows
        if row["scenario"] == "observed_null_ceiling_informative_icc10"
        and row["model_index"] == 1
    )
    threshold_shared_one_percent = next(
        row
        for row in threshold_rows
        if row["shared_item_failure"] == 0.01
    )

    def sha256_file(path: Path) -> str:
        digest = hashlib.sha256()
        with path.open("rb") as handle:
            for chunk in iter(lambda: handle.read(1024 * 1024), b""):
                digest.update(chunk)
        return digest.hexdigest()

    script_path = Path(__file__)
    output_hashes = {
        str(path): sha256_file(path)
        for path in [completeness_path, threshold_path, power_path, item_path]
    }

    summary = {
        "status": "SYNTHETIC_PLANNING_SIMULATION_ONLY",
        "python_version": platform.python_version(),
        "script_sha256": sha256_file(script_path),
        "seed": args.seed,
        "legacy_reps_per_scenario": args.reps,
        "item_reps_per_scenario": args.item_reps,
        "bootstrap_outer_reps_per_scenario": min(
            args.bootstrap_outer_reps, args.item_reps
        ),
        "bootstrap_resamples": args.bootstrap_resamples,
        "starting_families": N_START,
        "completeness_gate": N_GATE,
        "models": MODELS,
        "alpha_familywise": ALPHA,
        "multiplicity": (
            "Holm-Bonferroni across three fixed model-specific tests; "
            "failed-gate models enter with p=1"
        ),
        "sesoi_raw": SESOI,
        "model_test_correlation": MODEL_CORRELATION,
        "historical_known_sd_central_equal_effect": central_legacy,
        "historical_max_null_any_model_gate_qualified_rejection": max(
            row["any_model_gate_qualified_rejection"]
            for row in null_legacy_rows
        ),
        "item_level_single_active_anchor": central_single_item,
        "independent_null_item_t_any_model_fwer": item_null_anchor[
            "any_model_item_t_holm_rejection"
        ],
        "independent_null_cluster_cr1_any_model_fwer": item_null_anchor[
            "any_model_cluster_cr1_holm_rejection"
        ],
        "clustered_null_cluster_cr1_any_model_fwer": clustered_null_anchor[
            "any_model_cluster_cr1_holm_rejection"
        ],
        "ceiling_observed_null_cluster_cr1_any_model_fwer": (
            ceiling_observed_null_anchor[
                "any_model_cluster_cr1_holm_rejection"
            ]
        ),
        "single_active_80pct_power_pass": (
            central_single_item["cluster_cr1_holm_rejection"] >= 0.80
            and central_single_item["full_claim_gate_bootstrap_subset"] >= 0.80
        ),
        "required_cell_validity_with_1pct_shared_failure": (
            threshold_shared_one_percent[
                "required_equal_per_cell_validity"
            ]
        ),
        "limitations": [
            "Synthetic bounded-cell generator, not empirical model behavior.",
            "Interaction SD, ICC, ceiling behavior and missingness remain assumptions.",
            "Bootstrap operating-characteristic estimates use fewer outer replications than t-test estimates and report Monte Carlo uncertainty.",
            "CR1 inference assumes independent template clusters under the registered construction-frame model.",
            "The eight-family future pilot cannot precisely certify 1-2% failure rates or SD <= 0.15.",
        ],
        "output_sha256": output_hashes,
        "outputs": [
            str(completeness_path),
            str(threshold_path),
            str(power_path),
            str(item_path),
        ],
    }
    summary_path = args.output_dir / "simulation_summary.json"
    summary_path.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")

    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
