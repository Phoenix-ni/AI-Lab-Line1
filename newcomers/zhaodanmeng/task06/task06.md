# 截图
- ![1](3.png)
- ![2](4.png)
# 报错
- ![3](1.png)
  - 原因：命令输入时换行了
- ![4](2.png)
  - 原因：Dockerfile没有成功创建
  - 重新创建：
  ```bash
  cat > Dockerfile <<'EOF'
  ROM python:3.10-slim
  WORKDIR /app
  CMD ["python", "-c", "print('Hello AI-Lab Docker')"]
  EOF
  ```