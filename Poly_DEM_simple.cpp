#include <iostream>
#include <fstream>

int main() {
    std::ofstream vtkFile("cube_simple.vtk");

    // 写入VTK文件的头部信息
    vtkFile << "# vtk DataFile Version 3.0\n";
    vtkFile << "Cube example\n";
    vtkFile << "ASCII\n";
    vtkFile << "DATASET UNSTRUCTURED_GRID\n";

    // 写入顶点坐标
    vtkFile << "POINTS 8 float\n";
    vtkFile << "0.0 0.0 0.0\n";
    vtkFile << "1.0 0.0 0.0\n";
    vtkFile << "1.0 1.0 0.0\n";
    vtkFile << "0.0 1.0 0.0\n";
    vtkFile << "0.0 0.0 1.0\n";
    vtkFile << "1.0 0.0 1.0\n";
    vtkFile << "1.0 1.0 1.0\n";
    vtkFile << "0.0 1.0 1.0\n";

    // 写入六面体单元
    vtkFile << "CELLS 1 9\n";
    vtkFile << "8 0 1 2 3 4 5 6 7\n";

    // 写入单元类型
    vtkFile << "CELL_TYPES 1\n";
    vtkFile << "12\n"; // VTK_HEXAHEDRON 十二面体单元类型

    vtkFile.close();
    std::cout << "VTK file written successfully\n";

    return 0;
}
