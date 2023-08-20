import vtkmodules.all as vtk
import numpy as np

def create_superquadric(center, scale, phi_roundness, theta_roundness):
    superquadric = vtk.vtkSuperquadricSource()
    superquadric.SetCenter(center)
    superquadric.SetScale(scale)
    superquadric.SetPhiRoundness(phi_roundness)
    superquadric.SetThetaRoundness(theta_roundness)
    superquadric.SetThetaResolution(50)
    superquadric.SetPhiResolution(50)
    return superquadric

# Define parameters for five superquadrics
parameters = [
    ((1, 0, 0), (1, 0.5, 0.75), 0.5, 0.75),
    ((4, 0, 0), (1, 0.5, 0.75), 0.8, 0.6),
    ((6, 0, 0), (1, 0.5, 0.75), 0.3, 1.0),
    ((8, 0, 0), (1, 0.5, 0.75), 0.7, 0.9),
    ((10, 0, 0), (1, 0.5, 0.75), 0.6, 0.8)
]

# Create an append filter to combine the particles
append_filter = vtk.vtkAppendPolyData()

# Loop through each set of parameters and create superquadrics
for i, (center, scale, phi_roundness, theta_roundness) in enumerate(parameters):
    superquadric = create_superquadric(center, scale, phi_roundness, theta_roundness)
    append_filter.AddInputConnection(superquadric.GetOutputPort())

# Update the append filter
append_filter.Update()

# Export the combined particles to a single .vtk file
writer = vtk.vtkPolyDataWriter()
writer.SetInputData(append_filter.GetOutput())
writer.SetFileName("particles.vtk")
writer.Write()