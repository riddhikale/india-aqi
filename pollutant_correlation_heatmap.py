import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data.csv", encoding="cp1252", low_memory=False)
print(df.head())

pollutant_cols = ["so2", "no2", "rspm", "spm", "pm2_5"]
corr_matrix = df[pollutant_cols].corr()

