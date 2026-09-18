import numpy as np

def _sigmoid(z: np.ndarray) -> np.ndarray:
    """
    Returns elementwise sigmoid values.
    """
    return np.where(z >= 0, 1/(1+np.exp(-z)), np.exp(z)/(1+np.exp(z)))

def train_logistic_regression(X: np.ndarray, y: np.ndarray, lr: float = 0.1, steps: int = 1000) -> tuple[np.ndarray, float]:
    """
    Returns the trained weights and bias as (w, b).
    """
    # Write code here
    D = len(X[0])
    n = len(X)
    w, b = np.zeros(D), 0.0
    for _ in range(steps):
        f_wb = _sigmoid(np.matmul(X, w) + b)
        for j in range(D):
            w[j] -= lr * (1 / n * np.dot(f_wb - y, X[:, j]))
        b -= lr * (1 / n * np.sum(f_wb - y))

    return w, b