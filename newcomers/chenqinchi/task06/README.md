# Task06 原生Function Call工具调用Agent
## 任务目标
实现大模型原生Function Call（函数调用）Agent。
不再由代码硬编码判断是否计算，交给大模型自主决策：
- 遇到数学计算需求 → 模型输出工具调用指令，本地执行calculator，结果回传给模型，模型整理自然语言回复
- 普通问答/知识提问 → 不调用工具，直接返回回答

## 环境
- Python 3.11
- 依赖：openai SDK
- 平台：SiliconFlow，模型：deepseek-ai/DeepSeek-V3（支持原生function call）
- 源：conda清华源 + pip清华源

## 文件清单
- agent_funcall.py：主程序代码
- task06_screenshot.png：运行截图
- README.md：任务说明文档

## 运行命令
```bash
conda activate task05
python agent_funcall.py