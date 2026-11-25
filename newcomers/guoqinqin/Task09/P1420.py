# P1420 最长连续自然数
n = int(input())
a = list(map(int, input().split()))

best = 1
cur = 1

for i in range(1, n):
    if a[i] == a[i - 1] + 1:
        cur += 1
    else:
        cur = 1
    if cur > best:
        best = cur

print(best)