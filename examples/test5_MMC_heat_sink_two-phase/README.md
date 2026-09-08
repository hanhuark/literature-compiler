# test5: MMC vs. SMC Heat Sinks in Two-Phase Flow

## Research Question

For paired manifold microchannel (MMC) and straight microchannel (SMC) heat-sink studies in two-phase operation, how does thermal resistance vary with pumping power when phase condition, pressure boundary, and stability state are explicit?

## Scope Boundary

This case uses the same plotting objective as test4:

```text
Ppump = DeltaP x Qdot
```

but it does **not** apply the Curl single-phase laminar-to-turbulent crossover equation to boiling data. In two-phase operation, pumping power and thermal resistance also depend on heat flux, mass flux, inlet subcooling/pressure, vapor quality, confinement, phase distribution, flow instability, and dryout. A plotted point is therefore only comparable within its documented phase-condition class.

## Initial Critical Synthesis

- Lin et al. numerically evaluated multiple MMC arrangements in water single-phase flow and HFE-7100 two-phase flow. Their source explicitly treats the single- and two-phase heat-transfer mechanisms as different and identifies manifold arrangement and maldistribution as consequential variables.
- Luo et al. provide two-phase manifold-arrangement context, not a paired SMC control.
- Drummond's open dissertation is an important experimental MMC context because it reports both channel and overall pressure measurements. Its HFE-7100 results show why pressure-boundary identity must be preserved; it is not evidence that can be directly ranked against an SMC without a matched control.

The first source-checked pass did not identify a plot-ready paired experimental MMC-SMC two-phase dataset. This is a documented corpus limitation, not evidence that no such work exists. The case is designed to make the missing comparison measurable and to receive verified data when source figures/tables are audited.

## Application Layer

The two-phase corpus is tagged using only the application stated in the source. Its early entries are predominately `electronics_unspecified`; that is an evidence gap, not support for a CPU/GPU or power-module prevalence claim. See [`application_evidence.csv`](data/application_evidence.csv) and the shared [application framework](../mmc_smc_application_framework.md).

## Inclusion Criteria

- Flow boiling or evaporative two-phase operation with fluid, inlet state, heat flux, and mass/volumetric flow documented.
- Direct MMC-SMC comparison under a stated comparison constraint.
- Thermal resistance and pressure drop plus volumetric flow, or directly reported pumping power, at identifiable points.
- Pressure taps/boundary and a flow-stability or regime observation are available.

## Exclusion Criteria

- Single-phase points belong in test4.
- MMC topology-only studies remain source context, not MMC-SMC comparison points.
- Do not infer pumping power from mass flux without flow area and density at a stated thermodynamic state.
- Do not pool pre-dryout, unstable, dryout, or CHF-limited points without distinct labels.

## Reproduce

```powershell
python examples/test5_MMC_heat_sink_two-phase/build_pumping_power_plot.py
```

The command writes `data/compiled_points.csv` and creates `summary/test5_MMC_heat_sink_two-phase.png` when qualifying paired points exist. The initial input is header-only by design.

## Next Extraction Targets

1. Locate paired MMC-SMC flow-boiling studies with enough information to retain phase condition and pressure boundary.
2. Extract stable and unstable operating branches separately.
3. Add heat-flux, mass-flux, subcooling, pressure, and quality metadata before interpreting a pumping-power trade-off.
