import numpy as np

def pca_projection(X: list, k: int) -> list:
    """
    Returns the centered data projected onto the top components.
    """
    # Write code here
    X = np.asarray(X)
    X_mean = np.mean(X, axis = 0)
    X_centered = X - X_mean
    cov_matrix = np.cov(X_centered, rowvar = False)
    eigent_values, eigent_vectors = np.linalg.eig(cov_matrix)
    sorted_indices = np.argsort(eigent_values)[::-1]
    eigent_values = eigent_values[sorted_indices]
    eigent_vectors = eigent_vectors[:, sorted_indices]
    components = eigent_vectors[:, :k]
    return np.dot(X_centered, components)