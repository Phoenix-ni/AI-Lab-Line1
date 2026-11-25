# Linux终端基础与常用命令行实战

> 文档说明：在终端完成指定操作序列（创建指定目录树、批量重命名文件、过滤指定日志文本并输出为新文件），将执行历史（history）与操作截图整理为 Markdown 文档提交。

## 一、实验环境

| 项目 | 内容 |
| --- | --- |
| 连接方式 | Xshell 8 (Build 0119) SSH 远程连接 |
| 服务器地址 | 192.168.29.128:22 |
| 操作系统 | Rocky Linux（主机名 rocky） |
| 登录用户 | gongxi（命令提示符 `[gongxi@rocky ~]$`） |
| 会话起始目录 | `/home/gongxi` |

## 二、任务总览

三个任务的操作均在 `/home/gongxi/project/` 目录下完成，对应 history 中的命令编号如下：

| 任务 | 主要内容 | 涉及命令 | history 编号 |
| --- | --- | --- | --- |
| 任务一：创建指定目录树 | 用 `mkdir -p` 一次性创建多级目录 `project/data/bin/file`，并用 `ll`、`pwd` 验证 | `mkdir`、`cd`、`ll`、`pwd` | 3 ~ 6 |
| 任务二：批量重命名 | 将 `data` 改为 `data1`，再把 `bin` 下的 `file` 改为 `data2`，用 `ls -R` 递归验证 | `mv`、`ls -R` | 19 ~ 29 |
| 任务三：过滤日志文本 | 创建日志 `tast.log`，用 `grep` 过滤关键字 `12345` 并重定向输出到新文件 `result` | `cat`、`grep`、输出重定向 `>` | 30 ~ 35 |
| 执行历史留存 | 用 `history > cmd.txt` 把全部操作记录导出为文件 | `history`、`>` | 36 |

## 三、任务一：创建指定目录树

### 3.1 操作截图

![任务一：创建目录树并验证](images/01-创建目录树.png)

### 3.2 执行过程

```bash
[gongxi@rocky ~]$ ll                 # 查看家目录，此时无 project 目录
总用量 0
drwxr-xr-x. 2 gongxi gongxi 6 10月 23 23:42 公共
...（公共/模板/视频/图片/文档/下载/音乐/桌面）

[gongxi@rocky ~]$ mkdir -p project/data/bin/file   # -p 递归创建多级目录
[gongxi@rocky ~]$ cd project/data/bin/file/
[gongxi@rocky file]$ ll              # 总用量 0：新目录为空，创建成功
[gongxi@rocky file]$ pwd
/home/gongxi/project/data/bin/file
```

### 3.3 要点说明

- `mkdir -p` 是创建多级目录的关键参数，无需逐层创建，也不存在时不会报错。
- 目录树结构如下：

```text
/home/gongxi/project/
└── data/
    └── bin/
        └── file/
```

- 用 `pwd` 确认当前所在路径，用 `ll` 确认目录内容（总用量 0 表示空目录，符合预期）。

## 四、任务二：批量重命名

### 4.1 操作截图

![任务二：重命名目录并用 ls -R 验证](images/02-批量重命名.png)

### 4.2 执行过程

```bash
[gongxi@rocky ~]$ cd project
[gongxi@rocky project]$ ls -R          # 重命名前：data → bin → file
.:
data

./data:
bin

./data/bin:
file

./data/bin/file:

[gongxi@rocky project]$ mv data data1                       # 第 1 次改名：data → data1
[gongxi@rocky project]$ mv data1/bin/file data1/bin/data2   # 第 2 次改名：file → data2
[gongxi@rocky project]$ ls -R
.:
data1

./data1:
bin

./data1/bin:
data2

./data1/bin/data2:
```

### 4.3 要点说明

- `mv 源路径 目标路径` 在同一目录内执行即为“重命名”，无需 `-r` 参数。
- 重命名嵌套目录时应写完整路径（如 `data1/bin/file`），否则容易改错层级。
- 用 `ls -R` 递归查看，可以直观确认整棵目录树的名称变化：`data` → `data1`，`file` → `data2`。
- 重命名后原路径 `data/bin/file` 不再存在，后续操作必须使用新路径。

## 五、任务三：过滤指定日志文本并输出为新文件

### 5.1 操作截图

![任务三：创建日志并用 grep 过滤输出到 result](images/03-过滤日志.png)

### 5.2 执行过程

```bash
[gongxi@rocky project]$ cd data1/bin/data2
[gongxi@rocky data2]$ cat>tast.log<<EOF      # 用 heredoc 写入多行日志
> 12345
> 67890
> 54321
> 09876
> EOF
[gongxi@rocky data2]$ cat test.log           # 文件名拼写错误，报“没有那个文件或目录”
cat: test.log: 没有那个文件或目录
[gongxi@rocky data2]$ cat tast.log           # 查看日志真实内容
12345
67890
54321
09876
[gongxi@rocky data2]$ grep "12345" tast.log>result   # 过滤关键字并重定向到新文件 result
[gongxi@rocky data2]$ cat result
12345
```

