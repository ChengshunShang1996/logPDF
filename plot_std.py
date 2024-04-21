import numpy as np
import matplotlib.pyplot as plt
import random

# 生成随机列表数量
n_values = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 150, 200, 300, 400, 500, 1000, 5000, 10000, 50000, 100000, 500000, 1000000, 2000000]
#n_values = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# 存储每个列表的标准差
std_values = []

for n in n_values:
    # 生成n个长度为20的随机列表，值在0到100之间
    random_lists = np.random.uniform(0, 100, size=(n, 20))
    #random_lists = [[np.random.uniform(0, 100) for _ in range(20)] for _ in range(n)]
    # 计算每个列表的平均值
    means = np.mean(random_lists, axis=0)
    # 计算每个列表的标准差
    std = np.std(means)
    #print(means)
    std_values.append(std)

# 绘制标准差随列表数量变化的图表
plt.plot(n_values, std_values, marker='o')
plt.xlabel('Number of Lists')
plt.ylabel('Standard Deviation')
plt.title('Standard Deviation vs Number of Lists')
plt.xscale('log')  # 使用对数尺度显示列表数量
plt.show()
