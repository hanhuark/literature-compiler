# MMC/SMC Application Framework: Computing and Power Electronics

## Evidence rule

An application label records what the cited source states, rather than what a reviewer guesses from heat flux, substrate, coolant, or author affiliation. Allowed categories are `computing`, `power_electronics`, `electronics_unspecified`, `not_stated`, and `non_electronics`. A device label (for example, CPU, GPU, converter, or vehicle traction inverter) is entered only when the source supports it. The two case-level evidence tables retain source locators and distinguish a paired MMC--SMC comparison from MMC-only architecture context.

## First-principles common ground

Both categories are governed by the same coupled thermal--hydraulic balances. For a single-phase control volume, the coolant heat uptake is \(Q=\dot m c_p(T_{out}-T_{in})\), and the hydraulic price at a declared pressure boundary is \(P_{pump}=\Delta p\,\dot V\). A measured thermal resistance is meaningful only with its temperature reference and heat-input boundary. The total junction-to-coolant path additionally contains spreading, material, interface, and convection resistances. Thus an MMC may reduce channel flow length and improve distribution, while inlet/outlet turns, manifold contraction/expansion, and maldistribution can offset either benefit. No governing equation makes one architecture or application intrinsically superior.

In two-phase operation the same system energy and pumping-power bookkeeping applies, but saturation state, subcooling, mass flux, vapor quality, phase distribution, instability, and dryout add independent state variables. A two-phase point must not be placed on the single-phase transition map without a separate regime treatment.

## What the application changes

The optimization constraints differ, not the conservation laws. A computing tag often motivates a large die or multiple localized heat sources and a maximum-junction-temperature/uniformity objective. A power-electronics tag can add converter/module integration and electrical-isolation requirements. Neither characteristic is presumed: record heat-source map, cooled area, integration level, coolant, allowable temperature, pressure boundary, and packaging constraints for every source. These variables determine whether a thermal-resistance-versus-pumping-power comparison transfers across applications.

| Comparison item | Required source record | Why it can change the apparent MMC--SMC ordering |
| --- | --- | --- |
| Heat source | Total power, heated area, spatial map, thermal reference | A uniform heater and a localized hotspot probe different spreading and distribution penalties. |
| Hydraulic system | Coolant state, \(\Delta p\) tap locations, \(\dot V\), pumps/ports included | \(P_{pump}\) is boundary-dependent; core-only and system values are not interchangeable. |
| Package integration | Cold plate, embedded/interposer, near-junction; substrate and interfaces | Series conduction and interface resistances can mask or amplify a channel-level gain. |
| Operating regime | Single-phase Reynolds number or two-phase inlet state/quality/stability | The Curl transition model is a single-phase mapping aid, while boiling needs its own phase/regime map. |

## Current literature signal and limitation

The source-checked single-phase inventory has explicit power-electronics anchors: Zhang et al. identify power chips; Jung et al. identify vehicle power electronics; and van Erp et al. identify liquid-cooled converters. The current two-phase MMC inventory identifies electronics cooling but does not state a CPU/GPU or power-module device class in the retained records. This is a classification result, not a population statistic: plot-ready paired MMC--SMC records remain too sparse to estimate an application-specific crossover or to claim an application-specific performance advantage.

## Extraction additions

For each eligible curve or table point, preserve the usual thermal and hydraulic fields and add: application category; verbatim device/system label; evidence class; cooling integration level; heated area and spatial heating condition; coolant/electrical-isolation requirement if stated; and operating duty condition (steady, transient, or cycling if reported). The application tables are an audit layer, not a substitute for source-specific quantitative extraction.
