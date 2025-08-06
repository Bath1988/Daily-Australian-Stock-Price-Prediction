import pandas as pd

# Load and clean
df = pd.read_csv("../Data/output.csv")

# Rename columns if needed (make them easy to use)
df = df.rename(columns={"closing_price$": "closing_price", "date": "date"})

# Parse date, sort, and clean price string
df["date"] = pd.to_datetime(df["date"])
df["closing_price"] = (
    df["closing_price"]
    .astype(str)
    .str.replace(r"[\$,]", "", regex=True)  # remove $ and commas
    .astype(float)
)

df = df.sort_values("date").reset_index(drop=True)

# Quick sanity check
print(df.head())
print(df.tail())
print("Data range:", df["date"].min(), "to", df["date"].max())

# Example moving averages: 20-day and 50-day
df["ma_7"] = df["closing_price"].rolling(window=7, min_periods=1).mean()
df["ma_20"] = df["closing_price"].rolling(window=20, min_periods=1).mean()
df["ma_50"] = df["closing_price"].rolling(window=50, min_periods=1).mean()

import matplotlib.pyplot as plt

plt.figure(figsize=(12, 6))
plt.plot(df["date"], df["closing_price"], label="Closing Price", linewidth=1)
plt.plot(df["date"], df["ma_7"], label="7-day Moving Average", linewidth=1)
plt.title("Closing Price with Moving Averages")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

df

