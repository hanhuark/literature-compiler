import pytest
from pydantic import ValidationError

from litcomp.schema import DataPoint, Paper


def test_paper_requires_research_metadata():
    paper = Paper(
        paper_id="rohsenow_1952",
        title="A method of correlating heat-transfer data for surface boiling of liquids",
        authors=["W. M. Rohsenow"],
        year=1952,
        doi=None,
        tags={"process": "pool boiling", "fluid": "water"},
    )

    assert paper.paper_id == "rohsenow_1952"
    assert paper.tags["fluid"] == "water"


def test_data_point_normalizes_boiling_quantities():
    point = DataPoint(
        paper_id="demo",
        curve_id="curve_a",
        x_value=10.0,
        x_unit="K",
        y_value=100.0,
        y_unit="kW/m^2",
        source_type="digitized_figure",
        extraction_method="synthetic_image_threshold",
        digitization_confidence=0.9,
    )

    assert point.wall_superheat_K == pytest.approx(10.0)
    assert point.heat_flux_W_m2 == pytest.approx(100_000.0)


def test_data_point_rejects_unphysical_pool_boiling_values():
    with pytest.raises(ValidationError):
        DataPoint(
            paper_id="demo",
            curve_id="curve_a",
            x_value=-1.0,
            x_unit="K",
            y_value=100.0,
            y_unit="kW/m^2",
            source_type="digitized_figure",
            extraction_method="manual",
        )
