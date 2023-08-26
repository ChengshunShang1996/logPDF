import numpy as np
import matplotlib.pyplot as plt

# 生成随机颗粒堆积数据（示例）
num_particles = 100
box_size = 10.0
particles = np.random.rand(num_particles, 3) * box_size
print(particles)

# 选择一个参考颗粒
reference_particle = particles[0]

# 计算参考颗粒与其他颗粒的距离
distances = np.linalg.norm(particles - reference_particle, axis=1)

# 设置直方图参数
num_bins = 20
max_distance = np.sqrt(3) * box_size / 2
bin_edges = np.linspace(0, max_distance, num_bins + 1)

# 计算直方图
hist, _ = np.histogram(distances, bins=bin_edges)

# 归一化直方图
bin_width = bin_edges[1] - bin_edges[0]
rdf = hist / (4 * np.pi * bin_edges[1:]**2 * bin_width * num_particles / (box_size**3))

# 绘制径向分布函数图像
print(bin_edges[1:])
plt.plot(bin_edges[1:], rdf)
plt.xlabel("Distance")
plt.ylabel("RDF")
plt.title("Radial Distribution Function")
plt.show()
