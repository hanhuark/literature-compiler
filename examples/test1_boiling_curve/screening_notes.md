# test1 Screening And Extraction Notes

## Zotero Collection

Collection: `litcomp/test1_boiling_curve`

The first extraction pass used local Zotero PDFs where available. One unrelated item, `ChatGPT Material Explorer`, was present in the collection and was ignored.

## Extracted In This Pass

The current `data/literature_points.csv` is a preliminary dataset intended to create the first literature-summary plot. It mixes directly reported table values and first-pass manual digitization from rendered PDF pages.

| Source | Figure/table | Status | Notes |
| --- | --- | --- | --- |
| Huang et al. 2023 | Table 2 | included | Direct table transcription for pure copper; strongest current data source. |
| Pandey et al. 2024 | Fig. 7a | included | Manual digitization of black polished-Cu markers from rendered PDF. |
| McHale et al. 2011 | Fig. 4 | included | Manual digitization of bare-copper DI-water curve; dense plot, needs WebPlotDigitizer review. |
| Hadzic et al. 2022 | Fig. 3a | included | Representative reference-surface curve from five runs; needs curve-by-curve digitization later. |
| Shi et al. 2015 | Fig. 6 | included | Manual digitization of smooth-surface reference; plot is small, needs review. |
| Dharmendra et al. 2016 | Fig. 7 | included | Bare-copper validation data; Fig. 8 also contains bare-copper data but Fig. 7 is cleaner for this pass. |

## Added In Next-Target Pass

These entries execute the previously listed next extraction plan. Values remain first-pass manual digitizations and should be treated as review-ready scaffolding rather than final extracted data.

| Source | Figure/table | Status | Notes |
| --- | --- | --- | --- |
| Allred et al. 2018 PRL | Fig. 4a | included with caveat | User-requested Fig. 4 curve; added hydrophilic bare-copper comparison. This is a superhydrophobic-structure study and is not a perfect flat polished copper baseline. |
| Allred et al. 2019 | Fig. 3g | included | Smooth copper boiling curve added from the downloaded ScienceDirect PDF. |
| Hadzic et al. 2024 | Fig. 3 | included | Average boiling curve from 125 measurements on nominally identical bare copper reference surfaces. |
| Berce et al. 2024 | Fig. 4a | partially included | Untreated reference repeated-run family represented by REF run 1 and REF run 5 to capture the observed shift. |
| Moze et al. 2022 | Fig. 5a | included | Untreated reference curve added from the shallow-channel comparison figure. |
| McHale et al. 2011 | Fig. 4 | refined | Previous single bare-copper curve replaced with separate ascending and descending bare-copper curves. |

## Important Caveats

- Digitized values are approximate and should be refined with WebPlotDigitizer or the package's future calibrated digitization workflow.
- Rendered publisher figure pages are local screening artifacts and should not be committed.
- The summary plot should be treated as a first community-demo figure, not a finalized literature review.
- Some Zotero entries have duplicate or misplaced attachments; item-to-PDF links should be cleaned in Zotero and mirrored in `papers.yaml` later.

## Next Extraction Targets

- Calibrated re-digitization of the newly added Allred 2018/2019, Hadzic 2024, Berce 2024, Moze 2022, and McHale 2011 curves.
- Add all five Berce et al. 2024 reference runs instead of only the two representative runs.
- Extract Hadzic et al. 2024 supporting-information max/min superheat envelope if available.
- Clean Zotero attachment links and add item keys or PDF availability notes to `papers.yaml`.
- Add uncertainty columns or companion files for digitized x/y error estimates.
