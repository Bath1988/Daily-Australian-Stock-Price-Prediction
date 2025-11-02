import requests
import json
import pandas as pd
import os

with open("../credentials.txt") as f:
    credentials = dict(line.strip().split("=") for line in f if "=" in line)

url = "https://yahoo-finance15.p.rapidapi.com/api/v2/markets/stock/history"

# List of major Australian banks and mining companies (ASX symbols)
symbols = [
    "CBA.AX",  # Commonwealth Bank
    "NAB.AX",  # National Australia Bank
    "WBC.AX",  # Westpac
    "ANZ.AX",  # ANZ Bank
    "BHP.AX",  # BHP Group
    "RIO.AX",  # Rio Tinto
    "FMG.AX"   # Fortescue Metals
]

headers = {
    "x-rapidapi-key": credentials["RAPIDAPI_KEY"],
    "x-rapidapi-host": credentials["RAPIDAPI_HOST"]
}

data_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../Data"))
os.makedirs(data_dir, exist_ok=True)

for symbol in symbols:
    print(f"Fetching data for {symbol}...")
    querystring = {"symbol": symbol, "interval": "1d"}
    response = requests.get(url, headers=headers, params=querystring)

    if response.status_code == 200:
        data = response.json()
        # Save JSON
        json_path = os.path.join(data_dir, f"data_{symbol}.json")
        with open(json_path, "w") as f:
            json.dump(data, f, indent=4)
        print(f"Saved JSON to {json_path}")

        # Extract and save CSV
        body = data.get("body", [])
        if body:
            df = pd.DataFrame({
                "date": pd.to_datetime([v["timestamp"] for v in body]),
                "closing_price$": [v["close"] for v in body]
            })
            csv_path = os.path.join(data_dir, f"output_{symbol}.csv")
            df.to_csv(csv_path, index=False)
            print(f"Saved CSV to {csv_path}")
        else:
            print(f"Warning: No data in response body for {symbol}")
    else:
        print(f"Error: Unable to fetch data for {symbol}. Status code {response.status_code}")




