from sklearn.metrics import root_mean_squared_error, mean_absolute_error
from sklearn.linear_model import LinearRegression
from b_feature_engineering import df_prelag, df_clolag
import pandas as pd

# This function evaluate linear model for the initial train size and iterating forward creating models for each day
# Prediction is done for each model using model created in each iteration
def linear_model(df, train_size = 365, target = '', index = 'date'):
    preds = []
    actuals = []
    dates = []
    X = df.drop(columns= [index, target])
    Y = df[target]
  
    for i in range(train_size, len(df)):
        X_train = X.iloc[:i]
        y_train = Y.iloc[:i]
        X_test = X.iloc[i:i+1]
        y_test = Y.iloc[i:i+1]

        # simple model: linear regression
        model = LinearRegression()
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

df_eval1 = df_clolag.copy()
df_eval = linear_model(df = df_eval1, target = 'closing_price')
rmse = root_mean_squared_error(df_eval.actual, df_eval.predicted)
mae = mean_absolute_error(df_eval.actual, df_eval.predicted)

df_eval2 = df_prelag.copy()
df_eval = linear_model(df = df_prelag.drop(columns=["closing_price", "clolag_1"]), target = 'price_diff')
rmse = root_mean_squared_error(df_eval.actual, df_eval.predicted)
mae = mean_absolute_error(df_eval.actual, df_eval.predicted)
