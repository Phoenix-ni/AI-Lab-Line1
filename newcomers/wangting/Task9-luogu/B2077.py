N=int(input())
while N>1:
    if N%2==0:
        print(f"{N}/2={N//2}")
        N=N//2
    else:
        print(f"{N}*3+1={N*3+1}")
        N=N*3+1
print("End")