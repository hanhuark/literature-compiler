# test4: MMC vs. SMC Heat Sinks in Single-Phase Flow

## Research Question

For paired manifold microchannel (MMC) and straight microchannel (SMC) heat-sink studies in single-phase liquid cooling, how does thermal resistance vary with pumping power when the system boundary and comparison constraint are explicit?

## Why Pumping Power Is the Primary Comparison

For each operating point, the hydraulic cost is calculated as

```text
Ppump = DeltaP x Qdot
```

where `DeltaP` is the pressure drop over the documented boundary in Pa and `Qdot` is volumetric flow rate in m3/s. A thermal-resistance-versus-pumping-power plot compares what a design gains against what it pays. Separate thermal-resistance-versus-flow-rate and pressure-drop-versus-flow-rate plots remain source data, but flow rate alone does not impose an equal hydraulic cost.

## Initial Critical Synthesis

The initial source-checked corpus supports the following limited conclusions.

- Collins et al. experimentally fabricated paired straight and manifold designs with the same nominal 500 um hydraulic diameter in AlSi10Mg and tested water from 500 to 2000 kg/m2/s. The source establishes a strong candidate paired comparison, but numerical thermal-resistance and pressure-drop curves have not yet been checked against the authorized article figures or tables. It is therefore not plotted.
- Kong et al. numerically compared twelve MMC geometries with a conventional microchannel and reported geometry-dependent reductions in both thermal resistance and pressure drop. The reported maximum reductions are not necessarily at the same operating point; they must not be multiplied or converted into a synthetic pumping-power comparison.
- The first-pass corpus already contradicts an architecture-intrinsic superiority claim. Geometry, flow distribution, convective area, roughness/transition, and the pressure-measurement boundary can reverse the apparent ordering.

The evidence is **screening-level**. This case does not claim a universal crossover, model validation, or a quantitative literature trend until paired points are extracted with provenance.

## Inclusion Criteria

- Single-phase liquid operation with coolant and inlet state stated.
- MMC and SMC are directly compared, or a baseline SMC can be reconstructed under the same stated boundary and geometry constraints.
- Thermal resistance and either i) pressure drop plus volumetric flow or ii) pumping power are available at identifiable operating points.
- The temperature reference, heat-input basis, and pressure-drop taps/boundary are reported or recoverable.

## Exclusion Criteria

- MMC-only studies are retained as architecture context but are not plotted as MMC-versus-SMC evidence.
- Percentage improvements without a common operating point are not converted to data points.
- Results that mix chip-to-inlet, wall-to-inlet, and fluid-to-fluid thermal resistance without a traceable conversion are not pooled.
- Port/fitting losses are not combined with core-only pressure drop unless the source labels the boundary.

## Reproduce

```powershell
python examples/test4_MMC_heat_sink_single-phase/build_pumping_power_plot.py
```

The command validates plot-ready rows, calculates pumping power only from a matched pressure-drop and volumetric-flow record, writes `data/compiled_points.csv`, and produces `summary/test4_MMC_heat_sink_single-phase.png` once qualifying points exist. The committed input is intentionally header-only until authorized figure/table extraction is completed.

## Next Extraction Targets

1. Digitize paired curves from Collins et al. with one source-specific uncertainty estimate per curve.
2. Extract geometry, thermal-reference definition, and pressure-tap locations before mapping a study to the Curl single-phase model.
3. Record matched-flow-rate and matched-pumping-power ordering separately.
