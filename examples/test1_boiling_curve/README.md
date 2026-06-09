# test1: Boiling Curve

This demo shows how `literature-compiler` can support a community literature-compilation workflow around one quantitative research question.

## Research Question

What boiling curves have been reported for saturated pool boiling of water on nominally flat copper surfaces at 1 atm, and how do new measurements compare with prior literature and reference correlations?

## Scope

- Working fluid: water
- Process: saturated pool boiling
- Surface: nominally flat copper
- Pressure: 1 atm
- Primary variables: wall superheat and heat flux

## Workflow

1. Define inclusion and exclusion criteria.
2. Register candidate literature sources in `papers.yaml`.
3. Add reported table/text data or digitized figure data.
4. Compile the data into canonical units.
5. Plot literature curves, user data, and reference correlations.
6. Record uncertainty, gaps, and provenance so other contributors can improve the case.

## Demo Data

The included data are small demonstration values, not a complete literature review. Restricted publisher figures and PDFs should not be committed here unless redistribution is allowed.

Run:

```powershell
litcomp plot-csv examples/test1_boiling_curve/data/reported_points.csv results/test1_boiling_curve.png --with-models
```

## Community Contribution Ideas

- Add additional pool-boiling papers that match the scope.
- Add inclusion/exclusion notes for borderline cases.
- Replace demonstration points with attributed reported or digitized values.
- Add uncertainty estimates for digitized curves.
- Add additional correlations with validity notes.
