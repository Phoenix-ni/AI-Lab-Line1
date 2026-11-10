# B2046 骑车与走路
distance = int(input())

walk_time = distance / 1.2
bike_time = 27 + 23 + distance / 3.0

if bike_time < walk_time:
    print("Bike")
elif bike_time > walk_time:
    print("Walk")
else:
    print("All")