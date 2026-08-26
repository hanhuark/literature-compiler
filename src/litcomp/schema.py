from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, Field, model_validator

from .units import convert_value

SourceType = Literal["reported_table", "reported_text", "digitized_figure", "user_experiment"]
VerificationStatus = Literal["unverified", "screening", "source_checked", "independently_verified"]
RightsStatus = Literal["unknown", "metadata_only", "pending_review", "approved_for_release", "restricted"]
EvidenceClass = Literal["reported", "digitized", "measured"]


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
    study_id: str | None = None
    experiment_id: str | None = None
    source_group: str | None = None
    evidence_class: EvidenceClass | None = None
    verification_status: VerificationStatus = "unverified"
    rights_status: RightsStatus = "unknown"
    relative_uncertainty_pct: float | None = Field(default=None, ge=0.0)
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
        if self.study_id is None:
            self.study_id = self.paper_id
        if self.experiment_id is None:
            self.experiment_id = f"{self.paper_id}:{self.curve_id}"
        if self.source_group is None:
            self.source_group = self.study_id
        derived_evidence_class: EvidenceClass = (
            "digitized"
            if self.source_type == "digitized_figure"
            else "measured"
            if self.source_type == "user_experiment"
            else "reported"
        )
        if self.evidence_class is None:
            self.evidence_class = derived_evidence_class
        elif self.evidence_class != derived_evidence_class:
            raise ValueError("evidence_class must agree with source_type")
        return self
