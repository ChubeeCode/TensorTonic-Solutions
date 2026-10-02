import math
import numpy

def xavier_initialization(W: list, fan_in: int, fan_out: int) -> list:
    """
    Returns the weights mapped to the Xavier uniform range.
    """
    # Write code here
    W = np.asarray(W)
    L = np.sqrt(6. / (fan_in + fan_out))
    W = W * (2 * L) - L
    return W