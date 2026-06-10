# Literature Compilation Case Template

Use this template when adding a new community case under `examples/`.

## Case ID

`testN_short_name`

## Title

`testN: Descriptive case title`

## Research Question

State the quantitative literature question in one sentence.

## Scope

- System:
- Material or geometry:
- Operating condition:
- Primary x-variable:
- Primary y-variable:
- Comparison objective:

## Inclusion Criteria

- Include studies that:

## Exclusion Criteria

- Exclude studies that:

## Source Registry

Add reusable bibliographic metadata to `references/sources.yaml`. In the case folder, list case-specific source use in `papers.yaml`:

```yaml
papers:
  - ref_id: example_2024_surface_boiling
    status: screen
    relevance: Candidate baseline curve for this case.
    figure_leads:
      - "Fig. 3: heat flux versus wall temperature"
    notes: Explain why this paper is included, excluded, or still under review.
```

Run `litcomp refs validate` after adding or editing references.

## Data Extraction

For each dataset, record whether values are:

- reported in a table;
- reported in text;
- digitized from a figure;
- user experimental data.

For digitized data, record figure ID, curve label, axis calibration, extraction method, confidence, and manual corrections.

## Outputs

At minimum, provide one command that reproduces the main comparison plot.

```powershell
litcomp plot-csv examples/testN_short_name/data/reported_points.csv results/testN_short_name.png --with-models
```

## Known Gaps

List missing papers, unresolved boundary cases, uncertain extracted values, or correlations that need review.
