# Reference Hub

`literature-compiler` uses a shared reference hub so papers can be reused across research-question cases without duplicating bibliographic metadata.

## Files

- `references/sources.yaml`: canonical metadata for every paper known to the repository.
- `references/collections/*.yaml`: optional topical groupings of shared `ref_id`s.
- `examples/<case_id>/papers.yaml`: case-specific screening, inclusion, figure, and extraction notes that point back to shared references.

## Pattern

Add a paper once to `references/sources.yaml`:

```yaml
sources:
  example_2024_surface_boiling:
    title: Example surface boiling paper
    authors:
      - A. Researcher
    year: 2024
    doi: 10.1234/example
    source_url: https://doi.org/10.1234/example
    zotero_key: ABCD1234
    tags:
      - pool-boiling
      - water
      - copper
```

Then reference it from one or more cases:

```yaml
papers:
  - ref_id: example_2024_surface_boiling
    status: included
    relevance: Reports a smooth copper water boiling curve.
    figure_leads:
      - "Fig. 3: heat flux versus wall temperature"
    notes: Case-specific screening and extraction notes live here.
```

`references/sources.yaml` answers "what is this paper?" A case `papers.yaml` answers "why does this paper matter for this research question?"

## Zotero

Zotero is a useful import and local-PDF management tool, but contributors should not need access to another person's Zotero account. Store public metadata, DOI, URL, optional Zotero item key, and extracted quantitative data in the repository. Keep restricted PDFs and publisher figure renders local unless redistribution is allowed.

## Validation

Run:

```powershell
litcomp refs validate
```

The validator checks that every case-level `ref_id` exists in the shared hub and that the hub does not contain duplicate DOI entries.

To inspect the current registry:

```powershell
litcomp refs list
```
