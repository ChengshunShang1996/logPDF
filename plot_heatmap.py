import numpy as np
import matplotlib.pyplot as plt

# 样本数据
x = [1, 2, 3, 4]
y = [1, 2, 3, 4]
data = np.array([[5, 6, 7, 8],
                 [4, 3, 2, 1],
                 [9, 10, 11, 12],
                 [13, 14, 15, 16]])

# 绘制热力图
plt.imshow(data, cmap='binary', interpolation='nearest')

# 添加 x 和 y 轴的刻度
plt.xticks(np.arange(len(x)), x)
plt.yticks(np.arange(len(y)), y)

# 添加数值标签
#for i in range(len(x)):
#    for j in range(len(y)):
#        plt.text(j, i, data[i, j], ha='center', va='center', color='orange')

# 添加颜色条
plt.colorbar()

# 显示图形
plt.show()