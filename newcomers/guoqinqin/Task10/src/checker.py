import re
import os

def check_links(file_path):
    """检查 Markdown 文件中的死链接和损坏图片"""
    errors = []
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 正则匹配 Markdown 链接 [text](url) 和图片 ![alt](src)
    # 匹配本地文件路径（排除以 http:// 或 https:// 开头的网络链接）
    pattern = r'!?\[.*?\]\((.*?)\)'
    matches = re.findall(pattern, content)
    
    base_dir = os.path.dirname(file_path)
    
    for link in matches:
        # 忽略网络链接和锚点
        if link.startswith('http://') or link.startswith('https://') or link.startswith('#'):
            continue
        
        # 处理相对路径
        target_path = os.path.join(base_dir, link)
        if not os.path.exists(target_path):
            errors.append(f"损坏的引用: {link}")
            
    return errors
