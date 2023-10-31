import vtkmodules.all as vtk

# Create a plate geometry
plate = vtk.vtkCubeSource()
plate.SetCenter([0.0, 0.05, 0.0])
plate.SetXLength(0.1)  # Set the dimensions as needed
plate.SetYLength(0.001)
plate.SetZLength(0.1)   # Thickness of the plate

# Save the geometry to a VTK file in ASCII format
writer = vtk.vtkPolyDataWriter()
writer.SetFileName("plate_geometry.vtk")  # Set the file name
writer.SetInputConnection(plate.GetOutputPort())
writer.SetFileTypeToASCII()  # Set the file type to ASCII
writer.Write()

