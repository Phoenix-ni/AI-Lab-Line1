n = int(input())
nums = list(map(int,input().split()))
res = []
for i in range(n):
    cnt = 0
    for j in range(i):
        if nums[j] <= nums[i]:
            cnt += 1
    res.append(str(cnt))
print(' '.join(res))
