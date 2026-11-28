import re
from pathlib import Path
from urllib.parse import unquote

# 识别代码块和行内代码
CODE_RE = re.compile(r'```[\s\S]*?```|`[^`\n]*`')

# 识别图片
IMG_RE = re.compile(r'!\[(.*?)]\((.*?)\)')

# 识别链接：用 (?<!!) 排除前面带 ! 的，避免和图片重复
LINK_RE = re.compile(r'(?<!!)\[(.*?)]\((.*?)\)')

# 跳过外部地址的前缀
SKIP_PREFIX = ("http://", "https://", "mailto:", "tel:", "ftp://", "data:")

def clean_url(raw:str) -> str:
    '''清除URL中的标题'''
    raw = raw.split(' "')[0].split(' "')[0]
    return raw

def to_local_path(base: Path, raw: str):
    """把 URL 片段转成本地路径，外部链接、纯锚点返回 None"""
    raw = raw.strip()
    # 排除外部链接和纯锚点
    if not raw or raw.startswith("#"):
        return None
    if raw.lower().startswith(SKIP_PREFIX):
        return None

    # 去掉锚点和查询串，再解码转义
    path_part = raw.split("#", 1)[0].split("?", 1)[0]
    path_part = unquote(path_part)
    if not path_part:
        return None

    return Path(base).joinpath(path_part).resolve()

def check(file_path: Path):
    '''检查是否有死链接、死图片'''
    content = file_path.read_text(encoding="utf-8")
    content = CODE_RE.sub("", content)     

    base = file_path.parent
    broken_links, broken_images = [], []

    for match in IMG_RE.findall(content):
        # 取元组最后一个元素作为路径
        raw = match[-1].strip()
        raw = clean_url(raw)
        target = to_local_path(base, raw)
        if target and not target.exists():
            broken_images.append(raw)

    for match in LINK_RE.findall(content):
        raw = match[-1].strip()
        raw = clean_url(raw)
        target = to_local_path(base, raw)
        if target and not target.exists():
            broken_links.append(raw)
            
    return broken_links, broken_images

