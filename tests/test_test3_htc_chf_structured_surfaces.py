from __future__ import annotations

import importlib.util
from pathlib import Path

import pandas as pd
import pytest


REPO_ROOT = Path(__file__).resolve().parents[1]
CASE_DIR = REPO_ROOT / "examples" / "test3_htc_chf_structured_surfaces"


def load_builder():
    spec = importlib.util.spec_from_file_location("test3_builder", CASE_DIR / "build_manual_seed_dataset.py")
    assert spec is not None
    assert spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_test3_manual_seed_compiles_expected_points():
    builder = load_builder()
    seed = pd.read_csv(CASE_DIR / "data" / "manual_seed_points.csv")

    compiled = builder.build_compiled_points(seed)

    assert len(seed) == 26
    assert len(compiled) == 23
    assert set(compiled["surface_family"]) == {"hierarchical", "micro", "nano"}
    assert compiled.loc[compiled["manual_id"].eq("C1"), "htc_at_chf_W_cm2K"].iloc[0] == pytest.approx(12.5)
    assert compiled.loc[compiled["manual_id"].eq("C23"), "htc_at_chf_W_cm2K"].iloc[0] == pytest.approx(42.0)


def test_test3_reference_limits_match_manual_formula():
    builder = load_builder()

    limits = builder.build_reference_limits()
    zuber = limits.loc[limits["limit_id"].eq("zuber_hydrodynamic_limit"), "chf_W_cm2"].iloc[0]
    kinetic = limits.loc[limits["limit_id"].eq("kinetic_limit"), "chf_W_cm2"].iloc[0]

    assert zuber == pytest.approx(110.942, rel=1e-3)
    assert kinetic == pytest.approx(16_500.0)
