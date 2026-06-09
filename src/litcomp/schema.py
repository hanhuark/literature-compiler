from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, Field, model_validator

from .units import convert_value

SourceType = Literal["reported_table", "reported_text", "digitized_figure", "user_experiment"]


class Paper(BaseModel):
    paper_id: str
    title: str
    authors: list[str]
    year: int
    doi: str | None = None
    source_url: str | None = None
    zotero_item_key: str | None = None
    tags: dict[str, str] = Field(default_factory=dict)
    notes: str = ""


class DataPoint(BaseModel):
    paper_id: str
    curve_id: str
    x_value: float
    x_unit: str
    y_value: float
    y_unit: str
    source_type: SourceType
    extraction_method: str
    figure_id: str | None = None
    table_id: str | None = None
    digitization_confidence: float | None = Field(default=None, ge=0.0, le=1.0)
    notes: str = ""
    wall_superheat_K: float | None = None
    heat_flux_W_m2: float | None = None

    @model_validator(mode="after")
    def derive_and_validate_boiling_quantities(self) -> "DataPoint":
        if self.wall_superheat_K is None:
            self.wall_superheat_K = convert_value(
                self.x_value, self.x_unit, "K", quantity="temperature_difference"
            )
        if self.heat_flux_W_m2 is None:
            self.heat_flux_W_m2 = convert_value(self.y_value, self.y_unit, "W/m^2")
        if self.wall_superheat_K < 0:
            raise ValueError("wall_superheat_K must be nonnegative")
        if self.heat_flux_W_m2 <= 0:
            raise ValueError("heat_flux_W_m2 must be positive")
        return self
