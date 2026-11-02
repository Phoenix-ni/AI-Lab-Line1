def demo_tuple():
    t = (10, 20, 30, 20, 40)
    print("元组内容：", t)
    print("元组索引取值：", t[1])
def demo_dict():
    student = {"name":"Tom", "age":18, "gender":"male"}
    print("\n字典原始内容：", student)
    print("用get取值name：", student.get("name"))
    print("get取不存在的key，默认值：", student.get("score", 0))
    dict_demo = {i:i*10 for i in range(1,6)}
    print("字典推导式结果：", dict_demo)
if __name__ == "__main__":
    demo_tuple()
    demo_dict()
