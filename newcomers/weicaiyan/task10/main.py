import argparse
from md_checker import check_markdown_files

def main():
    parser = argparse.ArgumentParser(description="Markdown 标题统计工具")
    parser.add_argument("-d", "--dir", type=str, default="./test_docs", help="指定要扫描的目录路径")
    args = parser.parse_args()

    print(f"正在扫描目录: {args.dir}")
    results = check_markdown_files(args.dir)
    
    if not results:
        print("未找到任何 Markdown 文件。")
        return

    print("\n--- 扫描结果 ---")
    for filename, stats in results.items():
        print(f"{filename}: 包含 {stats['H1']} 个一级标题，{stats['H2']} 个二级标题。")
    print("----------------")

if __name__ == "__main__":
    main()
