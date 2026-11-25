#最大公约数
x,y,z = map(int,input().split())
m = min(x,y,z)
g = 1
for i in range (m,0,-1):
    if x % i == 0 and y % i == 0 and z % i == 0:
        g = i
        break
print(g)
