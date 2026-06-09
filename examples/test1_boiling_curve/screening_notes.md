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

## Important Caveats

- Digitized values are approximate and should be refined with WebPlotDigitizer or the package's future calibrated digitization workflow.
- Rendered publisher figure pages are local screening artifacts and should not be committed.
- The summary plot should be treated as a first community-demo figure, not a finalized literature review.
- Some Zotero entries have duplicate or misplaced attachments; item-to-PDF links should be cleaned in Zotero and mirrored in `papers.yaml` later.

## Next Extraction Targets

- Allred et al. PRL 2018 Fig. 4.
- Allred et al. 2019 Fig. 3 if the PDF is added to Zotero.
- Hadzic et al. 2024 average boiling curve and/or supporting data.
- Berce et al. 2024 untreated-reference repeated runs.
- Moze et al. 2022 untreated-reference curves.
- McHale et al. 2011 curve-by-curve refinement.
