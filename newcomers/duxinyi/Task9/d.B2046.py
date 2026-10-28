#骑车与走路
s = float(input())
t1 = 50 + s / 3
t2 = s / 1.2
if t1 < t2:
    print("Bike")
elif t1 > t2:
    print("Walk")
else:
    print("All")