# test3 Screening And Extraction Notes

## Manual Seed

The manual source is `main_CHF_vs_HTC.m` in the local Box folder listed in `literature_search.md`. The script defines CHF values in W/cm2 and wall superheats in K, then calculates HTC values as:

```text
hCHF = q''CHF / DeltaTsat,CHF
```

This case preserves those values in `data/manual_seed_points.csv` and regenerates the plotted subset in `data/compiled_points.csv`.

## Extracted In This Pass

| Dataset | Status | Notes |
| --- | --- | --- |
| `manual_seed_points.csv` | included | Transcribed from the MATLAB constants `C1` through `C26`; rows `C14`, `C24`, and `C26` are retained but excluded from the compiled plot because they were not plotted or were commented out. |
| `compiled_points.csv` | generated | Contains 23 included seed rows with recomputed HTC, SI conversions, source type, extraction method, and Zuber-limit ratio. |
| `reference_limits.csv` | generated | Contains the Zuber hydrodynamic CHF limit recomputed from the same water properties as the MATLAB script and the retained kinetic-limit line. |
| `summary/test3_htc_chf_structured_surfaces.png` | generated | First-pass broken-axis comparison plot grouped by surface family. |

## Verification Caveats

- The seed points are only as reliable as the prior manual extraction. Treat them as a benchmark target for the AI workflow, not as final literature values.
- Several source labels in the manual legend need title/DOI reconciliation. The placeholder reference entries intentionally say when verification remains open.
- HTC at CHF is recomputed from CHF divided by wall superheat at CHF. If a paper reports maximum HTC at a lower heat flux, that number should not be mixed with `hCHF`.
- Surface-family assignments follow the manual figure colors and should be checked against each source surface morphology.
- The manual plot clipped the high-HTC Jun et al. point with `h = 42 W/cm2K`; the regenerated plot keeps it visible.

## Next Extraction Targets

1. Verify every manual source label against the original paper title, DOI, and figure/table.
2. Add `figure_id`, `table_id`, heater area, pressure, bulk subcooling, surface material, and surface geometry columns as the sources are checked.
3. Redigitize any points taken from plotted boiling curves with calibrated axes and estimated uncertainty.
4. Add missing structured-surface water pool-boiling studies that report both CHF and wall superheat at CHF.
5. Split rows where source data are maximum HTC but not HTC at CHF.

