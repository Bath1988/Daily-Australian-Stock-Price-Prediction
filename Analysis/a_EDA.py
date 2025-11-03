
import pandas as pd

# Choose the company symbol for modeling
COMPANY = "CBA.AX"  # Change this to any symbol you want

# Load from the new combined file (pivoted format)
df_all = pd.read_csv("../Data/output_all_companies.csv", index_col=0, parse_dates=True)

# Select the series for the chosen company
df = df_all[[COMPANY]].rename(columns={COMPANY: "closing_price"}).copy()
df = df.reset_index().rename(columns={"index": "date"})

# Quick sanity check
print(df.head())
print(df.tail())
print("Data range:", df["date"].min(), "to", df["date"].max())

# Example moving averages: 7, 20, 50-day
df["ma_7"] = df["closing_price"].rolling(window=7, min_periods=1).mean()
df["ma_20"] = df["closing_price"].rolling(window=20, min_periods=1).mean()
df["ma_50"] = df["closing_price"].rolling(window=50, min_periods=1).mean()

import matplotlib.pyplot as plt
import os

plt.figure(figsize=(12, 6))
plt.plot(df["date"], df["closing_price"], label="Closing Price", linewidth=1)
plt.plot(df["date"], df["ma_7"], label="7-day Moving Average", linewidth=1)
plt.title(f"{COMPANY} Closing Price with Moving Averages")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()
plt.grid(True)
plt.tight_layout()
plots_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../docs/plots"))
os.makedirs(plots_dir, exist_ok=True)
plt.savefig(os.path.join(plots_dir, f"eda_{COMPANY}.png"))
print(f"EDA plot saved to {os.path.join(plots_dir, f'eda_{COMPANY}.png')}")
plt.show()

