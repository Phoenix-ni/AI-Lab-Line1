n,x=map(int,input().split())
count=0
for i in range(1,n+1):
    for ch in str(i):
        if int(ch)==x:
            count+=1
print(count)