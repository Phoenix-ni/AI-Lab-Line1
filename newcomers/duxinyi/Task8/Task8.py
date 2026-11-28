import json
from pathlib import Path

def count_file_content(file_path):
    lines = 0
    chars = 0
    try:
        with open(file_path,"r",encoding="utf-8") as f:
            for line in f:
                lines += 1
                chars += len(line)
                #计算函数和字符数
    except UnicodeDecodeError:
        print(f"文件{file_path}不是utf-8编码，已跳过")
    except PermissionError:
        print(f"无权读取文件{file_path}，已跳过")
    finally:
        return lines,chars

def main():
    base_dir = Path(__file__).resolve().parent
    target_dir = base_dir/"docs"

    summary_data = []
    total_files = 0
    total_lines = 0
    total_chars = 0
    for md_file in target_dir.rglob("*.md"):
        if md_file.is_file():
            lines,chars = count_file_content(md_file)
            rel_path = md_file.relative_to(base_dir)

            summary_data.append({
                "file":str(rel_path),
                "lines":lines,
                "chars":chars
            })
            total_files += 1
            total_lines += lines
            total_chars += chars

    result = {
        "summary": summary_data,
        "total_files":total_files,
        "total_lines":total_lines,
        "total_chars":total_chars
    }
    try:
        contents = json.dumps(result,ensure_ascii=False,indent=2)
        output_file = base_dir/"summary.json"
        output_file.write_text(contents,encoding="utf-8")
        print(f"结果已输出至：{output_file}")
    except PermissionError:
        print("无权写入文件")


if __name__ == "__main__":
    main()