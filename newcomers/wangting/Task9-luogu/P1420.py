n=int(input())
a=list(map(int,input().split()))
max_len=1
now=1
for i in range(1,n):
    if a[i]==a[i-1]+1:
        now+=1
        if now>max_len:
            max_len=now
    else:
        now=1
print(max_len)