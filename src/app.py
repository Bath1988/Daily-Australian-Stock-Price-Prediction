from fastapi import FastAPI
from prophet import Prophet
import pandas as pd
import json

app = FastAPI()

@app.get("/predict")
def predict():
    # Load saved data
    with open("../data.json") as f:
        data = json.load(f)
    
    # Extract the body section (time series data)
    body = data["body"]

# Create a DataFrame from the body
    df = pd.DataFrame({
    "ds": pd.to_datetime([v["date"] for v in body.values()]),  # convert 'date' strings to datetime
    "y": [v["close"] for v in body.values()]                   # use 'close' price as the target variable
    })

# Sort by date (optional but recommended for time series)
    df = df.sort_values("ds").reset_index(drop=True)
  
    # Train and predict
    model = Prophet()
    model.fit(df)
    future = model.make_future_dataframe(periods=1)
    forecast = model.predict(future)
    return forecast[["ds", "yhat"]].tail(1).to_dict()