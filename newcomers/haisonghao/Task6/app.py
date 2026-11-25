# Task 06 演示脚本：在容器内运行的极简 Python 程序
import platform
import sys

print("Hello AI-Lab Docker")
print("-" * 40)
print("Python 版本 :", platform.python_version())
print("解释器路径  :", sys.executable)
print("操作系统    :", platform.system(), platform.release())
print("机器架构    :", platform.machine())
