# exercise_3.py
# 练习三：综合应用（数据结构 + 函数设计 + 流程控制）

def add_student(students_list, name, **scores):
    """
    添加学生及其各科成绩
    :param students_list: 存储所有学生信息的列表 (List)
    :param name: 学生姓名 (str)
    :param scores: 不定长关键字参数，接收各科成绩，如 math=90, english=85 (Dict)
    """
    # 字典推导式：将传入的 scores 字典处理一下（比如只保留及格的科目）
    valid_scores = {subject: score for subject, score in scores.items() if score >= 60}

    # 构造一个学生字典
    student_info = {
        "name": name,
        "scores": valid_scores
    }

    # 将学生字典添加到列表中
    students_list.append(student_info)
    print(f"成功添加学生：{name}，及格科目成绩：{valid_scores}")


def analyze_students(students_list):
    """
    分析学生数据
    :param students_list: 存储所有学生信息的列表
    """
    if not students_list:
        print("当前没有学生数据。")
        return

    # 1. 使用集合 (Set) 统计所有出现过的科目（去重）
    all_subjects = set()
    for student in students_list:
        # 字典的 keys() 返回类似集合的对象，我们用 update 合并进 all_subjects
        all_subjects.update(student["scores"].keys())

    print(f"\n--- 成绩分析报告 ---")
    print(f"系统内包含的科目有: {all_subjects}")

    # 2. 统计每个科目的平均分 (结合字典和循环)
    subject_totals = {}
    subject_counts = {}

    for student in students_list:
        for subject, score in student["scores"].items():
            subject_totals[subject] = subject_totals.get(subject, 0) + score
            subject_counts[subject] = subject_counts.get(subject, 0) + 1

    # 字典推导式计算平均分
    subject_averages = {
        subject: round(subject_totals[subject] / subject_counts[subject], 1)
        for subject in subject_totals
    }
    print(f"各科平均分: {subject_averages}")

    # 3. 使用条件判断找最高分学生
    # 假设我们比较总分
    top_student = None
    max_total = 0

    for student in students_list:
        current_total = sum(student["scores"].values())
        if current_total > max_total:
            max_total = current_total
            top_student = student["name"]

    print(f"总分最高的学生是: {top_student} (总分: {max_total})")


if __name__ == "__main__":
    # 初始化一个空列表，用于存放所有学生数据
    database = []

    # 1. 录入数据（测试 **kwargs 和 函数调用）
    add_student(database, "张三", math=95, english=88, physics=55)  # 物理不及格会被过滤
    add_student(database, "李四", math=80, english=92, chemistry=78)
    add_student(database, "王五", math=60, english=59)  # 英语不及格被过滤

    # 2. 进行数据分析（测试集合去重、循环、字典运算）
    analyze_students(database)