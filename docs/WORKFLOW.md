# Analysis Workflow

## Phase 1: Post-level brand engagement metrics

Input: `data/public_metrics/01_brand_post_metrics_detexted.csv`

Purpose: inspect official brand post-level engagement using public metrics only.

Main variables:

- retweet_count
- reply_count
- like_count
- quote_count
- engagement_total
- Entertainment
- Trendiness
- Interaction
- Customization
- entropy_ce_score
- critic_ce_score

## Phase 2: Brand-month aggregation

Input: `data/public_metrics/02_brand_month_engagement_panel.csv`

Purpose: reproduce the brand-month modelling structure used in the published analysis.

Main outputs:

- `11_fixed_effects_model_panel.csv`
- brand-month score summaries
- monthly engagement comparisons

## Phase 3: Scoring-method comparison

Inputs:

- `04_entropy_weight_input.csv`
- `05_entropy_score_results.csv`
- `06_scoring_method_post_results.csv`
- `07_scoring_method_summary_by_brand.csv`

Purpose: compare entropy-based CE scores with alternative objective weighting/scoring methods.

## Phase 4: Customer sentiment and engagement summaries

Inputs:

- `08_customer_month_engagement_summary.csv`
- `09_sentiment_month_summary.csv`
- `10_sentiment_hour_profile.csv`

Purpose: inspect aggregated customer-side engagement and sentiment outcomes.

## Phase 5: Clustering

Input: `12_clustering_feature_matrix.csv`

Purpose: reproduce the hierarchical clustering features used in the published analysis.
