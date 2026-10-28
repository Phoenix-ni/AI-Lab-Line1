#淘淘摘苹果
apple_height = list(map(int, input().split()))
taotao_1 = int(input())
taotao_2 = taotao_1 + 30
count = 0
for height in apple_height:
    if height <= taotao_2:
        count += 1
print(count)
