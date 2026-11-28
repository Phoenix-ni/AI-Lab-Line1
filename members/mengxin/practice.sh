#!/usr/bin/env bash
set -euo pipefail

demo_dir="$(mktemp -d)"
trap 'rm -rf -- "$demo_dir"' EXIT

echo "当前目录："
pwd

echo "创建并读取文件："
printf 'Linux\nGit\nPython\n' > "$demo_dir/topics.txt"
cat "$demo_dir/topics.txt"

echo "查找 Git 所在行："
grep -n 'Git' "$demo_dir/topics.txt"

echo "统计行数："
wc -l < "$demo_dir/topics.txt"
