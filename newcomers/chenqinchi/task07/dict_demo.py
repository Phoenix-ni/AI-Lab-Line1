
def demo_dict():
    student = {
        "name": "Zhang",
        "age": 19,
        "major": "Math"
    }
    print("原始字典：", student)
    print(".get取name：", student.get("name"))
    # score不存在，返回默认0，不报错
    print(".get取score，默认0：", student.get("score", 0))

    # 新增key
    student["score"] = 95
    # 删除age
    del student["age"]
    print("修改后字典：", student)

    # 字典推导式
    square_dict = {i: i*i for i in range(1, 6)}
    print("字典推导式：", square_dict)

if __name__ == "__main__":
    demo_dict()
