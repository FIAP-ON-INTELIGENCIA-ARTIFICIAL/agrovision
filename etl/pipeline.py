import pandas as pd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "solo.csv"
OUT = ROOT / "data" / "solo_features.csv"

def run():
    df = pd.read_csv(RAW)
    df["ph_bin"] = pd.cut(df["ph"], [0,5.5,6.5,14], labels=["baixo","ideal","alto"])
    df.to_csv(OUT, index=False)
    print("OK ->", OUT)

if __name__ == "__main__":
    run()
