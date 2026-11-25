# md_stats.py
from pathlib import Path
import json


def analyze_single_file(file_path):
    """
    读取单个文件，统计行数和字数。
    使用 try...except 捕获可能发生的异常。
    """
    try:
        # 使用 with open 安全打开文件，必须指定 encoding="utf-8"
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        # 统计行数：按换行符分割，并过滤掉末尾可能产生的空字符串
        lines = content.splitlines()
        line_count = len(lines)

        # 统计字数：这里采用简单的逻辑，去除所有空白字符后的字符总数
        # (也可以按空格分词算单词数，这里按照通用“字数”理解)
        word_count = len(content.replace(" ", "").replace("\n", "").replace("\r", ""))

        return {
            "lines": line_count,
            "words": word_count,
            "status": "success"
        }

    except UnicodeDecodeError:
        # 专门捕获编码错误
        print(f"  [!] 警告：文件 {file_path.name} 编码错误，跳过。")
        return {"status": "error", "reason": "encoding_error"}

    except Exception as e:
        # 捕获其他所有意外错误
        print(f"  [!] 警告：读取文件 {file_path.name} 失败: {e}")
        return {"status": "error", "reason": str(e)}


def process_directory(target_dir):
    """扫描目录并处理所有 .md 文件"""
    folder_path = Path(target_dir)

    if not folder_path.exists() or not folder_path.is_dir():
        print(f"错误：找不到文件夹 '{target_dir}'。")
        return

    md_files = list(folder_path.glob("*.md"))
    print(f"开始处理文件夹 '{target_dir}'，共找到 {len(md_files)} 个 .md 文件：\n")

    # 用一个字典来暂存所有文件的统计结果
    stats_result = {}

    for file in md_files:
        print(f"正在分析: {file.name} ...")
        result = analyze_single_file(file)

        # 把统计结果存入大字典
        if result["status"] == "success":
            stats_result[file.name] = {
                "line_count": result["lines"],
                "word_count": result["words"]
            }
            print(f"  -> 行数: {result['lines']}, 字数: {result['words']}")
        else:
            print(f"  -> 处理失败，原因: {result['reason']}")

    print("\n--- 所有文件处理完毕 ---")
    # --- 新增：保存为 JSON 文件 ---
    output_file = Path("summary.json")
    try:
        # 使用 with open 写入文件，指定编码为 utf-8，确保中文正常显示
        # indent=4 让生成的 JSON 文件有缩进，方便人类阅读
        # ensure_ascii=False 防止中文被转义成 \uXXXX 这种乱码
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(stats_result, f, indent=4, ensure_ascii=False)
        print(f"✅ 成功！统计结果已保存到: {output_file.absolute()}")
    except Exception as e:
        print(f"❌ 保存 JSON 失败: {e}")


if __name__ == "__main__":
    print("--- 开始测试文件读取与异常处理 ---")
    process_directory("test_docs")