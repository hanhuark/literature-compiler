# test3: HTC at CHF vs. CHF on Structured Surfaces

This case starts a reproducible compilation for heat-transfer coefficient at critical heat flux versus critical heat flux during saturated pool boiling of water on structured surfaces.

## Research Question

What heat-transfer coefficients at critical heat flux have been reported for saturated pool boiling of water on structured surfaces, and how do the reported CHF and HTC-at-CHF values trade off across micro-, nano-, and hierarchical surface families?

## Scope

- Working fluid: water.
- Process: saturated pool boiling.
- Pressure: atmospheric or near-atmospheric unless recorded otherwise.
- Surfaces: microstructured, nanostructured, and hierarchical enhanced surfaces.
- Primary variables: CHF and HTC at CHF.
- Secondary variables: wall superheat at CHF, surface family, surface geometry descriptors, and reference limits.

## Included Data

- `data/manual_seed_points.csv`: direct transcription of the prior MATLAB compilation values in `main_CHF_vs_HTC.m`, including three values that were defined but not included in the manual plot.
- `data/compiled_points.csv`: deterministic output from `build_manual_seed_dataset.py`, using only rows marked `include_in_seed_plot=true`.
- `data/reference_limits.csv`: Zuber hydrodynamic CHF limit recomputed with the same water properties as the MATLAB script plus the retained kinetic-limit comparison line.
- `papers.yaml`: case-specific screening and verification notes linked to shared source metadata.

## Reproduce

```powershell
python examples/test3_htc_chf_structured_surfaces/build_manual_seed_dataset.py
```

The script recomputes `hCHF = q''CHF / DeltaTsat,CHF`, writes the compiled table, writes the reference-limit table, and generates `summary/test3_htc_chf_structured_surfaces.png`.

## Caveat

This is a seed benchmark, not a finalized systematic review. Several source labels still need DOI/title verification, and every point should be checked against the original paper to confirm whether the value is truly HTC at CHF rather than maximum HTC elsewhere on the boiling curve.

