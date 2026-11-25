import csv
from pathlib import Path
import json
# 从脚本所在目录寻找数据，避免受终端当前目录影响。
data_path = Path(__file__).resolve().parent / "scores.csv"

# utf-8-sig 兼容普通 UTF-8 和带 BOM 的 UTF-8 文件。
with data_path.open(encoding="utf-8-sig", newline="") as file:
    reader = csv.DictReader(file)
    rows = list(reader)

clean_rows = []
seen = set()

for row in rows:
    name = row["name"].strip()
    score_text = row["score"].strip()

    # 排除姓名或成绩缺失的记录。
    if not name or not score_text:
        print("排除缺失数据：", row)
        continue

    # CSV 读出的成绩是字符串，需要转换为数字。
    try:
        score = float(score_text)
    except ValueError:
        print("排除非数字成绩：", row)
        continue

    # 成绩必须在 0～100 之间，同时排除 NaN 等无效值。
    if not 0 <= score <= 100:
        print("排除超范围或无效成绩：", row)
        continue

    # 按清理后的姓名和数值成绩识别重复记录。
    key = (name, score)
    if key in seen:
        print("排除重复记录：", row)
        continue

    seen.add(key)
    clean_rows.append({"name": name, "score": score})

print("原始记录数：", len(rows))
print("有效记录数：", len(clean_rows))

for row in clean_rows:
    print(row)

# 没有有效成绩时，用 None 表示统计值不可用。
scores = [row["score"] for row in clean_rows]

summary = {
    "original_count": len(rows),
    "valid_count": len(clean_rows),
    "removed_count": len(rows) - len(clean_rows),
    "average_score": round(sum(scores) / len(scores), 2) if scores else None,
    "max_score": max(scores) if scores else None,
    "min_score": min(scores) if scores else None,
}

# 将清洗后的记录保存为 CSV。
clean_path = data_path.parent / "clean_scores.csv"
with clean_path.open("w", encoding="utf-8-sig", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "score"])
    writer.writeheader()
    writer.writerows(clean_rows)

# 将统计结果保存为 JSON。
summary_path = data_path.parent / "summary.json"
with summary_path.open("w", encoding="utf-8") as file:
    json.dump(summary, file, ensure_ascii=False, indent=2)

print("统计结果：", summary)
print("清洗数据已保存：", clean_path)
print("统计结果已保存：", summary_path)