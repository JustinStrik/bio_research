import numpy as np
import tensorly as tl
from tensorly.decomposition import parafac

# Initialize the dim-d array arr with random binary values 0 and 1
# dimensions m, n, o

dimension = 3
rank = 15

# rand value of shape for each dimension
shape = [np.random.randint(2, 10) for i in range(dimension)]

A = np.random.randint(2, size=shape)

# Convert A to a floating-point tensor
A = tl.tensor(A, dtype=np.float64)

# Perform matrix factorization on matrix A with different initialization
decomposed = parafac(A, rank=rank, n_iter_max=1000, init='random')

# test the decomposition on random data
print( tl.norm(A - tl.kruskal_to_tensor(decomposed)))

# and for specific values in the array
print("The error for the specific values in the array is: ")
print(tl.norm(A[1, 2, 3] - tl.kruskal_to_tensor(decomposed)[1, 2, 3]))

# find how well the decomposition works on random specific values
for i in range(100):
    # random values for the indices
    indices = [np.random.randint(0, shape[j]) for j in range(dimension)]
    print("index: ", indices, "value: ", A[indices])
    print("decomposed value: ", tl.kruskal_to_tensor(decomposed)[indices])

    print("The error for the specific values in the array is: ")
    print(tl.norm(A[indices] - tl.kruskal_to_tensor(decomposed)[indices ]))

