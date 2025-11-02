import os
import pandas as pd
import matplotlib.pyplot as plt

# List of company symbols (should match those in fetch.py)
symbols = [
    "CBA.AX", "NAB.AX", "WBC.AX", "ANZ.AX", "BHP.AX", "RIO.AX", "FMG.AX"
]

# Data directory (relative to this script)
data_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../Data"))

plt.figure(figsize=(14, 7))

for symbol in symbols:
    csv_path = os.path.join(data_dir, f"output_{symbol}.csv")
    if os.path.exists(csv_path):
        df = pd.read_csv(csv_path)
        df["date"] = pd.to_datetime(df["date"])
        plt.plot(df["date"], df["closing_price$"] , label=symbol)
    else:
        print(f"Warning: {csv_path} not found.")

plt.title("Stock Price Trends: Major Australian Banks & Mining Companies")
plt.xlabel("Date")
plt.ylabel("Closing Price ($)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
