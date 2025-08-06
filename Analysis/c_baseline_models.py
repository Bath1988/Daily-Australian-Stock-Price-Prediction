from sklearn.metrics import root_mean_squared_error, mean_absolute_error
from b_feature_engineering import df_prelag, df_clolag

# Import feature engineered data set with closing price lags for this analysis
df_eval2 = df_clolag.copy()

# In this first base line prediction, the day before closing stock price used as the prediction.
# Root mean squired error as rmse and Mean absolute error as mae were calculated as the error metrics.
rmse = root_mean_squared_error(df_eval2['closing_price'], df_eval2['clolag_1'])
mae = mean_absolute_error(df_eval2['closing_price'], df_eval2['clolag_1'])

# In this second base line prediction, the previous five days average used as the prediction.
# Root mean squired error as rmse and Mean absolute error as mae were calculated as the error metrics.

df_eval2['avg'] = df_eval2[['clolag_1', 'clolag_2', 'clolag_3', 'clolag_4', 'clolag_5']].mean(axis=1)
rmse = root_mean_squared_error(df_eval2['closing_price'], df_eval2['avg'])
mae = mean_absolute_error(df_eval2['closing_price'], df_eval2['avg'])

# Import feature engineered data set with price difference lags for this analysis
df_eval3 = df_prelag.copy()

# In this base line prediction, the difference between previous two days added to the previous day value.
# Root mean squired error as rmse and Mean absolute error as mae were calculated as the error metrics.

df_eval3['predict'] = df_eval3['clolag_1'] + df_eval3['prilag_1']
rmse = root_mean_squared_error(df_eval3['closing_price'], df_eval3['predict'])
mae = mean_absolute_error(df_eval3['closing_price'], df_eval3['predict'])
