
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt

# Choose the company symbol for modeling
COMPANY = "CBA.AX"  # Change this to any symbol you want

# Load from the new combined file (pivoted format)
df_all = pd.read_csv("../Data/output_all_companies.csv", index_col=0, parse_dates=True)

# Select the series for the chosen company
df = df_all[[COMPANY]].rename(columns={COMPANY: "closing_price"}).copy()
df = df.reset_index().rename(columns={"index": "date"})
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

if __name__ == "__main__":
    print("First few rows of df_clolag (lagged closing prices):")
    print(df_clolag.head())
    print("\nFirst few rows of df_prelag (lagged price differences):")
    print(df_prelag.head())
    # Save the final feature-engineered table to the Data folder
    data_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../Data"))
    os.makedirs(data_dir, exist_ok=True)
    feature_csv_path = os.path.join(data_dir, f"feature_engineered_{COMPANY}.csv")
    df_prelag.to_csv(feature_csv_path, index=False)
    print(f"\nFeature-engineered table saved to {feature_csv_path}")
    # Also save a copy to the docs folder
    docs_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../docs"))
    os.makedirs(docs_dir, exist_ok=True)
    feature_csv_docs_path = os.path.join(docs_dir, f"feature_engineered_{COMPANY}.csv")
    df_prelag.head(6).to_csv(feature_csv_docs_path, index=False)
    print(f"Feature-engineered table (first 6 rows) also saved to {feature_csv_docs_path}")
df_clolag
df_prelag