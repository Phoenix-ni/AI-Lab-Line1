"""Task 08：Markdown 扫描器 —— 文件 I/O、pathlib 与异常处理实战。

扫描指定文件夹下的所有 .md 文件，统计每个文件的行数与字符数，
把结果汇总写入 summary.json。

运行方式（在 lab 环境里）：
    python task08-python-io/scan_markdown.py
"""

from pathlib import Path
import json

# 用 Path 拼路径，比手动加 "/" 安全（跨系统都适用）
# __file__ 是当前脚本自己的路径，.parent 是它所在的文件夹
SAMPLE_DIR = Path(__file__).parent / "111"
OUTPUT_FILE = Path(__file__).parent / "summary.json"


def read_stats(md_path):
    """读取一个 md 文件，返回统计字典；读不了就返回 None 并打印警告。

    提示：
        1. 用上下文管理器读文件（with 会自动关文件，忘不了）：
               with open(md_path, "r", encoding="utf-8") as f:
                   text = f.read()
        2. 行数 = text.splitlines() 的长度
        3. 字数 = len(text)（最简单的口径：所有字符都算）
        4. 把读取部分用 try/except 包住，捕获这两类错误并打印警告：
               FileNotFoundError（文件消失）
               UnicodeDecodeError（不是 utf-8 的文件）
           出问题时 return None，主流程会跳过它——
           程序绝不能因为一个坏文件就整体崩溃
    返回：{"文件名": ..., "行数": ..., "字符数": ...} 或 None
    """
    try:
        with open(md_path, "r", encoding="utf-8") as f:
            text = f.read()
        return {
            "文件名": md_path.name,
            "行数": len(text.splitlines()),
            "字符数": len(text),
        }
    except (FileNotFoundError, UnicodeDecodeError) as e:
        print(f"跳过无法读取的文件 {md_path.name}：{e}")
        return None


def collect_stats(folder):
    """遍历 folder 下所有 .md 文件，返回成功统计的列表。

    提示：folder.glob("*.md") 给出文件夹里每个 .md 文件的 Path，
    对每个调用 read_stats()，把不是 None 的结果收进列表。
    """
    results = []
    for md_file in folder.glob("*.md"):
        stats = read_stats(md_file)
        if stats is not None:
            results.append(stats)
    return results


def write_summary(stats, out_path):
    """把统计列表写成 JSON 文件。

    提示：
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(stats, f, ensure_ascii=False, indent=2)
    ensure_ascii=False 让中文原样保存（否则会变成 \\uXXXX）；
    indent=2 是美化缩进，方便人读。
    """
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(stats, f, ensure_ascii=False, indent=2)


def main():
    stats = collect_stats(SAMPLE_DIR)
    print(f"成功统计 {len(stats)} 个文件")
    write_summary(stats, OUTPUT_FILE)
    print(f"结果已写入：{OUTPUT_FILE}")


if __name__ == "__main__":
    main()
