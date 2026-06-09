from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from .models import RohsenowParameters, rohsenow_heat_flux
from .schema import DataPoint

WATER_SATURATION_TEMPERATURE_1ATM_C = 100.0


def plot_boiling_curve(
    points: list[DataPoint],
    output_path: str | Path,
    include_rohsenow: bool = False,
    include_envelope: bool = True,
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
            [_wall_temperature_C(point) for point in sorted_group],
            [_heat_flux_W_cm2(point) for point in sorted_group],
            marker="o",
            linestyle="-",
            label=f"{paper_id}:{curve_id}",
        )
    if include_envelope and len(groups) >= 2:
        _plot_literature_envelope(ax, groups)
    if include_rohsenow:
        x_max = max(point.wall_superheat_K or 1.0 for point in points)
        superheat = np.linspace(0.1, max(20.0, x_max), 120)
        wall_temperature = WATER_SATURATION_TEMPERATURE_1ATM_C + superheat
        ax.plot(
            wall_temperature,
            rohsenow_heat_flux(superheat, RohsenowParameters()) / 10000.0,
            "k--",
            label="Rohsenow demo",
        )
    ax.set_xlabel(r"Wall temperature, $T_{\mathrm{w}}$ (°C)")
    ax.set_ylabel(r"Heat flux, $q''$ (W/cm²)")
    ax.set_yscale("log")
    data_fluxes = [_heat_flux_W_cm2(point) for point in points if point.heat_flux_W_m2]
    if data_fluxes:
        ax.set_ylim(max(min(data_fluxes) * 0.5, 1.0), max(data_fluxes) * 1.8)
    ax.grid(True, which="both", alpha=0.3)
    ax.legend(fontsize=8)
    fig.savefig(destination, dpi=200)
    plt.close(fig)
    return destination


def _wall_temperature_C(point: DataPoint) -> float | None:
    if point.wall_superheat_K is None:
        return None
    return WATER_SATURATION_TEMPERATURE_1ATM_C + point.wall_superheat_K


def _heat_flux_W_cm2(point: DataPoint) -> float:
    return (point.heat_flux_W_m2 or 0.0) / 10000.0


def _plot_literature_envelope(ax: plt.Axes, groups: dict[tuple[str, str], list[DataPoint]]) -> None:
    x_min = min(_wall_temperature_C(point) or 0.0 for group in groups.values() for point in group)
    x_max = max(_wall_temperature_C(point) or 0.0 for group in groups.values() for point in group)
    x_grid = np.linspace(x_min, x_max, 160)
    lower: list[float] = []
    upper: list[float] = []
    x_envelope: list[float] = []
    for x_value in x_grid:
        y_values: list[float] = []
        for group in groups.values():
            sorted_group = sorted(group, key=lambda point: point.wall_superheat_K or 0.0)
            x_points = np.array(
                [_wall_temperature_C(point) for point in sorted_group if point.wall_superheat_K is not None]
            )
            y_points = np.array([_heat_flux_W_cm2(point) for point in sorted_group if point.wall_superheat_K is not None])
            if len(x_points) >= 2 and x_points[0] <= x_value <= x_points[-1]:
                y_values.append(float(np.interp(x_value, x_points, y_points)))
        if len(y_values) >= 2:
            x_envelope.append(float(x_value))
            lower.append(min(y_values))
            upper.append(max(y_values))
    if x_envelope:
        ax.fill_between(x_envelope, lower, upper, color="0.75", alpha=0.25, label="Literature range")
