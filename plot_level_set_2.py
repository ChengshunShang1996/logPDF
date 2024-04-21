import numpy as np
import pyvista as pv

def torus_level_set(radius_major, radius_minor, center, grid_shape):
    # Create a grid
    x = np.linspace(-1, 1, grid_shape[0])
    y = np.linspace(-1, 1, grid_shape[1])
    z = np.linspace(-1, 1, grid_shape[2])
    xx, yy, zz = np.meshgrid(x, y, z, indexing='ij')
    
    # Compute the level set function for a torus
    distance_field = np.sqrt((np.sqrt(xx**2 + yy**2) - radius_major)**2 + zz**2) - radius_minor
    
    return distance_field

# Define torus parameters
radius_major = 0.8
radius_minor = 0.2
center = (0, 0, 0)
grid_shape = (100, 100, 100)  # Adjust grid resolution as needed

# Generate the level set representation of the torus
distance_field = torus_level_set(radius_major, radius_minor, center, grid_shape)

# Create a PyVista grid
grid = pv.UniformGrid()
grid.dimensions = distance_field.shape
grid.origin = (-1, -1, -1)
grid.spacing = (2/(grid_shape[0]-1), 2/(grid_shape[1]-1), 2/(grid_shape[2]-1))

# Set the distance field as the point data
grid.point_data["DistanceField"] = distance_field.flatten(order='F')

# Save the grid as a VTK file
grid.save("torus.vtk")
