# Community Literature Workflow

`literature-compiler` organizes quantitative literature review as a reproducible community workflow. The goal is not only to collect papers, but to make comparable data, assumptions, and uncertainty visible.

## 1. Define The Research Question

A case starts with a scoped quantitative question. Good questions name the system, operating condition, material or geometry, and comparison metric.

Example:

> What boiling curves have been reported for saturated pool boiling of water on nominally flat copper surfaces at 1 atm?

## 2. Set Inclusion And Exclusion Criteria

Document what counts as comparable literature. For `test1: boiling curve`, inclusion might require saturated pool boiling, water, flat copper, and near-atmospheric pressure. Exclusions might include enhanced surfaces, other fluids, flow boiling, or substantially different pressure ranges.

## 3. Register Sources

Add candidate papers to `papers.yaml` with identifiers, metadata, tags, and notes. Zotero can help manage DOI metadata, BibTeX keys, collections, and local attachments.

## 4. Extract Quantitative Data

Prefer reported tables when available. When data exist only in plots, digitize figures with explicit calibration and manual review. Every extracted value should preserve provenance:

- paper ID;
- figure or table ID;
- curve label;
- original units;
- normalized units;
- extraction method;
- confidence or uncertainty notes.

## 5. Compile And Validate

Compile data into canonical variables and units. Validation should catch missing identifiers, invalid units, duplicate IDs, nonphysical values, and suspicious digitization outputs.

## 6. Plot And Interpret

Generate comparison plots that show individual sources, ranges, user data, and reference correlations when appropriate. The plot should help reveal agreement, disagreement, gaps, and uncertainty.

## 7. Invite Community Improvement

Each case should list open tasks: missing papers, uncertain curves, correlations needing review, or boundary cases needing discussion.
