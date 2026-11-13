apples = list(map(int, input().split()))
height = int(input()) + 30
count = 0
for a in apples:
    if a <= height:
        count += 1
print(count)