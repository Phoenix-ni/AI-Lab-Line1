import os

def find_markdown_files(target_dir):
    """扫描指定目录，返回所有 .md 文件的绝对路径列表"""
    md_files = []
    # 遍历目录
    for root, dirs, files in os.walk(target_dir):
        for file in files:
            if file.endswith('.md'):
                md_files.append(os.path.join(root, file))
    return md_files
