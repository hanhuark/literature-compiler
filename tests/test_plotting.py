from pathlib import Path

from litcomp.plotting import plot_boiling_curve
from litcomp.schema import DataPoint


def test_plot_boiling_curve_writes_png(tmp_path: Path):
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
        ),
        DataPoint(
            paper_id="demo",
            curve_id="curve",
            x_value=10,
            x_unit="K",
            y_value=120,
            y_unit="kW/m^2",
            source_type="reported_table",
            extraction_method="reported",
        ),
    ]
    out = tmp_path / "plot.png"

    plot_boiling_curve(points, out, include_rohsenow=True)

    assert out.exists()
    assert out.stat().st_size > 0
