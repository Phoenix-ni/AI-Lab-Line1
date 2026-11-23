data = input().split()
nums = list(map(int,data))

idx = nums.index(0)
res = nums[:idx]
res.reverse()
print(' '.join(map(str,res)))
