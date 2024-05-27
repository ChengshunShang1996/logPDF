import numpy as np
import pyvista as pv

def superquadric_level_set(a, b, c, epsilon1, epsilon2, center, grid_shape):
    # Create a grid
    x = np.linspace(-1, 1, grid_shape[0])
    y = np.linspace(-1, 1, grid_shape[1])
    z = np.linspace(-1, 1, grid_shape[2])
    xx, yy, zz = np.meshgrid(x, y, z, indexing='ij')
    
    # Compute the level set function for a superquadric
    term1 = np.power(np.abs((xx - center[0]) / a), 2 / epsilon2)
    term2 = np.power(np.abs((yy - center[1]) / b), 2 / epsilon2)
    term3 = np.power(term1 + term2, epsilon2 / epsilon1)
    term4 = np.power(np.abs((zz - center[2]) / c), 2 / epsilon1)
    
    distance_field = term3 + term4 - 1
    
    return distance_field

def create_grid(a, b, c, epsilon1, epsilon2, center, grid_shape, grid_origin):
    # Generate the distance field
    distance_field = superquadric_level_set(a, b, c, epsilon1, epsilon2, center, grid_shape)
    
    # Create a PyVista grid
    grid = pv.UniformGrid()
    grid.dimensions = distance_field.shape
    #grid.origin = (-1, -1, -1)
    grid.origin = (grid_origin[0] - 1, grid_origin[1] - 1, grid_origin[2] - 1)
    grid.spacing = (2/(grid_shape[0]-1), 2/(grid_shape[1]-1), 2/(grid_shape[2]-1))
    
    # Set the distance field as the point data
    grid.point_data["DistanceField"] = distance_field.flatten(order='F')
    
    return grid

# Parameters for different superquadrics
superquadric_params = [
    {"a": 1, "b": 1, "c": 1, "epsilon1": 1, "epsilon2": 1, "center": [0, 0, 0], "grid_shape": (50, 50, 50), "grid_origin": [0, 0, 0]},
    {"a": 1, "b": 0.3, "c": 0.5, "epsilon1": 1, "epsilon2": 1, "center": [0, 0, 0], "grid_shape": (50, 50, 50), "grid_origin": [2, 2, 2]},
    {"a": 1, "b": 1, "c": 1, "epsilon1": 0.1, "epsilon2": 0.1, "center": [0, 0, 0], "grid_shape": (50, 50, 50), "grid_origin": [4, 4, 4]},
    {"a": 1, "b": 0.5, "c": 1, "epsilon1": 1, "epsilon2": 1, "center": [0, 0, 0], "grid_shape": (50, 50, 50), "grid_origin": [6, 6, 6]}
]

# Create a MultiBlock dataset
multi_block = pv.MultiBlock()

# Create and add grids to the MultiBlock dataset
for i, params in enumerate(superquadric_params):
    grid = create_grid(**params)
    multi_block.append(grid)

# Save the MultiBlock dataset as a VTK file
multi_block.save("superquadrics_LS.vtm")
