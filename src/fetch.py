import requests
import json

with open("credentials.txt") as f:
    credentials = dict(line.strip().split("=") for line in f if "=" in line)

url = "https://yahoo-finance15.p.rapidapi.com/api/v1/markets/stock/history"

querystring = {"symbol":"CBA.AX","interval":"1d","diffandsplits":"false"}

headers = {
    "x-rapidapi-key": credentials["RAPIDAPI_KEY"],
    "x-rapidapi-host": credentials["RAPIDAPI_HOST"]
}

response = requests.get(url, headers=headers, params=querystring)



# Check if the request was successful
if response.status_code == 200:
    # Convert the response to JSON format
    data = response.json()

    # Pretty print the JSON data
    print(json.dumps(data, indent=4))  # Using json.dumps to format the output
    
    with open("data.json", "w") as f:
        json.dump(data, f, indent=4)

else:
    print(f"Error: Unable to fetch data. Status code {response.status_code}")


    



