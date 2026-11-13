import json
from pathlib import Path

def scan_md_files(folder_path):
    """扫描指定文件夹下的 .md 文件，统计字数和行数"""
    # 使用 pathlib 进行路径处理
    target_dir = Path(folder_path)
    
    # 判断文件夹是否存在
    if not target_dir.exists() or not target_dir.is_dir():
        print(f"错误：文件夹 {folder_path} 不存在！")
        return

    summary_data = {}
    
    # 使用 glob 遍历所有 .md 文件
    for md_file in target_dir.glob("*.md"):
        try:
            # 使用 with open 上下文管理器，指定 utf-8 编码
            with open(md_file, "r", encoding="utf-8") as f:
                content = f.read()
                
                # 统计行数和字数（去除首尾空白后按字符算）
                line_count = len(content.splitlines())
                word_count = len(content.strip())
                
                # 将结果存入字典
                summary_data[md_file.name] = {
                    "lines": line_count,
                    "characters": word_count
                }
        except Exception as e:
            # 捕获异常，避免程序崩溃
            print(f"读取文件 {md_file.name} 时出错: {e}")
            
    # 使用 with open 写入 JSON 文件
    output_file = target_dir / "summary.json"
    try:
        with open(output_file, "w", encoding="utf-8") as f:
            # 序列化 JSON，ensure_ascii=False 保证中文正常显示，indent 美化格式
            json.dump(summary_data, f, ensure_ascii=False, indent=4)
        print(f"统计完成！结果已保存至 {output_file.name}")
    except Exception as e:
        print(f"写入 JSON 文件失败: {e}")

if __name__ == "__main__":
    # 扫描当前目录
    scan_md_files(".")