def demo_tuple():
    my_tuple = (10, 20, 30)
    print("\n元组：", my_tuple)
    print("取索引1：", my_tuple[1])
    # 下面这行取消注释会报错！元组不能修改
    # my_tuple[0] = 999
demo_tuple()
