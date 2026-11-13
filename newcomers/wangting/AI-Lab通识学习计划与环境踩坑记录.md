# AI-Lab 通识学习计划与环境踩坑记录

## 一、学习计划

按文档中的 Task 清单，1个月内完成所有任务。

### 目标

- 完成 Task 清单中的所有任务

### Task 清单（共 9 个）

#### Task 1：现代 AI 编程环境（Trae / VSCode）与 CLI 协同工具配置
- 安装 Trae / VSCode及CLI工具Opencode
- 完成标准：
  1.成功用Trae编写了一个简单的Python程序"hello"

  ```python
  print("hello ")
  ```
  2.成功用Opencode编写了从1到100累加整数和的Python程序
  ```python
  total = 0
  for i in range(1, 101):
    total += i
  print(total)
  ```
  还进行了一次交互，修改了代码，让用户自定义累加范围
  ```python
  n== int(input("请输入一个正整数："))
  total = 0
  for i in range(1, n+1):
    total += i
  print(total)
  ```

#### Task 2：Linux 终端基础与常用命令行实战
- 在VMware Workstation中安装Linux系统（Rocky Linux）
1. 熟练掌握目录与文件操作命令：pwd、cd、ls (或 eza)、mkdir、rm、cp、mv、cat、head、tail、find；
2. 熟练掌握文本过滤与管道操作：grep、wc、标准输入输出重定向（>、>>、|）；
3. 熟悉系统状态与进程排查：ps aux、top (或 btop)、kill、df -h、free -m；
4. 掌握文件权限基础：chmod、chown。
- 完成标准：

![VMware Workstation 中运行的 Rocky Linux 桌面](images/task2-rocky-linux.png)

![通过 Xshell 远程登录 Rocky Linux，使用 ls、mkdir -p、cd、pwd 完成目录创建与切换](images/task2-1-mkdir-cd-pwd.png)

![使用 ls -R 查看目录树，并用 mv 重命名 data → data1、file → data2](images/task2-2-ls-mv.png)

![使用 cat 重定向写入日志、grep 过滤并重定向输出到 result](images/task2-3-cat-grep.png)

