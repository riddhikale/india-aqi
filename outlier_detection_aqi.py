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
    
   


    