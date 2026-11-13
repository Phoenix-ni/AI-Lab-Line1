# exercise_2.py
# 练习二：函数设计（默认值、*args、**kwargs、作用域）

# 定义一个全局变量，用于测试作用域
global_var = "我是全局变量"


def function_design_demo(name, greeting="你好", *args, **kwargs):
    """
    演示函数设计的各种特性
    :param name: 必填参数
    :param greeting: 默认参数
    :param args: 可变位置参数 (元组)
    :param kwargs: 可变关键字参数 (字典)
    """
    # 1. 测试变量作用域：在函数内部尝试读取全局变量
    print(f"[作用域测试] 读取全局变量: {global_var}")

    # 2. 处理默认参数和必填参数
    print(f"{greeting}，{name}！")

    # 3. 处理 *args（接收多余的【位置参数】，打包成元组）
    if args:
        print(f"[*args测试] 接收到的额外位置参数 (元组): {args}")

    # 4. 处理 **kwargs（接收多余的【关键字参数】，打包成字典）
    if kwargs:
        print(f"[**kwargs测试] 接收到的额外关键字参数 (字典): {kwargs}")
        # 提取特定信息（可选操作）
        if "age" in kwargs:
            print(f"   -> 提取到年龄信息: {kwargs['age']} 岁")


def calculate_sum(*numbers):
    """练习：不定长参数求和并返回结果"""
    total = 0
    for num in numbers:
        total += num
    return total


if __name__ == "__main__":
    print("--- 测试 1: 仅传必填参数，使用默认值 ---")
    function_design_demo("小明")
    print("\n")

    print("--- 测试 2: 覆盖默认值，传入 *args 和 **kwargs ---")
    # 这里的 "早上好" 覆盖了 greeting
    # 10, 20 被 *args 接收
    # age=25, city="北京" 被 **kwargs 接收
    function_design_demo("小红", "早上好", 10, 20, age=25, city="北京")
    print("\n")

    print("--- 测试 3: 测试带返回值的函数 ---")
    result = calculate_sum(1, 2, 3, 4, 5)
    print(f"不定长参数求和结果: {result}")