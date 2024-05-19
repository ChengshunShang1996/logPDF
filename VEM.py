import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spla

# 定义一维问题的参数
L = 1.0        # 问题区域长度
N = 10         # 网格单元数量
f = lambda x: 1.0  # 源项函数

# 生成网格节点
x = np.linspace(0, L, N+1)
h = L / N  # 网格大小

# 构造局部刚度矩阵（虚拟单元）
def local_stiffness():
    return np.array([[1, -1], [-1, 1]]) / h

# 构造全局刚度矩阵和载荷向量
K = sp.lil_matrix((N+1, N+1))
F = np.zeros(N+1)

for i in range(N):
    Ke = local_stiffness()
    Fe = np.array([f(x[i]) * h / 2, f(x[i+1]) * h / 2])
    
    K[i:i+2, i:i+2] += Ke
    F[i:i+2] += Fe

# 施加边界条件 (u(0) = 0, u(L) = 0)
K = K.tocsr()
K[0, 0] = 1.0
K[0, 1:] = 0.0
K[1:, 0] = 0.0

K[-1, -1] = 1.0
K[-1, :-1] = 0.0
K[:-1, -1] = 0.0

F[0] = 0.0
F[-1] = 0.0

# 求解线性系统
u = spla.spsolve(K, F)

# 打印结果
print("节点坐标:", x)
print("位移解:", u)

# 可视化结果
import matplotlib.pyplot as plt

plt.plot(x, u, '-o', label='位移解')
plt.xlabel('x')
plt.ylabel('u(x)')
plt.title('一维问题的虚拟单元法解')
plt.legend()
plt.show()
