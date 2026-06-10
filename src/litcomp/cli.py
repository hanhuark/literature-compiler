from __future__ import annotations

from pathlib import Path

import typer

from . import __version__
from .database import load_points_csv
from .plotting import plot_boiling_curve
from .references import load_sources, validate_reference_hub
from .schema import DataPoint

app = typer.Typer(help="Compile quantitative literature data with provenance.")
refs_app = typer.Typer(help="Inspect and validate the shared reference hub.")
app.add_typer(refs_app, name="refs")


@app.command()
def version() -> None:
    typer.echo(f"literature-compiler {__version__}")


@app.command("plot-csv")
def plot_csv(
    csv_path: Path = typer.Argument(..., exists=True, dir_okay=False),
    output_path: Path = typer.Argument(...),
    with_models: bool = typer.Option(False, "--with-models", help="Overlay demonstration correlations."),
) -> None:
    frame = load_points_csv(csv_path)
    points = [DataPoint(**row.dropna().to_dict()) for _, row in frame.iterrows()]
    written = plot_boiling_curve(points, output_path, include_rohsenow=with_models)
    typer.echo(str(written))


@refs_app.command("validate")
def refs_validate(repo_root: Path = typer.Option(Path("."), "--repo-root", help="Repository root to validate.")) -> None:
    report = validate_reference_hub(repo_root)
    for warning in report.warnings:
        typer.echo(f"WARNING: {warning}")
    if not report.ok:
        for error in report.errors:
            typer.echo(f"ERROR: {error}")
        raise typer.Exit(code=1)
    case_count = len(report.case_refs)
    ref_count = sum(len(refs) for refs in report.case_refs.values())
    typer.echo(f"Reference hub OK: {case_count} case(s), {ref_count} case reference link(s).")


@refs_app.command("list")
def refs_list(
    sources_path: Path = typer.Option(Path("references/sources.yaml"), "--sources", help="Path to sources.yaml."),
) -> None:
    sources = load_sources(sources_path)
    for ref_id, source in sorted(sources.items()):
        year = source.year if source.year is not None else "n.d."
        doi = f" DOI: {source.doi}" if source.doi else ""
        typer.echo(f"{ref_id} ({year}) - {source.title}{doi}")


if __name__ == "__main__":
    app()
