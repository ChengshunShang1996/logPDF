import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def fcc_lattice(n):
    lattice_points = []
    for i in range(n):
        for j in range(n):
            for k in range(n):
                lattice_points.append([i, j, k])
                lattice_points.append([i + 0.5, j + 0.5, k])
                lattice_points.append([i, j + 0.5, k + 0.5])
                lattice_points.append([i + 0.5, j, k + 0.5])
    return np.array(lattice_points)

def plot_fcc(arr):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(arr[:,0], arr[:,1], arr[:,2], color='b', alpha=0.6, s=100)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Face-Centered Cubic (FCC) Arrangement')
    plt.show()

# Define the size of the lattice
n = 5

# Generate FCC lattice points
fcc_points = fcc_lattice(n)

# Plot the FCC lattice
plot_fcc(fcc_points)