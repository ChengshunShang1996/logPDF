import vtk

# 创建一个立方体的顶点坐标
points = vtk.vtkPoints()
points.InsertNextPoint(0, 0, 0)
points.InsertNextPoint(2, 0, 0)
points.InsertNextPoint(1, 1, 0)
points.InsertNextPoint(0, 1, 0)
points.InsertNextPoint(0, 0, 1)
points.InsertNextPoint(1, 0, 1)
points.InsertNextPoint(1, 1, 1)
points.InsertNextPoint(0, 1, 1)

# 创建多面体的面
cube = vtk.vtkHexahedron()
for i in range(8):
    cube.GetPointIds().SetId(i, i)

# 创建拓扑单元
cellArray = vtk.vtkCellArray()
cellArray.InsertNextCell(cube)

# 创建一个包含多面体单元的vtkUnstructuredGrid对象
ugrid = vtk.vtkUnstructuredGrid()
ugrid.SetPoints(points)
ugrid.SetCells(vtk.VTK_HEXAHEDRON, cellArray)

# 写出到vtk文件
writer = vtk.vtkUnstructuredGridWriter()
writer.SetFileName("cube.vtk")
writer.SetInputData(ugrid)
writer.Write()
