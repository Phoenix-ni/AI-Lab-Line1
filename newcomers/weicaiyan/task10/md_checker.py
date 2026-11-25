import os

def check_markdown_files(directory):
    results = {}
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".md"):
                filepath = os.path.join(root, file)
                h1_count, h2_count = 0, 0
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        for line in f:
                            if line.startswith("# "):
                                h1_count += 1
                            elif line.startswith("## "):
                                h2_count += 1
                    results[file] = {"H1": h1_count, "H2": h2_count}
                except Exception:
                    pass
    return results
