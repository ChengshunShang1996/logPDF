import numpy as np
import matplotlib.pyplot as plt
from scipy.sparse import lil_matrix, csr_matrix
from scipy.sparse.linalg import spsolve
from scipy.spatial import Delaunay
import time

# 定义问题区域和参数
Lx, Ly = 1.0, 1.0   # 问题区域大小
Nx, Ny = 30, 30     # 网格划分数量
f = lambda x, y: 1.0  # 源项函数

# 生成网格节点
x = np.linspace(0, Lx, Nx+1)
y = np.linspace(0, Ly, Ny+1)
X, Y = np.meshgrid(x, y)
points = np.vstack((X.flatten(), Y.flatten())).T

# 三角剖分生成网格单元
tri = Delaunay(points)
elements = tri.simplices

# FEM 实现
def fem():
    def shape_function_gradients(vertices):
        B = np.array([
            [1, vertices[0][0], vertices[0][1]],
            [1, vertices[1][0], vertices[1][1]],
            [1, vertices[2][0], vertices[2][1]]
        ])
        Area = 0.5 * np.linalg.det(B)
        C = np.linalg.inv(B)[1:3, :]
        return Area, C

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

    boundary_nodes = np.where((points[:, 0] == 0) | (points[:, 0] == Lx) | (points[:, 1] == 0) | (points[:, 1] == Ly))[0]
    for node in boundary_nodes:
        K[node, :] = 0
        K[node, node] = 1
        F[node] = 0

    K = K.tocsr()
    u = spsolve(K, F)
    return u

# VEM 实现
def vem():
    def local_stiffness(vertices):
        B = np.array([
            [1, vertices[0][0], vertices[0][1]],
            [1, vertices[1][0], vertices[1][1]],
            [1, vertices[2][0], vertices[2][1]]
        ])
        Area = 0.5 * np.linalg.det(B)
        C = np.linalg.inv(B)[1:3, :]
        Ke = Area * (C.T @ C)
        return Ke

    N_nodes = points.shape[0]
    K = lil_matrix((N_nodes, N_nodes))
    F = np.zeros(N_nodes)

    for element in elements:
        vertices = points[element]
        Ke = local_stiffness(vertices)
        Fe = np.zeros(3)
        for i in range(3):
            Fe[i] = f(vertices[i][0], vertices[i][1]) * (1/3) * np.linalg.det(np.array([
                [1, vertices[0][0], vertices[0][1]],
                [1, vertices[1][0], vertices[1][1]],
                [1, vertices[2][0], vertices[2][1]]
            ])) / 2
        for i in range(3):
            for j in range(3):
                K[element[i], element[j]] += Ke[i, j]
            F[element[i]] += Fe[i]

    boundary_nodes = np.where((points[:, 0] == 0) | (points[:, 0] == Lx) | (points[:, 1] == 0) | (points[:, 1] == Ly))[0]
    for node in boundary_nodes:
        K[node, :] = 0
        K[node, node] = 1
        F[node] = 0

    K = K.tocsr()
    u = spsolve(K, F)
    return u

# 运行 FEM 和 VEM 并计时
start_fem = time.time()
u_fem = fem()
end_fem = time.time()
print(f"FEM 运行时间: {end_fem - start_fem:.4f} 秒")

start_vem = time.time()
u_vem = vem()
end_vem = time.time()
print(f"VEM 运行时间: {end_vem - start_vem:.4f} 秒")

# 绘制 FEM 结果
U_fem = u_fem.reshape((Ny+1, Nx+1))
fig_fem = plt.figure()
ax_fem = fig_fem.add_subplot(111, projection='3d')
X, Y = np.meshgrid(x, y)
ax_fem.plot_surface(X, Y, U_fem, cmap='viridis')
plt.xlabel('x')
plt.ylabel('y')
ax_fem.set_zlabel('u(x, y)')
plt.title('FEM: 二维泊松方程解')

# 绘制 VEM 结果
U_vem = u_vem.reshape((Ny+1, Nx+1))
fig_vem = plt.figure()
ax_vem = fig_vem.add_subplot(111, projection='3d')
X, Y = np.meshgrid(x, y)
ax_vem.plot_surface(X, Y, U_vem, cmap='viridis')
plt.xlabel('x')
plt.ylabel('y')
ax_vem.set_zlabel('u(x, y)')
plt.title('VEM: 二维泊松方程解')

plt.show()
