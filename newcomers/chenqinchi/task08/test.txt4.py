# ① read()：一次性全部读出来，返回字符串
print("==== read() ====")
with open("test.txt", "r", encoding="utf-8") as f:
    res1 = f.read()
print(res1)

# ② readline()：一次只读 一行
print("\n==== readline() ====")
with open("test.txt", "r", encoding="utf-8") as f:
    line1 = f.readline()
    line2 = f.readline()
print(line1) # strip() 删掉换行符 \n
print(line2.strip())

# ③ readlines()：读出全部行，放到列表里，一行=列表一个元素
print("\n==== readlines() ====")
with open("test.txt", "r", encoding="utf-8") as f:
    res_list = f.readlines()
print(res_list)
