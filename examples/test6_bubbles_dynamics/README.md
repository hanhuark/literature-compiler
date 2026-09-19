# test6: Bubble Dynamics

## Research Question

What bubble growth and bubble departure characteristics have been reported during pool boiling, and how do these results vary with operating and surface conditions?

## Scope

This test collects quantitative bubble-dynamics data reported in pool-boiling literature.

The initial focus is on:

- bubble growth or bubble growth rate;
- bubble size, diameter, or radius;
- bubble departure diameter;
- bubble growth time, departure period, or departure frequency;
- operating conditions associated with the reported bubble dynamics;
- surface conditions associated with the reported bubble dynamics.

## Included Data

The first-pass dataset contains quantitative bubble-dynamics measurements extracted from published figures.

The current dataset contains:

- bubble departure-diameter measurements;
- bubble departure-period measurements;
- bubble series numbers;
- departure diameter in µm;
- departure period in ms;
- source figure and extraction metadata;
- experimental conditions.

The extracted values are stored in:

`data/bubble_dynamics_metrics.csv`

The values were manually digitized from published figures and are therefore approximate.

## Reproduce

From the repository root, run:

```powershell
python examples\test6_bubbles_dynamics\plot_departure_diameter.py

python examples\test6_bubbles_dynamics\plot_departure_period.py
```

## Next Extraction Targets

- Add additional quantitative bubble-dynamics measurements from suitable pool-boiling studies.
- Add bubble growth measurements such as growth rate or growth time.
- Add additional operating and surface conditions where they are reported.