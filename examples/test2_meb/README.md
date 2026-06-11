# test2: Microbubble Emission Boiling

This case follows the `literature-compiler` community workflow for a first-pass quantitative compilation of microbubble emission boiling (MEB) literature and comparison against BoilingLab subcooled pool-boiling tests.

## Research Question

What heat-flux, wall-superheat, oscillation-frequency, and acoustic-signature ranges have been reported for MEB, and how do BoilingLab cases Boiling-412, Boiling-413, Boiling-416, and Boiling-417 compare?

## Scope

- Working fluid: water.
- Primary process: subcooled pool boiling with MEB or MEB-like transition.
- Context processes: confined reduced-pressure pool boiling, flow MEB in open microchannels, and acoustic boiling-state detection.
- Primary comparable variables: wall superheat and heat flux.
- Secondary variables: MEB onset condition, characteristic frequency, acoustic sensor type, and time-resolved oscillation/envelope signatures.

## Included Data

- `data/literature_points.csv`: first-pass reported-text points where both wall superheat and heat flux were available.
- `data/boilinglab_points.csv`: decimated BoilingLab heating-only data from the generated four-case comparison.
- `data/combined_points.csv`: literature and BoilingLab points in the package's canonical boiling-curve schema.
- `data/meb_regime_signatures.csv`: richer MEB-specific metrics that do not fit into a simple boiling-curve table.
- `papers.yaml`: case-specific screening notes linked to shared reference metadata in `../../references/sources.yaml`.

## Reproduce

```powershell
litcomp refs validate
litcomp plot-csv examples/test2_meb/data/combined_points.csv examples/test2_meb/summary/test2_meb_boiling_curve_comparison.png
```

The richer MEB-signature summary figure was generated from `data/meb_regime_signatures.csv` and is stored at `summary/test2_meb_signature_summary.png`.

## Caveat

This is a screening compilation, not a finalized systematic review. Values marked `reported_text` were extracted from available text snippets or indexed full text and should be checked against the original figures/tables before manuscript submission. Restricted PDFs and publisher figures are intentionally not committed.
