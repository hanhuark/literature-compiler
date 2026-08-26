import json
from pathlib import Path

import pandas as pd

from litcomp.benchmark import export_thermal_ai_commons_manifest, make_group_split, write_group_split


def test_source_group_split_is_deterministic_and_prevents_group_overlap(tmp_path: Path):
    frame = pd.DataFrame(
        {
            "paper_id": ["a", "a", "b", "b", "c", "d", "e", "f"],
            "curve_id": ["1", "2", "1", "2", "1", "1", "1", "1"],
        }
    )
    first = make_group_split(frame, dataset_id="demo-v0.1", seed=42)
    second = make_group_split(frame.sample(frac=1, random_state=1), dataset_id="demo-v0.1", seed=42)

    assert first.assignments == second.assignments
    assert first.group_column == "paper_id"
    assert set(first.assignments) == set(frame["paper_id"])
    assert set(first.assignments.values()) == {"train", "validation", "test"}

    output = tmp_path / "split.json"
    write_group_split(output, first)
    assert json.loads(output.read_text(encoding="utf-8"))["assignments"] == first.assignments


def test_commons_export_is_conservative_and_hashes_source_csv(tmp_path: Path):
    data = tmp_path / "compiled.csv"
    pd.DataFrame(
        {
            "paper_id": ["paper-a", "paper-b"],
            "source_type": ["reported_table", "digitized_figure"],
        }
    ).to_csv(data, index=False)
    case = tmp_path / "case.yaml"
    case.write_text("case_id: benchmark-demo\ntitle: Benchmark demo\nprocess: pool boiling\nfluid: water\n", encoding="utf-8")
    output = tmp_path / "manifest.json"

    manifest = export_thermal_ai_commons_manifest(data, case, output)

    assert manifest["experiment_id"] == "benchmark-demo"
    assert manifest["evidence_class"] == "derived"
    assert manifest["rights"]["redistribution_permission"] == "pending"
    assert manifest["literature_compilation"]["record_count"] == 2
    assert len(manifest["literature_compilation"]["data_sha256"]) == 64
