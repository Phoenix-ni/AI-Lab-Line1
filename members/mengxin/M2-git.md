\# M2：我的 Git 协作实践



\## 环境与流程

我在 Windows Git Bash 中操作。

仓库后来移动到 D:\\line\\Line\\AI-Lab-Line1。

原仓库是 Phoenix-ni/AI-Lab-Line1，

我的 Fork 是 mx111-jiayou/AI-Lab-Line1。



我完成了 Fork、clone、创建 basic/mengxin 分支、

添加文件、commit、push，并向原仓库创建草稿 PR #1。

作业文件放在 newcomers/mengxin/ 下。



\## 实际提交

\- 5c8602b：添加 Bash 脚本、M1 笔记及换行规则。

\- 35618fd：补充 WSL2 验证记录和运行截图。



\## 踩坑与处理



\### 不在仓库目录中

在用户主目录执行 Git 命令，出现：

fatal: not a git repository。



进入正确仓库目录后继续操作。



\### 混用终端路径

Git Bash 使用 /d/...，WSL 使用 /mnt/d/...，

PowerShell 使用 D:\\...。

我混用路径时出现“找不到目录”，后来根据当前终端调整。



\### HTTPS 上传出现 403

上传时出现 Permission denied 和 HTTP 403。

清除缓存凭据并重新完成浏览器授权后，上传成功。

具体权限原因没有进一步确认。



\### HTTPS 连接反复被重置

上传第二次提交时，反复出现 Connection was reset。

我改为测试 SSH：



```bash

ssh -T git@github.com

```



返回的认证账号是 mx111-jiayou。



随后修改远程地址并上传：



```bash

git remote set-url origin git@github.com:mx111-jiayou/AI-Lab-Line1.git

git push

```



上传成功，远程分支从 5c8602b 更新到 35618fd。



\## 我的理解

commit 保存本地版本，push 将提交上传到远程。

本地提交成功但上传失败时，不需要重新提交同样的内容。

向同一分支继续 push，会更新已有 PR。



\## 待完成

草稿 PR 尚待转为正式评审。

收到组长意见后，我会在同一分支修改、提交并上传。

