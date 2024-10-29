import numpy as np
import tensorly as tl
from tensorly.decomposition import parafac
from read_adj_matrix_input import read_adj_matrix_input
import sys

# tl.kruskal_to_tensor is a function in the TensorLy library used to reconstruct a full tensor from its Kruskal decomposition (CP decomposition).

# pass in both the original matrix and the decomposed matrix
def test_single_value_accuracy(A, decomposed):
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

if __name__ == "__main__":

    A = read_adj_matrix_input("results_adj_COHP_44940_480__F_B_w0.csv")
    dimensions = A.shape

    # if cmd line input
    if len(sys.argv) > 1:
        rank = int(sys.argv[1])
    else:
        rank = 10

    # Perform matrix factorization on matrix A with different initialization
    decomposed = parafac(A, rank=rank, n_iter_max=1000, init='svd') # if random, risk of being singular

    test_single_value_accuracy(A, decomposed)

