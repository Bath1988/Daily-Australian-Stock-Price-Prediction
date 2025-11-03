from sklearn.metrics import mean_absolute_error, mean_squared_error
from prophet import Prophet
from b_feature_engineering import df_clolag
import pandas as pd
import numpy as np
import os
import csv

def prophet_model(df, target='closing_price', date_col='date', train_size=365):
    # Prophet expects columns: ds (date), y (target)
    df_prophet = df[[date_col, target]].rename(columns={date_col: 'ds', target: 'y'}).copy()
    preds = []
    actuals = []
    dates = []
    for i in range(train_size, len(df_prophet)):
        train = df_prophet.iloc[:i]
        test = df_prophet.iloc[i:i+1]
        model = Prophet(daily_seasonality=True, yearly_seasonality=True)
        model.fit(train)
        future = test[['ds']]
        forecast = model.predict(future)
        y_pred = forecast['yhat'].values[0]
        preds.append(y_pred)
        actuals.append(test['y'].values[0])
        dates.append(test['ds'].values[0])
    df_results = pd.DataFrame({'date': dates, 'actual': actuals, 'predicted': preds})
    return df_results

# Directory and file for validation results
val_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../docs/validations"))
os.makedirs(val_dir, exist_ok=True)
val_path = os.path.join(val_dir, "prophet_model_results.csv")
header = ["model", "target", "rmse", "mae"]
write_header = not os.path.exists(val_path)

# Prophet model for closing price
df = df_clolag.copy()
df_eval = prophet_model(df, target='closing_price', date_col='date')
rmse = np.sqrt(mean_squared_error(df_eval.actual, df_eval.predicted))
mae = mean_absolute_error(df_eval.actual, df_eval.predicted)
row = ["prophet", "closing_price", rmse, mae]

# Write results
with open(val_path, "a", newline="") as f:
    writer = csv.writer(f)
    if write_header:
        writer.writerow(header)
    writer.writerow(row)
print(f"Validation results saved to {val_path}")
