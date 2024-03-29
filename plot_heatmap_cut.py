import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 生成示例数据
x = np.arange(3)
y = np.arange(3)
z = np.arange(3)
data = np.random.rand(3, 3, 3)

# 创建三维图形
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# 绘制三个切面
X, Y = np.meshgrid(x, y)

# 绘制 x-z 平面
ax.contourf(X-1, np.zeros_like(Y), data[:, :, 1], zdir='y', offset=0, cmap='hot')

# 绘制 y-z 平面
ax.contourf(np.zeros_like(X), Y-1, data[1, :, :], zdir='x', offset=0, cmap='hot')

# 绘制 x-y 平面
ax.contourf(X-1, Y-1, np.zeros_like(data[:, :, 1]), zdir='z', offset=0, cmap='hot')

# 设置坐标轴范围
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_zlim(-1, 1)

# 设置坐标轴标签
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()
