import numpy as np

def random_forest_vote(predictions: list) -> list:
    """
    Returns the majority-vote label for every sample.
    """
    # Write code here
    n = len(predictions[0])
    results = []
    for i in range(n):
        sample_preds = [tree[i] for tree in predictions]
        values = set(sample_preds)
        pairs = sorted(
            (-1 * np.sum(np.array(sample_preds) == value), value)
            for value in values
        )
        results.append(pairs[0][1])
    return results
        