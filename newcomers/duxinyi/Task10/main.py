import argparse
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(description="Markdown文档检查与清洗工具")
    parser.add_argument("target_dir", type=str, help="目标文件夹路径")
    args = parser.parse_args()

    #检查目录是否存在
    target_path = Path(args.target_dir)
    if not target_path.exists() or not target_path.is_dir():
        print(f"错误: 目录不存在 -> {target_path}")
        return

    #遍历该目录，统计md文件个数
    md_files = list(target_path.rglob("*.md"))
    print(f"发现 {len(md_files)} 个 Markdown 文件。")
    
    from check import check,to_local_path
    from analyze_headings import analyze_headings
    from generate_toc import generate_toc

    #先写好目录索引大标题，便于后续写入
    script_dir = Path(__file__).parent.resolve()
    output_file = script_dir/ "Toc.md"
    with open(output_file,"w",encoding="utf-8")as f:
        f.write("# 目录索引\n\n")

    for md_file in md_files:
        #检查死链接、死图片
        broken_links, broken_images = check(md_file)
        if broken_links:
            print("发现死链接：")
            for link in broken_links:
                print(f"-{link}\n")
        else:
            print("未发现死链接")
        if broken_images:
            print("发现死图片：")
            for img in broken_images:
                print(f"-{img}\n")
        else:
            print("未发现死图片")

        #统计层级标题并生成目录索引
        headings = analyze_headings(md_file)
        if headings:
            for h in headings:
                 print(f"{h}")  
        else:
             print("未提取到标题\n")
        toc_path = Path(__file__).resolve()  
        toc = generate_toc(headings,md_file,toc_path)
        try:
            with open(output_file,"a",encoding="utf-8")as f:
                f.write(f"## {md_file.relative_to(target_path)}目录\n")
                f.write(toc)
                f.write("\n\n")
            print(f"目录已生成至{output_file}\n")
        except PermissionError:
                print("没有写入权限")
        finally:
                print("生成索引任务结束")


if __name__ == "__main__":
    main()