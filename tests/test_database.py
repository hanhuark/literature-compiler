from pathlib import Path

import pandas as pd

from litcomp.database import compile_points, load_points_csv, save_points_csv
from litcomp.schema import DataPoint


def test_compile_points_returns_canonical_dataframe():
    points = [
        DataPoint(
            paper_id="demo",
            figure_id="fig1",
            curve_id="water",
            x_value=10,
            x_unit="K",
            y_value=100,
            y_unit="kW/m^2",
            source_type="digitized_figure",
            extraction_method="manual",
        )
    ]

    frame = compile_points(points)

    assert list(frame["paper_id"]) == ["demo"]
    assert list(frame["wall_superheat_K"]) == [10.0]
    assert list(frame["heat_flux_W_m2"]) == [100_000.0]


def test_saves_and_loads_points_csv(tmp_path: Path):
    out = tmp_path / "points.csv"
    points = [
        DataPoint(
            paper_id="demo",
            curve_id="curve",
            x_value=5,
            x_unit="K",
            y_value=50,
            y_unit="kW/m^2",
            source_type="reported_table",
            extraction_method="reported",
        )
    ]

    save_points_csv(points, out)
    loaded = load_points_csv(out)

    assert isinstance(loaded, pd.DataFrame)
    assert loaded.loc[0, "heat_flux_W_m2"] == 50_000.0
