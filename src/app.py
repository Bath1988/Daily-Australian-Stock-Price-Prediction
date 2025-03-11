import requests
import json

url = "https://yahoo-finance15.p.rapidapi.com/api/v1/markets/stock/history"

querystring = {"symbol":"CMB.AX","interval":"5m","diffandsplits":"false"}

headers = {
	"x-rapidapi-key": "d79a3883b7msh00d863286e8567bp132781jsn1518cc26254e",
	"x-rapidapi-host": "yahoo-finance15.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)



# Check if the request was successful
if response.status_code == 200:
    # Convert the response to JSON format
    data = response.json()

    # Pretty print the JSON data
    print(json.dumps(data, indent=4))  # Using json.dumps to format the output
    
else:
    print(f"Error: Unable to fetch data. Status code {response.status_code}")


    



