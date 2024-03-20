import math
import matplotlib.pyplot as plt

def GammaForHertzThornton(e):
    if e < 0.001:
        e = 0.001

    if e > 0.999:
        return 0.0

    h1  = -6.918798
    h2  = -16.41105
    h3  =  146.8049
    h4  = -796.4559
    h5  =  2928.711
    h6  = -7206.864
    h7  =  11494.29
    h8  = -11342.18
    h9  =  6276.757
    h10 = -1489.915

    alpha = e*(h1+e*(h2+e*(h3+e*(h4+e*(h5+e*(h6+e*(h7+e*(h8+e*(h9+e*h10)))))))))

    return math.sqrt(1.0/(1.0 - (1.0+e)*(1.0+e) * math.exp(alpha)) - 1.0)

e_list = []
gamma_list = []
for e in range(1, 1001):
    e = e/1000
    e_list.append(e)
    gamma_list.append(GammaForHertzThornton(e))

plt.plot(e_list, gamma_list, '-o')
plt.show()

i = 0
for e in e_list:
    print(str(e) + ' ' + str(gamma_list[i]))
    i += 1
