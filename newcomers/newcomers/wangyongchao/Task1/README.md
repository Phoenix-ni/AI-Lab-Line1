# AI-Lab 准入任务实战通关记录

> 申请人：[你的名字]
> 日期：2026年10月16日
> 环境：Windows / Trae CN / Python 3.13

## 一、 阶段一：开发工具链与环境搭建

### 1. 现代 AI IDE 配置 (Task 01 - a)
由于未成年实名限制，我无法注册外部大模型 API（如 SiliconFlow、DeepSeek）。因此我选择了**字节跳动推出的 Trae CN** 作为核心开发环境，它开箱即用，内置大模型，完美满足了开发需求。
- **插件安装**：安装了 Python、Prettier 等，并安装了 Trae 推荐的 `BasedPyright`（类型检查）插件，实现了现代化的代码提示环境。

### 2. 终端/CLI AI 协同工具实战 (Task 01 - b)
因为缺乏外部 API Key，我采用了 **Trae AI 助手 + 网页版 DeepSeek + 本地 PowerShell 终端** 的替代方案，通过真实的终端报错来测试 AI 的协同调试能力。

**实战案例：打印 1-100 的质数 `print_primes.py`**
1. 让 Trae 编写 Python 脚本，在终端运行时出现 `[Errno 2] No such file or directory` 路径报错，利用 Trae AI 对话窗口进行排查。
2. 修复路径后，又遇到了 `SyntaxError: expected ':'` 语法错误，根据 AI 提示修复了第 1 行 `def is_prime(n):` 缺失的冒号。
3. 安装 Python 扩展后，最终在 PowerShell 终端成功运行了 `print_primes.py`，输出了 1-100 之间的全部 25 个质数。

## 二、 交付物截图

### 1. IDE/工作台工作界面截图
![IDE配置截图](此处粘贴你之前带设置面板的截图)

### 2. 终端/CLI协同交互与成功运行截图
![终端成功运行截图](此处粘贴你刚才这张完美的成功运行截图)

## 三、 后续进阶计划
虽然当前无法申请云端 API，但我已经掌握了利用 Trae 辅助开发、排查终端报错的核心能力。下一步我计划学习 **Ollama**，在本地部署开源小模型（如 Qwen2.5），以彻底打通本地 API 调用的环节。
