# test2: Microbubble Emission Boiling

This case follows the `literature-compiler` community workflow for a quantitative screening compilation of microbubble emission boiling (MEB) literature and comparison against BoilingLab subcooled pool-boiling tests.

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
- `data/literature_digitized_curves.csv`: approximate manual digitizations of selected published boiling-curve traces from locally available PDF renders. These rows are intended to improve the manuscript comparison beyond isolated literature points; they should be redigitized with calibrated axes before final cross-study scaling.
- `data/literature_boiling_curve_points_publication.csv`: manuscript-ready literature point table used for the final BoilingLab MEB paper literature-context figure. It records reported-text points and screening envelope points in W/cm^2.
- `data/literature_digitized_boiling_points_publication.csv`: manuscript-ready digitized literature boiling-curve table used for the same literature-context figure. It preserves source, figure, curve, branch, and recommended-use metadata for the plotted literature curves.
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

This is a screening compilation, not a finalized systematic review. Values marked `reported_text` were extracted from available text snippets or indexed full text and should be checked against the original figures/tables before manuscript submission. Values marked `figure_digitized_or_curve_point` are approximate manual extractions from rendered local PDFs and should be verified with a calibrated digitizer before quantitative meta-analysis. Restricted PDFs and publisher figures are intentionally not committed.
