# Research cases

This directory is retained as `examples/` for package compatibility, but its
contents are research cases rather than generic examples. Each case starts from
a specific research question and builds toward a reproducible quantitative
comparison. Its status describes the current evidence maturity, not a model
training or validation claim.

## Current Cases

| Case | Question | Status |
| --- | --- | --- |
| [`test1: Boiling Curve`](test1_boiling_curve/) | What boiling curves have been reported for saturated pool boiling of water on nominally flat copper surfaces at 1 atm? | Demo scaffold |
| [`test2: Microbubble Emission Boiling`](test2_meb/) | What MEB heat-flux, wall-superheat, oscillation-frequency, and acoustic-signature ranges have been reported, and how do BoilingLab cases compare? | First-pass screening scaffold |
| [`test3: HTC at CHF vs. CHF on Structured Surfaces`](test3_htc_chf_structured_surfaces/) | What HTC-at-CHF and CHF values have been reported for saturated pool boiling of water on structured surfaces? | Manual seed dataset and verification scaffold |
| [`test4: MMC vs. SMC, single phase`](test4_MMC_heat_sink_single-phase/) | Under matched pumping power, how do reported thermal resistances of MMC and SMC heat sinks compare during single-phase operation? | Source-checked screening and extraction scaffold |
| [`test5: MMC vs. SMC, two phase`](test5_MMC_heat_sink_two-phase/) | Under matched pumping power, how do reported thermal resistances of MMC and SMC heat sinks compare during two-phase operation? | Source-checked screening and extraction scaffold |

The MMC/SMC cases share an [application-evidence and first-principles framework](mmc_smc_application_framework.md). It separates computing, power-electronics, and unspecified-electronics records without inferring application from a heat-sink geometry.

## Add A Case

Use [the case template](../docs/case-template.md) and the [community workflow](../docs/community-workflow.md) when starting another research-question case.
