import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

# 生成随机数据
num_points = 100
x = np.random.rand(num_points)
ys = np.random.rand(num_points)

# 使用不重复的颜色绘制数据点
#cmap = get_cmap('tab10')  # 选择一个颜色映射，这里选择了 'tab10' colormap
#indices = np.arange(num_points)  # 生成一系列不同的整数
#np.random.shuffle(indices)  # 随机打乱顺序以确保颜色不重复
#colors = cmap(indices)  # 根据索引获取不重复的颜色

colors = cm.rainbow(np.linspace(0, 1, num_points))
#for y, c in zip(ys, colors):
#    plt.scatter(x, y, color=c)

# 绘制数据点
plt.scatter(x, ys, color=colors)

# 显示图例
plt.colorbar()

# 显示图形
plt.show()