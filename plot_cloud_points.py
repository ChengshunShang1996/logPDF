import numpy as np
from scipy.spatial import ConvexHull
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import os
import vtk

points_data_list = []
disp_data_list = []
points_start = False
disp_start = False
with open("Structure_0_6013750.vtk", 'r') as file:
    for line in file:
        if line.strip():
                values = [s for s in line.split()]
                if values[0] == "POINTS":
                    points_start = True
                    continue
                if values[0] == "CELLS":
                    points_start = False
                    continue
                if points_start == True:
                    points_data_list.append([float(values[0]), float(values[1]), float(values[2])]) 

                if values[0] == "DISPLACEMENT":
                    disp_start = True
                    continue
                if values[0] == "REACTION":
                    disp_start = False
                    continue
                if disp_start == True:
                    disp_data_list.append([float(values[0]), float(values[1]), float(values[2])]) 

    real_points_data_list = [(p1[0] + p2[0], p1[1] + p2[1], p1[2] + p2[2]) for p1, p2 in zip(points_data_list, disp_data_list)]

points = np.array(real_points_data_list)

# 进行凸包计算
hull = ConvexHull(points, qhull_options='QJ')

vtk_points = vtk.vtkPoints()
for point in points:
    vtk_points.InsertNextPoint(point)

polydata = vtk.vtkPolyData()
polydata.SetPoints(vtk_points)

# Write polydata to vtk file
writer = vtk.vtkPolyDataWriter()
writer.SetFileName("points_output.vtk")
writer.SetInputData(polydata)
writer.Write()

# Create a vtkCellArray to store the convex hull faces
vtk_faces = vtk.vtkCellArray()
for simplex in hull.simplices:
    triangle = vtk.vtkTriangle()
    for i, vertex_index in enumerate(simplex):
        triangle.GetPointIds().SetId(i, vertex_index)
    vtk_faces.InsertNextCell(triangle)

# Create a polydata object and set points and faces
polydata = vtk.vtkPolyData()
polydata.SetPoints(vtk_points)
polydata.SetPolys(vtk_faces)

# Write polydata to vtk file
writer = vtk.vtkPolyDataWriter()
writer.SetFileName("hull_output.vtk")
writer.SetInputData(polydata)
writer.Write()

# 创建一个 3D 图形对象
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 绘制凸包
for simplex in hull.simplices:
    ax.plot(points[simplex, 0], points[simplex, 1], points[simplex, 2], 'k-')

# 绘制点云数据
ax.scatter(points[:, 0], points[:, 1], points[:, 2], c='b', marker='o')

# 设置图形标题和坐标轴标签
#ax.set_title('Convex Hull of Random Point Cloud')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# 显示图形
plt.show()

# 计算凸包的体积
volume_hull = hull.volume

print("Volume approximation using Convex Hull:", volume_hull)