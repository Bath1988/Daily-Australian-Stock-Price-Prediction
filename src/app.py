from fastapi import FastAPI
from prophet import Prophet
import pandas as pd

app = FastAPI()

@app.get("/")
def predict():

    df = pd.read_csv('../Data/output.csv') 
    # Train and predict
    model = Prophet()
    model.fit(df)
    future = model.make_future_dataframe(periods=1)
    forecast = model.predict(future)
    return forecast[["Next_Day_Closing_Value", "yhat"]].tail(1).to_dict()