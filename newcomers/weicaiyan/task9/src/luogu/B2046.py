s = int(input())
bike_time = s / 3.0 + 50
walk_time = s / 1.2
if bike_time < walk_time:
    print("Bike")
elif walk_time < bike_time:
    print("Walk")
else:
    print("All")