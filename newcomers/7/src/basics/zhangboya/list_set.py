def demo_list():
    fruit_list = ["apple","banana","orange","grape"]
    print("原始列表：", fruit_list)
    fruit_list.append("pear")
    print("append添加pear：", fruit_list)
    fruit_list[1] = "blueberry"
    print("修改后：", fruit_list)
    slice_res = fruit_list[0:3]
    print("切片结果：", slice_res)
    num_list = [i * 2 for i in range(1, 6)]
    print("列表推导式：", num_list)
    print("\nfor循环遍历列表：")
    for item in fruit_list:
        print(item)
def demo_set():
    raw = [1, 2, 2, 3, 3, 3, 4]
    num_set = set(raw)
    print("\n集合自动去重：", num_set)
    set_a = {1, 2, 3, 4}
    set_b = {3, 4, 5, 6}
    print("交集 &：", set_a & set_b)
    print("并集 |：", set_a | set_b)
    print("差集 a-b：", set_a - set_b)
if __name__ == "__main__":
    demo_list()
    demo_set()
