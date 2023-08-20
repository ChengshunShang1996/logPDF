import numpy as np

# 创建一个对称矩阵（二阶张量）
tensor = np.array([[2, 2, 2],
                   [2, 2, 2],
                   [2, 2, 2]])

# 求解特征值和特征向量
eigenvalues, eigenvectors = np.linalg.eig(tensor)

print("Eigenvalues:", eigenvalues)
print("Eigenvectors:", eigenvectors)