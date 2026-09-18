import numpy as np

def cross_entropy_loss(y_true: list[int], y_pred: list[list[float]]) -> float:
    """
    Returns the mean multiclass cross-entropy loss as a Python float.
    """
    # Write code here
    loss = 0.0
    n = len(y_true)
    for i in range(n):
        loss -= np.log(y_pred[i][y_true[i]])

    return loss / n