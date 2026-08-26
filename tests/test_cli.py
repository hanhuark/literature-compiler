import json

from typer.testing import CliRunner

from litcomp.cli import app


def test_cli_version():
    runner = CliRunner()
    result = runner.invoke(app, ["version"])

    assert result.exit_code == 0
    assert "literature-compiler" in result.output


def test_cli_creates_source_group_split_and_commons_manifest(tmp_path):
    csv_path = tmp_path / "points.csv"
    csv_path.write_text(
        "paper_id,source_type\na,reported_table\nb,reported_table\nc,digitized_figure\n",
        encoding="utf-8",
    )
    case_path = tmp_path / "case.yaml"
    case_path.write_text("case_id: cli-demo\ntitle: CLI demo\n", encoding="utf-8")
    split_path = tmp_path / "split.json"
    manifest_path = tmp_path / "manifest.json"
    runner = CliRunner()

    split_result = runner.invoke(
        app,
        ["benchmark", "split", str(csv_path), str(split_path), "--dataset-id", "cli-demo", "--seed", "3"],
    )
    manifest_result = runner.invoke(
        app,
        ["commons", "export-manifest", str(csv_path), "--case", str(case_path), str(manifest_path)],
    )

    assert split_result.exit_code == 0
    assert manifest_result.exit_code == 0
    assert set(json.loads(split_path.read_text(encoding="utf-8"))["assignments"].values()) == {
        "train",
        "validation",
        "test",
    }
    assert json.loads(manifest_path.read_text(encoding="utf-8"))["rights"]["review_state"] == "in_review"
