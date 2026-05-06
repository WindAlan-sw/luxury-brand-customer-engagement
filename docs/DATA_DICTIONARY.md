# Public Metrics Data Dictionary

## `01_brand_post_metrics_detexted.csv`

Rows: 18964

Columns:
- `public_post_id`
- `brand`
- `brand_id`
- `year`
- `month`
- `year_month`
- `month_index`
- `weekday`
- `hour`
- `retweet_count`
- `reply_count`
- `like_count`
- `quote_count`
- `engagement_total`
- `hashtag_count`
- `mention_count`
- `is_retweet`
- `Entertainment`
- `Trendiness`
- `Interaction`
- `Customization`
- `entropy_ce_score`
- `critic_ce_score`
- `cilos_score`
- `idocriw_score`
- `merec_score`
- `additive_engagement_score`

## `02_brand_month_engagement_panel.csv`

Rows: 322

Columns:
- `brand`
- `brand_id`
- `year`
- `month`
- `year_month`
- `month_index`
- `post_count`
- `retweet_count_sum`
- `retweet_count_mean`
- `retweet_count_median`
- `reply_count_sum`
- `reply_count_mean`
- `reply_count_median`
- `like_count_sum`
- `like_count_mean`
- `like_count_median`
- `quote_count_sum`
- `quote_count_mean`
- `quote_count_median`
- `engagement_total_sum`
- `engagement_total_mean`
- `engagement_total_median`
- `hashtag_count_sum`
- `hashtag_count_mean`
- `mention_count_sum`
- `mention_count_mean`
- `Entertainment_sum`
- `Trendiness_sum`
- `Interaction_sum`
- `Customization_sum`
- `entropy_ce_score_sum`
- `entropy_ce_score_mean`
- `entropy_ce_score_median`
- `critic_ce_score_sum`
- `critic_ce_score_mean`
- `critic_ce_score_median`
- `cilos_score_mean`
- `idocriw_score_mean`
- `merec_score_mean`
- `additive_engagement_score_mean`

## `03_brand_overall_engagement_summary.csv`

Rows: 6

Columns:
- `brand`
- `brand_id`
- `post_count`
- `retweet_count_sum`
- `reply_count_sum`
- `like_count_sum`
- `quote_count_sum`
- `engagement_total_sum`
- `entropy_ce_score_mean`
- `entropy_ce_score_median`
- `critic_ce_score_mean`
- `Entertainment_sum`
- `Trendiness_sum`
- `Interaction_sum`
- `Customization_sum`

## `04_entropy_weight_input.csv`

Rows: 18964

Columns:
- `public_post_id`
- `brand`
- `retweet_count`
- `reply_count`
- `like_count`
- `quote_count`

## `05_entropy_score_results.csv`

Rows: 18964

Columns:
- `public_post_id`
- `brand`
- `entropy_ce_score`

## `06_scoring_method_post_results.csv`

Rows: 18964

Columns:
- `public_post_id`
- `brand`
- `entropy_ce_score`
- `critic_ce_score`
- `cilos_score`
- `idocriw_score`
- `merec_score`
- `additive_engagement_score`

## `07_scoring_method_summary_by_brand.csv`

Rows: 6

Columns:
- `brand`
- `entropy_ce_score_mean`
- `entropy_ce_score_median`
- `entropy_ce_score_std`
- `entropy_ce_score_min`
- `entropy_ce_score_max`
- `critic_ce_score_mean`
- `critic_ce_score_median`
- `critic_ce_score_std`
- `critic_ce_score_min`
- `critic_ce_score_max`
- `cilos_score_mean`
- `cilos_score_median`
- `cilos_score_std`
- `cilos_score_min`
- `cilos_score_max`
- `idocriw_score_mean`
- `idocriw_score_median`
- `idocriw_score_std`
- `idocriw_score_min`
- `idocriw_score_max`
- `merec_score_mean`
- `merec_score_median`
- `merec_score_std`
- `merec_score_min`
- `merec_score_max`
- `additive_engagement_score_mean`
- `additive_engagement_score_median`
- `additive_engagement_score_std`
- `additive_engagement_score_min`
- `additive_engagement_score_max`

## `08_customer_month_engagement_summary.csv`

Rows: 6

Columns:
- `brand`
- `year`
- `month`
- `year_month`
- `customer_post_count`
- `followers_mean`
- `followers_median`
- `retweets_sum`
- `retweets_mean`
- `favorites_sum`
- `favorites_mean`

## `09_sentiment_month_summary.csv`

Rows: 6

Columns:
- `brand`
- `year`
- `month`
- `year_month`
- `customer_post_count`
- `sentiment_score_mean`
- `sentiment_score_median`
- `positive_count`
- `neutral_count`
- `negative_count`
- `positive_share`
- `neutral_share`
- `negative_share`

## `10_sentiment_hour_profile.csv`

Rows: 138

Columns:
- `brand`
- `hour`
- `customer_post_count`
- `sentiment_score_mean`
- `positive_count`
- `neutral_count`
- `negative_count`

## `11_fixed_effects_model_panel.csv`

Rows: 322

Columns:
- `brand`
- `brand_id`
- `month_index`
- `year`
- `month`
- `year_month`
- `post_count`
- `score`
- `Entertainment`
- `Trendiness`
- `Interaction`
- `Customization`
- `entropy_ce_score_mean`
- `critic_ce_score_mean`
- `engagement_total_sum`
- `brand_Armani`
- `brand_Burberry`
- `brand_Chanel`
- `brand_Dior`
- `brand_Gucci`
- `brand_LV`

## `12_clustering_feature_matrix.csv`

Rows: 6

Columns:
- `brand`
- `mean_CE_score`
- `CE_level`
- `mean_sentiment_score`
- `source_note`

## `13_brand_month_full_public_panel.csv`

Rows: 322

Columns:
- `brand`
- `brand_id`
- `year`
- `month`
- `year_month`
- `month_index`
- `post_count`
- `retweet_count_sum`
- `retweet_count_mean`
- `retweet_count_median`
- `reply_count_sum`
- `reply_count_mean`
- `reply_count_median`
- `like_count_sum`
- `like_count_mean`
- `like_count_median`
- `quote_count_sum`
- `quote_count_mean`
- `quote_count_median`
- `engagement_total_sum`
- `engagement_total_mean`
- `engagement_total_median`
- `hashtag_count_sum`
- `hashtag_count_mean`
- `mention_count_sum`
- `mention_count_mean`
- `Entertainment_sum`
- `Trendiness_sum`
- `Interaction_sum`
- `Customization_sum`
- `entropy_ce_score_sum`
- `entropy_ce_score_mean`
- `entropy_ce_score_median`
- `critic_ce_score_sum`
- `critic_ce_score_mean`
- `critic_ce_score_median`
- `cilos_score_mean`
- `idocriw_score_mean`
- `merec_score_mean`
- `additive_engagement_score_mean`
- `customer_post_count`
- `sentiment_score_mean`
- `sentiment_score_median`
- `positive_count`
- `neutral_count`
- `negative_count`
- `positive_share`
- `neutral_share`
- `negative_share`
- `customer_post_count_customer`
- `followers_mean`
- `followers_median`
- `retweets_sum`
- `retweets_mean`
- `favorites_sum`
- `favorites_mean`

