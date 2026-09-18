import numpy as np

def information_gain(y: list, split_mask: list) -> float:
    """
    Returns the information gain as a float.
    """

    def H(y):
        n = len(y)
        if n == 0:
            return 0

        res = 0.0
        values = np.unique(y)
        for value in values:
            p_i = np.sum(value == y) / n
            res -= p_i * np.log2(p_i)
            
        return res
        
    
    n = len(y)
    y_lf = [y[i] for i in range(n) if split_mask[i] == True]
    y_rg = [y[i] for i in range(n) if split_mask[i] == False]
    return H(y) - (len(y_lf) / n * H(y_lf) + len(y_rg) / n * H(y_rg))
    