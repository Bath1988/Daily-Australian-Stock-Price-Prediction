from sklearn.metrics import root_mean_squared_error, mean_absolute_error
from b_feature_engineering import df_prelag, df_clolag
import os
import csv



# Directory and file for validation results
val_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../docs/validations"))
os.makedirs(val_dir, exist_ok=True)
val_path = os.path.join(val_dir, "baseline_model_results.csv")
header = ["model", "target", "rmse", "mae"]
write_header = not os.path.exists(val_path)
rows = []


# 1. Previous day closing price as prediction
df_eval2 = df_clolag.copy()
rmse1 = root_mean_squared_error(df_eval2['closing_price'], df_eval2['clolag_1'])
mae1 = mean_absolute_error(df_eval2['closing_price'], df_eval2['clolag_1'])
rows.append(["naive_previous_day", "closing_price", rmse1, mae1])

# 2. Previous five days average as prediction (use a fresh copy to avoid column overwrite issues)
df_eval2_avg = df_clolag.copy()
df_eval2_avg['avg'] = df_eval2_avg[['clolag_1', 'clolag_2', 'clolag_3', 'clolag_4', 'clolag_5']].mean(axis=1)
rmse2 = root_mean_squared_error(df_eval2_avg['closing_price'], df_eval2_avg['avg'])
mae2 = mean_absolute_error(df_eval2_avg['closing_price'], df_eval2_avg['avg'])
rows.append(["naive_5day_avg", "closing_price", rmse2, mae2])

# 3. Previous day + previous price diff as prediction
df_eval3 = df_prelag.copy()
df_eval3['predict'] = df_eval3['clolag_1'] + df_eval3['prilag_1']
rmse3 = root_mean_squared_error(df_eval3['closing_price'], df_eval3['predict'])
mae3 = mean_absolute_error(df_eval3['closing_price'], df_eval3['predict'])
rows.append(["naive_diff_addition", "closing_price", rmse3, mae3])

# Write results
with open(val_path, "a", newline="") as f:
	writer = csv.writer(f)
	if write_header:
		writer.writerow(header)
	writer.writerows(rows)
print(f"Validation results saved to {val_path}")
