**Task 05：Conda 虚拟环境隔离与镜像源加速配置 操作记录**

**一、 Conda 镜像源配置截图**
![屏幕截图 2026-11-09 134020](C:\Users\17529\Desktop\AI-lab\Task05\屏幕截图 2026-11-09 134020.png)
*附：核心配置命令记录*

```bash
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
conda config --set show_channel_urls yes
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```

**二、 创建指定 Python 版本的独立环境**
![屏幕截图 2026-11-09 135358](C:\Users\17529\Desktop\AI-lab\Task05\屏幕截图 2026-11-09 135358.png)
*操作记录：*

1. 创建环境：`conda create -n py310 python=3.10 -y`
2. 激活环境：`conda activate py310`
3. 验证版本：`python --version` （输出 Python 3.10.22）
4. 退出环境：`conda deactivate`

**三、 环境列表查看**
![屏幕截图 2026-11-09 135826](C:\Users\17529\Desktop\AI-lab\Task05\屏幕截图 2026-11-09 135826.png)
*操作记录：*
执行 `conda env list`，可清晰看到 `base` 和 `py310` 两个隔离环境，证明环境创建成功。

**四、 依赖导出与复现**

![屏幕截图 2026-11-09 140855](C:\Users\17529\Desktop\AI-lab\Task05\屏幕截图 2026-11-09 140855.png)

![屏幕截图 2026-11-09 141116](C:\Users\17529\Desktop\AI-lab\Task05\屏幕截图 2026-11-09 141116.png)

*操作记录：*

1. 在 `py310` 环境下安装测试包：`pip install requests`
2. 导出依赖：`pip freeze > requirements.txt`
3. 复现依赖验证：`pip install -r requirements.txt` （提示已满足依赖）

*注：已掌握环境删除命令 conda remove -n py310 --all，本次实操为保留环境故未执行。*