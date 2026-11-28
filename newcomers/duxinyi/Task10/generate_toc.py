import re
import html
import os
from pathlib import Path
from pathlib import PurePosixPath

def slugify(text):
    '''将文本转化为符合markdown规范字符串'''
    # 解码html，去掉首尾空白，英文文本转小写
    text = html.unescape(text).strip().lower()
    # 删除特殊字符
    text = re.sub(r"[^\w\s-]", "", text) 

    return re.sub(r"\s+", "-", text).strip("-")


def generate_toc(headings,doc_path:Path,toc_path:Path):
    '''根据目录生成索引'''
    lines = [""]
    used = {}
    for h in headings:
        # 读取标题
        name = html.unescape(h["name"]).strip()
        if not name:
            continue

        # 生成锚点
        base = slugify(name) 
        # 如果重名，添加后缀区分
        n = used.get(base, 0)
        used[base] = n + 1
        if n == 0:
            anchor = base 
        else:
            f"{base}-{n}"
        # 生成索引   
        indent = "  " * max(h["level"] - 1, 0)
        if doc_path and toc_path:
            # 将相对路径反斜杠转为正斜杠
            link_path = Path(os.path.relpath(doc_path,start=toc_path.parent)).as_posix()
            lines.append(f"{indent}- [{name}]({link_path}#{anchor})")
        else:
            lines.append(f"{indent}- [{name}](#{anchor})")
    return "\n".join(lines)