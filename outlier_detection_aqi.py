import numpy as np
import pandas as pd

df = pd.read_csv("data.csv", encoding="cp1252", low_memory=False)
print(df.head())

delhi = df[df["state"] == "Delhi"]
print(f"Delhi rows: {len(delhi)}")

def detect_outliers(data, label):
    sorted_data = np.sort(data)
    n = len(sorted_data)