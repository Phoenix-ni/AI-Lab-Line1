# P1009 [NOIP1998 普及组] 阶乘之和
n = int(input())

fact = 1
total = 0

for i in range(1, n + 1):
    fact *= i
    total += fact

print(total)