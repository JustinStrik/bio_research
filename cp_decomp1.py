import numpy as np
import tensorly as tl
from tensorly.decomposition import parafac, non_negative_parafac
from read_adj_matrix_input import read_adj_matrix_input, test_mod, read_edge_list_input, get_full_matrix
from get_adj_matrix_files import get_adj_matrix_files, get_edge_list_files
import sys
import sparse
import scipy.sparse as sp
from check_sheet import check_against_test_sheet

global execution_report_file # name later when we know the sheet index (x,y)

# constants
TOTAL_GENES = 1432
TOTAL_WEEKS = 20
TOTAL_MICE = 20
DEBUG_MAX = 2

# tl.kruskal_to_tensor is a function in the TensorLy library used to reconstruct a full tensor from its Kruskal decomposition (CP decomposition).
# pass in both the original matrix and the decomposed matrix
def test_single_value_accuracy(A, decomposed):
    # test the decomposition on random data
    print("The error for the entire array is: ")
    print(tl.norm(A - tl.kruskal_to_tensor(decomposed)))
   
    # redo print norm difference with boolean operator
    # print(tl.norm(A ^ tl.kruskal_to_tensor(decomposed)))

    # find how well the decomposition works on random specific values
    for i in range(10):
        # random values for the indices
        # i = np.random.randint(dimensions[0])
        # j = np.random.randint(dimensions[1])
        i = np.random.randint(TOTAL_GENES)
        j = np.random.randint(TOTAL_GENES * TOTAL_MICE)

        # print the error for the specific values in the array
        print("The error for", i, j, "is: ")
        print(tl.norm(A[i, j] - tl.kruskal_to_tensor(decomposed)[i, j]))
        print("The actual value is: ")
        print(A[i, j])

if __name__ == "__main__":

    # files = get_adj_matrix_files()
    files = get_edge_list_files()
    # A = np.zeros((TOTAL_GENES, TOTAL_GENES * len(TOTAL_MICE), TOTAL_WEEKS))
    # init to have values be -1
    
    # each sheet is a mouse at a time
    # each row is an edge connecting two genes

    # get matrix from edge list for each mouse
    A, mask = get_full_matrix(files, DEBUG_MAX)

    # if cmd line input
    if len(sys.argv) > 1:
        RANK = int(sys.argv[1])
    else:
        RANK = 10

    # check if mask and A are the same shape
    print("mask shape")
    print(mask.shape)
    print("A shape")
    print(A.shape)

    # change A from sparse to dense using todense()
    A = A.todense()
    
    # Perform matrix factorization on matrix A with different initialization
    decomposed = parafac(A, rank=RANK, n_iter_max=2, init='svd', mask=mask) # if random, risk of being singular
    decomposed_array = tl.kruskal_to_tensor(decomposed)

    focused_array = decomposed_array[0]

    check_against_test_sheet(A, decomposed_array)


    # make sparse tensor
    # A = sparse.COO(A)

    # # output A to a file as tuples of 3d coordinates
    # with open("results_mega_matrix.csv", "w") as f:
    #     # find positions of non-zero values
    #     non_zero = np.nonzero(A)
    #     for i in range(len(non_zero[0])):
    #         # the data is int
    #         f.write(str(non_zero[0][i]) + "," + str(non_zero[1][i]) + "," + str(A[non_zero[0][i], non_zero[1][i]]) + "\n")


    # make A sparse tensor !!!
    # A = np.zeros((TOTAL_GENES, TOTAL_GENES * len(mouse_matrices), TOTAL_WEEKS))

    # mouse i will start it's matrix at i * TOTAL_GENES
    # the depth of the tensor is the number of weeks
    # for i, (mouse_id, matrices) in enumerate(mouse_matrices.items()):
    #     for week, matrix in matrices:
    #         # put the mouse matrices where they belong in the tensor A
    #         # remember mouse matrices are sparse
    #         for val in matrix:
    #             A[val[0], i * TOTAL_GENES + val[1], week] = val[2]


    # A = read_adj_matrix_input("results_adj_COHP_44940_480__F_B_w0.csv")
    # dimensions = A.shape

    # Perform matrix factorization on matrix A with different initialization
    decomposed = parafac(A, rank=10, n_iter_max=20, init='svd') # if random, risk of being singular


    test_single_value_accuracy(A, decomposed)