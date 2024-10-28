import numpy as np

arr = [] # 3d array, binary values. m x n x o

def initialize():
    # Read the file and initialize the array
    pass

def initialize_arr_random(m, n, o):
    # Initialize the 3d array arr with random binary values 0 and 1
    arr = np.random.randint(2, size=(m, n, o))
    return arr

def get_error_ijk(arr, i, j, k, r):
    # Calculate the error for the i,j,k position
    # error ijk = x_i,j,k - sum(from(f=1 to r) (a(f)*b(f)*c(f))
    # r in this instance is the number of time steps ?/

    # Get the value of x_i,j,k
    x = arr[i][j][k]

    # Get the sum of the product of a, b, c
    sum_abc = 0
    for f in range(1, r+1):
        sum_abc += arr[i][j][k-f]
    return (x - sum_abc)**2

# implement adam optimizer for the error function

# parameter definitions: 
# x: the value of x_i,j,k; y: the value of a(f); z: the value of b(f); 
# arr: the 3d array; 
# i, j, k: the position in the 3d array; r: the number of time steps

def adam_optimizer(x, y, z, arr, i, j, k, r, learning_rate=0.001, beta1=0.9, beta2=0.999, epsilon=1e-8, num_iterations=1000):
    # Initialize m and v
    m = np.zeros_like(x)
    v = np.zeros_like(x)
    o = 0

    for _ in range(num_iterations):
        o += 1
        # Compute gradients (this is a placeholder, replace with actual gradient computation)
        grad = np.gradient(get_error_ijk(arr, i, j, k, r))

        # Update biased first moment estimate
        m = beta1 * m + (1 - beta1) * grad

        # Update biased second raw moment estimate
        v = beta2 * v + (1 - beta2) * (grad ** 2)

        # Compute bias-corrected first moment estimate
        m_hat = m / (1 - beta1 ** o)

        # Compute bias-corrected second raw moment estimate
        v_hat = v / (1 - beta2 ** o)

        # Update parameters
        x -= learning_rate * m_hat / (np.sqrt(v_hat) + epsilon)

    return x

# sum from 1=1 to r (a(f)*b(f)*c(f))
#FN1
def get_estimated_sum_value(A, B, C):
    # Get the sum of the product of a, b, c
    # len A is going to be r
    sum_abc = 0
    # a[0] * b[0] * c[0] + a[1] * b[1] * c[1] + a[2] * b[2] * c[2]...etc
    for f in range(1, len(A)):
        sum_abc += A[f] * B[f] * C[f]

    return sum_abc

    
# def sum_at_Ai_Bj_Ck(A, B, C, i, j, k):
#     # sum from 1=1 to r (a(f)*b(f)*c(f))
#     sum_abc = 0
#     # a[0] * b[0] * c[0] + a[1] * b[1] * c[1] + a[2] * b[2] * c[2]...etc
#      # for each combination of a[0], b[0], c[0], a[0], b[0], c[1]...etc
#     for f in range(1, len(A)):
#         sum_abc += A[f] * B[f] * C[f]
#     return sum

# # def get_all_com
# def get_sum_at_m_n_o(A, B, C, m, n, o):
#     pass


def get_approx_x_ijk(A, B, C, i, j, k): # , r
    # Get the approximate value of x_ijk

    a, b, c = A[i], B[j], C[k] # get necessary rows from A, B, C
    return np.dot(np.dot(a, b), c) # sum_abc

def get_error_ijk_at_r(arr, i, j, k, A, B, C, r):
    # norm squared of (error ijk - x_ijk)^2 (norm of 3d array)
    # x_ijk is the actual value of the 3d array at position i, j, k
    approximated_x = get_approx_x_ijk(arr, i, j, k, r)
    actual_x = arr[i][j][k]
    np.linalg.norm(approximated_x - actual_x) ** 2 # norm squared of the difference between the approximated value and the actual value

#FN4
def get_total_error(error_arr, regularization, gamma):
    # error_arr is 3d array of error values at each i, j, k position
    # error array total
    # gamma array is the regularization parameter, how much you care about the regularization term
    return error_arr.sum() + gamma * regularization # = total error

def get_total_loss(arr, A, B, C, r, regularization, gamma):
    # Get the total loss of the error function
    # error_arr is the 3d array of error values at each i, j, k position
    # regularization is the regularization term
    # gamma is the regularization parameter, how much you care about the regularization term

    error_arr = np.zeros_like(arr)
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            for k in range(len(arr[0][0])):
                error_arr[i][j][k] = get_error_ijk_at_r(arr, i, j, k, A, B, C, r)

    return get_total_error(error_arr, regularization, gamma)

if __name__ == "__main__":
    # m, n, o correspond to the dimensions i, j, k of the 3d array
    m = 3
    n = 4
    o = 5
    # x is a 3d array of size m x n x o, with random binary values
    # arr = x
    arr = initialize_arr_random(m, n, o)
    # val = adam_optimizer(0, 2, 0, arr, 1, 1, 1, 3)
    # print(val)

    # different tests will have different rank values
    rank = 3


    # A is a 2d array of size m x r, with random values # changed in opt to minimize error function
    A = np.random.rand(m, 3)
    # B is a 2d array of size n x r, with random values
    B = np.random.rand(n, 3)
    # C is a 2d array of size o x r, with random values
    C = np.random.rand(o, 3)

    # minimize the error function


