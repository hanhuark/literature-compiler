from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


ROOT = Path(__file__).resolve().parent
DATA_DIR = ROOT / "data"
SUMMARY_DIR = ROOT / "summary"
REQUIRED_COLUMNS = {
    "paper_id",
    "architecture",
    "point_id",
    "thermal_resistance_K_W",
    "pressure_drop_Pa",
    "volumetric_flow_m3_s",
    "pumping_power_W",
    "thermal_resistance_definition",
    "pressure_boundary",
    "source_type",
    "extraction_method",
    "include_in_plot",
}


def load_reported_points(path: Path) -> pd.DataFrame:
    points = pd.read_csv(path)
    missing = REQUIRED_COLUMNS.difference(points.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")
    return points


def compile_points(points: pd.DataFrame) -> pd.DataFrame:
    if points.empty:
        return points.assign(pumping_power_calculation="no_plot_ready_points")

    compiled = points.copy()
    compiled["architecture"] = compiled["architecture"].astype(str).str.upper()
    if not compiled["architecture"].isin({"MMC", "SMC"}).all():
        raise ValueError("architecture must be MMC or SMC")
    compiled["include_in_plot"] = compiled["include_in_plot"].astype(str).str.lower().eq("true")
    derived = compiled["pressure_drop_Pa"] * compiled["volumetric_flow_m3_s"]
    reported = pd.to_numeric(compiled["pumping_power_W"], errors="coerce")
    compiled["pumping_power_W"] = reported.where(reported.notna(), derived)
    compiled["pumping_power_calculation"] = reported.notna().map({True: "reported", False: "pressure_drop_x_volumetric_flow"})

    plotted = compiled[compiled["include_in_plot"]].copy()
    if plotted.empty:
        return compiled
    needed = ["thermal_resistance_K_W", "pumping_power_W", "thermal_resistance_definition", "pressure_boundary"]
    if plotted[needed].isna().any().any() or (plotted["thermal_resistance_K_W"] <= 0).any() or (plotted["pumping_power_W"] <= 0).any():
        raise ValueError("Plot-ready rows need positive thermal resistance and pumping power plus named thermal and pressure boundaries")
    return compiled


def write_plot(compiled: pd.DataFrame, output_path: Path) -> Path | None:
    plotted = compiled[compiled["include_in_plot"]].copy() if "include_in_plot" in compiled else compiled.iloc[0:0]
    if plotted.empty:
        return None
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fig, ax = plt.subplots(figsize=(7.2, 4.8), constrained_layout=True)
    colors = {"MMC": "#1f77b4", "SMC": "#d62728"}
    for (paper_id, architecture), group in plotted.groupby(["paper_id", "architecture"], sort=True):
        group = group.sort_values("pumping_power_W")
        ax.plot(group["pumping_power_W"], group["thermal_resistance_K_W"], marker="o", linewidth=1.3, markersize=4.5, color=colors[architecture], label=f"{paper_id}: {architecture}")
    ax.set_xscale("log")
    ax.set_xlabel("Pumping power, Ppump (W)")
    ax.set_ylabel("Thermal resistance, Rth (K/W)")
    ax.set_title("Single-phase MMC and SMC literature points")
    ax.grid(True, which="both", alpha=0.25)
    ax.legend(fontsize=8)
    fig.savefig(output_path, dpi=220)
    plt.close(fig)
    return output_path


def build_case_outputs() -> tuple[Path, Path | None]:
    reported_path = DATA_DIR / "reported_points.csv"
    compiled_path = DATA_DIR / "compiled_points.csv"
    plot_path = SUMMARY_DIR / "test4_MMC_heat_sink_single-phase.png"
    compiled = compile_points(load_reported_points(reported_path))
    compiled.to_csv(compiled_path, index=False)
    return compiled_path, write_plot(compiled, plot_path)


def main() -> None:
    compiled_path, plot_path = build_case_outputs()
    print(f"Wrote compiled points to {compiled_path}")
    print(f"Wrote plot to {plot_path}" if plot_path else "No plot written: no source-audited plot-ready points are currently committed.")


if __name__ == "__main__":
    main()
