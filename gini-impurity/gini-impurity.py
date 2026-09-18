import numpy as np

def gini_impurity(y_left: list, y_right: list) -> float:
    """
    Returns the impurity as a float.
    """
    # Write code here
    def gini_score(y: list):
        n = len(y)
        if n == 0:
            return 0.0
        res = 1.0
        values = np.unique(y)
        for value in values:
            p_i = np.sum(y == value) / n
            res -= p_i**2
        return res

    n = len(y_left) + len(y_right)
    if n == 0:
        return 0.0
    return len(y_left) / n * gini_score(y_left) + len(y_right) / n * gini_score(y_right)