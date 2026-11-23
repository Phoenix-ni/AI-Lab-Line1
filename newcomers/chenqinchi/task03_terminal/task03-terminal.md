# Task03 终端基础命令练习
## 练习环境
系统：Windows CMD
工作目录：C:\Users\zhou\Desktop\AI-Lab

## 命令记录
1. cd：不带参数，查看当前所在路径；cd 目录名 切换目录；cd .. 返回上一级
2. dir：列出当前目录下的文件和文件夹
3. mkdir 文件夹名：新建文件夹
4. echo 内容 > 文件名：创建文件并写入内容
5. type 文件名：查看文件里面的内容
6. copy 源文件 目标文件：复制文件
7. ren 旧文件名 新文件名：重命名文件
8. move 源 目标：移动文件
9. del 文件名：删除文件
10. rd /s /q 文件夹名：删除带内容的文件夹

## 实操截图
![CMD终端练习记录](./screenshots/cmd-task03.jpg)

## 练习踩坑记录
- CMD 不支持 pwd、ls、cat 这些PowerShell/Linux命令，命令不能混用
- copy、move 命令，**文件名之间必须加空格**，连在一起会报错
- rd 默认不能删除里面有文件的文件夹，必须加上 /s /q
- 文件夹名字下划线 `test_dir` 和短横 `test-dir` 是两个不同名字，不要弄混