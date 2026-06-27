import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data.csv", encoding="cp1252", low_memory=False)
print(df.head())


pollutant_cols = ["so2", "no2", "rspm", "spm", "pm2_5"]
corr_matrix = df[pollutant_cols].corr()

print("Correlation matrix:")
print(corr_matrix.round(2))


print("\nStrongest correlations:")

for i in range(len(pollutant_cols)):
    for j in range(i+1, len(pollutant_cols)):
        corr_val = corr_matrix.iloc[i, j]
        if abs(corr_val) > 0.5:
            print(f"  {pollutant_cols[i]} vs {pollutant_cols[j]}: {corr_val:.2f}")

