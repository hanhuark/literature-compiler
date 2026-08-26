# Literature benchmark workflow

`literature-compiler` supports preparation of a traceable thermal literature
benchmark. It does not by itself verify every source value, establish reuse
rights, or validate a predictive model.

## Record boundary

For model-ready curation, each record should link a paper, study, experiment,
source group, curve, operating condition, and observation. `DataPoint` now
defaults `study_id` and `source_group` to `paper_id` and `experiment_id` to
`paper_id:curve_id`; curators should replace those defaults when a paper reports
multiple independent facilities or experiments.

Every record declares one of four verification stages:

- `unverified`: provisional import only;
- `screening`: usable to identify coverage, not for headline performance;
- `source_checked`: checked against the original authorized paper location; or
- `independently_verified`: a second curator or independent source confirmed it.

`rights_status` is separate from verification. A technically verified point is
not automatically cleared for redistribution, model training, or release.

## Source-group split

Never report a headline benchmark split made by random curve point. Use a whole
literature source (or a more conservative facility/experiment group) as the
partition unit:

```powershell
litcomp benchmark split <compiled-points.csv> <split.json> `
  --dataset-id structured-surfaces-v0.1 --group-column source_group --seed 42
```

If `source_group` is not yet in the table, the command falls back to `paper_id`
or `ref_id` and records the actual column selected. This avoids accidental
point-level leakage but cannot prove physical independence among literature
studies.

## Thermal AI Commons export

```powershell
litcomp commons export-manifest <compiled-points.csv> `
  --case <case.yaml> <manifest.json>
```

The exported manifest is compatible with the core NED3 Thermal AI Commons
experiment contract. It classifies literature records as derived (or mixed when
user experiments are present), hashes the compiled CSV, and defaults data
access to `not_released` plus rights review to `in_review`. It is a provenance
record, not a data release or a validation result.
