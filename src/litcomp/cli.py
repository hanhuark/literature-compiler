from __future__ import annotations

from pathlib import Path

import typer

from . import __version__
from .database import load_points_csv
from .plotting import plot_boiling_curve
from .schema import DataPoint

app = typer.Typer(help="Compile quantitative literature data with provenance.")


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


if __name__ == "__main__":
    app()
