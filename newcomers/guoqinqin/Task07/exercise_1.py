# exercise_1.py
# 练习一：四大内置集合类型的基础操作与推导式

def process_data():
    # 1. 列表 (List) 练习
    raw_list = [1, 2, 2, 3, 4, 5]
    # 切片操作：获取前三个元素
    sliced_list = raw_list[:3]
    # 列表推导式：将列表中的偶数平方
    squared_evens = [x**2 for x in raw_list if x % 2 == 0]
    print(f"原列表: {raw_list}")
    print(f"切片前三个: {sliced_list}")
    print(f"偶数平方列表推导式: {squared_evens}")

    # 2. 字典 (Dict) 练习
    student_scores = {"Alice": 85, "Bob": 92}
    # get 方法：安全获取，如果没有则返回默认值
    charlie_score = student_scores.get("Charlie", 0)
    # 字典推导式：将分数转换为等级
    grade_dict = {name: "A" if score >= 90 else "B" for name, score in student_scores.items()}
    print(f"Charlie 的分数: {charlie_score}")
    print(f"等级字典推导式: {grade_dict}")

    # 3. 集合 (Set) 练习
    set_a = {1, 2, 3, 4}
    set_b = {3, 4, 5, 6}
    # 去重与交并差运算
    print(f"并集 (|): {set_a | set_b}")
    print(f"交集 (&): {set_a & set_b}")
    print(f"差集 (-): {set_a - set_b}")

if __name__ == "__main__":
    process_data()