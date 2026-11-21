import re

def parse_headings(file_path):
    """解析 Markdown 文件，统计标题层级并提取标题内容"""
    heading_stats = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    headings_list = []
    
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    for line in lines:
        # 正则匹配 1-6 级标题 (例如: # 标题, ## 标题)
        match = re.match(r'^(#{1,6})\s+(.*)', line.strip())
        if match:
            level = len(match.group(1))
            title = match.group(2).strip()
            heading_stats[level] += 1
            headings_list.append((level, title))
            
    return heading_stats, headings_list
