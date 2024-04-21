import numpy as np
import pyvista as pv

def sphere_level_set(radius, center, grid_shape):
    # Create a grid
    x = np.linspace(-1, 1, grid_shape[0])
    y = np.linspace(-1, 1, grid_shape[1])
    z = np.linspace(-1, 1, grid_shape[2])
    xx, yy, zz = np.meshgrid(x, y, z, indexing='ij')
    
    # Compute the level set function for a sphere
    distance_field = np.sqrt((xx - center[0])**2 + (yy - center[1])**2 + (zz - center[2])**2) - radius
    
    return distance_field

# Define sphere parameters
radius = 0.25
center = (0, 0, 0)
grid_shape = (25, 25, 25)  # Adjust grid resolution as needed

# Generate the level set representation of the sphere
distance_field = sphere_level_set(radius, center, grid_shape)

# Create a PyVista grid
grid = pv.UniformGrid()
grid.dimensions = distance_field.shape
grid.origin = (-1, -1, -1)
grid.spacing = (2/(grid_shape[0]-1), 2/(grid_shape[1]-1), 2/(grid_shape[2]-1))

# Set the distance field as the point data
grid.point_data["DistanceField"] = distance_field.flatten(order='F')

# Save the grid as a VTK file
grid.save("sphere.vtk")
