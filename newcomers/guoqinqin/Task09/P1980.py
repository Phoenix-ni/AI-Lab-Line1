# P1980 [NOIP2013 普及组] 计数问题
n, x = map(int, input().split())
x = str(x)

count = 0
for i in range(1, n + 1):
    count += str(i).count(x)

print(count)