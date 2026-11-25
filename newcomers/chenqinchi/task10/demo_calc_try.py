try:
    num1 = int(input("输入第一个数字："))
    num2 = int(input("输入第二个数字："))
    res = num1 / num2
except ValueError:
    print("❌ 错误：你输入的不是数字！")
except ZeroDivisionError:
    print("❌ 错误：除数不能是0！")
else:
    print(f"计算结果：{res}")
finally:
    print("计算流程结束")
