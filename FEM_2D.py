import numpy as np
import matplotlib.pyplot as plt
from scipy.sparse import lil_matrix, csr_matrix
from scipy.sparse.linalg import spsolve
from scipy.spatial import Delaunay

# 定义问题区域和参数
Lx, Ly = 1.0, 1.0   # 问题区域大小
Nx, Ny = 10, 10     # 网格划分数量
f = lambda x, y: 1.0  # 源项函数

# 生成网格节点
x = np.linspace(0, Lx, Nx+1)
y = np.linspace(0, Ly, Ny+1)
X, Y = np.meshgrid(x, y)
points = np.vstack((X.flatten(), Y.flatten())).T

# 三角剖分生成网格单元
tri = Delaunay(points)
elements = tri.simplices

# 定义线性形函数及其梯度
def shape_function_gradients(vertices):
    B = np.array([
        [1, vertices[0][0], vertices[0][1]],
        [1, vertices[1][0], vertices[1][1]],
        [1, vertices[2][0], vertices[2][1]]
    ])
    Area = 0.5 * np.linalg.det(B)
    C = np.linalg.inv(B)[1:3, :]
    return Area, C

# 构造全局刚度矩阵和载荷向量
N_nodes = points.shape[0]
K = lil_matrix((N_nodes, N_nodes))
F = np.zeros(N_nodes)

for element in elements:
    vertices = points[element]
    Area, C = shape_function_gradients(vertices)
    
    Ke = Area * (C.T @ C)
    Fe = np.zeros(3)
    for i in range(3):
        Fe[i] = f(vertices[i][0], vertices[i][1]) * Area / 3
    
    for i in range(3):
        for j in range(3):
            K[element[i], element[j]] += Ke[i, j]
        F[element[i]] += Fe[i]

# 施加边界条件 (Dirichlet 边界条件 u = 0)
boundary_nodes = np.where((points[:, 0] == 0) | (points[:, 0] == Lx) | (points[:, 1] == 0) | (points[:, 1] == Ly))[0]
for node in boundary_nodes:
    K[node, :] = 0
    K[node, node] = 1
    F[node] = 0

# 求解线性系统
K = K.tocsr()
u = spsolve(K, F)

# 绘制结果
U = u.reshape((Ny+1, Nx+1))

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
X, Y = np.meshgrid(x, y)
ax.plot_surface(X, Y, U, cmap='viridis')
plt.xlabel('x')
plt.ylabel('y')
ax.set_zlabel('u(x, y)')
plt.title('二维泊松方程的有限元法解')
plt.show()
