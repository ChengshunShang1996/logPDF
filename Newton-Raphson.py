import numpy as np
import matplotlib.pyplot as plt

# 定义一个示例的非线性方程
def f(x):
    return x**3 - 2*x**2 + 2

# 定义方程的导数
def df(x):
    return 3*x**2 - 4*x

# 牛顿-拉普森迭代
def newton_raphson(initial_guess, tol=1e-6, max_iter=150):
    x = initial_guess
    x_values = [x]
    
    for i in range(max_iter):
        x_new = x - f(x) / df(x)
        x_values.append(x_new)
        
        if abs(x_new - x) < tol:
            break
        
        x = x_new
    
    return x_values

# 初始猜测解
initial_guess = 1.5

# 执行迭代
x_values = newton_raphson(initial_guess)

# 绘制收敛图
plt.figure(figsize=(10, 6))
plt.plot(x_values, marker='o', linestyle='-')
plt.xlabel('Iteration')
plt.ylabel('Approximate Solution')
plt.title('Newton-Raphson Iteration Convergence')
plt.grid(True)
plt.show()
