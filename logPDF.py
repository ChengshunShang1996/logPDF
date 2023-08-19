import os
import numpy as np
import matplotlib.pyplot as plt
import math


#plt.figure(1)
#plt.title('Hertz model')  
#plt.xlabel('$d_i$')  
#plt.ylabel('Probability density function (PDF)')   

sigma_list = [0.1, 0.2, 0.5, 1, 2]
mu = 0.5
X = [i/10000 for i in range(1, 50000)]
for sigma in sigma_list:   
    Y = []
    for x in X:
        Y.append(1/(math.sqrt(2* math.pi) * sigma * x) * (math.e ** (-0.5*((math.log(x) - mu) / sigma)**2))) 
    my_label = '$\mu$ =' + str(mu) + ', $\sigma$ =' + str(sigma)
    Y_i = []
    y_0 = 0.0
    for y in Y:
        y_0 += y/10000
        Y_i.append(y_0)
    #plt.plot(X, Y, '-', label = my_label)


plt.figure(2)
#plt.title('Hertz model')  
plt.xlabel('$d_i$')  
plt.ylabel('Truncated coefficient $C_t$')   

 
sigma_list = [0.1, 0.2, 0.3, 0.4, 0.5]
mu = 0
x_truncted_list = [i/10 for i in range(1, 31)]
X = [i/10000 for i in range(1, 35000)]
for sigma in sigma_list:   
    Y = []
    for x in X:
        Y.append(1/(math.sqrt(2* math.pi) * sigma * x) * (math.e ** (-0.5*((math.log(x) - mu) / sigma)**2))) 
    my_label = '$\mu$ =' + str(mu) + ', $\sigma$ =' + str(sigma)
    alpha_truncted_list = []
    for x_truncted in x_truncted_list:
        for x in X:
            if x > x_truncted:
                x_truncted_id = X.index(x)
                break
        y_0 = 0.0
        start_plus = False
        for y in Y:
            if not start_plus:
                if Y.index(y) >= x_truncted_id:
                    start_plus = True
            if start_plus:
                y_0 += y/10000
        alpha_truncted_list.append(y_0)
        print('finish ' + str(x_truncted))
    plt.plot(x_truncted_list, alpha_truncted_list, '-o', label = my_label)

#plt.axhline(y=7.12776, color='red', linestyle='-')


#plt.xlim((0, 3))
#plt.ylim((0, 2))
plt.legend(prop={'size': 10})
plt.show()  

        