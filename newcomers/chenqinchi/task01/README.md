# Task01 开发工具链与基础环境搭建
## 一、任务简介
本任务为 AI-Lab 入门基础任务，目标是完成本地开发工具链部署、终端AI Agent环境搭建、大模型API连通调试，搭建可自动化辅助编程的本地AI开发环境。

## 二、技术栈说明
- IDE：VSCode
- 运行环境：Python、Node.js
- 版本控制：Git
- API平台：SiliconFlow 硅基流动
- 初始Agent：DSH（DeepSeek Harness，自定义profile：chi）
- 备选/当前可正常运行Agent：Aider
  - Aider调用模型：DeepSeekV3
- 连通测试脚本 `api_test.py` 使用模型：Qwen/Qwen2.5-7B-Instruct

## 三、搭建过程记录
1. **初始搭建（DSH阶段）**
最初完成环境搭建，选用DSH作为CLI Agent，配置SiliconFlow密钥、chi配置文件，完成终端交互、API连通测试。
仓库内 `screenshots` 目录中 `dsh_` 开头截图，就是当时DSH环境的验收留存截图。

2. **环境故障原因**
Windows自动系统更新，重置用户环境变量，DSH的配置、运行环境失效，无法再次启动DSH。
但是当时DSH的截图文件、api_test.py脚本被保留在仓库内。

3. **备选方案验证（Aider阶段）**
为保证任务可正常验收，启用备选Agent Aider，重新配置：
- Aider对接SiliconFlow，指定调用DeepSeekV3
- 成功实现读取本地文件、新建/修改代码、执行终端命令，Agent功能验证通过
- 新增Aider交互截图存入 `screenshots` 文件夹

> 总结：DSH为最初方案，历史截图存档保留；当前可正常使用的CLI Agent为Aider，二者功能定位一致，满足任务验收要求。

## 四、各工具作用
1. VSCode：代码编辑器，管理项目、编写代码、预览Markdown
2. Git：版本控制，记录代码变更，后续提交PR评审
3. Node.js：CLI工具依赖运行环境
4. Python：运行API连通测试脚本，验证接口链路
5. DSH（初始Agent）：终端AI编程智能体（当前环境无法启动，历史留存）
6. Aider（当前可用Agent）：终端AI编程智能体，读取项目代码、辅助开发排错，通过SiliconFlow调用DeepSeekV3
7. SiliconFlow API：统一大模型调用通道，提供推理服务

## 五、交付物清单
- api_test.py 接口连通测试脚本
- README.md 任务说明文档
- screenshots/ 截图目录
  - 旧截图：dsh系列截图、环境版本截图、api代码截图、api返回结果截图
  - 新增截图：Aider终端交互成功截图