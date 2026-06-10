# literature-compiler

`literature-compiler` is a community workflow and Python toolkit for compiling quantitative literature data with explicit provenance.

The project is organized around research-question cases. Each case defines a focused question, registers relevant papers, extracts reported or digitized data, compiles canonical variables, and produces comparison plots that others can inspect and improve.

The first demo is [`test1: Boiling Curve`](examples/test1_boiling_curve/), which compares saturated pool boiling of water on nominally flat copper at 1 atm using boiling curves, digitized or reported data, and reference correlations.

## What It Does

- Provides a repeatable workflow for community literature-compilation cases.
- Registers literature sources and experimental-condition metadata.
- Converts reported or digitized data into canonical variables and units.
- Supports human-in-the-loop semi-automatic digitization from figure images.
- Preserves provenance for each data point: paper, figure/table, curve, extraction method, confidence, units, and notes.
- Plots literature data and optional reference correlations.

## Community Workflow

Each case should document:

- research question;
- inclusion and exclusion criteria;
- source registry;
- extraction method;
- canonical variables and units;
- compiled dataset;
- comparison plot;
- provenance notes;
- known gaps and requested community contributions.

See [docs/community-workflow.md](docs/community-workflow.md), [docs/case-template.md](docs/case-template.md), and [CONTRIBUTING.md](CONTRIBUTING.md).

Shared bibliographic metadata lives in [references/sources.yaml](references/sources.yaml). Individual cases link to those records and add case-specific screening or extraction notes. See [docs/reference-hub.md](docs/reference-hub.md).

## Install

```powershell
python -m pip install -e .[dev]
```

## Quick Start

```powershell
litcomp version
litcomp refs validate
litcomp plot-csv examples/test1_boiling_curve/data/reported_points.csv results/test1_boiling_curve.png --with-models
```

The example data are demonstration values only. They are not a complete pool-boiling literature review.

## Python Usage

```python
from litcomp.schema import DataPoint
from litcomp.plotting import plot_boiling_curve

points = [
    DataPoint(
        paper_id="demo_literature",
        curve_id="flat_copper",
        x_value=10,
        x_unit="K",
        y_value=125,
        y_unit="kW/m^2",
        source_type="reported_table",
        extraction_method="demo",
    )
]

plot_boiling_curve(points, "results/example.png", include_rohsenow=True)
```

## Paper Access Policy

This project does not bypass paywalls, institutional authentication, publisher licenses, or copyright limits. Use authorized access to obtain papers. Zotero is the preferred bridge for storing PDFs, DOI metadata, tags, BibTeX keys, and local attachment paths.

Do not commit restricted PDFs or publisher figures unless redistribution is allowed. Store metadata, local file references, extracted quantitative data, synthetic figures, and open/example assets instead.

## Development

```powershell
python -m pytest -q
```
