import numpy as np

def compute_central_tendency(data, label):
    """
    Compute mean, median, and mode from scratch using numpy.
    No pandas .mean() or .median() shortcuts.
    
    data  : numpy array of float values (NaNs already removed)
    label : string name for printing
    """

 # ── MEAN ──────────────────────────────────────────────
    # Formula: sum of all values divided by count
    mean_val = np.sum(data) / len(data)

# Verify against numpy's built in
    assert abs(mean_val - np.mean(data)) < 0.001, "Mean mismatch"