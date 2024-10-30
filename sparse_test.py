import numpy as np
import tensorly as tl
from tensorly.decomposition import parafac

# Example matrix with missing values (NaNs)
A = np.array([[1, 2, np.nan], [4, np.nan, 6], [7, 8, 9]])

# Create a mask for the observed values
mask = ~np.isnan(A)

# Replace NaNs with zeros (or any other value, as they will be ignored)
A[np.isnan(A)] = 0

# Perform PARAFAC decomposition with the mask
decomposed = parafac(A, rank=3, n_iter_max=100, init='random', mask=mask)

# test the decomposition on random data
print("The error for the entire array is: ")
print(tl.norm(A - tl.kruskal_to_tensor(decomposed)))
