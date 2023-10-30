from stl import mesh
import numpy as np

# Load the first STL file
mesh1 = mesh.Mesh.from_file('test_hope0.stl')

# Load the second STL file
mesh2 = mesh.Mesh.from_file('test_hope1.stl')

# Combine the two meshes into a single mesh
combined_mesh = mesh.Mesh(np.concatenate([mesh1.data, mesh2.data]))

# Save the combined mesh to a new STL file
combined_mesh.save('combined.stl')