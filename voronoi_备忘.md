# 目前使用的Voro++ 是Github版本
https://github.com/chr1shr/voro.git

编译方法：

1. 安装 CMake： 如果尚未安装 CMake，请下载并安装它。你可以从 CMake 官方网站（https://cmake.org/download/）下载安装程序并按照指示进行安装。

2. 打开命令行终端： 打开 Windows 的命令提示符（Command Prompt）或者 Windows PowerShell。

3. 导航到项目目录： 使用 cd 命令导航到包含 CMakeLists.txt 和源代码的项目目录。

4. 创建一个构建目录： 建议在项目目录下创建一个名为 build 的子目录，用于存放编译生成的文件。

5. 运行 CMake： 在命令行中运行以下命令来生成 Makefile（或 Visual Studio 项目文件）：

> cmake -S . -B build

  这会在 build 目录中生成适用于你的编译环境的构建文件

6. 用Visual Studio 2019打开Build目录下的All_Build项目，进行编译，生成exe可执行文件