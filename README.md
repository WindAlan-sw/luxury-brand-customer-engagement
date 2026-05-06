# Measuring Social Media Customer Engagement with Luxury Brands

This repository is a public companion for the published article:

> Xiao, S., & Chen, X. (2025). *Measuring social media customer engagement with brands based on information entropy: an application case of luxury brand*. Journal of Brand Management, 32, 184–202. https://doi.org/10.1057/s41262-024-00376-7

The repository provides de-texted public metric datasets and notebooks that allow readers to inspect and reproduce the main public-metric analysis workflow:

1. post-level brand engagement measurement;
2. entropy-based customer engagement score construction;
3. comparison with alternative MCDM weighting methods;
4. fixed-effect modelling using EITC dimensions;
5. customer sentiment summaries;
6. hierarchical clustering of luxury brands.

The original comprehensive research framewrok is shown in below:
<img width="535" height="721" alt="Screenshot 2025-06-23 at 14 53 58" src="https://github.com/user-attachments/assets/6d38a1e7-db4e-42da-ae25-5b79b597ab48" />


Raw X/Twitter text, user handles, URLs, and other row-level user-identifying fields are not redistributed.

## Who may find this repository useful?

### Researchers

This repository may be useful for researchers studying:

- social media customer engagement;
- brand-generated content;
- luxury branding;
- entropy-based measurement;
- multi-criteria decision-making methods in marketing analytics;
- sentiment analysis and brand benchmarking.

### Practitioners

The workflow can also support practitioners who want to compare engagement performance across brands, campaigns, or time periods using public interaction metrics such as replies, reposts, likes, and quotes.


## How to use this repo
### Option 1: use GitHub/Colab
Open `notebooks/01_Check_Published_Results.ipynb` and run all cells.
[![Open score results notebook in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/WindAlan-sw/luxury-brand-customer-engagement/blob/main/notebooks/01_Check_Published_Results.ipynb)

Open `notebooks/02_Reproduce_Public_Metric_Analysis.ipynb` and run all cells.
[![Open analysis notebook in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/WindAlan-sw/luxury-brand-customer-engagement/blob/main/notebooks/02_Reproduce_Public_Metric_Analysis.ipynb)

Open `notebooks/05_Apply_Framework_To_Your_Data.ipynb` and run all cells.
[![Open framework notebook in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/WindAlan-sw/luxury-brand-customer-engagement/blob/main/notebooks/05_Apply_Framework_To_Your_Data.ipynb)

### Option 2: run locally

```bash
pip install -r requirements.txt
python check_public_release.py
```

## What is included

This version uses **de-texted public metric datasets** derived from the original research files. It keeps the empirical structure of the published study while removing raw social-media text and user-identifying fields.

The analysis is organized in two phases, consistent with the paper's logic:

1. **Post-level brand engagement analysis** using official brand post metrics with text removed.
2. **Brand-month aggregation and modelling** for entropy/CRITIC comparisons, fixed-effect analysis, sentiment summaries, and clustering.

## Data files

Public analysis-ready metrics are in `data/public_metrics/`.

Key files:

- `01_brand_post_metrics_detexted.csv` — official brand post-level metrics with text and URLs removed.
- `02_brand_month_engagement_panel.csv` — brand-month aggregation derived from post-level metrics.
- `04_entropy_weight_input.csv` — retweet/reply/like/quote input matrix for entropy scoring.
- `05_entropy_score_results.csv` — entropy CE score results.
- `06_scoring_method_post_results.csv` — entropy, CRITIC, CILOS, IDOCRIW, MEREC, and additive scores.
- `08_customer_month_engagement_summary.csv` — aggregated customer engagement metrics.
- `09_sentiment_month_summary.csv` — aggregated sentiment metrics.
- `11_fixed_effects_model_panel.csv` — public model panel for reproducing the main fixed-effect style regression.
- `12_clustering_feature_matrix.csv` — clustering feature matrix used to reproduce the hierarchical clustering demonstration.

## What is not included

The repository does **not** include raw X/Twitter post text, cleaned text, user handles, display names, post URLs, mentions, hashtags, or original row-level customer records.

| Paper output                       | Public repo file/notebook                                                        | Publicly reproducible? | Notes                                       |
| ---------------------------------- | -------------------------------------------------------------------------------- | ---------------------: | ------------------------------------------- |
| Fig. 2 CE score histogram          | `01_brand_post_metrics_detexted.csv`; notebook 01                                |                    Yes | Recreated from de-texted post-level metrics |
| Fig. 3 CE score boxplot            | `01_brand_post_metrics_detexted.csv`; notebook 01                                |                    Yes | Text not needed                             |
| Fig. 4 weighting comparison        | `04_entropy_weight_input.csv`, `06_scoring_method_post_results.csv`; notebook 02 |                    Yes | Recreated from public metrics               |
| Table 7 updated fixed-effect model | `11_fixed_effects_model_panel.csv`; notebook 02                                  |                    Yes | Based on de-texted brand-month panel        |
| Table 8 sentiment results          | `09_sentiment_month_summary.csv`; notebook 01/02                                 |                 Partly | Public aggregate sentiment only             |
| Fig. 6 clustering dendrogram       | `12_clustering_feature_matrix.csv`; notebook 02                                  |                    Yes | Recreated from public metrics               |
| Raw tweet examples in appendix     | Not included                                                                     |                     No | Raw text intentionally excluded             |

See `docs/RESTRICTED_DATA_NOTE.md` for details.

## Contact

For questions, contact: xiaosiwei1006@gmail.com

## License

Code is released under the MIT License. Public aggregate/metric data are released under CC BY 4.0. Raw restricted data are not redistributed.
