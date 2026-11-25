# M5：成绩数据清洗与统计

## 项目功能
读取练习用 scores.csv，排除无效和重复记录，
输出清洗后的 CSV 和统计结果 JSON。

本项目使用人工编写的练习数据，不是真实学生成绩。

## 环境
Python 3.10，仅使用标准库，无需安装第三方依赖。

## 运行方法
在仓库根目录执行：

```powershell
python newcomers/mengxin/M5-data/main.py
```

脚本从自身所在目录读取 scores.csv。
每次运行会覆盖 clean_scores.csv 和 summary.json。

## 清洗规则
- 去除姓名和成绩两端的空格。
- 排除姓名或成绩为空的记录。
- 排除无法转换为数字的成绩。
- 排除不在 0～100 范围内的成绩。
- 按清理后的姓名与数值成绩去重。

同一姓名但不同成绩会保留为不同记录。

## 本次实际结果

| 指标 | 结果 |
|---|---:|
| 原始记录 | 8 |
| 有效记录 | 4 |
| 排除记录 | 4 |
| 平均分 | 78.75 |
| 最高分 | 92 |
| 最低分 | 60 |

## 输出文件
- clean_scores.csv：清洗后的姓名和成绩。
- summary.json：记录数量、平均分、最高分、最低分。

## 实际遇到的问题
我最初把文件夹命名为 M5-date，并放在 newcomers 下，
运行时出现找不到 main.py 的错误。

查看 VSCode 文件树后，我将文件夹改名为 M5-data，
并移动到 newcomers/mengxin/ 下，再运行成功。

## 当前局限
输入必须是 UTF-8 编码的 CSV，并包含 name、score 两列。
目前还没有针对缺少表头或文件损坏提供友好的错误提示。
没有有效记录时，平均分、最高分和最低分输出为 null。
## Docker 运行

保持 Docker Desktop 运行，在仓库根目录执行：

```powershell
docker build -t ailab-mengxin-scores newcomers/mengxin/M5-data
docker run --rm ailab-mengxin-scores
```

此方式使用镜像自带的数据，输出文件位于容器内部，
容器退出后被删除。

如需将结果保存到电脑，在 Windows PowerShell 中执行：

```powershell
docker run --rm --mount "type=bind,source=$($PWD.Path)\newcomers\mengxin\M5-data,target=/app" ailab-mengxin-scores
```

此方式使用本机目录中的代码和数据，并覆盖该目录内的输出文件。