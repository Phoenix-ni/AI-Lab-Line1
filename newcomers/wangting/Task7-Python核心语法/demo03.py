def sum(base=0,*args,**kwargs):
    total=base
    for x in args:
        total+=x
    for y in kwargs.values():
        total+=y
    return total

result=sum(10,1,2,3,a=4,b=5)
print("求和结果：",result)