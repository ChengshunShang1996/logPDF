import os
import numpy as np
import matplotlib.pyplot as plt
import math


plt.figure(1)
#plt.title('Hertz model')  
plt.xlabel('R increase ratio / %')  
plt.ylabel('Porosity change ratio / %')   

r_cylinder = 0.05
h_cylinder = 0.1
ini_porosity = 0.359
volume_particle = math.pi * r_cylinder * r_cylinder * h_cylinder * (1.0 - ini_porosity)

X = [i/10 for i in range(0, 11)] 
Y = []
for x in X:
    r = r_cylinder * (1 + x * 0.01)
    volume_cylinder = math.pi * r * r * h_cylinder
    current_porosity = 1.0 - (volume_particle / volume_cylinder)
    Y.append((current_porosity - ini_porosity) / ini_porosity * 100) 
#my_label = '$\mu$ =' + str(mu) + ', $\sigma$ =' + str(sigma)
plt.plot(X, Y, 'o-')

#plt.axhline(y=7.12776, color='red', linestyle='-')


#plt.xlim((0, 3))
#plt.ylim((0, 2))
plt.legend(prop={'size': 10})
plt.show()  