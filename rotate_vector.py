import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the source vector and the target vector
source_vector = np.array([1, -5, 4])  # The vector you want to rotate
target_vector = np.array([1, 2, 0])  # The vector you want to align with
initial_target_vector = target_vector

# 判断是否旋转到目标向量的相反方向
if np.dot(source_vector, target_vector) < 0:
    # 如果点积为负值，旋转到目标向量的相反方向
    target_vector = -1 * target_vector

# Calculate the rotation axis and angle
source_normalized = source_vector / np.linalg.norm(source_vector)
target_normalized = target_vector / np.linalg.norm(target_vector)
rotation_axis = np.cross(source_normalized, target_normalized) / np.linalg.norm(np.cross(source_normalized, target_normalized))

# 计算旋转角度
dot_product = np.dot(source_normalized, target_normalized)
rotation_angle = np.arccos(dot_product)

# Create the rotation matrix using the axis-angle representation
c = np.cos(rotation_angle)
s = np.sin(rotation_angle)
t = 1 - c
x, y, z = rotation_axis
rotation_matrix = np.array([
    [t * x * x + c, t * x * y - s * z, t * x * z + s * y],
    [t * x * y + s * z, t * y * y + c, t * y * z - s * x],
    [t * x * z - s * y, t * y * z + s * x, t * z * z + c]
])

print(c)
print(s)
print(t)
print(rotation_axis)
print(rotation_matrix)

# Rotate the source vector to align with the target vector
aligned_vector = np.dot(rotation_matrix, source_vector)

print(aligned_vector)

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the source vector
ax.quiver(0, 0, 0, source_vector[0], source_vector[1], source_vector[2], color='b', label='Source Vector')

# Plot the target vector
ax.quiver(0, 0, 0, initial_target_vector[0], initial_target_vector[1], initial_target_vector[2], color='g', label='Target Vector')

# Plot the aligned vector
ax.quiver(0, 0, 0, aligned_vector[0], aligned_vector[1], aligned_vector[2], color='r', label='Aligned Vector')

# Set plot limits
ax.set_xlim([-5, 5])
ax.set_ylim([-5, 5])
ax.set_zlim([-5, 5])

# Add labels and legend
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()

# Show the plot
plt.show()
