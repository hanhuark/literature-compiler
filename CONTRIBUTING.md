# Contributing

`literature-compiler` is meant to grow through community-maintained literature compilation cases. A good contribution should make quantitative literature easier to inspect, reproduce, and challenge.

## Ways To Contribute

- Add a new research-question case under `examples/`.
- Add reusable paper metadata to `references/sources.yaml`.
- Improve an existing case by adding sources, data, digitization notes, or uncertainty estimates.
- Add reference correlations with clear assumptions and validity limits.
- Improve digitization, validation, plotting, or data-export tooling.
- Improve documentation for reproducible literature workflows.

## Case Contribution Checklist

Each case should include:

- A clear research question.
- Inclusion and exclusion criteria.
- Shared source IDs from `references/sources.yaml`, plus case-specific relevance notes in `papers.yaml`.
- Canonical variables and units.
- Data provenance for every point.
- Notes on whether values are reported directly or digitized from figures.
- A plot or command that reproduces the main comparison.
- Known gaps and requested community contributions.

## Data And Copyright

Do not commit restricted PDFs or publisher figures unless redistribution is allowed. Use authorized access for papers, keep restricted assets local, and commit metadata plus extracted quantitative values with provenance.

Zotero is encouraged for managing authorized local paper libraries, DOI metadata, BibTeX exports, tags, and attachment paths.

## Reference Hub

Add papers once to `references/sources.yaml`, then link to them from each case with `ref_id`. This lets one paper support multiple research questions without copying bibliographic metadata.

Validate references before opening a pull request:

```powershell
litcomp refs validate
```

## Development

Install locally:

```powershell
python -m pip install -e .[dev]
```

Run tests:

```powershell
python -m pytest -q
```
