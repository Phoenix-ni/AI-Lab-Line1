import argparse
import sys
from src.scanner import find_markdown_files
from src.checker import check_links
from src.parser import parse_headings
from src.reporter import generate_report

def main():
    parser = argparse.ArgumentParser(description="Markdown 文档检查与清洗工具")
    parser.add_argument("-d", "--dir", type=str, required=True, help="指定要扫描的目录路径")
    parser.add_argument("-o", "--output", type=str, default="report.md", help="指定输出报告的路径（默认 report.md）")
    args = parser.parse_args()

    target_dir = args.dir
    output_path = args.output
    print(f"开始扫描目录: {target_dir}")
    
    md_files = find_markdown_files(target_dir)
    print(f"共发现 {len(md_files)} 个 Markdown 文件，正在分析...")
    
    all_errors = []
    all_stats = {}
    
    for f in md_files:
        errors = check_links(f)
        for err in errors:
            all_errors.append((f, err))
            
        stats, _ = parse_headings(f)
        all_stats[f] = stats
        
    generate_report(output_path, md_files, all_errors, all_stats)
    print(f"\n✅ 检查完成！报告已生成: {output_path}")

if __name__ == "__main__":
    main()
