**Task 06：Docker 容器化技术初探 操作记录**

**一、 镜像与容器的理解**

- **镜像（Image）：** 类似于面向对象编程中的“类”，是一个只读的模板，包含了运行应用程序所需的所有代码、运行时、库和环境变量（如本实验拉取的 `python:3.10-slim`）。
- **容器（Container）：** 类似于“实例”，是镜像运行时的实体。容器之间相互隔离，拥有自己的文件系统、网络和进程空间。

**二、 核心命令实操记录**

1. **拉取镜像：** `docker pull python:3.10-slim`
2. **查看列表：** 使用 `docker images` 查看本地镜像；使用 `docker ps -a` 查看容器状态。
3. **挂载与运行：** 使用 `-v` 参数将宿主机当前目录挂载到容器内，成功运行并输出测试信息。
   *执行命令：* `docker run -it --rm -v ${PWD}:/app -w /app python:3.10-slim python -c "print('Hello AI-Lab Docker')"`
   ![屏幕截图 2026-11-09 215915](C:\Users\17529\Desktop\AI-lab\Task06\屏幕截图 2026-11-09 215915.png)
4. **生命周期管理：** 成功使用 `docker stop` 和 `docker rm` 停止并清理了测试容器。

**三、 编写 Dockerfile 与构建专属镜像**

1. **Dockerfile 源码：**

```
FROM python:3.10-slim
WORKDIR /app
RUN echo "print('Hello from my custom Docker image!')" > app.py
CMD ["python", "app.py"]
```

1. **构建镜像：**
   *执行命令：* `docker build -t my-python-app:v1 .`
   ![屏幕截图 2026-11-09 220343](C:\Users\17529\Desktop\AI-lab\Task06\屏幕截图 2026-11-09 220343.png)
2. **运行自建容器：**
   *执行命令：* `docker run --rm my-python-app:v1`
   ![屏幕截图 2026-11-09 220420](C:\Users\17529\Desktop\AI-lab\Task06\屏幕截图 2026-11-09 220420.png)