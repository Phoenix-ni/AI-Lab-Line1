def analyze_tags(tags1,tags2,ignore = False):
    """
    接收两个标签集合，计算并返回两个集合的交集、并集和差集
    输入：两个标签集合，一个可选参数ignore（默认为False），表示是否忽略大小写
    输出：一个字典，包含交集、并集和差集
    """
    if ignore:
        tags1 = {tag.lower() for tag in tags1}
        tags2 = {tag.lower() for tag in tags2}
    intersection = tags1 & tags2
    union = tags1 | tags2
    difference_1 = tags1 - tags2
    difference_2 = tags2 - tags1
    return {
        "intersection": intersection,
        "union": union,
        "difference_1": difference_1,
        "difference_2": difference_2
    }

set1 = {"Python", "Java", "docker", "JavaScript"}
set2 = {"python", "Linux", "Docker", "JavaScript"}

result1 = analyze_tags(set1, set2, ignore=True)
print("-----忽略大小写的结果-----")
print("交集：", result1["intersection"])
print("并集：", result1["union"])
print("差集1：", result1["difference_1"])
print("差集2：", result1["difference_2"])

result2 = analyze_tags(set1, set2)
print("-----不忽略大小写的结果-----")
print("交集：", result2["intersection"])
print("并集：", result2["union"])
print("差集1：", result2["difference_1"])
print("差集2：", result2["difference_2"])

