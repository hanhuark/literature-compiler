# test4 Screening Notes

## Evidence Boundary

`reported_points.csv` is intentionally empty at creation. This is a positive screening result: the first source-checked pass found a strong paired experimental candidate but not yet an audited set of figure/table points that can be plotted without mixing system boundaries.

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
