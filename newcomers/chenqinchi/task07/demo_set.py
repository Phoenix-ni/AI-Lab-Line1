def demo_set():
    set_a = {1, 2, 3, 4, 5}
    set_b = {4, 5, 6, 7, 8}
    print("\n集合A：", set_a)
    print("集合B：", set_b)
    print("交集（两边都有的）：", set_a & set_b)
    print("并集（全部合起来，去重）：", set_a | set_b)
    print("差集A-B（A有B没有）：", set_a - set_b)

    # 列表去重
    raw = [1, 1, 2, 2, 3]
    dedup = set(raw)
    print("原列表", raw, "去重后", dedup)
demo_set()
