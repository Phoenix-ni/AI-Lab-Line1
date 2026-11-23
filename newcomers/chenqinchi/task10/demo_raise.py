age = int(input("输入年龄:"))
if age < 0:
    raise ValueError("年龄不能是负数!")
print("你的年龄是:",age)
