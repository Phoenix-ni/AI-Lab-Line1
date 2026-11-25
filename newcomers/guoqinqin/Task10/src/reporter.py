import os

def generate_report(output_path, md_files, all_errors, all_stats):
    """生成 Markdown 格式的检查报告"""
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("# Markdown 文档检查报告\n\n")
        f.write(f"共扫描到 {len(md_files)} 个文件。\n\n")
        
        f.write("## 1. 死链接与损坏图片\n\n")
        if not all_errors:
            f.write("✅ 未发现死链接或损坏图片。\n\n")
        else:
            f.write("| 文件路径 | 错误信息 |\n|---|---|\n")
            for file, err in all_errors:
                f.write(f"| {file} | {err} |\n")
            f.write("\n")
            
        f.write("## 2. 标题层级统计\n\n")
        f.write("| 文件路径 | H1 | H2 | H3 | H4 | H5 | H6 |\n")
        f.write("|---|---|---|---|---|---|---|\n")
        for file, stats in all_stats.items():
            f.write(f"| {file} | {stats[1]} | {stats[2]} | {stats[3]} | {stats[4]} | {stats[5]} | {stats[6]} |\n")
