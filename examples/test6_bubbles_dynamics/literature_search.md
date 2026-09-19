# test6 Literature Search Log

## Research Question

What bubble growth and bubble departure characteristics have been reported during pool boiling, and how do these results vary with operating and surface conditions?

## Search Logic

Bubble dynamics during pool boiling may be discussed under different terms,
including bubble growth, bubble departure, bubble visualization, and nucleate
boiling. The search should therefore not depend on exact title or keyword
matches such as "bubble dynamics". Useful search terms include:

- `"bubble dynamics" "pool boiling"`
- `"bubble growth" "pool boiling"`
- `"bubble departure" "pool boiling"`
- `"bubble departure diameter" boiling`
- `"bubble growth rate" boiling`
- `"bubble growth time" boiling`
- `"bubble departure frequency" boiling`

## Inclusion Criteria For First Pass

Include papers likely to contain one or more quantitative measurements or data series for:

- bubble growth or bubble growth rate;
- bubble size, diameter, or radius;
- bubble departure or departure diameter;
- bubble growth time, departure period, or departure frequency;
- operating conditions associated with the reported bubble dynamics;
- surface conditions associated with the reported bubble dynamics;
- pool-boiling experiments or analyses where the bubble dynamics are relevant to the study.

## Exclusion Or Lower-Priority Criteria

Lower priority or exclude:

- flow-boiling studies without a directly relevant pool-boiling case;
- studies where bubble dynamics are mentioned but no relevant quantitative information is reported;
- studies focused on boiling systems or fluids outside the scope of this test when the reported bubble dynamics cannot be meaningfully compared;
- studies that do not provide enough information to identify or extract the relevant bubble-dynamics measurements.

## First-Pass Candidate Groups

### Selected Initial Source

**Sun et al. (2017)**, "Bubble Dynamics and Heat Transfer During Pool Boiling on Wettability Patterned Surfaces."

The paper was selected as the initial Test 6 data source because it provides quantitative bubble-dynamics measurements during pool boiling, including bubble departure diameter and bubble departure period.

DOI: `10.1080/01457632.2017.1325676`

Extracted data:

- Fig. 12: bubble departure diameter
- Fig. 13: bubble departure period
- Conditions: 18.22 W/cm², atmospheric pressure, degassed DI water
- Extraction method: manual digitization from published figures

### Additional Candidate Sources

**Mahmoud and Karayiannis (2023)**, "Bubble growth models in saturated pool boiling of water on a smooth metallic surface: Assessment and a new recommendation."

The paper is relevant to bubble-growth measurements and remains a potential source for a later extraction pass.

DOI: `10.1016/j.ijheatmasstransfer.2023.124065`

**Tecchio et al. (2024)**, "Microlayer evaporation during bubble growth in nucleate boiling."

The paper is relevant to bubble growth and associated heat-transfer measurements and remains a potential source for a later extraction pass.

DOI: `10.1016/j.ijheatmasstransfer.2024.125860`

## Current Extraction Status

The first extraction pass uses Sun et al. (2017) only. The extracted measurements are stored in:

`data/bubble_dynamics_metrics.csv`

The current dataset contains manually digitized bubble departure diameter and bubble departure period measurements from Figs. 12 and 13. The digitized values are approximate and retain their figure number, extraction method, experimental conditions, and notes in the CSV.