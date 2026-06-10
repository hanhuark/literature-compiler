from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml
from pydantic import BaseModel, Field


class ReferenceSource(BaseModel):
    title: str
    authors: list[str] = Field(default_factory=list)
    year: int | None = None
    doi: str | None = None
    source_url: str | None = None
    zotero_key: str | None = None
    tags: list[str] | dict[str, Any] = Field(default_factory=list)
    notes: str | None = None


@dataclass
class ReferenceValidationReport:
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    case_refs: dict[str, list[str]] = field(default_factory=dict)

    @property
    def ok(self) -> bool:
        return not self.errors


def load_sources(path: str | Path) -> dict[str, ReferenceSource]:
    source_path = Path(path)
    raw = yaml.safe_load(source_path.read_text(encoding="utf-8")) or {}
    sources = raw.get("sources", {})
    if not isinstance(sources, dict):
        raise ValueError(f"{source_path} must contain a mapping named 'sources'")
    return {ref_id: ReferenceSource(**metadata) for ref_id, metadata in sources.items()}


def validate_reference_hub(repo_root: str | Path = ".") -> ReferenceValidationReport:
    root = Path(repo_root)
    report = ReferenceValidationReport()
    source_path = root / "references" / "sources.yaml"
    if not source_path.exists():
        report.errors.append("missing references/sources.yaml")
        return report

    try:
        sources = load_sources(source_path)
    except Exception as exc:
        report.errors.append(f"could not load references/sources.yaml: {exc}")
        return report

    _validate_duplicate_dois(sources, report)
    case_paths = sorted((root / "examples").glob("*/papers.yaml"))
    for case_path in case_paths:
        case_id = case_path.parent.name
        refs = _load_case_ref_ids(case_path)
        report.case_refs[case_id] = refs
        for ref_id in refs:
            if ref_id not in sources:
                report.errors.append(f"{case_id} references unknown ref_id {ref_id}")
    used_refs = {ref_id for refs in report.case_refs.values() for ref_id in refs}
    for ref_id in sorted(set(sources) - used_refs):
        report.warnings.append(f"{ref_id} is in references/sources.yaml but is not used by any case")
    return report


def _validate_duplicate_dois(sources: dict[str, ReferenceSource], report: ReferenceValidationReport) -> None:
    seen: dict[str, str] = {}
    for ref_id, source in sources.items():
        if not source.doi:
            continue
        doi = source.doi.lower()
        if doi in seen:
            report.errors.append(f"duplicate DOI {source.doi} used by {seen[doi]} and {ref_id}")
        else:
            seen[doi] = ref_id


def _load_case_ref_ids(path: Path) -> list[str]:
    raw = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    papers = raw.get("papers", [])
    refs: list[str] = []
    for item in papers:
        if not isinstance(item, dict):
            continue
        ref_id = item.get("ref_id") or item.get("paper_id")
        if ref_id:
            refs.append(str(ref_id))
    return refs
