import json
import argparse
import sys
from datetime import datetime
from pathlib import Path


def count_file(path: Path) -> dict:
    with open(path, "r", encoding="utf-8", errors="replace") as handle:
        text = handle.read()
    return {
        "lines": len(text.splitlines()),
        "chars": len("".join(text.split())),
        "total_chars": len(text),
    }


def collect(root: Path, recursive: bool = True) -> list:
    pattern = root.rglob("*") if recursive else root.glob("*")
    return sorted(
        (path for path in pattern if path.is_file() and path.suffix.lower() == ".md"),
        key=lambda path: path.as_posix().lower(),
    )


def build_summary(root: Path, recursive: bool = True) -> dict:
    records = []
    errors = []
    for path in collect(root, recursive):
        relative = path.relative_to(root).as_posix()
        try:
            records.append({"file": relative, **count_file(path)})
        except (OSError, UnicodeError) as exc:
            errors.append({"file": relative, "error": str(exc)})
            print(f"警告：跳过无法读取的文件 {relative}：{exc}", file=sys.stderr)

    records.sort(key=lambda record: record["file"].lower())
    return {
        "root": str(root),
        "generated_at": datetime.now().astimezone().isoformat(timespec="seconds"),
        "total_files": len(records),
        "totals": {
            "lines": sum(record["lines"] for record in records),
            "chars": sum(record["chars"] for record in records),
            "total_chars": sum(record["total_chars"] for record in records),
        },
        "files": records,
        "errors": errors,
    }


def parse_args(argv=None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="统计 Markdown 文件字数与行数")
    parser.add_argument("folder", nargs="?", default=".", help="要扫描的文件夹（默认当前目录）")
    parser.add_argument("-o", "--output", default="summary.json", help="输出 JSON 路径")
    parser.add_argument("--no-recursive", action="store_true", help="只扫描当前层，不扫描子目录")
    return parser.parse_args(argv)


def main(argv=None) -> int:
    if hasattr(sys.stdout, "reconfigure"):
        try:
            sys.stdout.reconfigure(encoding="utf-8")
            sys.stderr.reconfigure(encoding="utf-8")
        except (AttributeError, ValueError):
            pass

    args = parse_args(argv)
    root = Path(args.folder).expanduser().resolve()

    if not root.exists():
        print(f"错误：文件夹不存在：{root}", file=sys.stderr)
        return 1
    if not root.is_dir():
        print(f"错误：这不是文件夹：{root}", file=sys.stderr)
        return 1

    output = Path(args.output)
    if not output.is_absolute():
        output = Path.cwd() / output
    if output.exists():
        print(f"提示：将覆盖已有文件 {output}")

    try:
        summary = build_summary(root, recursive=not args.no_recursive)
        output.parent.mkdir(parents=True, exist_ok=True)

        with open(output, "w", encoding="utf-8") as handle:
            json.dump(summary, handle, ensure_ascii=False, indent=2)
            handle.write("\n")

        with open(output, "r", encoding="utf-8") as handle:
            saved = json.load(handle)

        if saved.get("total_files") != summary["total_files"]:
            print("警告：回读校验不一致，请检查文件", file=sys.stderr)
        else:
            print(f"回读校验通过，共 {saved['total_files']} 条记录")

        print(f"已扫描 {summary['total_files']} 个 Markdown 文件")
        print(f"总行数：{summary['totals']['lines']}  总字数：{summary['totals']['chars']}")
        print(f"结果已写入：{output}")

        if summary["errors"]:
            print(
                f"其中有 {len(summary['errors'])} 个文件读取失败，已记录在 errors 字段",
                file=sys.stderr,
            )
            return 2
        return 0
    except (OSError, json.JSONDecodeError) as exc:
        print(f"错误：写入或读出 {output} 失败：{exc}", file=sys.stderr)
        return 1
    finally:
        print("统计流程结束")


if __name__ == "__main__":
    raise SystemExit(main())