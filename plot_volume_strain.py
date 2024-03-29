import matplotlib.pyplot as plt
import numpy as np

strain_list, volume_list = [], []
with open('strain_volume.txt', 'r') as s_v_data:
    for line in s_v_data:
        values = [float(s) for s in line.split()]
        #strain_list.append(values[0] - 0.145002)
        strain_list.append(values[0] - 0.3)
        volume_list.append(((values[1] - 3.1425053129724597e-06) / 0.00019639495267568686) * 100)

fig = plt.figure()
plt.xlabel('Strain / %')
plt.ylabel('Volume starin / %')
plt.plot(strain_list, volume_list, 'bo-')

plt.axhline(y=0.0, color='black', linestyle='-')

plt.xlim((0, 13))
plt.grid(True)
plt.show()