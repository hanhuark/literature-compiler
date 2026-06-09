from __future__ import annotations

from dataclasses import dataclass

import numpy as np


@dataclass(frozen=True)
class RohsenowParameters:
    """Default water/copper-like parameters for demonstration, not universal design constants."""

    mu_l: float = 2.82e-4
    h_fg: float = 2.257e6
    g: float = 9.80665
    rho_l: float = 958.0
    rho_v: float = 0.597
    sigma: float = 0.0589
    c_p_l: float = 4217.0
    pr_l: float = 1.75
    c_sf: float = 0.013
    n: float = 1.0


def rohsenow_heat_flux(wall_superheat_K: np.ndarray | list[float], params: RohsenowParameters) -> np.ndarray:
    """Return nucleate pool-boiling heat flux in W/m^2 using a Rohsenow-style correlation."""

    delta_t = np.asarray(wall_superheat_K, dtype=float)
    if np.any(delta_t < 0):
        raise ValueError("wall_superheat_K must be nonnegative")
    coefficient = (
        params.mu_l
        * params.h_fg
        * np.sqrt(params.g * (params.rho_l - params.rho_v) / params.sigma)
    )
    bracket = params.c_p_l * delta_t / (params.c_sf * params.h_fg * params.pr_l**params.n)
    return coefficient * bracket**3
