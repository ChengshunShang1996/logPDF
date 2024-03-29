import numpy as np
from scipy.spatial import ConvexHull
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import os
import math

files_name = os.listdir('vtk_output')
timestep = 2e-8
loading_velosity = 0.05
radius = 0.025
height = 0.1
volume_list = []
strain_list = []
first_step = True
n = 0
for i in range(len(files_name)):
    
    n += 1
    print(n)

    steps = (i + 1) * 1250
    aim_file_name = 'Structure_0_' + str(steps) + '.vtk'

    time_used = steps * timestep

    aim_path_and_name = os.path.join(os.getcwd(),'vtk_output', aim_file_name)

    points_data_list = []
    disp_data_list = []
    points_start = False
    disp_start = False
    with open(aim_path_and_name, 'r') as vtk_data:
        for line in vtk_data:
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
    # 生成随机点云数据
    #points = np.random.rand(10, 3)  # 生成100个随机点，每个点有3个坐标（x, y, z）

    '''
    points = []
    with open("points.txt", 'r') as file:
        for line in file:
            # 按空格分割每一行的数据，并转换为浮点数
            x, y, z = map(float, line.strip().split())
            points.append([x, y, z])

    points = np.array(points)'''

    points = np.array(real_points_data_list)

    #y1 = 0.0
    #y2 = 1.0

    # Filter points based on y-coordinate range
    #filtered_points = points[(points[:, 1] >= y1) & (points[:, 1] <= y2)]

    # 进行凸包计算
    hull = ConvexHull(points, qhull_options='QJ')
    '''
    # 创建一个 3D 图形对象
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # 绘制凸包
    for simplex in hull.simplices:
        ax.plot(points[simplex, 0], points[simplex, 1], points[simplex, 2], 'k-')

    # 绘制点云数据
    ax.scatter(points[:, 0], points[:, 1], points[:, 2], c='b', marker='o')

    # 设置图形标题和坐标轴标签
    ax.set_title('Convex Hull of Random Point Cloud')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    # 显示图形
    plt.show()'''

    # 计算凸包的体积
    volume_hull = hull.volume

    volume_hull -= math.pi * radius * radius * loading_velosity * time_used * 2

    if first_step:
        volume_ini = volume_hull
        first_step = False
        strain_list.append(0.0)
        volume_list.append(0.0)
        continue

    strain = loading_velosity * time_used * 2 / height * 100

    volume_change = volume_hull - volume_ini

    strain_list.append(strain)
    volume_list.append(volume_change)

fig = plt.figure()
plt.xlabel('Strain / %')
plt.ylabel('Volume change')
plt.plot(strain_list, volume_list, 'bo-')
plt.show()

with open("strain_volume.txt", 'w') as file:
    for i in range(len(strain_list)):
        file.write(str(strain_list[i]) + ' ' + str(volume_list[i]) + '\n')

# 计算Delaunay三角剖分的体积
#volume_tri = sum(tri.volumes)

#print("Volume approximation using Convex Hull:", volume_hull)

#real = 3.1415926 * 0.025 * 0.025 * 0.1
#print(real)
#print("Volume approximation using Delaunay Triangulation:", volume_tri)