# Testing Guide

## 1. Local test

```bash
pip install -r requirements.txt
python check_public_release.py
```

Expected final message:

```text
PASS: public metric files load and no restricted columns were found.
```

## 2. Colab test

Open the GitHub repository and launch:

- `notebooks/01_Check_Published_Results.ipynb`
- `notebooks/02_Reproduce_Public_Metric_Analysis.ipynb`
- `notebooks/05_Apply_Framework_To_Your_Data.ipynb`

Run all cells from a fresh runtime.

## 3. Manual content check

Confirm that no public CSV file contains columns named:

```text
Tweet, Text, clean_tweet, Handle, Name, URL, mentioned, hashtags, retweeted
```

The script `check_public_release.py` performs this check automatically.
