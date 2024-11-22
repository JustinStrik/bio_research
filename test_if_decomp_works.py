# import parafac from tensorly
from tensorly.decomposition import parafac
from tensorly import kruskal_to_tensor
import numpy as np

# create 3x3x3 tensor of ones
tensor = np.ones((3, 3, 3))

# decompose tensor into 3 factors
factors = parafac(tensor, rank=20, init='random', n_iter_max=10)

# create tensor2 that has a 5 in the middle, and ones elsewhere
tensor2 = np.ones((3, 3, 3))
tensor2[1, 1, 1] = 5

# decompose tensor2 into 3 factors
factors2 = parafac(tensor2, rank=20, init='random', n_iter_max=100)

# see if middle factor is 5, use kruskal_to_tensor
reconstructed_tensor2 = kruskal_to_tensor(factors2)
print(reconstructed_tensor2[1, 1, 1])  # should print 5

# see if middle factor is 1, use kruskal_to_tensor
reconstructed_tensor = kruskal_to_tensor(factors)
print(reconstructed_tensor[1, 1, 1])  # should print 1

# now mask the middle factor of tensor2
mask = np.ones((3, 3, 3))
mask[1, 1, 1] = 0

# mask the middle factor of tensor2
factors2_withmask = parafac(tensor2 * mask, rank=20, init='random', n_iter_max=100)

# see if middle factor is 1, use kruskal_to_tensor
reconstructed_tensor2_withmask = kruskal_to_tensor(factors2_withmask)
print(reconstructed_tensor2_withmask[1, 1, 1])  # should print 1

# create a 100x100x100 tensor of ones
tensor3 = np.ones((100, 100, 100))

# make one 100x100 slice of tensor3 all 5s
tensor3[0, :, :] = 5

# make a mask to cover the 5s 100x100 slice
mask2 = np.ones((100, 100, 100))
mask2[0, :, :] = 0

# decompose tensor3 with the mask
factors3_withmask = parafac(tensor3 * mask2, rank=20, init='random', n_iter_max=100)

# see if the 100x100 slice is all 1s
reconstructed_tensor3_withmask = kruskal_to_tensor(factors3_withmask)
print(reconstructed_tensor3_withmask[0, :, :])  # should print 1s



