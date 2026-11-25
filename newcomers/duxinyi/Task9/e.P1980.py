#计数问题
n,x = map(int,input().split())
x = str(x)
count_s = 0
for i in range(1,n+1):
    count_s += str(i).count(x)

print(count_s)   
    
        