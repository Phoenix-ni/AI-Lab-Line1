"""练习 3：成绩计算器。

一组处理学生成绩的函数，专门练函数设计：
*args（任意多个参数）、**kwargs（任意多个关键字参数）、
默认参数、变量作用域。

运行方式（在 lab 环境里）：
    python src/basics/practice3_functions.py
"""

PASS_LINE = 60  # 及格线。全大写 = 常量，这是 PEP8 的约定


def average(*scores):
    """接收任意多个分数，返回平均值；一个都没给时返回 0。

    *scores 的意思：调用时给几个分数都行，它们会被收进一个元组。
    比如 average(92, 87, 78) 里，scores 就是 (92, 87, 78)。

    注意坑：空元组求平均会除零，所以要先判断 len(scores)。
    """
    if len(scores) == 0:
        return 0
    return sum(scores) / len(scores)



def grade(score, pass_line=PASS_LINE):
    """判断单个分数是否及格，返回 "及格" 或 "不及格"。

    pass_line 是带默认值的参数：调用时不传就用 PASS_LINE，
    传了就用传进来的值，比如 grade(58, pass_line=50)。
    """
    if score >= pass_line:
        return "及格"
    return "不及格"


def report(name, *scores, **extra):
    """打印一份学生成绩报告。

    name 必填；scores 收任意多个分数；extra 收"名字=值"形式的附加信息。
    比如 report("小明", 92, 87, 78, group="一班", note="进步明显")
    那么 extra 就是 {"group": "一班", "note": "进步明显"}
    """
    avg: float | int = average(*scores)  # 把元组原样转交给 average
    print(f"===== {name} 的成绩报告 =====")

    # TODO 1: 用 enumerate 遍历 scores，对每个分数调用 grade()
    #         打印形如「第 1 科：92（及格）」的一行
    for index, score in enumerate(scores, start=1):
        print(f"第 {index} 科：{score}（{grade(score)}）")
    # TODO 2: 打印平均分，保留 1 位小数：{avg:.1f}
    print(f"平均分：{avg:.1f}")
    # TODO 3: 遍历 extra.items()，把每条附加信息打印出来
    #         .items() 会给出 (键, 值) 对，比如 ("group", "一班")
    for key, value in extra.items():
        print(f"{key}：{value}")
def scope_demo():
    """演示变量作用域：函数内可以"读"全局变量，但一旦给它赋值，
    整个函数里这个名字就会变成局部变量——连前面读它的那行都会报错。
    """
    print(f"函数内读到的及格线：{PASS_LINE}")  # 实验 1：只读，合法

    # 实验 2：把下面这行的注释去掉，保存后运行——
    # 你会看到 UnboundLocalError，就在上面那行 print 的位置。
    # 把报错截图存进笔记（这就是"局部遮蔽全局"的证据），再把注释加回去。
    # PASS_LINE = 100


def main():
    """串起所有函数。"""
    print(f"三门课的平均分：{average(92, 87, 78):.1f}")
    print(f"零个分数的平均分：{average()}")
    print(f"85 分：{grade(85)}；58 分：{grade(58)}")
    print()
    report("小明", 92, 87, 78, group="一班", note="进步明显")
    print()
    scope_demo()


if __name__ == "__main__":
    main()
