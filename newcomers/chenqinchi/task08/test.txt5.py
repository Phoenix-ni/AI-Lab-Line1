with open("test.txt", "r", encoding="utf-8") as f:
    for line in f:
        # line自带换行符，strip去掉
        print("行内容：", line.strip())
