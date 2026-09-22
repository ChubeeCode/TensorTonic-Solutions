import numpy as np

def calculate_eigenvalues(matrix: list) -> np.ndarray:
    """
    Returns a sorted NumPy array of real eigenvalues.
    """
    # Write code here
    X = np.asarray(matrix)
    eigen_values, eigen_vectors = np.linalg.eig(X)
    eigen_values.sort()
    return eigen_values