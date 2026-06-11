# test2 Screening And Extraction Notes

## Zotero Collection

Collection: `litcomp/test2_meb` / local BoilingLab MEB review packet.

The first pass used the local Zotero-derived packet previously generated under the BoilingLab demo artifacts. No restricted PDFs, page renders, or publisher figures are committed.

## Extracted In This Pass

| Dataset | Status | Notes |
| --- | --- | --- |
| `literature_points.csv` | included | First-pass reported-text values where both wall superheat and heat flux were visible in indexed text. These are suitable for a screening plot only. |
| `boilinglab_points.csv` | included | Decimated heating-only points from BoilingLab's four-case comparison (`Boiling-412`, `Boiling-413`, `Boiling-416`, `Boiling-417`). |
| `meb_regime_signatures.csv` | included | MEB-specific onset, heat-flux, frequency, acoustic-sensor, and notes table. This is the main test2 table for deciding what to extract next. |

## Preliminary Interpretation

BoilingLab cases occupy lower heat-flux ranges than many high-subcooling MEB literature demonstrations, but Boiling-416 and Boiling-417 provide unusually synchronized time-resolved wall-temperature, heat-flux, hydrophone, and AE diagnostics. That makes the local dataset valuable for MEB state identification and transient development rather than as a record-setting heat-flux dataset.

## Important Caveats

- Reported-text range endpoints are not digitized curves.
- Some rows pair endpoints from a reported range to make a screening envelope; these should not be interpreted as exact experimental points.
- Acoustic-frequency values span different meanings: bubble oscillation, boiling sound peak, hydrophone sampling rate, and low-frequency envelope modulation. The `frequency_type` field must be used when comparing values.
- BoilingLab low-frequency modulation values are envelope/regime modulation frequencies, not the high-frequency bubble-collapse or sound-carrier frequencies reported in many MEB studies.

## Next Extraction Targets

1. Digitize MEB boiling curves from Tang/Horiuchi/Kobayashi papers with calibrated axes.
2. Extract MEB onset wall superheat versus subcooling/surface condition from Kobayashi et al. 2022 and reduced-pressure work.
3. Extract reported sound or pressure spectral peaks with sensor type, bandwidth, and sampling rate.
4. Separate pool-boiling MEB, confined/reduced-pressure MEB, and flow-microchannel MEB into comparable subgroups.
5. Add uncertainty and confidence scores for every digitized point.
