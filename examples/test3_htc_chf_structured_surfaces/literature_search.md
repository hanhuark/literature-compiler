# test3 Literature Search Log

## Research Question

What heat-transfer coefficients at critical heat flux have been reported for saturated pool boiling of water on structured surfaces, and how do CHF and HTC-at-CHF trade off across micro-, nano-, and hierarchical surface families?

## Starting Collection

The first pass starts from the local manual compilation:

`C:\Users\hanhu\Box\NED3_Share\0_Data_Infrastructure\literature-compiler\Codes for Fig2_CHF vs HTC\Codes for Fig2_CHF vs HTC`

The MATLAB seed script defines 26 CHF values and computes HTC as `CHF / wall_superheat_at_CHF`; 23 of those points are plotted in the manual figure.

## Search Logic

Useful search terms for expanding and verifying the case include:

- `"pool boiling" water structured surface CHF HTC`
- `"pool boiling" "HTC" "CHF" "W/cm2" water`
- `"critical heat flux" "heat transfer coefficient" "structured surfaces" boiling water`
- `"microstructured" "pool boiling" water "critical heat flux"`
- `"nanostructured" "pool boiling" water "critical heat flux"`
- `"hierarchical" "pool boiling" water "critical heat flux"`
- `"heat transfer coefficient at CHF" "pool boiling"`
- `"wall superheat at CHF" "pool boiling" "structured surface"`

## Inclusion Criteria

Include studies that report or allow extraction of all of the following:

- water, DI water, distilled water, or nearly pure water as working fluid;
- pool boiling rather than flow boiling;
- saturated or near-saturated bulk condition, with subcooling recorded if present;
- structured heat-transfer surface, grouped as microstructured, nanostructured, or hierarchical;
- CHF and either wall superheat at CHF or directly reported HTC at CHF;
- enough metadata to record pressure, heater geometry, substrate/coating material, and surface dimensions when available.

## Exclusion Or Context-Only Criteria

Mark studies as context-only when they focus on:

- non-water fluids unless used to explain a mechanism;
- nanofluids where surface deposition evolves during the test and the final surface state is ambiguous;
- flow boiling, spray boiling, or confined channel boiling unless clearly separated from pool boiling;
- CHF-only papers that do not provide wall superheat or HTC near CHF;
- maximum HTC values that occur away from CHF unless the distinction is explicit.

## AI Workflow Targets

The AI-assisted workflow should improve the manual compilation by:

1. Resolving each manual legend label to a verified title, DOI, and source URL.
2. Extracting CHF and wall superheat at CHF from source tables, text, or calibrated figure digitization.
3. Recording whether `h` is computed as `q''CHF / DeltaTsat,CHF`, directly reported as HTC at CHF, or reported as a separate maximum HTC.
4. Adding surface metadata: substrate, coating material, geometry scale, wettability/contact angle, porosity, wickability, roughness, and heater area.
5. Separating atmospheric saturated pool boiling from subcooled or pressure-shifted conditions.
6. Preserving uncertainty and confidence for every digitized or inferred point.

