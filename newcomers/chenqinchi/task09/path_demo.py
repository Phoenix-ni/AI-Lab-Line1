import os

# ① 获取当前脚本的绝对完整路径
script_full = os.path.abspath(__file__)
# ② 获取脚本所在的文件夹（也就是task08文件夹）
script_dir = os.path.dirname(script_full)
# ③ 获取终端当前所在目录（你的终端现在在AI-Lab）
terminal_dir = os.getcwd()

print("======== Task08 路径对比演示 ========")
print(f"脚本完整路径：{script_full}")
print(f"脚本所在文件夹：{script_dir}")
print(f"终端工作目录：{terminal_dir}")
print("-" * 40)

# 拼接文件路径：在task08文件夹下创建test.txt
target_file = os.path.join(script_dir, "test.txt")

# 写入文件
with open(target_file, "w", encoding="utf-8") as f:
    f.write("Task08 路径练习\n")
    f.write("文件自动保存在py脚本所在文件夹\n")

print(f"✅ 文件创建成功，路径：{target_file}")