### 5.3 要点说明

- `cat > tast.log << EOF` 通过输入重定向 + 结束标记 `EOF` 直接生成多行日志文件，适合快速构造测试数据。
- `cat test.log` 报错是因为实际文件名是 `tast.log`（拼写不一致），也侧面验证了文件名必须严格匹配。
- `grep "12345" tast.log > result`：`>` 为覆盖式输出重定向，命令本身的标准输出不会打印到终端，因此需要再用 `cat result` 查看结果。
- 过滤结果是唯一包含 `12345` 的行，说明过滤与输出均正确；若需追加写入可改用 `>>`。

## 六、完整执行历史（history）

### 6.1 操作截图

![历史记录导出：history > cmd.txt](images/04-history.png)

### 6.2 导出命令

```bash
[gongxi@rocky data2]$ history > cmd.txt   # 将全部历史命令保存为 cmd.txt
[gongxi@rocky data2]$ cat cmd.txt         # 查看导出的历史
```

### 6.3 history 原文（编号 1 ~ 36）

```text
    1  su - root
    2  ll
    3  mkdir -p project/data/bin/file
    4  cd project/data/bin/file/
    5  ll
    6  pwd
    7  cd project
    8  cd~
    9  cd ~
   10  cd project
   11  ll
   12  mv data/data1/
   13  cd ~
   14  cd project
   15  ll
   16  mv project/data project/data1
   17  cd project
   18  ll
   19  mv data data1
   20  mv bin data2
   21  mv data1/bin/file data1/bin/data2
   22  mv data1 data
   23  mv data/bin/data2 data/bin/file
   24  ls -R
   25  cd project
   26  ls -R
   27  mv data data1
   28  mv data1/bin/file data1/bin/data2
   29  ls -R
   30  cd data1/bin/data2
   31  cat>tast.log<<EOF
12345
67890
54321
09876
EOF
   32  cat test.log
   33  cat tast.log
   34  grep "12345" tast.log>result
   35  cat result
   36  history > cmd.txt
```

### 6.4 历史命令与任务对应关系

| 编号 | 命令 | 归属任务 | 说明 |
| --- | --- | --- | --- |
| 2 ~ 6 | `ll` / `mkdir -p project/data/bin/file` / `cd` / `pwd` | 任务一 | 创建并验证目录树 |
| 7 ~ 18 | `cd project` / `ll` / `mv ...` | 任务二（试做） | 早期改名尝试，如 `mv project/data project/data1` |
| 19 ~ 21 | `mv data data1` / `mv bin data2` / `mv data1/bin/file data1/bin/data2` | 任务二（试做） | 先后尝试的单层、嵌套改名 |
| 22 ~ 23 | `mv data1 data` / `mv data/bin/data2 data/bin/file` | 任务二（还原） | 将试改结果改回原名 |
| 24 ~ 29 | `ls -R` / `mv data data1` / `mv data1/bin/file data1/bin/data2` | 任务二（最终） | 正式完成两处重命名并递归验证 |
| 30 ~ 35 | `cd data1/bin/data2` / `cat>tast.log<<EOF` / `cat` / `grep "12345" tast.log>result` / `cat result` | 任务三 | 造数据、排错、过滤并输出新文件 |
| 36 | `history > cmd.txt` | 历史留存 | 导出完整操作记录 |

### 6.5 输入错误与修正记录

| 现象 | 原因 | 处理方式 |
| --- | --- | --- |
| `mv data/data1/`（编号 12）执行异常 | 缺少空格，且源路径与目标写在同一参数中 | 后续改用 `mv data data1` |
| `mv project/data project/data1`（编号 16） | 在 `project` 目录内又写了 `project/` 前缀，路径重复 | 改为在 `project` 内执行 `mv data data1` |
| `mv bin data2`（编号 20） | 只改 `bin`，未按要求改 `bin` 下的 `file` | 用 `mv data1/bin/file data1/bin/data2` 修正 |
| `cat: test.log: 没有那个文件或目录`（编号 32） | 文件名拼写错误（应为 `tast.log`） | 改用正确文件名 `cat tast.log` |
| history 中编号 24 之前目录已还原 | `data1 → data`、`data/bin/data2 → data/bin/file` 两次回改 | 最终以 27、28 两条命令重新完成改名 |

## 七、结论

1. 目录树可用一条 `mkdir -p project/data/bin/file` 创建完成，并用 `pwd`、`ll` 验证路径与内容。
2. 批量重命名使用 `mv` 逐项完成，配合 `ls -R` 递归核对层级；本例最终结构为 `project/data1/bin/data2`。
3. 日志过滤采用 `grep "关键字" 源文件 > 目标文件`，既能筛选文本，又能直接生成新文件，本次输出 `result` 中仅含 `12345`。
4. 通过 `history > cmd.txt` 将全部操作留痕为文件，便于复查与复现；history 中的试错命令也说明“先试做、再还原、最后定稿”的过程同样需要记录。
