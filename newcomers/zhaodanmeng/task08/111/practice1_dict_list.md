"""练习 1：词频统计器。

统计一段英文文本里每个单词出现的次数，输出出现次数最多的前 3 名。
涉及知识点：str 方法、list、dict、列表推导式、sorted、f-string。

运行方式（在 lab 环境里）：
    python src/basics/practice1_dict_list.py
"""

TEXT = (
    "the quick brown fox jumps over the lazy dog. "
    "the dog barks and the fox runs away. "
    "a quick fox is better than a lazy dog."
)


def clean_words(text):
    """把文本拆成纯小写的单词列表，标点全部去掉。

    步骤提示：
        1. 先统一小写：text.lower()
        2. 按空格切开：.split()
        3. 用列表推导式过滤掉带标点的词：只保留 w.isalpha() 为真的
           （"dog." 这种会因为有小数点被过滤掉，正好达到去标点的目的）
    返回：list[str]
    """
    return [w for w in text.lower().split() if w.isalpha()]



def count_words(words):
    """统计每个单词出现的次数，返回 {单词: 次数} 这样的字典。

    提示：遍历 words，对每个 w 做
        counts[w] = counts.get(w, 0) + 1
    别写成 counts[w] += 1 —— 第一次遇到的词会直接 KeyError。
    返回：dict[str, int]
    """
    # TODO: 实现计数，把下面的 return 换掉
    counts = {}
    for w in words:
        counts[w] = counts.get(w, 0) + 1
    return counts


def top_n(counts, n=3):
    """按出现次数从多到少取前 n 名，返回 [("the", 4), ("fox", 3)]。

    提示：字典本身不能排序，先转成 (单词, 次数) 的列表：counts.items()
         sorted(..., key=lambda pair: pair[1], reverse=True)
         pair[1] 就是元组里的第二个元素，也就是次数。
    返回：list[tuple[str, int]]
    """
    # TODO: 实现排序取前 n，把下面的 return 换掉
    return sorted(counts.items(), key=lambda pair: pair[1], reverse=True)[:n]



def main():
    """跑通整条流程并打印结果。"""
    words = clean_words(TEXT)
    counts = count_words(words)
    ranking = top_n(counts, 3)

    print(f"总词数：{len(words)}，不同单词：{len(counts)}")
    for index, (word, times) in enumerate(ranking, start=1):
        print(f"{index}. {word} —— 出现 {times} 次")


if __name__ == "__main__":
    main()
