# Plot-Ready Data Contract

One row is one reported or digitized operating point. `architecture` must be `SMC` or `MMC`. Supply either `pumping_power_W`, or both `pressure_drop_Pa` and `volumetric_flow_m3_s`; the builder calculates the latter product in SI units. Values from different pressure boundaries or thermal-resistance definitions may coexist in the file but must not be interpreted as a pooled performance ranking.
