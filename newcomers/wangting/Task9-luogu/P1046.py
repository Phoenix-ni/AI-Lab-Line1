m=map(int,input().split(" "))
n=int(input())
list1=list(m)
count=0
i=0
while i <len(list1):
    if (n>=list1[i])|((n+30)>=list1[i]):
        count+=1
    i+=1
print(count)