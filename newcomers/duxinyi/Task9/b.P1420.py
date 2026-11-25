#最长连数问题
n = int(input())
nums = list(map(int, input().split()))
now_len = 1
max_len = 1
for i in range (n):
    if nums[i] == nums[i-1] + 1:
        now_len += 1
        if now_len > max_len:
            max_len = now_len
    else:
        now_len = 1

print (max_len)