# Plot-Ready Data Contract

One row is one reported or digitized operating point. `architecture` must be `SMC` or `MMC`. Supply either `pumping_power_W`, or both `pressure_drop_Pa` and `volumetric_flow_m3_s`. Never reconstruct volumetric flow from two-phase mass flow without a stated fluid state and density method. Preserve `stability_state` and do not pool different boiling branches as one curve.
