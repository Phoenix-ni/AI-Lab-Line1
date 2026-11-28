"""练习 2：名单清洗。

两张名单：报名的人、实际签到的人。用集合运算找出四种人。
涉及知识点：set 的交并差、tuple 的不可变性、sorted 排序、f-string。

运行方式（在 lab 环境里）：
    python src/basics/practice2_set_tuple.py
"""

REGISTERED = {"小明", "小红", "小刚", "小丽", "小强", "小美"}
CHECKED_IN = {"小红", "小刚", "小强", "阿伟"}

# 签到流水：每条是 (日期, 姓名)。这种"记下就不该再改"的数据用 tuple 存。
CHECKIN_LOG = [
    ("2026-11-23", "小红"),
    ("2026-11-23", "小刚"),
    ("2026-11-24", "小强"),
    ("2026-11-24", "阿伟"),
]


def find_both(registered, checked_in):
    """既报名又签到的人（两个名单的交集）。"""
    both = registered & checked_in
    return set(both)


def find_no_show(registered, checked_in):
    """报了名但没来的人。想想减号 - 的方向：谁减谁？"""
    no_show = registered - checked_in
    return set(no_show)


def find_walk_in(registered, checked_in):
    """没报名却来了的人。和上面是反方向的减法。"""
    walk_in = checked_in - registered
    return set(walk_in)


def find_all(registered, checked_in):
    """所有关联过的人（两个名单的并集）。"""
    returned = registered | checked_in
    return set(returned)


def main():
    """跑通整条流程并打印结果。"""
    both = find_both(REGISTERED, CHECKED_IN)
    no_show = find_no_show(REGISTERED, CHECKED_IN)
    walk_in = find_walk_in(REGISTERED, CHECKED_IN)
    everyone = find_all(REGISTERED, CHECKED_IN)

    print(f"既报名又签到：{sorted(both)}")
    print(f"报名但没来  ：{sorted(no_show)}")
    print(f"没报名却来了：{sorted(walk_in)}")
    print(f"全部相关人员：{sorted(everyone)}")

    # 体验 tuple 的不可变性：把下面这行的注释去掉，运行一次，
    # 看到报错后截个图存进笔记，再把注释加回去。
    # CHECKIN_LOG[0][1] = "别人"

    print(f"签到流水共 {len(CHECKIN_LOG)} 条，第一条是：{CHECKIN_LOG[0]}")


if __name__ == "__main__":
    main()
