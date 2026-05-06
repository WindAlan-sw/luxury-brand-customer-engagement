# Reproducibility

This repository supports practical reproducibility from de-texted public metrics.

## What can be reproduced publicly

- post-level engagement score inspection;
- entropy-weighting input analysis;
- entropy/CRITIC/CILOS/IDOCRIW/MEREC score comparisons;
- brand-month panel construction;
- fixed-effect style OLS modelling on the public model panel;
- brand sentiment summaries;
- hierarchical clustering feature matrix and dendrogram.

## What cannot be reproduced publicly

- API-based data collection;
- raw text cleaning;
- sentiment re-inference from original text;
- any analysis requiring raw social-media text, handles, URLs, or original customer-level records.

## Paper outputs vs Repository outputs
| Paper output                       | Public repo file/notebook                                                        | Publicly reproducible? | Notes                                       |
| ---------------------------------- | -------------------------------------------------------------------------------- | ---------------------: | ------------------------------------------- |
| Fig. 2 CE score histogram          | `01_brand_post_metrics_detexted.csv`; notebook 01                                |                    Yes | Recreated from de-texted post-level metrics |
| Fig. 3 CE score boxplot            | `01_brand_post_metrics_detexted.csv`; notebook 01                                |                    Yes | Text not needed                             |
| Fig. 4 weighting comparison        | `04_entropy_weight_input.csv`, `06_scoring_method_post_results.csv`; notebook 02 |                    Yes | Recreated from public metrics               |
| Table 7 updated fixed-effect model | `11_fixed_effects_model_panel.csv`; notebook 02                                  |                    Yes | Based on de-texted brand-month panel        |
| Table 8 sentiment results          | `09_sentiment_month_summary.csv`; notebook 01/02                                 |                 Partly | Public aggregate sentiment only             |
| Fig. 6 clustering dendrogram       | `12_clustering_feature_matrix.csv`; notebook 02                                  |                    Yes | Recreated from public metrics               |
| Raw tweet examples in appendix     | Not included                                                                     |                     No | Raw text intentionally excluded             |


## Recommended citation wording

The repository reproduces the empirical analysis from de-texted, analysis-ready public metrics. Raw social-media content and user identifiers are not redistributed.
