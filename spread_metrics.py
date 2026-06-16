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

    #3: average the squared deviations
    variance = np.sum(squared_devs) / len(data)

    #standard deviation: square root of variance
    std_dev = np.sqrt(variance)

    #range: simplest spread measure
    range_val = np.max(data) - np.min(data)

    assert abs(variance - np.var(data))  < 0.01
    assert abs(std_dev  - np.std(data))  < 0.01 

    print('----------')
    print(f" Variance   : {variance:.2f}")
    print(f" Standard Deviation   : {std_dev:.2f}")
    print(f" Range   : {range_val:.2f}")

    return {
        "pollutant": label,
        "variance": round(variance, 2),
        "standard deviance": round(std_dev, 2),
        "range": round(range_val, 2),
    }


results = []

# PM2.5
pm25 = delhi["pm2_5"].dropna().values
results.append(compute_spread(pm25, "PM2.5 — Delhi"))

# PM10 
pm10 = delhi["rspm"].dropna().values
results.append(compute_spread(pm10, "PM10 (rspm) — Delhi"))

# NO2
no2 = delhi["no2"].dropna().values
results.append(compute_spread(no2, "NO2 — Delhi"))