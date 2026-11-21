# 使用官方轻量级 Python 3.10 镜像
FROM python:3.10-slim

# 设置容器内的工作目录
WORKDIR /app

# 先复制依赖文件，利用 Docker 缓存加速
COPY requirements.txt .

# 安装依赖（如果有的话）
RUN pip install --no-cache-dir -r requirements.txt

# 将当前目录下的所有文件复制到容器的 /app 目录
COPY . .

# 设置容器启动时的默认命令，即运行我们的 CLI 工具，默认扫描 /app 目录
ENTRYPOINT ["python3", "main.py", "-d", "/app", "-o", "/app/docker_report.md"]
