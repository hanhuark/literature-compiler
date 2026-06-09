import numpy as np

from litcomp.models import RohsenowParameters, rohsenow_heat_flux


def test_rohsenow_heat_flux_increases_with_wall_superheat():
    params = RohsenowParameters()
    heat_flux = rohsenow_heat_flux(np.array([5.0, 10.0, 15.0]), params)

    assert heat_flux[0] > 0
    assert heat_flux[2] > heat_flux[1] > heat_flux[0]


def test_rohsenow_returns_w_per_m2_scale():
    params = RohsenowParameters()
    heat_flux = rohsenow_heat_flux(np.array([10.0]), params)

    assert 1_000.0 < heat_flux[0] < 10_000_000.0
