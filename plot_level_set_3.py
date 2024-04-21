import numpy as np
import pyvista as pv

def torus_level_set(radius_major, radius_minor, center, resolution):
    def level_set_function(x, y, z):
        # Compute the distance to the surface of the torus
        distance = np.sqrt((np.sqrt(x**2 + y**2) - radius_major)**2 + z**2) - radius_minor
        return distance

    return level_set_function

# Define torus parameters
radius_major = 0.8
radius_minor = 0.2
center = (0, 0, 0)
resolution = 50  # Adjust resolution as needed

# Generate the level set representation of the torus
torus_function = torus_level_set(radius_major, radius_minor, center, resolution)

# Create a PyVista grid to sample the function
grid = pv.UniformGrid()
grid.dimensions = [resolution, resolution, resolution]
grid.origin = (-1, -1, -1)
grid.spacing = (2/(resolution-1), 2/(resolution-1), 2/(resolution-1))

# Sample the level set function on the grid
points = grid.points
distances = np.zeros(points.shape[0])

for i, (x, y, z) in enumerate(points):
    distances[i] = torus_function(x, y, z)

# Set the sampled distances as the point data
grid.point_data["DistanceField"] = distances

# Save the grid as a VTK file
grid.save("torus_continuous.vtk")
