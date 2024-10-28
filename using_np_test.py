import numpy as np
from sklearn.decomposition import NMF

def matrix_factorization(A, n, R):
    """
    Perform matrix factorization on matrix A into n matrices of rank R.
    
    Parameters:
    A (numpy.ndarray): The input matrix to be factorized.
    n (int): The number of matrices to factorize into.
    R (int): The rank of the factorized matrices.
    
    Returns:
    list: A list of n factorized matrices.
    """
    # Initialize NMF model
    model = NMF(n_components=R, init='random', random_state=0)
    
    # Fit the model and transform the data
    W = model.fit_transform(A)
    H = model.components_
    
    # Create a list to store the factorized matrices
    factorized_matrices = []
    
    # Split W into n matrices of rank R
    for i in range(n):
        factorized_matrices.append(W[:, i*R:(i+1)*R])
    
    return factorized_matrices, H

# Example usage
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
n = 2
R = 2

factorized_matrices, H = matrix_factorization(A, n, R)

print("Factorized Matrices:")
for i, matrix in enumerate(factorized_matrices):
    print(f"Matrix {i+1}:\n{matrix}")

print("H Matrix:\n", H)
