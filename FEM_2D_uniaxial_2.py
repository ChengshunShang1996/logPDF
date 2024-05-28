import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spla
import vtk
from vtk.util.numpy_support import numpy_to_vtk
import matplotlib.pyplot as plt

# Define the dimensions
length = 50.0  # mm
height = 100.0   # mm

# Number of elements in each direction
nx = 5
ny = 10

# Create the mesh
x = np.linspace(0, length, nx + 1)
y = np.linspace(0, height, ny + 1)
xx, yy = np.meshgrid(x, y)
points = np.vstack([xx.ravel(), yy.ravel()]).T

# Create connectivity
cells = []
for j in range(ny):
    for i in range(nx):
        n1 = i + j * (nx + 1)
        n2 = (i + 1) + j * (nx + 1)
        n3 = (i + 1) + (j + 1) * (nx + 1)
        n4 = i + (j + 1) * (nx + 1)
        cells.append([n1, n2, n3, n4])
cells = np.array(cells)

# Plot the mesh
for cell in cells:
    plt.fill(points[cell, 0], points[cell, 1], edgecolor='black', fill=False)
plt.gca().set_aspect('equal')
plt.show()

class Material:
    def __init__(self, E, nu, cohesion, friction_angle):
        self.E = E
        self.nu = nu
        self.cohesion = cohesion
        self.friction_angle = friction_angle

# Define material properties
material = Material(E=30e9, nu=0.3, cohesion=2e6, friction_angle=np.radians(30))

# Boundary conditions
def apply_boundary_conditions(K, F, points, length, height):
    for i, point in enumerate(points):
        if point[1] == 0.0:  # Fix bottom edge in y direction
            K[2*i, :] = 0.0
            K[2*i, 2*i] = 1.0
            F[2*i] = 0.0
            K[2*i+1, :] = 0.0
            K[2*i+1, 2*i+1] = 1.0
            F[2*i+1] = 0.0
        #if point[0] == 0.0:  # Fix left edge in x direction
        #    K[2*i, :] = 0.0
        #    K[2*i, 2*i] = 1.0
        #    F[2*i] = 0.0
    return K, F

# Number of degrees of freedom
num_dofs = 2 * len(points)

# Initialize global stiffness matrix and force vector
K = sp.lil_matrix((num_dofs, num_dofs))
F = np.zeros(num_dofs)

# Shape functions derivatives for a quadrilateral element
def shape_function_derivatives(xi, eta):
    dN_dxi = np.array([
        [-(1 - eta),  (1 - eta), (1 + eta), -(1 + eta)],
        [-(1 - xi),  -(1 + xi),  (1 + xi),   (1 - xi)]
    ]) / 4.0
    return dN_dxi

# B-matrix for a quadrilateral element
def B_matrix(dN_dxi, J_inv):
    B = np.zeros((3, 8))
    for i in range(4):
        dN_dx = J_inv @ dN_dxi[:, i]
        B[0, 2 * i] = dN_dx[0]
        B[1, 2 * i + 1] = dN_dx[1]
        B[2, 2 * i] = dN_dx[1]
        B[2, 2 * i + 1] = dN_dx[0]
    return B

# Elasticity matrix for plane stress
def elasticity_matrix(E, nu):
    C = E / (1 - nu**2) * np.array([
        [1, nu, 0],
        [nu, 1, 0],
        [0, 0, (1 - nu) / 2]
    ])
    return C

# Element stiffness matrix for a quadrilateral element
def element_stiffness_matrix(E, nu, coords):
    gauss_points = [(-1 / np.sqrt(3), -1 / np.sqrt(3)), (1 / np.sqrt(3), -1 / np.sqrt(3)), (1 / np.sqrt(3), 1 / np.sqrt(3)), (-1 / np.sqrt(3), 1 / np.sqrt(3))]
    C = elasticity_matrix(E, nu)
    ke = np.zeros((8, 8))
    for xi, eta in gauss_points:
        dN_dxi = shape_function_derivatives(xi, eta)
        J = dN_dxi @ coords
        J_inv = np.linalg.inv(J)
        detJ = np.linalg.det(J)
        B = B_matrix(dN_dxi, J_inv)
        ke += B.T @ C @ B * detJ
    return ke

# Assemble global stiffness matrix
for cell in cells:
    coords = points[cell]
    ke = element_stiffness_matrix(material.E, material.nu, coords)
    for i in range(4):
        for j in range(4):
            K[2*cell[i]:2*cell[i]+2, 2*cell[j]:2*cell[j]+2] += ke[2*i:2*i+2, 2*j:2*j+2]

