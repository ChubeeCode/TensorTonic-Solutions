import numpy as np

def covariance_matrix(X: list) -> np.ndarray:
    """
    Returns the covariance matrix as a NumPy array.
    """
    # Write code here
    N = len(X)
    X = np.asarray(X)
    X_mean = np.mean(X, axis = 0)
    X_centered = X - X_mean
    return np.matmul(X_centered.T, X_centered) / (N - 1)