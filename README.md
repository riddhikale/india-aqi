# India Air Quality — Exploratory Data Analysis

## Dataset

India Air Quality Data — 435,000+ rows across Indian cities.
Source: Kaggle — shrutibhargava94/india-air-quality-data

## What I built

- central_tendency_aqi.py — mean, median, mode from scratch
- spread_metrics.py — variance and std deviation from scratch
- outlier_detection_aqi.py — IQR outlier detection from scratch
- eda_india_aqi.ipynb — full EDA notebook
- visualisation_gallery_aqi.ipynb — heatmaps, charts, null matrix

## Key findings

- Delhi has the highest average PM2.5 (95.11 µg/m³)
- PM2.5 is missing for 97.86% of the national dataset —
  most cities had no sensors
- Bhopal is the most volatile city (std dev 64.46) but
  Delhi is consistently worse on average
- All four pollutants are right-skewed — need log transform
- rspm and spm are 0.80 correlated — multicollinearity flag
