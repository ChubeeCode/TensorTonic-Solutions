import numpy as np

def pca_projection(X: list, k: int) -> list:
    """
    Returns the centered data projected onto the top components.
    """
    # Write code here
    X = np.asarray(X)
    X_centered = X - np.mean(X, axis = 0)
    cov_matrix = np.cov(X_centered, rowvar = False)
    eigen_values, eigen_vectors = np.linalg.eig(cov_matrix)
    sorted_indicies = np.argsort(eigen_values)[::-1]
    eigen_values = eigen_values[sorted_indicies]
    eigen_vectors = eigen_vectors[:, sorted_indicies]
    components = eigen_vectors[:, :k]
    return np.matmul(X_centered, components)