from __future__ import annotations

_ALIASES = {
    "w/m2": "W/m^2",
    "w/m^2": "W/m^2",
    "kw/m2": "kW/m^2",
    "kw/m^2": "kW/m^2",
    "mw/m2": "MW/m^2",
    "mw/m^2": "MW/m^2",
    "k": "K",
    "kelvin": "K",
    "c": "C",
    "degc": "C",
    "f": "F",
    "degf": "F",
}

_HEAT_FLUX_TO_W_M2 = {
    "W/m^2": 1.0,
    "kW/m^2": 1_000.0,
    "MW/m^2": 1_000_000.0,
}


def normalize_unit(unit: str) -> str:
    key = unit.strip().replace(" ", "").lower()
    if key in _ALIASES:
        return _ALIASES[key]
    if unit in _HEAT_FLUX_TO_W_M2 or unit == "K":
        return unit
    raise ValueError(f"Unsupported unit: {unit}")


def convert_value(value: float, from_unit: str, to_unit: str, quantity: str | None = None) -> float:
    source = normalize_unit(from_unit)
    target = normalize_unit(to_unit)
    if source == target:
        return float(value)
    if source in _HEAT_FLUX_TO_W_M2 and target in _HEAT_FLUX_TO_W_M2:
        return float(value) * _HEAT_FLUX_TO_W_M2[source] / _HEAT_FLUX_TO_W_M2[target]
    if quantity == "temperature_difference" and target == "K":
        if source == "C":
            return float(value)
        if source == "F":
            return float(value) * 5.0 / 9.0
    raise ValueError(f"Cannot convert {from_unit} to {to_unit}")
