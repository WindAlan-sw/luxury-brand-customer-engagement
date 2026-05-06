"""Utility functions for the luxury-brand customer engagement public metrics repository."""
from pathlib import Path
import numpy as np
import pandas as pd


def load_public_metrics(repo_root="."):
    root = Path(repo_root)
    data_dir = root / "data" / "public_metrics"
    return {p.stem: pd.read_csv(p) for p in sorted(data_dir.glob("*.csv"))}


def compute_entropy_weights(metric_df, metric_cols):
    """Compute entropy weights for non-negative engagement metrics.

    Parameters
    ----------
    metric_df : pandas.DataFrame
        DataFrame containing non-negative engagement indicators.
    metric_cols : list[str]
        Columns to use as indicators.
    """
    X = metric_df[metric_cols].astype(float).clip(lower=0).to_numpy()
    X = X + 1e-12
    P = X / X.sum(axis=0, keepdims=True)
    n = X.shape[0]
    k = 1 / np.log(n)
    entropy = -k * np.sum(P * np.log(P), axis=0)
    diversification = 1 - entropy
    weights = diversification / diversification.sum()
    return pd.Series(weights, index=metric_cols, name="entropy_weight")


def score_with_weights(metric_df, metric_cols, weights):
    X = metric_df[metric_cols].astype(float)
    # min-max normalization
    denom = (X.max() - X.min()).replace(0, 1)
    Xn = (X - X.min()) / denom
    return Xn.mul(weights, axis=1).sum(axis=1)


def make_brand_month_panel(post_metrics):
    agg = post_metrics.groupby(["brand", "year", "month", "year_month", "month_index"], dropna=False).agg(
        post_count=("public_post_id", "count"),
        score=("entropy_ce_score", "sum"),
        mean_score=("entropy_ce_score", "mean"),
        Entertainment=("Entertainment", "sum"),
        Trendiness=("Trendiness", "sum"),
        Interaction=("Interaction", "sum"),
        Customization=("Customization", "sum"),
        engagement_total=("engagement_total", "sum"),
    ).reset_index()
    return agg
