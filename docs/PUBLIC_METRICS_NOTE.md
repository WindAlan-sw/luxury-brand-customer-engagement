# Public Metrics Note

This repository uses a public-metrics release strategy. The goal is to preserve the empirical implications of the published study while excluding raw platform content.

## Golden rule

The public files should stay consistent with the published paper's workflow:

1. Start from post-level brand engagement metrics.
2. Derive brand-month aggregate panels.
3. Use those panels for entropy/CRITIC comparisons, fixed-effect style modelling, sentiment summaries, and clustering.

## Removed fields

The following types of variables are intentionally excluded from public data:

- raw tweet/post text;
- cleaned tweet/post text;
- handles and display names;
- URLs and exact post links;
- raw mentions and hashtags;
- retweeted-user strings;
- original customer-level text records.

## Retained fields

The public files retain numerical and categorical metrics needed to inspect and reuse the research framework, including engagement counts, scores, month identifiers, brand identifiers, EITC variables, and aggregate sentiment metrics.
