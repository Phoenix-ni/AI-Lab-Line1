#角谷猜想
N = int(input())
a = 0
while N != 1:
    if N % 2 == 0:
        a = N
        N = N // 2
        print(f"{a}/2={N}")
    else:
        a = N
        N = N * 3 + 1
        print(f"{a}*3+1={N}")
print("End")
        

