import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# 设定平均值和标准差
mean = 2000
stddev = 20

# 生成一组 x 值，覆盖正态分布的范围
x = np.linspace(mean - 3*stddev, mean + 3*stddev, 100)

# 计算对应于这些 x 值的概率密度函数（PDF）值
pdf = norm.pdf(x, mean, stddev)

# 绘制正态分布曲线
plt.plot(x, pdf, label='Normal Distribution (mean=2000, stddev=20)')
plt.xlabel('Value')
plt.ylabel('Probability Density')
plt.title('Normal Distribution')
plt.legend()
plt.grid(True)
plt.show()