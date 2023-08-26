import numpy as np
import matplotlib.pyplot as plt

# 创建一个36x36的二维数组，初始值为0
depth_array = np.zeros((36, 36))

# 定义36等分的θ和φ的取值范围
theta_vec = np.linspace(0, 2 * np.pi, 36)
phi_vec = np.linspace(0, 2 * np.pi, 36)

# 定义5个向量（示例）
vectors = np.array([[1, 2, 3],
                    [2, -1, 4],
                    [-1, -3, 2],
                    [0, 1, -1],
                    [3, 0, 2]])

# 遍历每个向量，计算对应的θ和φ索引，并在数组中对应位置加1
for vector in vectors:
    x, y, z = vector
    vector_length = np.linalg.norm(vector)
    theta = np.arccos(z / vector_length)
    phi = np.arctan2(y, x)
    
    theta_index = int(theta / (2 * np.pi) * 36)
    phi_index = int(phi / (2 * np.pi) * 36)
    
    depth_array[phi_index, theta_index] += 1

# 绘制深度图
plt.imshow(depth_array, cmap='viridis', extent=[0, 2*np.pi, 0, np.pi], aspect='auto', origin='lower')
plt.colorbar(label='Depth')
plt.title('Depth Map in Spherical Coordinates')
plt.xlabel('Theta')
plt.ylabel('Phi')

plt.show()

np.savetxt('depth_array.txt', depth_array, fmt='%d', delimiter=' ')