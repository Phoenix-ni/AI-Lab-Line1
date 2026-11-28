# 1. 基础镜像
FROM python:3.10-slim

# 2. 环境变量设置
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# 3. 设置容器内工作目录
WORKDIR /app

# 4. 创建非 root 用户
RUN groupadd -r appgroup && useradd -r -g appgroup appuser

# 5. 复制依赖清单并安装
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 6. 复制项目代码
COPY . .

# 7. 给非 root 用户目录权限
RUN chown -R appuser:appgroup /app

# 8. 切换到非 root 用户运行
USER appuser

# 9. 默认启动命令
CMD ["python", "main.py"]