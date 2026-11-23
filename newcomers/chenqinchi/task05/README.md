# Task05 工具调用Agent（计算器）
## 任务目标
实现一个具备工具调用能力的AI Agent，内置计算器工具。
Agent自动判断用户输入：
- 如果包含 `+ - * /` 四则运算符号，触发计算器工具，返回计算结果
- 如果是普通文本对话，交给DeepSeek大模型回答

## 环境
- Python 3.11
- 依赖：openai SDK
- 平台：SiliconFlow，模型：deepseek-ai/DeepSeek-V3
- 源：已配置conda清华源 + pip清华源

## 文件清单
- agent.py：主程序
- run_result.png：运行截图
- README.md：任务文档

## 运行命令
```bash
conda activate task05
python agent.py