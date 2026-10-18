# Task 03 · GitHub 网页版提交步骤（手动）

> 适用场景：这台电脑没有仓库、不想折腾 git 命令行，直接用浏览器把文件传上去。
> 前置条件：浏览器能正常打开 GitHub（校园网直连不通，需开 VPN 或用手机热点）。

---

## 第 0 步 · 先确认要传的东西在哪

```
E:\Task03-提交\task03\          ← 整个 task03 文件夹，13 个文件，505 KB
├─ Task03-Linux命令行实战.md     ← 主文档
├─ assets\                       ← 4 张截图
└─ lab\                          ← history、脚本、日志
```

**注意：要拖的是 `task03` 这个文件夹本身**，不是里面的散文件 —— 这样 GitHub 上才会形成 `task03/` 目录。

---

## 第 1 步 · 打开仓库并确认分支

1. 浏览器登录 GitHub
2. 打开你的课程仓库：`https://github.com/你的用户名/AI-Lab-Line1`
3. 看左上角 **Branch 下拉框**（默认显示 `main`）

**情况 A：下拉列表里已有 `basic/duxinyi`**
→ 直接选中它，跳到第 2 步。

**情况 B：没有这个分支**（大概率是这种情况，因为之前的 `git push` 失败过，远程还没建）
→ 点击分支下拉框 → 在输入框里输入 `basic/duxinyi` → 下方会出现
　**「Create branch: basic/duxinyi from 'main'」** → 点它。
→ 创建成功后页面会自动切到新分支。

> 如果老师没要求用自己的分支，也可以跳过这步，直接提交到 `main`。但按你之前的习惯（`basic/duxinyi`），建议建分支。

---

## 第 2 步 · 进入上传页面

确认页面左上角显示的是 **`basic/duxinyi`**（不是 main），然后：

1. 点右上方的 **`Add file`** 按钮
2. 选 **`Upload files`**

---

## 第 3 步 · 把文件夹拖进去

1. 打开资源管理器，进到 `E:\Task03-提交\`
2. **把 `task03` 文件夹整个拖到浏览器页面的虚线框里**
3. 等待上传列表出现 —— 应该显示 13 个文件，路径类似：
   ```
   task03/Task03-Linux命令行实战.md
   task03/assets/01-session-full.png
   task03/lab/command-history.txt
   ...
   ```

**常见问题**：
- 拖拽没反应 → 换 Chrome 或 Edge（Firefox 对文件夹拖拽支持一般）
- 只能选文件、不能拖文件夹 → 用下方的 `choose your files` 多选文件，但**会丢失目录结构**（所有文件平铺在仓库根目录，图片会裂）。这种情况建议改用第 6 步的备选方案。

---

## 第 4 步 · 写提交说明并提交

页面底部：

1. **Commit message** 填：
   ```
   feat: Task03 Linux 终端命令行实战、执行历史与踩坑记录
   ```
2. 下面选 **`Commit directly to the basic/duxinyi branch`**（不要选 "Create a new branch"）
3. 点绿色按钮 **`Commit changes`**

---

## 第 5 步 · 验证（很重要，别跳过）

1. 回到仓库首页，确认分支仍是 `basic/duxinyi`
2. 点开 `task03` 文件夹 → 点开 `Task03-Linux命令行实战.md`
3. 检查三件事：
   - **图片是否正常显示**（4 张都要能看到；裂图说明 assets 没传对）
   - 「三、执行历史」的代码块是否可读
   - 表格是否渲染成表格（不是一堆竖线）
4. 复制当前页面 URL，作为作业提交链接，例如：
   `https://github.com/你的用户名/AI-Lab-Line1/tree/basic/duxinyi/task03`

---

## 备选方案 · 拖拽不成功怎么办

### 方案一 · GitHub Desktop（图形界面，最省心）

1. 下载安装：`https://desktop.github.com/`
2. 登录 GitHub 账号
3. `File → Clone repository` → 选 `AI-Lab-Line1` → 克隆到 `E:\AI-Lab-Line1`
4. 把 `E:\Task03-提交\task03` 整个文件夹**复制**进 `E:\AI-Lab-Line1\`
5. 回到 GitHub Desktop：左侧会列出变更 → 左下角填提交说明 → 点 **Commit to basic/duxinyi**
6. 点右上角 **Push origin** → 完成

> 第一次 Push 会要求登录，用浏览器授权即可，**不需要手动弄 Token**。

### 方案二 · 网页逐个上传（最笨但一定能成）

如果连文件夹都拖不进去，就在网页上先建目录：

1. `Add file → Create new file`
2. 文件名输入 `task03/assets/.gitkeep`（GitHub 会自动把 `task03/assets/` 建成目录）
3. 提交后进入该目录，再 `Add file → Upload files` 传图片
4. `lab` 目录同样处理

麻烦，但遇到工具限制时能兜底。

---

## 上传限制（不会碰到，但知道一下）

| 限制 | 数值 | 我们的情况 |
| :--- | :--- | :--- |
| 单文件大小 | 25 MB | 最大 167 KB ✅ |
| 单次上传文件数 | 100 个 | 13 个 ✅ |

---

## 交作业前最后自检

- [ ] 分支是 `basic/duxinyi`（或老师指定的分支）
- [ ] 仓库里能看到 `task03/` 目录，里面有 md、assets、lab
- [ ] 点开 md 文件，4 张图都能显示
- [ ] 提交说明写清楚了（不是默认的 "Add files via upload"）
- [ ] 把 md 文件的页面链接发给老师
