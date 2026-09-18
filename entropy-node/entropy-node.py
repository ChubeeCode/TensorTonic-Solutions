import numpy as np

def entropy_node(y: list[int]) -> float:
    """
    Returns the Shannon entropy as a Python float.
    """
    # Write code here
    n = len(y)
    if n == 0:
        return 0.0

    entropy = 0.0
    y = np.array(y)
    values = np.unique(y)
    for value in values:
        p_i = np.sum(value == y) / n
        entropy -= p_i * np.log2(p_i)
    return entropy
    