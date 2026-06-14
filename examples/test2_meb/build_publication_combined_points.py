from __future__ import annotations

from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parent
DATA_DIR = ROOT / "data"


def _base_row(
    *,
    paper_id: str,
    curve_id: str,
    x_value: float,
    y_value: float,
    source_type: str,
    extraction_method: str,
    figure_id: str = "",
    table_id: str = "",
    digitization_confidence: str | float = "",
    notes: str = "",
) -> dict[str, str | float]:
    return {
        "paper_id": paper_id,
        "curve_id": curve_id,
        "x_value": x_value,
        "x_unit": "K",
        "y_value": y_value,
        "y_unit": "W/m^2",
        "source_type": source_type,
        "extraction_method": extraction_method,
        "figure_id": figure_id,
        "table_id": table_id,
        "digitization_confidence": digitization_confidence,
        "notes": notes,
    }


def build_combined_points() -> pd.DataFrame:
    boilinglab = pd.read_csv(DATA_DIR / "boilinglab_points.csv")
    publication_points = pd.read_csv(DATA_DIR / "literature_boiling_curve_points_publication.csv")
    digitized_points = pd.read_csv(DATA_DIR / "literature_digitized_boiling_points_publication.csv")

    rows: list[dict[str, str | float]] = []
    for _, row in boilinglab.iterrows():
        rows.append(
            {
                "paper_id": row["paper_id"],
                "curve_id": row["curve_id"],
                "x_value": row["x_value"],
                "x_unit": row["x_unit"],
                "y_value": row["y_value"],
                "y_unit": row["y_unit"],
                "source_type": row["source_type"],
                "extraction_method": row["extraction_method"],
                "figure_id": row.get("figure_id", ""),
                "table_id": row.get("table_id", ""),
                "digitization_confidence": row.get("digitization_confidence", ""),
                "notes": row.get("notes", ""),
            }
        )

    for _, row in publication_points.iterrows():
        wall_superheat = float(row["wall_superheat_K"])
        if wall_superheat < 0:
            continue
        rows.append(
            _base_row(
                paper_id=row["paper_id"],
                curve_id=row["curve_id"],
                x_value=wall_superheat,
                y_value=float(row["heat_flux_W_cm2"]) * 10000.0,
                source_type="reported_text",
                extraction_method="publication_analysis_extraction",
                notes=row.get("notes", ""),
            )
        )

    if "digitization_status" in digitized_points.columns:
        digitized_points = digitized_points[
            ~digitized_points["digitization_status"].astype(str).str.contains("reported_text", case=False, na=False)
        ]
    for _, row in digitized_points.iterrows():
        wall_superheat = float(row["wall_superheat_K"])
        if wall_superheat < 0:
            continue
        rows.append(
            _base_row(
                paper_id=row["paper_id"],
                curve_id=row["curve_id"],
                x_value=wall_superheat,
                y_value=float(row["heat_flux_W_cm2"]) * 10000.0,
                source_type="digitized_figure",
                extraction_method=row.get("digitization_status", "publication_analysis_digitized_curve"),
                figure_id=row.get("figure_id", ""),
                notes=row.get("notes", ""),
            )
        )

    return pd.DataFrame(rows)


def main() -> None:
    combined = build_combined_points()
    output_path = DATA_DIR / "combined_points.csv"
    combined.to_csv(output_path, index=False)
    print(f"Wrote {len(combined)} rows to {output_path}")
    print(combined.groupby("source_type").size().to_string())


if __name__ == "__main__":
    main()
