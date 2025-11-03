

import os
import pandas as pd
import matplotlib.pyplot as plt

# Data directory (relative to this script)
data_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../Data"))
csv_path = os.path.join(data_dir, "output_all_companies.csv")

# Only plot the current companies in fetch.py
symbols = [
    "CBA.AX",  # Commonwealth Bank
    "NAB.AX",  # National Australia Bank
    "WBC.AX",  # Westpac
    "ANZ.AX",  # ANZ Bank
    "BHP.AX",  # BHP Group
    "RIO.AX",  # Rio Tinto
    "FMG.AX",  # Fortescue Metals
    "ORG.AX",  # Origin Energy
    "AGL.AX"   # AGL Energy
]

df = pd.read_csv(csv_path, parse_dates=["date"] if "date" in pd.read_csv(csv_path, nrows=1).columns else None)

# If 'date' is not a column, it's the index
if "date" not in df.columns:
    df.index = pd.to_datetime(df.index)
    df_for_plot = df
else:
    df["date"] = pd.to_datetime(df["date"])
    df.set_index("date", inplace=True)
    df_for_plot = df

plt.figure(figsize=(14, 7))
for symbol in symbols:
    if symbol in df_for_plot.columns:
        plt.plot(df_for_plot.index, df_for_plot[symbol], label=symbol)

plt.title("Stock Price Trends: Major Australian Banks, Miners & Energy Companies")
plt.xlabel("Date")
plt.ylabel("Closing Price ($)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
