"""Leakage-aware benchmark records for compiled thermal literature data."""

from __future__ import annotations

import hashlib
import json
import random
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Mapping

import pandas as pd
import yaml


@dataclass(frozen=True)
class GroupSplitManifest:
    """Deterministic study-level benchmark assignments.

    The manifest prevents a group from appearing in more than one partition.
    It cannot establish that reported studies are physically independent.
    """

    split_version: str
    dataset_id: str
    group_column: str
    seed: int
    assignments: Mapping[str, str]

    def as_dict(self) -> dict[str, object]:
        return asdict(self)


def _resolve_group_column(frame: pd.DataFrame, requested: str) -> str:
    if requested in frame.columns:
        return requested
    if requested == "source_group":
        for candidate in ("paper_id", "ref_id"):
            if candidate in frame.columns:
                return candidate
    raise ValueError(f"group column {requested!r} is absent and no literature-source fallback is available")


def make_group_split(
    frame: pd.DataFrame,
    *,
    dataset_id: str,
    group_column: str = "source_group",
    seed: int = 0,
    fractions: tuple[float, float, float] = (0.7, 0.15, 0.15),
) -> GroupSplitManifest:
    """Partition full literature sources, never individual curve points."""
    if not dataset_id.strip():
        raise ValueError("dataset_id must be non-empty")
    resolved_column = _resolve_group_column(frame, group_column)
    groups = sorted({str(value).strip() for value in frame[resolved_column].dropna() if str(value).strip()})
    if len(groups) < 3:
        raise ValueError("at least three non-empty source groups are required")
    if len(fractions) != 3 or any(value <= 0 for value in fractions):
        raise ValueError("train, validation, and test fractions must each be positive")
    shuffled = groups.copy()
    random.Random(seed).shuffle(shuffled)
    remaining = len(shuffled) - 3
    normalized = [value / sum(fractions) for value in fractions]
    extras = [int(remaining * value) for value in normalized]
    for index in sorted(range(3), key=lambda item: (remaining * normalized[item] % 1, -item), reverse=True)[
        : remaining - sum(extras)
    ]:
        extras[index] += 1
    train_count, validation_count, _ = [1 + value for value in extras]
    assignments = {
        group: "train" if index < train_count else "validation" if index < train_count + validation_count else "test"
        for index, group in enumerate(shuffled)
    }
    return GroupSplitManifest(
        split_version="0.1.0",
        dataset_id=dataset_id,
        group_column=resolved_column,
        seed=seed,
        assignments=dict(sorted(assignments.items())),
    )


def write_group_split(path: Path, split: GroupSplitManifest) -> None:
    """Write a stable split artifact without modifying the compiled dataset."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(split.as_dict(), indent=2, sort_keys=True) + "\n", encoding="utf-8")


def _sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def export_thermal_ai_commons_manifest(
    data_path: Path, case_path: Path, output_path: Path
) -> dict[str, object]:
    """Export a core Thermal AI Commons manifest for a literature compilation.

    The output identifies records as derived literature data and deliberately
    keeps redistribution permission pending until each source is reviewed.
    """
    case = yaml.safe_load(case_path.read_text(encoding="utf-8"))
    frame = pd.read_csv(data_path)
    source_types = set(frame.get("source_type", pd.Series(dtype=str)).dropna())
    evidence_class = "mixed" if "user_experiment" in source_types else "derived"
    manifest: dict[str, object] = {
        "schema_version": "0.1.0",
        "experiment_id": case["case_id"],
        "evidence_class": evidence_class,
        "modalities": [
            {
                "name": "other",
                "time_base": "not_applicable_literature_records",
                "units": "canonical units are defined per compiled variable",
                "data_access": "not_released",
            }
        ],
        "operating_conditions": {
            "case_title": case.get("title"),
            "process": case.get("process"),
            "fluid": case.get("fluid"),
            "pressure": case.get("pressure"),
        },
        "calibration": {"status": "source_or_digitization_dependent"},
        "uncertainty": {"status": "source_dependent_not_uniformly_verified"},
        "rights": {
            "owner": "Literature compiler contributors; source-specific rights pending review",
            "redistribution_permission": "pending",
            "review_state": "in_review",
        },
        "literature_compilation": {
            "data_path": data_path.as_posix(),
            "data_sha256": _sha256_file(data_path),
            "record_count": int(len(frame)),
            "source_types": sorted(source_types),
            "claim_boundary": "Provenance export only; not evidence of data verification or model validation.",
        },
    }
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return manifest
