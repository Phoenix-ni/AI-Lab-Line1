def func_default(a, b=10):
    """带默认参数"""
    return a + b

def func_args(*args):
    """args是元组，接收随便多个数字求和"""
    total = 0
    for num in args:
        total += num
    return total

def func_kwargs(**kwargs):
    """kwargs是字典，接收一堆key=value"""
    for k, v in kwargs.items():
        print(f"{k}: {v}")

def scope_demo():
    outer_var = "外部变量"
    def inner():
        nonlocal outer_var
        outer_var = "被内层改掉了"
        print("inner里：", outer_var)
    inner()
    print("外层：", outer_var)

if __name__ == "__main__":
    print("默认参数 func_default(5) →", func_default(5))
    print("*args求和 1,2,3,4 →", func_args(1,2,3,4))
    print("\n**kwargs测试：")
    func_kwargs(city="Taiyuan", school="TUT")
    print("\n作用域测试：")
    scope_demo()
