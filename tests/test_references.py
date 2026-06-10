from pathlib import Path

import yaml
from typer.testing import CliRunner

from litcomp.cli import app
from litcomp.references import load_sources, validate_reference_hub


def write_yaml(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(yaml.safe_dump(data, sort_keys=False), encoding="utf-8")


def test_load_sources_reads_canonical_registry(tmp_path: Path):
    source_path = tmp_path / "references" / "sources.yaml"
    write_yaml(
        source_path,
        {
            "sources": {
                "paper_a": {
                    "title": "A paper",
                    "authors": ["A. Researcher"],
                    "year": 2024,
                    "doi": "10.1234/example",
                    "tags": ["pool-boiling", "copper"],
                }
            }
        },
    )

    sources = load_sources(source_path)

    assert sources["paper_a"].title == "A paper"
    assert sources["paper_a"].doi == "10.1234/example"


def test_validate_reference_hub_accepts_case_refs(tmp_path: Path):
    write_yaml(
        tmp_path / "references" / "sources.yaml",
        {"sources": {"paper_a": {"title": "A paper", "authors": [], "year": 2024}}},
    )
    write_yaml(
        tmp_path / "examples" / "case_a" / "papers.yaml",
        {"papers": [{"ref_id": "paper_a", "status": "included", "notes": "case-specific note"}]},
    )

    report = validate_reference_hub(tmp_path)

    assert report.ok
    assert report.case_refs["case_a"] == ["paper_a"]


def test_validate_reference_hub_reports_missing_refs_and_duplicate_dois(tmp_path: Path):
    write_yaml(
        tmp_path / "references" / "sources.yaml",
        {
            "sources": {
                "paper_a": {"title": "A paper", "authors": [], "year": 2024, "doi": "10.1234/example"},
                "paper_b": {"title": "B paper", "authors": [], "year": 2025, "doi": "10.1234/example"},
            }
        },
    )
    write_yaml(
        tmp_path / "examples" / "case_a" / "papers.yaml",
        {"papers": [{"ref_id": "missing_paper", "status": "screen"}]},
    )

    report = validate_reference_hub(tmp_path)

    assert not report.ok
    assert "case_a references unknown ref_id missing_paper" in report.errors
    assert "duplicate DOI 10.1234/example used by paper_a and paper_b" in report.errors


def test_refs_validate_cli_reports_ok_for_repo():
    runner = CliRunner()

    result = runner.invoke(app, ["refs", "validate"])

    assert result.exit_code == 0
    assert "Reference hub OK" in result.output


def test_refs_list_cli_shows_sources_for_repo():
    runner = CliRunner()

    result = runner.invoke(app, ["refs", "list"])

    assert result.exit_code == 0
    assert "rohsenow_1952" in result.output
