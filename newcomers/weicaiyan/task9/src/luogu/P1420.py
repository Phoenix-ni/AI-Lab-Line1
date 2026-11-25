n = int(input())
nums = list(map(int, input().split()))
max_len = 1
cur_len = 1
for i in range(1, n):
    if nums[i] == nums[i-1] + 1:
        cur_len += 1
        if cur_len > max_len:
            max_len = cur_len
    else:
        cur_len = 1
print(max_len)