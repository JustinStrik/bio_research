import numpy as np
import tensorly as tl
from tensorly.decomposition import parafac
from read_adj_matrix_input import read_adj_matrix_input

# tl.kruskal_to_tensor is a function in the TensorLy library used to reconstruct a full tensor from its Kruskal decomposition (CP decomposition).

def test_single_value_accuracy(decomposed):
    # test the decomposition on random data
    print("The error for the entire array is: ")
    print(tl.norm(A - tl.kruskal_to_tensor(decomposed)))

    # find how well the decomposition works on random specific values
    for i in range(100):
        # random values for the indices
        i = np.random.randint(dimensions[0])
        j = np.random.randint(dimensions[1])

        # print the error for the specific values in the array
        print("The error for", i, j, "is: ")
        print(tl.norm(A[i, j] - tl.kruskal_to_tensor(decomposed)[i, j]))
        print("The actual value is: ")
        print(A[i, j])

# dimension = 3
rank = 2

A = read_adj_matrix_input("results_adj_COHP_44940_480__F_B_w0.csv")
dimensions = A.shape

# Perform matrix factorization on matrix A with different initialization
decomposed = parafac(A, rank=rank, n_iter_max=1000, init='svd') # if random, risk of being singular

# test the decomposition on random data
print( tl.norm(A - tl.kruskal_to_tensor(decomposed)))

# and for specific values in the array
print("The error for the specific values in the array is: ")
print(tl.norm(A[1, 2] - tl.kruskal_to_tensor(decomposed)[1, 2]))

# find how well the decomposition works on random specific values
for i in range(100):
    # random values for the indices
    i = np.random.randint(dimensions[0])
    j = np.random.randint(dimensions[1])

    # print the error for the specific values in the array
    print("The error for", i, j, "is: ")
    print(tl.norm(A[i, j] - tl.kruskal_to_tensor(decomposed)[i, j]))
    print("The actual value is: ")
    print(A[i, j])


