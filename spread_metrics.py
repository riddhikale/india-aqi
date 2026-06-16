import numpy as np
import pandas as pd

df = pd.read_csv("data.csv", encoding="cp1252", low_memory=False)
print(df.head())

delhi = df[df["state"] == "Delhi"]
print(f"Delhi rows: {len(delhi)}")

def compute_spread(data, label):
    #1: distance of each value from the mean
    deviations = data - np.mean(data)

    #2: square each deviation (makes all positive)
    squared_devs = deviations ** 2

