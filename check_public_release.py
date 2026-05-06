from pathlib import Path
import pandas as pd

RESTRICTED_TERMS = {
    "tweet", "text", "clean_tweet", "handle", "name", "url",
    "mentioned", "hashtags", "retweeted", "full_text", "screen_name"
}

def main():
    root = Path(__file__).resolve().parent
    public_dir = root / "data" / "public_metrics"
    files = sorted(public_dir.glob("*.csv"))
    if not files:
        raise FileNotFoundError("No public metric CSV files found.")
    for path in files:
        df = pd.read_csv(path, nrows=5)
        risky = [c for c in df.columns if c.lower() in RESTRICTED_TERMS]
        if risky:
            raise ValueError(f"Restricted columns found in {path.name}: {risky}")
        print(f"OK: {path.name} ({len(pd.read_csv(path))} rows)")
    print("PASS: public metric files load and no restricted columns were found.")

if __name__ == "__main__":
    main()
