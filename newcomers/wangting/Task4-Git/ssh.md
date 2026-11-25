# Github SSH Key 配置记录
>场景：Windows用户名含中文，将SSH 密钥放在 D 盘自定义目录；使用 Git Bash、VSCode 连接 GitHub，解决端口 22 被封、配置不生效及VSCode 使用问题。
## 一、问题汇总
1.本机 Windows 用户名为中文，默认 C 盘用户目录会出现路径乱码，密钥生成失败。
- 原因：Git Bash 对中文用户名的原生 OpenSSH 路径解析异常。
- 解决方案：将密钥存放至 D 盘，避开中文路径。 

2.ssh -T git@github.com  报  port 22: Connection refused 
- 原因：网络封禁 GitHub 的 22 SSH 端口。
- 方案：改用 443 端口，连接  ssh.github.com:443 。

3. 密钥放在 D 盘，直接  git push / pull  提示  Permission denied (publickey) 
- 原因：SSH 默认只会读取  ~/.ssh/  下的配置，不会自动加载 D 盘的  config  和私钥。

4. 单独  ssh -F /d/git/ssh/config -T git@github.com  认证成功，但直接  git push  失败
- 原因：Git 默认不会带上  -F  指定配置文件参数。
 
## 二、生成密钥
在 D 盘提前建好文件夹 D:\git\ssh
```
ssh-keygen -t ed25519 -C "邮箱"
```
保存路径填写：/d/git/ssh/id_ed25519
密码：不设置私钥密码
上传公钥到 GitHub：
```
cat /d/git/ssh/id_ed25519.pub
```
步骤：GitHub 头像 → Settings → SSH and GPG keys → New SSH key。
 
## 三、编写 SSH 配置文件  /d/git/ssh/config 
ssh-config
```
    Host github.com ssh.github.com
        Hostname ssh.github.com
        Port 443
        User git
        IdentityFile /d/git/ssh/id_ed25519
```
同时匹配  github.com  和  ssh.github.com ，统一走 443 端口。
 
## 四、Git 全局配置
 
VSCode 里面的 Git Bash 终端，可以直接  git push  /  git pull ，不用每次加  GIT_SSH_COMMAND 
  
1.设置全局 git 使用指定 ssh 配置
```
git config --global core.sshCommand "ssh -F /d/git/ssh/config"
```
2.校验是否写入成功
```
git config --global --get core.sshCommand
```
输出： ssh -F /d/git/ssh/config  代表成功。
 