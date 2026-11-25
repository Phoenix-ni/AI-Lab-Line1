import math

# 读取一行输入的三个正整数
x, y, z = map(int, input().split())

# 先求 x 和 y 的最大公约数，再与 z 求最大公约数
ans = math.gcd(math.gcd(x, y), z)

# 输出结果
print(ans)