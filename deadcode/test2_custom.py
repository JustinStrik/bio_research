import numpy as np

def custom_matrix_factorization(A, R1, R2, iterations=1000):
    """
    Perform matrix factorization on matrix A into three matrices U, V, and W.
    
    Parameters:
    A (numpy.ndarray): The input matrix to be factorized.
    R1 (int): The rank of the first factorized matrix.
    R2 (int): The rank of the second factorized matrix.
    iterations (int): Number of iterations for optimization.
    
    Returns:
    tuple: Three factorized matrices U, V, and W.
    """
    # Initialize random matrices
    U = np.random.rand(A.shape[0], R1)
    V = np.random.rand(R1, R2)
    W = np.random.rand(R2, A.shape[1])
    
    # Optimization loop
    for _ in range(iterations):
        # Update U
        U = np.linalg.lstsq(np.dot(V, W), A.T, rcond=None)[0].T
        # Update V
        V = np.linalg.lstsq(np.dot(U.T, U), np.dot(U.T, A).dot(W.T), rcond=None)[0].T
        # Update W
        W = np.linalg.lstsq(np.dot(V.T, V), np.dot(V.T, A.T).dot(U), rcond=None)[0].T
    
    return U, V, W

# Example usage
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
R1 = 2
R2 = 2

U, V, W = custom_matrix_factorization(A, R1, R2)

print("U Matrix:\n", U)
print("V Matrix:\n", V)
print("W Matrix:\n", W)
