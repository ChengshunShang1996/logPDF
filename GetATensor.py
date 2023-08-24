import numpy as np

empty_tensor = np.empty((3, 3))
# 创建两个数组
array1 = np.array([1, 2, 3])

array2 = np.array([-1, -2, -3])

# 通过数组的乘法创建二阶张量（矩阵）
tensor = np.outer(array1, array2)

empty_tensor = tensor + tensor

print("Array 1:")
print(array1)

print("\nArray 2:")
print(array2)

print("\nTensor (Matrix) created by array multiplication:")
print(tensor)

eigenvalues, eigenvectors = np.linalg.eig(tensor)

print("Eigenvalues:", eigenvalues)
print("Eigenvectors:", eigenvectors)
#print(empty_tensor)