- 踩坑记录：[见「坑 1」](#坑-1关联-task-2)

#### Task 3：Git 版本管理规范与 GitHub 协作实操

- 设置VS Code为Git默认编辑器
- 完成标准：

![alt text](<屏幕截图 2026-11-04 220148.png>)

![alt text](<屏幕截图 2026-11-04 212225.png>)

- 踩坑记录：[见「坑 2」](#坑-2关联-task-3)

#### Task 4：Conda 虚拟环境隔离与镜像源加速配置
1.通过清华镜像网站快速安装Conda，并设置环境变量

https://mirrors.tuna.tsinghua.edu.cn/

2.清华镜像网站的使用帮助配置Conda源

3.创建虚拟环境
```
conda create -n PY python=3.10
```
4.激活环境
```
conda activate PY
```
退出环境
```
conda deactivate
```

5.安装包
```
conda install 包名
```

6.导出和复现
```
pip freeze > requirements.txt
pip install -r requirements.txt
```

- 完成标准:
  ![alt text](c3aa769af800e119165cc6e5d50959ac.png)

  ![alt text](<屏幕截图 2026-11-05 211001.png>)

  ![alt text](<屏幕截图 2026-11-05 211018.png>)

#### Task 5：Docker 容器化技术初探
- 环境准备：安装 Docker Desktop，开启 CPU 虚拟化，后端依赖 WSL2
- 以 Python 镜像为例：
  1. 编写 `hello.py`
  2. 编写 `Dockerfile`（文件名无后缀）
  3. 在 CMD 中切换到项目目录
  4. 构建镜像：`docker build -t hello .`
     - `-t hello`：为镜像指定名称
     - 末尾的 `.`：以当前目录作为构建上下文
  5. 运行容器：`docker run --rm hello`
- 完成标准：

![alt text](<屏幕截图 2026-11-08 000242.png>)

![alt text](<屏幕截图 2026-11-07 231808.png>)

- 踩坑记录：[见「坑 3」](#坑-3关联-task-5)
#### Task 6：Python 核心语法与常用数据结构

- 通过三个 demo 代码对以下知识点进行了实操：
  1. 列表（List）：增删改查、切片操作、列表推导式
  2. 字典（Dict）：键值对操作、`get` 方法、字典推导式
  3. 集合（Set）：不可变性、集合去重与交并差运算
  4. 函数设计：参数默认值、`*args`、`**kwargs`、返回值与变量作用域

- 完成标准：见 `newcomers/wangting/Task7-Python核心语法` 的代码提交记录

#### Task 7：Python 文件 I/O、异常处理与工程基础

- 完成标准：

#### Task 8：经典算法与编程逻辑专项巩固

- 练习方式：
  1. 在 PyCharm 中编写洛谷题目，借助 IDE 的报错提示定位并修正问题
  2. 本地成功运行后，再复制代码到洛谷提交测评
  3. 若思考超过 10 分钟仍无法解决报错，则借助 AI 获取解题思路，再反复修改验证

- 完成标准：见 `newcomers/wangting/luogu` 的代码提交记录

![alt text](d07511b058992e9a3923363d8ef1e90e.jpg)

- 踩坑记录：[见「坑 4」](#坑-4关联-task-8)

#### Task 9：通识综合微项目实战

- 完成标准：

## 二、环境踩坑记录

### 坑 1（关联 Task 2）

#### 现象

B 站主流教学视频均采用 CentOS 7 演示，但该系统已停止维护，照教程操作无法获得可用、稳定的环境。

#### 原因

CentOS 7 已停止维护（EOL），原有镜像源逐步下线，教程中的安装与配源步骤已过期，直接照做会卡在镜像源不可用这一步。

#### 解决方法

与 AI 智能体反复交互，确认可用 Rocky Linux 替代 CentOS（同为 RHEL 系、命令基本一致）；再通过小红书等社区帖子找到可用的镜像网站，从而快速完成系统下载与配置。

### 坑 2（关联 Task 3）

#### 现象

1. 本机 Windows 用户名为中文，默认 C 盘用户目录出现路径乱码，密钥生成失败。
2. `ssh -T git@github.com` 报 `port 22: Connection refused`。
3. 密钥放在 D 盘后，直接 `git push` / `git pull` 提示 `Permission denied (publickey)`。
4. 单独执行 `ssh -F /d/git/ssh/config -T git@github.com` 认证成功，但直接 `git push` 失败。

#### 原因

1. Git Bash 对中文用户名的原生 OpenSSH 路径解析异常。
2. 网络封禁了 GitHub 的 22 SSH 端口。
3. SSH 默认只读取 `~/.ssh/` 下的配置，不会自动加载 D 盘的 `config` 和私钥。
4. Git 执行 push/pull 时不会自动带上 `-F` 指定的配置文件参数。

#### 解决方法

1. 将密钥存放至 D 盘，避开中文路径。
2. 改用 443 端口，连接 `ssh.github.com:443`。
3. 让 SSH 默认也读到 D 盘的配置：在 `~/.ssh/config` 顶部加一行 `Include D:/git/ssh/config`，使 `git push` / `pull` 走默认路径时也能加载 D 盘的 config 与私钥。
4. 让 Git 自动带上 `-F`：执行 `git config --global core.sshCommand "ssh -F /d/git/ssh/config"`，此后 git 执行远程操作时会自动使用该配置文件。

### 坑 3（关联 Task 5）

#### 现象

1. Dockerfile 被误命名为 `Dockerfile.txt`，构建时 Docker 无法识别该文件。
2. 在 Windows CMD 中执行 `cd D:\Docker\docker-lab` 后，提示符仍停留在 C 盘，未真正进入目标目录，后续 `docker build` 找不到 Dockerfile 而构建失败。

#### 原因

1. 资源管理器未开启「文件扩展名」显示，重命名时实际后缀 `.txt` 仍被保留，导致文件名变成了 `Dockerfile.txt`。
2. CMD 中单独使用 `cd` 只能在同一盘符内切换目录，无法跨盘符跳转；仅写 `cd D:\...` 只是记录了目标路径，并不会切换到 D 盘。

#### 解决方法

1. 在资源管理器顶部「查看」中勾选「文件扩展名」，再将文件重命名为无后缀的 `Dockerfile`。
2. 使用带 `/d` 参数的 `cd /d D:\Docker\docker-lab` 一步到位跨盘切换；或先执行 `D:` 切换盘符，再 `cd Docker\docker-lab`。

### 坑 4（关联 Task 8）

#### 现象

1. 角谷猜想题目重复输出：开头单独写了 `if N==1: print("End")`，循环结束后又打印一次 `End`，输入 1 时输出两行，OJ 报 `Too many lines`（输出行数过多 WA）。
2. 同一份代码在 Python3 下超时，很多点换个语言就能 AC。
3. 统计总数的场景下结果不对，最终只拿到最后一组的数据。

#### 原因

1. `End` 在「特判分支」和「循环结束统一打印」两处各输出一次，输入 1 时两者都会命中，导致多输出一行。
2. Python3 解释执行速度较慢，同样的算法在严格时限下容易超时。
3. `count = 0` 写在了内层循环里，每组循环都会清零，最后只保留了最后一组的结果。

#### 解决方法

1. 删掉开头单独判断 `N == 1` 的分支，改为循环结束后统一打印一次 `End`。
2. 改用 PyPy3 提交，运行速度远快于 Python3，原先超时的测试点可正常 AC。
3. 把用于统计总计数的变量初始化放在所有循环的最外层，避免被重复清零。