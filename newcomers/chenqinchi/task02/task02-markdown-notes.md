# AI-Lab 通识学习计划与环境踩坑记录

> **路线方向**：Line1 文档智能与知识库
> **周期**：30天上限，尽量提前验收
> **创建日期**：2026-10-25

---

## 一、通识任务总排期

| 任务编号 | 任务名称 | 预估耗时 | 验收状态 |
| :------: | :------- | :------: | :------: |
| Task01 | 开发工具链与基础环境搭建 | 3h | ✅ 已完成 |
| Task02 | Markdown 规范排版与笔记系统 | 2h | ✅ 已完成 |
| Task03 | Linux 终端基础 | 4h | 待启动 |
| Task04 | Git 版本管理 + GitHub | 3h | 待启动 |
| Task05 | Conda 虚拟环境 | 2h | 待启动 |
| Task06 | Docker 初探 | 2h | 待启动 |

---

## 二、环境搭建记录（Task01）

### 2.1 工具清单

- **IDE**：VSCode + WSL2
- **AI Agent**：DSH（终端内调用）
- **模型 API**：SiliconFlow（硅基流动）
- **远程仓库**：GitHub

### 2.2 配置步骤

1. Windows 启用 WSL2，安装 Ubuntu
2. VSCode 安装插件：WSL、GitLens、Markdown All in One
3. 配置 SiliconFlow API Key
4. 生成 SSH Key 并添加到 GitHub

### 2.3 环境截图

![VSCode插件界面截图](./screenshots/extensions_1.jpg)

![DSH终端启动截图](./screenshots/dsh_terminal_start .jpg)

---

## 三、Markdown 语法示例

### 3.1 代码块

```bash
# 查看当前目录
pwd

# 列出文件
ls -la

# 创建目录
mkdir -p ailab/task03
