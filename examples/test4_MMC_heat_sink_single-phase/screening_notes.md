# test4 Screening Notes

## Evidence Boundary

`reported_points.csv` is intentionally empty at creation. This is a positive screening result: the first source-checked pass found a strong paired experimental candidate but not yet an audited set of figure/table points that can be plotted without mixing system boundaries.

## Source-Audited Screening Facts

| Source | Evidence | What is directly reported | Why it is not plotted as Rth versus Ppump yet |
| --- | --- | --- | --- |
| Boteler (2011), Ch. 3 | Numerical paired MMC-SMC comparison | At the stated matched system-flow condition, MMC/SMC chip temperature rises are 40.8/36.3 C and pressure drops are 2.395/91.925 kPa. | The thermal quantity is normalized by heat flux; the model heat area must be checked before conversion to K/W. |
| Zhang et al. (2022), Fig. 7 | Experimental paired MMC-SMC comparison | At 1200 W/cm2 and a 60 C maximum temperature rise, the 8 x 50 um MMC COP is 3.38 times the 50 um SMC value. Fig. 7b separately provides pumping power versus flow rate. | The source does not provide Rth at the corresponding pumping-power points. COP values must not be treated as Rth values. |

## Required Fields Before Inclusion

- `thermal_resistance_K_W` and its temperature/heat-input definition;
- `pressure_drop_Pa` over the named boundary;
- `volumetric_flow_m3_s`, or directly reported `pumping_power_W`;
- coolant state and single-phase confirmation;
- source figure/table locator and extraction method;
- architecture and comparison constraint.

## Interpretation Guardrails

- Use `Ppump = DeltaP x Qdot`; do not use mass flow rate unless density and its evaluation state are documented.
- Preserve core-only versus system pressure drops as separate classes.
- A post hoc agreement between a study and the Curl model is a retrospective consistency assessment, not independent validation.
