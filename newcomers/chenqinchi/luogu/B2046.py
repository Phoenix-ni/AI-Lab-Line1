n = int(input())
t1 = n / 1.2
t2 = n / 3.0
t2_m =t2 + 27 + 23
if t2_m < t1:
    print("Bike")
elif t2_m > t1:
    print("Walk")
else:
    print("All")
