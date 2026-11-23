def demo_list():
    my_list = [1, 2, 3, 4, 5]
    print("原始列表：", my_list)
    # 切片：取第2、3、4个元素（索引1,2,3）
    print("切片 my_list[1:4] → ", my_list[1:4])

    # 增
    my_list.append(6)
    # 删索引0
    my_list.pop(0)
    # 修改索引1的值
    my_list[1] = 99
    print("增删改之后：", my_list)

    # 列表推导式：1~5每个数求平方
    square_list = [x * x for x in range(1, 6)]
    print("列表推导式平方：", square_list)

# 先单独跑列表部分
if __name__ == "__main__":
    demo_list()

def demo_tuple():
    my_tuple = (10, 20, 30)
    print("\n元组：", my_tuple)
    print("取索引1：", my_tuple[1])
    # 下面这行取消注释会报错！元组不能修改
    # my_tuple[0] = 999
demo_tuple()
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
