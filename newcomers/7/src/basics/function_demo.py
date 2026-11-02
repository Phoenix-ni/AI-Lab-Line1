def demo_default_param(a, b=10):
    return (a + b)
def demo_args(*args):
    print("*args拿到的全部参数：", args)
    total = 0
    for num in args:
        total += num
    return total
if __name__ == "__main__":
    print("\n===== *args 不定长位置参数 =====")
    res = demo_args(1,2,3,4)
    print("args求和结果：", res)
    
