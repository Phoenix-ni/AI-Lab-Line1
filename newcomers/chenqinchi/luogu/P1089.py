n,x = input().split()
count = 0
for i in range(1,int(n)+1):
    count += str(i).count(x)
print(count)
