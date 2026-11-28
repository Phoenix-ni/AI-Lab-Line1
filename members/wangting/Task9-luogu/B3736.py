x,y,z=map(int,input().split())
while y!=0:
    temp=x%y
    x=y
    y=temp
while z!=0:
    temp=x%z
    x=z
    z=temp
print(x)