import numpy as np

def linear_regression_closed_form(X: list, y: list) -> list:
    """
    Returns the optimal weight vector as a list.
    """
    # Write code here
    X = np.asarray(X)
    y = np.asarray(y)
    return np.matmul(np.matmul(np.linalg.inv(np.matmul(X.T, X)), X.T), y)