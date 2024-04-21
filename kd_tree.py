import numpy as np
import matplotlib.pyplot as plt

class Node:
    def __init__(self, point, left=None, right=None, axis=None):
        self.point = point  # 数据点
        self.left = left    # 左子树
        self.right = right  # 右子树
        self.axis = axis    # 划分轴

def build_kdtree(points, depth=0):
    if len(points) == 0:
        return None
    
    # 按照当前深度选择划分轴
    axis = depth % len(points[0])
    
    # 根据划分轴排序数据点
    points.sort(key=lambda x: x[axis])
    
    # 选择中位数作为根节点
    median_idx = len(points) // 2
    median_point = points[median_idx]
    
    # 递归构建左子树和右子树
    return Node(
        point=median_point,
        left=build_kdtree(points[:median_idx], depth + 1),
        right=build_kdtree(points[median_idx + 1:], depth + 1),
        axis=axis
    )

def search_kdtree(node, target_point, radius, result=[]):
    if node is None:
        return
    
    # 计算目标点到当前节点的距离
    dist = np.linalg.norm(np.array(target_point) - np.array(node.point))
    
    # 如果当前节点在球内，则将其加入结果列表
    if dist <= radius:
        result.append(node.point)
    
    # 按照划分轴选择子树
    if target_point[node.axis] - radius <= node.point[node.axis]:
        search_kdtree(node.left, target_point, radius, result)
    if target_point[node.axis] + radius >= node.point[node.axis]:
        search_kdtree(node.right, target_point, radius, result)

    return result

def find_points_in_sphere(points, target_point, radius):
    # 构建K-d树
    kdtree = build_kdtree(points)
    
    # 搜索球内的所有颗粒
    result = search_kdtree(kdtree, target_point, radius)
    
    return result

def plot_points_and_circle(points, target_point, radius, points_in_sphere):
    fig, ax = plt.subplots()
    
    # 绘制所有点
    x = [p[0] for p in points]
    y = [p[1] for p in points]
    ax.scatter(x, y, color='blue', label='All Points')
    
    # 绘制圆心
    ax.scatter(target_point[0], target_point[1], color='red', label='Circle Center')
    
    # 绘制球内的点
    x_in_sphere = [p[0] for p in points_in_sphere]
    y_in_sphere = [p[1] for p in points_in_sphere]
    ax.scatter(x_in_sphere, y_in_sphere, color='green', label='Points in Sphere')
    
    # 绘制圆
    circle = plt.Circle(target_point, radius, color='red', fill=False, linestyle='--', label='Sphere')
    ax.add_artist(circle)
    
    ax.set_aspect('equal', adjustable='box')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title('Points and Circle')
    ax.legend()
    
    plt.show()

# 示例用法
if __name__ == "__main__":
    # 构建一些示例数据点
    points = [(2,3), (5,4), (9,6), (4,7), (8,1), (7,2), (5, 1), (3, 1), (8, 6)]
    
    # 设置目标点和球的半径
    target_point = (6, 4)
    radius = 3
    
    # 查找颗粒中心位于球内的点
    points_in_sphere = find_points_in_sphere(points, target_point, radius)
    
    # 绘制点和圆
    plot_points_and_circle(points, target_point, radius, points_in_sphere)
