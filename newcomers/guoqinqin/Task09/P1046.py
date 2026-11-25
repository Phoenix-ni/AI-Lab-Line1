# P1046 [NOIP2005 普及组] 陶陶摘苹果
heights = list(map(int, input().split()))
tao = int(input())
limit = tao + 30

count = 0
for h in heights:
    if h <= limit:
        count += 1

print(count)