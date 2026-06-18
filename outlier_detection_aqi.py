import numpy as np
import pandas as pd

df = pd.read_csv("data.csv", encoding="cp1252", low_memory=False)
print(df.head())

delhi = df[df["state"] == "Delhi"]
print(f"Delhi rows: {len(delhi)}")

def detect_outliers(data, label):
    sorted_data = np.sort(data)
    n = len(sorted_data)

    lower_half = sorted_data[:n//2]
    upper_half = sorted_data[n//2 + (n%2):]


    # Q1 = median of lower_half
    m = len(lower_half)
    if m % 2 == 1:
        q1 = lower_half[n // 2]
    else:
        mid = m // 2
        q1 = (lower_half[mid-1] + lower_half[mid]) / 2
    
    # Q3 = median of upper_half
    m = len(upper_half)
    if m % 2 == 1:
        q3 = upper_half[n // 2]
    else:
        mid = m // 2
        q3 = (upper_half[mid-1] + upper_half[mid]) / 2
    

    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    
    outlier_mask = (data < lower_bound) | (data > upper_bound)
    outlier_count = np.sum(outlier_mask)

    assert abs(q1 - np.percentile(data, 25)) < 0.5
    assert abs(q3 - np.percentile(data, 75)) < 0.5


    print('----------')
    print(f" Q1   : {q1:.2f}")
    print(f" Q3   : {q3:.2f}")
    print(f" IQR   : {iqr:.2f}")
    print(f" Lower Bound   : {lower_bound:.2f}")
    print(f" Upper Bound   : {upper_bound:.2f}")
    print(f" Outlier Count   : {outlier_count:.2f}")

    return {
        "label": label,           
        "q1": round(q1, 2),
        "q3": round(q3, 2),
        "iqr": round(iqr, 2),
        "lower_bound": round(lower_bound, 2),
        "upper_bound": round(upper_bound, 2),
        "outlier_count": round(outlier_count, 2)
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
   


    