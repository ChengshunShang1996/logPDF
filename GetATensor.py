import numpy as np

empty_tensor = np.empty((3, 3))
# 创建两个数组
vector1 = np.array([2, 4, 2])

v1_norm = np.linalg.norm(vector1)

vector1_unit = vector1 / v1_norm

# 通过数组的乘法创建二阶张量（矩阵）
tensor = np.outer(vector1_unit, vector1_unit)

empty_tensor = tensor + tensor

print("Array 1:")
print(vector1_unit)

#print("\nArray 2:")
#print(array2)

print("\nTensor (Matrix) created by array multiplication:")
print(tensor)

eigenvalues, eigenvectors = np.linalg.eig(tensor)

print("Eigenvalues:", eigenvalues)
print("Eigenvectors:", eigenvectors)
#print(empty_tensor)

n = 3  # Specify the size of the square matrix
identity_matrix = np.eye(n)

print("Identity matrix:\n", identity_matrix)

A = np.array([1, 2])
B = np.array([5, 6])

double_dot_product = np.sum(A * B)

print("Double dot product:", double_dot_product)

z = -1
x = 1
phi = np.arctan2(z, x)
print(phi)