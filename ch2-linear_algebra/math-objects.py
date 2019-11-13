import numpy as np

# Scalar is a single number, vector of 1 length, 1x1 sized matrix, 1x1x1 sized tensor

scalar = 1
print("Scalar :")
print(scalar)

# Vector is an array of numbers with the length of N, Nx1 sized matrix, Nx1x1 sized tensor

# This is a vector with the length of 3
vector = np.array([1, 2, 3])
print("Vector :")
print(vector)

# Matrix is an array of vectors with the size of NxN, NxNx1 sized tensor

# This is a 2x2 matrix
matrix = np.array([[1, 2], 
                   [1, 2]])
print("Matrix :")
print(matrix)

# Tensor is an array of vectors with more than two axes

# This is a 2x2x3 Sized Vector
tensor = np.array([
                   [[1, 2],
                    [3, 4]], 
                   [[1, 2],
                    [3, 4]],
                   [[1, 2],
                    [3, 4]]
                   ])

print("Tensor :")
print(tensor)