# Measuring Social Media Customer Engagement with Luxury Brands

This repository is a public companion for the published article:

> Xiao, S., & Chen, X. (2025). *Measuring social media customer engagement with brands based on information entropy: an application case of luxury brand*. Journal of Brand Management, 32, 184–202. https://doi.org/10.1057/s41262-024-00376-7

The repository is designed for readers who want to quickly check the empirical results and apply a similar framework to their own data.

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

See `docs/RESTRICTED_DATA_NOTE.md` for details.

## Contact

For questions, contact: xiaosiwei1006@gmail.com

## License

Code is released under the MIT License. Public aggregate/metric data are released under CC BY 4.0. Raw restricted data are not redistributed.