# Prepare function to apply loads
def apply_loads(load_values, points, height):
    top_edge_nodes = np.where(points[:, 1] == height)[0]
    displacements = []
    stresses = []
    strains = []

    for load in load_values:
        # Apply load on top edge
        F = np.zeros(num_dofs)
        F[2*top_edge_nodes + 1] = -load  # Apply a downward load on each node of the top edge

        # Apply boundary conditions
        K_copy = K.copy()
        K_copy, F = apply_boundary_conditions(K_copy, F, points, length, height)

        # Solve the system
        displacement = spla.spsolve(K_copy.tocsr(), F)

        # Calculate stress and strain
        stress = np.zeros(len(points))
        strain = np.zeros(len(points))

        for cell in cells:
            coords = points[cell]
            dN_dxi = shape_function_derivatives(0, 0)
            J = dN_dxi @ coords
            J_inv = np.linalg.inv(J)
            B = B_matrix(dN_dxi, J_inv)
            element_displacements = np.zeros(8)
            for i in range(4):
                element_displacements[2*i:2*i+2] = displacement[2*cell[i]:2*cell[i]+2]
            element_strain = B @ element_displacements
            element_stress = elasticity_matrix(material.E, material.nu) @ element_strain
            for i in range(4):
                strain[cell[i]] += np.linalg.norm(element_strain)
                stress[cell[i]] += np.linalg.norm(element_stress)

        # Average the values at the nodes
        stress /= np.array([len(np.where(cells == i)[0]) for i in range(len(points))])
        strain /= np.array([len(np.where(cells == i)[0]) for i in range(len(points))])

        displacements.append(displacement)
        stresses.append(stress)
        strains.append(strain)

    return displacements, stresses, strains

# Define load values (in N)
load_values = np.linspace(1000, 10000, 10)

# Apply loads and get results
displacements, stresses, strains = apply_loads(load_values, points, height)

# Create a VTK file for the results
def write_vtk(filename, points, displacements, stresses, strains):
    vtk_points = vtk.vtkPoints()
    for point in points:
        vtk_points.InsertNextPoint(point[0], point[1], 0.0)

    grid = vtk.vtkUnstructuredGrid()
    grid.SetPoints(vtk_points)

    # Create cells
    vtk_cells = vtk.vtkCellArray()
    for cell in cells:
        vtk_cells.InsertNextCell(len(cell), cell)
    grid.SetCells(vtk.VTK_QUAD, vtk_cells)

    # Create displacement vectors
    vtk_displacements = np.zeros((len(points), 3))
    vtk_displacements_x = np.zeros(len(points))
    vtk_displacements_y = np.zeros(len(points))
    for i in range(len(points)):
        vtk_displacements[i, 0:2] = [displacements[2*i], displacements[2*i+1]]
        vtk_displacements_x[i] = displacements[2*i]
        vtk_displacements_y[i] = displacements[2*i+1]
    vtk_displacements_vtk = numpy_to_vtk(vtk_displacements, deep=True)
    vtk_displacements_vtk.SetName("Displacements")
    grid.GetPointData().AddArray(vtk_displacements_vtk)

    vtk_displacements_x_vtk = numpy_to_vtk(vtk_displacements_x, deep=True)
    vtk_displacements_x_vtk.SetName("Displacement_X")
    grid.GetPointData().AddArray(vtk_displacements_x_vtk)

    vtk_displacements_y_vtk = numpy_to_vtk(vtk_displacements_y, deep=True)
    vtk_displacements_y_vtk.SetName("Displacement_Y")
    grid.GetPointData().AddArray(vtk_displacements_y_vtk)

    # Create stress scalars
    vtk_stresses_vtk = numpy_to_vtk(stresses, deep=True)
    vtk_stresses_vtk.SetName("Stresses")
    grid.GetPointData().AddArray(vtk_stresses_vtk)

    # Create strain scalars
    vtk_strains_vtk = numpy_to_vtk(strains, deep=True)
    vtk_strains_vtk.SetName("Strains")
    grid.GetPointData().AddArray(vtk_strains_vtk)

    writer = vtk.vtkXMLUnstructuredGridWriter()
    writer.SetFileName(filename)
    writer.SetInputData(grid)
    writer.Write()

# Save results for each load case
for i, load in enumerate(load_values):
    filename = f"output_load_{int(load)}.vtu"
    write_vtk(filename, points, displacements[i], stresses[i], strains[i])

# Plot displacement and stress for different loads
top_edge_nodes = np.where(points[:, 1] == height)[0]
top_edge_displacements = [np.mean(displacements[i][2*top_edge_nodes + 1]) for i in range(len(load_values))]
top_edge_stresses = [np.mean(stresses[i][top_edge_nodes]) for i in range(len(load_values))]

plt.figure()
plt.plot(load_values, top_edge_displacements, label='Top Edge Displacement')
plt.xlabel('Load (N)')
plt.ylabel('Displacement (mm)')
plt.legend()
plt.grid(True)
plt.show()

plt.figure()
plt.plot(load_values, top_edge_stresses, label='Top Edge Stress')
plt.xlabel('Load (N)')
plt.ylabel('Stress (Pa)')
plt.legend()
plt.grid(True)
plt.show()
