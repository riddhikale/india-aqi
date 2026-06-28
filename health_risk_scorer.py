"""

health_risk_scorer_stub.py

Feature pipeline for the Air Quality Health Risk Scorer.

-----------------------------------------------
IMPUTATION:
  PM2.5 → median  (mean-median gap = 9.11, right skewed)
  PM10  → median  (mean-median gap = 25.64, strongly skewed)
  NO2   → mean    (gap = 6.49, roughly symmetric)
  SO2   → median  (skewness = 3.46, extreme skew)

TRANSFORMS (before modelling):
  PM2.5 → np.log()
  PM10  → np.log()
  NO2   → np.log()
  SO2   → np.log()  (min = 0.5, no zeros, safe)

FEATURES TO DROP:
  spm → correlated 0.80 with rspm (multicollinearity)

FEATURES TO ADD:
  is_extreme_event → 1 for October–November readings
                     0 otherwise

STANDARDISATION:
  Compute std dev per city, not nationally.
  Bhopal and Delhi have very different volatility profiles.
"""