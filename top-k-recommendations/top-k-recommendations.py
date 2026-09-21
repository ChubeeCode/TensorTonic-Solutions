import numpy as np 
def top_k_recommendations(scores: list, rated_indices: list, k: int) -> list:
    """
    Returns the highest-scoring unrated item indices.
    """
    # Write code here
    unrated = [(scores[i], i) for i in range(len(scores)) if i not in rated_indices]
    unrated.sort(key=lambda pair: (-pair[0], pair[1]))
    return [idx for _, idx in unrated[:k]]
        