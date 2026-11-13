n = int(input())
sum_val = 0
fact = 1
for i in range(1, n + 1):
    fact *= i
    sum_val += fact
print(sum_val)