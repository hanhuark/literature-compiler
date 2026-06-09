import pytest

from litcomp.units import convert_value, normalize_unit


def test_converts_heat_flux_units_to_w_per_m2():
    assert convert_value(100.0, "kW/m^2", "W/m^2") == pytest.approx(100_000.0)
    assert convert_value(1.2, "MW/m^2", "W/m^2") == pytest.approx(1_200_000.0)


def test_converts_temperature_difference_units_to_kelvin():
    assert convert_value(12.5, "C", "K", quantity="temperature_difference") == pytest.approx(12.5)
    assert convert_value(18.0, "F", "K", quantity="temperature_difference") == pytest.approx(10.0)


def test_rejects_unknown_units():
    with pytest.raises(ValueError, match="Unsupported unit"):
        normalize_unit("BTU banana")
