from sklearn.metrics import root_mean_squared_error, mean_absolute_error
from xgboost import XGBRegressor
from b_feature_engineering import df_prelag, df_clolag
import pandas as pd
import os
import csv

def xgboost_model(df, train_size = 365, target = '', index = 'date'):
    preds = []
    actuals = []
    dates = []
    X = df.drop(columns= [index, target])
    Y = df[target]
    model = (XGBRegressor(
            objective="reg:squarederror",
            max_depth=7,
            learning_rate=0.001,
            n_estimators=150,
            random_state=42))
    for i in range(train_size, len(df)):
        X_train = X.iloc[:i]
        y_train = Y.iloc[:i]
        X_test = X.iloc[i:i+1]
        y_test = Y.iloc[i:i+1]
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        preds.append(y_pred[0])
        actuals.append(y_test.values[0])
        dates.append(df.loc[i,index])
    df_results = (pd.DataFrame({
                    "date": dates,
                    "actual": actuals,
                    "predicted": preds }))
    return df_results

# Directory and file for validation results
val_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../docs/validations"))
os.makedirs(val_dir, exist_ok=True)
val_path = os.path.join(val_dir, "xgboost_model_results.csv")
header = ["model", "target", "rmse", "mae"]
write_header = not os.path.exists(val_path)

# XGBoost model for price_diff
df = df_prelag.drop(columns=["closing_price", "clolag_1"]).copy()
df_eval = xgboost_model(df = df , target = 'price_diff')
rmse = root_mean_squared_error(df_eval.actual, df_eval.predicted)
mae = mean_absolute_error(df_eval.actual, df_eval.predicted)
row = ["xgboost", "price_diff", rmse, mae]

# Write results
with open(val_path, "a", newline="") as f:
    writer = csv.writer(f)
    if write_header:
        writer.writerow(header)
    writer.writerow(row)
print(f"Validation results saved to {val_path}")
