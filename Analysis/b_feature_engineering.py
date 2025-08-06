import pandas as pd
import numpy as np
from pathlib import Path


# Load and clean data
df = pd.read_csv(Path("../Data/output.csv"))
df = df.rename(columns={"closing_price$": "closing_price", "date": "date"})
df["date"] = pd.to_datetime(df["date"])
df["closing_price"] = df["closing_price"].astype(float)

# ---- Create features (lagged prices) ----
def create_lags(data, lags=5, feature = ''):
    df_feat = data.copy()
    for lag in range(1, lags + 1):
        df_feat[f"{feature[0:3]}lag_{lag}"] = df_feat[feature].shift(lag)
    return df_feat

# Remove rows with null values due to value shifts
df_clolag = create_lags(df, lags=5, feature = 'closing_price').dropna().reset_index(drop=True)

# Create price difference column in a new dataframe
df_prelag = df_clolag[['date', 'closing_price', 'clolag_1']].copy()
df_prelag["price_diff"] = df_prelag["closing_price"] - df_prelag["clolag_1"]

df_prelag = create_lags(df_prelag, lags=5, feature = 'price_diff').dropna().reset_index(drop=True)

df_clolag
df_prelag