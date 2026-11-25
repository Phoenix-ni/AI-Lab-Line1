# Task 03：Linux 终端基础与常用命令行实战

## 1. 环境说明
- 系统：Ubuntu 24.04.5 LTS
- Shell：bash
- 操作目录：`~/ai-lab/task03`

## 2. 操作序列一：创建指定目录树
### 命令
```bash
mkdir -p project/{src/{core,utils},logs/archive,docs,tests}
find project -type d | sort
```
### 结果
```bash
project
project/docs
project/logs
project/logs/archive
project/src
project/src/core
project/src/utils
project/tests
```

### 截图
![屏幕截图 2026-11-03 195841](C:\Users\17529\Desktop\AI-lab\Task03\屏幕截图 2026-11-03 195841.png)

## 3. 操作序列二：批量重命名文件
### 造样例文件
```bash
for i in {1..5}; do echo "content $i" > draft_$i.txt; done
```
### 批量重命名
```bash
for f in draft_*.txt; do mv "$f" "${f/draft_/module_}".md; done
ls
```
### 结果与截图
![屏幕截图 2026-11-03 200439](C:\Users\17529\Desktop\AI-lab\Task03\屏幕截图 2026-11-03 200439.png)

## 4. 操作序列三：过滤日志并输出新文件
### 原始日志样例
```bash
2024-05-01 10:00:01 INFO  service started
2024-05-01 10:00:05 ERROR failed to connect db: timeout
2024-05-01 10:00:07 INFO  retry connection
2024-05-01 10:00:12 ERROR disk quota exceeded
2024-05-01 10:00:20 WARN  memory usage 85%
2024-05-01 10:00:31 INFO  health check ok
2024-05-01 10:00:44 ERROR null pointer at handler.py:42
```

### 过滤命令
```bash
grep "ERROR" assets/sample.log > assets/error_filtered.log
wc -l assets/error_filtered.log
```
### 输出结果
```bash
2024-05-01 10:00:05 ERROR failed to connect db: timeout
2024-05-01 10:00:12 ERROR disk quota exceeded
2024-05-01 10:00:44 ERROR null pointer at handler.py:42
```

### 截图
![屏幕截图 2026-11-03 200720](C:\Users\17529\Desktop\AI-lab\Task03\屏幕截图 2026-11-03 200720.png)

## 5. 系统状态与权限命令
```bash
ps aux | head -n 5
df -h
free -m
chmod 644 assets/sample.log && ls -l assets/
```
![屏幕截图 2026-11-03 200904](C:\Users\17529\Desktop\AI-lab\Task03\屏幕截图 2026-11-03 200904.png)

## 6. 执行历史（history）
```bash
history | tail -n 60 > task03_history.txt
```
![屏幕截图 2026-11-03 223528](C:\Users\17529\Desktop\AI-lab\Task03\屏幕截图 2026-11-03 223528.png)

## 7. 排错记录（Troubleshooting）
- 问题：`tree` 命令不存在 → 解决：`sudo apt install tree`
- 问题：`rename` 命令不存在 → 解决：改用 for 循环 + mv
- 问题：Windows 换行符导致 grep 匹配异常 → 解决：`dos2unix` 或 `sed -i 's/\r$//'`
