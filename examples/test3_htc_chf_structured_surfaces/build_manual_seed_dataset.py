from __future__ import annotations

import math
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


ROOT = Path(__file__).resolve().parent
DATA_DIR = ROOT / "data"
SUMMARY_DIR = ROOT / "summary"

WATER_PROPERTIES_1ATM = {
    "surface_tension_N_m": 0.0589,
    "latent_heat_J_kg": 2.2567e6,
    "liquid_density_kg_m3": 958.0,
    "vapor_density_kg_m3": 0.6,
    "gravity_m_s2": 9.8,
}

KINETIC_LIMIT_W_CM2 = 16_500.0


def zuber_limit_water_W_cm2() -> float:
    props = WATER_PROPERTIES_1ATM
    chf_W_m2 = (
        math.pi
        / 24.0
        * math.sqrt(props["vapor_density_kg_m3"])
        * props["latent_heat_J_kg"]
        * (
            props["surface_tension_N_m"]
            * props["gravity_m_s2"]
            * (props["liquid_density_kg_m3"] - props["vapor_density_kg_m3"])
        )
        ** 0.25
    )
    return chf_W_m2 / 10_000.0


def build_compiled_points(seed: pd.DataFrame) -> pd.DataFrame:
    included = seed[seed["include_in_seed_plot"].astype(str).str.lower().eq("true")].copy()
    included["chf_W_m2"] = included["chf_W_cm2"] * 10_000.0
    included["htc_at_chf_W_cm2K"] = included["chf_W_cm2"] / included["wall_superheat_at_chf_K"]
    included["htc_at_chf_W_m2K"] = included["htc_at_chf_W_cm2K"] * 10_000.0
    included["zuber_limit_ratio"] = included["chf_W_cm2"] / zuber_limit_water_W_cm2()
    included["extraction_method"] = "manual_matlab_seed_chf_divided_by_wall_superheat"
    included["source_type"] = "manual_seed_from_prior_compilation"
    included["units_note"] = "CHF in W/cm2; wall superheat in K; HTC computed as CHF / wall_superheat_at_chf."
    return included.sort_values(["surface_family", "chf_W_cm2", "manual_id"]).reset_index(drop=True)


def build_reference_limits() -> pd.DataFrame:
    return pd.DataFrame(
        [
            {
                "limit_id": "zuber_hydrodynamic_limit",
                "chf_W_cm2": zuber_limit_water_W_cm2(),
                "basis": "Water at 0.1 MPa and 100 C using the same properties as the manual MATLAB script.",
            },
            {
                "limit_id": "kinetic_limit",
                "chf_W_cm2": KINETIC_LIMIT_W_CM2,
                "basis": "Manual comparison line retained from the MATLAB seed script.",
            },
        ]
    )


def write_summary_plot(compiled: pd.DataFrame, limits: pd.DataFrame, output_path: Path) -> Path:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    colors = {"hierarchical": "#1b7f3a", "micro": "#2468d8", "nano": "#d62728"}
    markers = {"hierarchical": "s", "micro": "o", "nano": "^"}

    fig, (ax_left, ax_right) = plt.subplots(
        1,
        2,
        figsize=(9.2, 5.0),
        sharey=True,
        gridspec_kw={"width_ratios": [5.5, 1.2], "wspace": 0.06},
        constrained_layout=True,
    )

    for family, group in compiled.groupby("surface_family"):
        for axis in (ax_left, ax_right):
            axis.scatter(
                group["chf_W_cm2"],
                group["htc_at_chf_W_cm2K"],
                label=family if axis is ax_left else None,
                s=52,
                marker=markers.get(family, "o"),
                facecolors="none",
                edgecolors=colors.get(family, "0.2"),
                linewidths=1.5,
            )

    zuber = float(limits.loc[limits["limit_id"].eq("zuber_hydrodynamic_limit"), "chf_W_cm2"].iloc[0])
    kinetic = float(limits.loc[limits["limit_id"].eq("kinetic_limit"), "chf_W_cm2"].iloc[0])
    ax_left.axvline(zuber, color="0.35", linestyle="--", linewidth=1.4)
    ax_right.axvline(kinetic, color="0.35", linestyle="--", linewidth=1.4)
    ax_left.text(zuber + 4, 0.03, "Zuber", transform=ax_left.get_xaxis_transform(), va="bottom", fontsize=9)
    ax_right.text(kinetic, 0.96, "Kinetic", transform=ax_right.get_xaxis_transform(), va="top", ha="center", fontsize=9)

    ax_left.set_xlim(80, 430)
    ax_right.set_xlim(16_450, 16_550)
    ax_left.set_ylim(0, max(45.0, compiled["htc_at_chf_W_cm2K"].max() * 1.08))
    ax_left.set_xlabel("Critical heat flux, q''CHF (W/cm2)")
    ax_right.set_xlabel("")
    ax_left.set_ylabel("HTC at CHF, hCHF (W/cm2K)")
    ax_left.set_title("Manual seed: saturated pool boiling of water on structured surfaces")
    ax_left.grid(True, alpha=0.25)
    ax_right.grid(True, axis="x", alpha=0.25)
    ax_right.tick_params(labelleft=False, left=False)
    ax_left.legend(title="Surface family", loc="upper left", fontsize=8, title_fontsize=9)

    ax_left.spines["right"].set_visible(False)
    ax_right.spines["left"].set_visible(False)
    diagonal_kwargs = dict(marker=[(-1, -0.7), (1, 0.7)], markersize=8, linestyle="none", color="k", mec="k", mew=1)
    ax_left.plot([1, 1], [0, 1], transform=ax_left.transAxes, **diagonal_kwargs)
    ax_right.plot([0, 0], [0, 1], transform=ax_right.transAxes, **diagonal_kwargs)

    fig.savefig(output_path, dpi=220)
    plt.close(fig)
    return output_path


def build_case_outputs() -> tuple[Path, Path, Path]:
    seed = pd.read_csv(DATA_DIR / "manual_seed_points.csv")
    compiled = build_compiled_points(seed)
    limits = build_reference_limits()

    compiled_path = DATA_DIR / "compiled_points.csv"
    limits_path = DATA_DIR / "reference_limits.csv"
    plot_path = SUMMARY_DIR / "test3_htc_chf_structured_surfaces.png"

    compiled.to_csv(compiled_path, index=False)
    limits.to_csv(limits_path, index=False)
    write_summary_plot(compiled, limits, plot_path)
    return compiled_path, limits_path, plot_path


def main() -> None:
    compiled_path, limits_path, plot_path = build_case_outputs()
    compiled = pd.read_csv(compiled_path)
    print(f"Wrote {len(compiled)} compiled points to {compiled_path}")
    print(f"Wrote reference limits to {limits_path}")
    print(f"Wrote summary plot to {plot_path}")
    print(compiled.groupby("surface_family").size().to_string())


if __name__ == "__main__":
    main()
