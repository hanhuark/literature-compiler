from __future__ import annotations

import importlib.util
from pathlib import Path

import pandas as pd


REPO_ROOT = Path(__file__).resolve().parents[1]


def load_builder(case_id: str):
    case_dir = REPO_ROOT / "examples" / case_id
    spec = importlib.util.spec_from_file_location(f"{case_id}_builder", case_dir / "build_pumping_power_plot.py")
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module, case_dir


def test_single_phase_case_compiles_empty_screening_dataset():
    builder, case_dir = load_builder("test4_MMC_heat_sink_single-phase")
    compiled = builder.compile_points(pd.read_csv(case_dir / "data" / "reported_points.csv"))
    assert compiled.empty
    assert "pumping_power_calculation" in compiled.columns


def test_two_phase_case_compiles_empty_screening_dataset():
    builder, case_dir = load_builder("test5_MMC_heat_sink_two-phase")
    compiled = builder.compile_points(pd.read_csv(case_dir / "data" / "reported_points.csv"))
    assert compiled.empty
    assert "pumping_power_calculation" in compiled.columns


def test_pumping_power_is_calculated_in_si_units():
    builder, _ = load_builder("test4_MMC_heat_sink_single-phase")
    point = pd.DataFrame([{
        "paper_id": "synthetic", "architecture": "MMC", "point_id": "p1", "thermal_resistance_K_W": 0.1,
        "pressure_drop_Pa": 5000.0, "volumetric_flow_m3_s": 2.0e-5, "pumping_power_W": float("nan"),
        "thermal_resistance_definition": "heater-to-inlet", "pressure_boundary": "core", "source_type": "reported_table",
        "extraction_method": "synthetic_test", "include_in_plot": "true",
    }])
    compiled = builder.compile_points(point)
    assert compiled.loc[0, "pumping_power_W"] == 0.1
    assert compiled.loc[0, "pumping_power_calculation"] == "pressure_drop_x_volumetric_flow"
