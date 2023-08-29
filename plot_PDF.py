import matplotlib.pyplot as plt
import numpy as np

# 生成随机整数数组，范围从1到100，共生成1000个随机整数
random_integers = np.random.randint(1, 101, size=1000)

# 计算每个整数的概率分布
hist, bins = np.histogram(random_integers, bins=np.arange(1, 102, 5), density=True)
bin_centers = (bins[:-1] + bins[1:]) / 2

# 绘制概率分布图
plt.plot(bin_centers, hist, '-o')
plt.xlabel('Integer')
plt.ylabel('Probability')
plt.title('Probability Distribution of Random Integers from 1 to 100')
plt.xticks(np.arange(0, 101, step=10))  # 设置X轴刻度
plt.grid(True)
plt.show()