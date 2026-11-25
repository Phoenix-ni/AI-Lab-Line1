def process_student_data(query_name,*args):
    """
    处理学生成绩数据，筛选及格学生并转化为字典
    输入：查询学生姓名，学生成绩数据（可变参数）
    输出：查询学生的成绩，如果未找到该学生则返回“未找到该学生”
    """
    passed_students = []
    for name,score in args:
        if score >= 60:
            passed_students.append ((name,score))
    student_dict = dict(passed_students)
    result = student_dict.get(query_name,"未找到该学生")
    return result

student_data = []
print("-----开始录入学生成绩-----")
while True:
    name = input("请输入学生姓名（输入0退出）：")
    if name == "0":
        break
    score = int(input(f"请输入{name}的成绩："))
    student_data.append((name, score))

print("-----学生成绩录入完成-----")
while True:
    query_name = input("请输入要查询的学生姓名（输入0退出）：")
    if query_name == "0":
        break
    print(f"{query_name}的成绩为：{process_student_data(query_name, *student_data)}")

