n = int(input())
nums = list(map(int,input().split()))
max_len = 1
current = 1
for i in range(1,n):
    if nums[i] == nums[i-1] + 1:
        current = current + 1
        if current > max_len:
            max_len = current
    else:
        current = 1
print(max_len)
