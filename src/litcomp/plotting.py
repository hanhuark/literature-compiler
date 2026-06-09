from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from .models import RohsenowParameters, rohsenow_heat_flux
from .schema import DataPoint


def plot_boiling_curve(
    points: list[DataPoint],
    output_path: str | Path,
    include_rohsenow: bool = False,
) -> Path:
    destination = Path(output_path)
    destination.parent.mkdir(parents=True, exist_ok=True)
    fig, ax = plt.subplots(figsize=(6.5, 4.5), constrained_layout=True)
    groups: dict[tuple[str, str], list[DataPoint]] = {}
    for point in points:
        groups.setdefault((point.paper_id, point.curve_id), []).append(point)
    for (paper_id, curve_id), group in groups.items():
        sorted_group = sorted(group, key=lambda point: point.wall_superheat_K or 0.0)
        ax.plot(
            [point.wall_superheat_K for point in sorted_group],
            [(point.heat_flux_W_m2 or 0.0) / 1000.0 for point in sorted_group],
            marker="o",
            linestyle="-",
            label=f"{paper_id}:{curve_id}",
        )
    if include_rohsenow:
        x_max = max(point.wall_superheat_K or 1.0 for point in points)
        x = np.linspace(0.1, max(20.0, x_max), 120)
        ax.plot(x, rohsenow_heat_flux(x, RohsenowParameters()) / 1000.0, "k--", label="Rohsenow demo")
    ax.set_xlabel("Wall superheat, ΔT [K]")
    ax.set_ylabel("Heat flux, q'' [kW/m²]")
    ax.set_yscale("log")
    ax.grid(True, which="both", alpha=0.3)
    ax.legend(fontsize=8)
    fig.savefig(destination, dpi=200)
    plt.close(fig)
    return destination
