# Task 06 最小 Dockerfile：把 app.py 打包成可分发镜像
# 基础镜像：官方 Python 3.10 精简版（约 45 MB）
FROM python:3.10-slim

# 容器内工作目录
WORKDIR /app

# 只复制脚本本身，利用层缓存
COPY app.py .

# 容器启动时执行的默认命令
CMD ["python", "app.py"]
