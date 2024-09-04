import cProfile
import numpy as np
from io import StringIO
import pstats

def matrix_operations_python_lists():
    # Define matrices using Python lists
    A = [
        [3.7827, 3.3454, 3.2341],
        [2.2122, 3.5678, 3.9087],
        [1.1234, 2.8934, 5.9087]
    ]

    B = [
        [3.1234, 3.0987, 3.1234],
        [2.1111, 3.2222, 3.3333],
        [1.0987, 1.3456, 5.1234]
    ]

    C = [
        [3.1243, 3.0989, 3.1256],
        [2.6721, 3.6785, 3.9017],
        [1.1254, 2.8956, 5.9187]
    ]

    # Matrix addition using Python lists
    def add_matrices(mat1, mat2):
        return [[mat1[i][j] + mat2[i][j] for j in range(len(mat1[0]))] for i in range(len(mat1))]

    # Matrix subtraction using Python lists
    def subtract_matrices(mat1, mat2):
        return [[mat1[i][j] - mat2[i][j] for j in range(len(mat1[0]))] for i in range(len(mat1))]

    # Perform operations
    print("Matrix Addition of A and B:")
    result_add_ab = add_matrices(A, B)
    for row in result_add_ab:
        print(row)

    print("\nMatrix Subtraction of A and B:")
    result_sub_ab = subtract_matrices(A, B)
    for row in result_sub_ab:
        print(row)

def matrix_operations_numpy():
    # Define matrices using NumPy
    A = np.array([
        [3.7827, 3.3454, 3.2341],
        [2.2122, 3.5678, 3.9087],
        [1.1234, 2.8934, 5.9087]
    ])

    B = np.array([
        [3.1234, 3.0987, 3.1234],
        [2.1111, 3.2222, 3.3333],
        [1.0987, 1.3456, 5.1234]
    ])

    C = np.array([
        [3.1243, 3.0989, 3.1256],
        [2.6721, 3.6785, 3.9017],
        [1.1254, 2.8956, 5.9187]
    ])

    # Perform operations
    print("\nMatrix Addition of A and B (NumPy):")
    result_add_ab = A + B
    print(result_add_ab)

    print("\nMatrix Subtraction of A and B (NumPy):")
    result_sub_ab = A - B
    print(result_sub_ab)

def profile_code():
    pr = cProfile.Profile()
    pr.enable()
    
    # Run both matrix operations
    matrix_operations_python_lists()
    matrix_operations_numpy()
    
    pr.disable()
    s = StringIO()
    sortby = 'cumulative'
    ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
    ps.print_stats()
    print("\nProfiling Results:")
    print(s.getvalue())

if __name__ == "__main__":
    profile_code()
