import matplotlib.pyplot as plt
import math
import numpy as np

# Define the coordinates of the four points defining the cubic
points = [(1, 1), (1, -1), (-1, -1), (-1, 1), (1, 1)]

# Add the center point (0, 0)
#center = (0, 0)
#points.append(center)

# Extract x and y coordinates
x, y = zip(*points)

# Define the order of connecting the points to form the cubic
#order = [0, 1, 2, 3, 0]

# Plot the cubic
#plt.plot(x, y, marker='o')
for i in range(4):
    plt.plot([x[i], x[i+1]], [y[i], y[i + 1]], 'bo-')

tensor_gradient_u = np.array([[-0.2, 0.0], 
                              [0.0, -0.2]])

update_points = []
for point in points:
    vector_r = np.array([[point[0]], [point[1]]])
    vector_d = np.dot(tensor_gradient_u, vector_r)
    update_point_x = point[0] + vector_d[0][0] 
    update_point_y = point[1] + vector_d[1][0]
    update_points.append((update_point_x, update_point_y))

print(update_points)

x1, y1 = zip(*update_points)

for i in range(4):
    plt.plot([x1[i], x1[i+1]], [y1[i], y1[i + 1]], 'ro--')

# Set axis limits for better visualization
plt.xlim(-2, 2)
plt.ylim(-2, 2)

# Add labels
plt.xlabel('X')
plt.ylabel('Y')

plt.title("Pure compression")
# Show the plot
plt.grid()
plt.show()
