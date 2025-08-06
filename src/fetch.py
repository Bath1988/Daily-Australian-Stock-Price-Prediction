import requests
import json

with open("../credentials.txt") as f:
    credentials = dict(line.strip().split("=") for line in f if "=" in line)

url = "https://yahoo-finance15.p.rapidapi.com/api/v2/markets/stock/history"

# This is 'YH Finance' API in RapidAPI

querystring = {"symbol":"CBA.AX","interval":"1d"}

headers = {
    "x-rapidapi-key": credentials["RAPIDAPI_KEY"],
    "x-rapidapi-host": credentials["RAPIDAPI_HOST"]
}

response = requests.get(url, headers=headers, params=querystring)


if response.status_code == 200:
    # Retrieve data from the response to JSON format
    data = response.json()

 # Using json.dumps to format the output
    print(json.dumps(data, indent=4)) 

    with open("../Data/data.json", "w") as f:
        json.dump(data, f, indent=4)

else:
    print(f"Error: Unable to fetch data. Status code {response.status_code}")

# Below code get date and closing stock price from data and save as csv file
import pandas as pd

body = data["body"]

# Convert to DataFrame
df = pd.DataFrame({
    "date": pd.to_datetime([v["timestamp"] for v in body]), 
    "closing_price$": [v["close"] for v in body]            
})

#df = df.sort_values("ds").reset_index(drop=True)
df.to_csv('../Data/output.csv', index=False) 
    



