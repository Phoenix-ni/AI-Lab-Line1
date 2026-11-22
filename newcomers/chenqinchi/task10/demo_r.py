import os
base_path = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_path,"data.txt")
try:    
    with open(file_path,"r+",encoding="utf-8")as f:
        f.write("这是第一行内容\n")
        f.write("这是第二行内容\n")
        print("w模式写入完成!")
except FileNotFoundError:
    print("报错:找不到这个文件!检查文件位置")
else:
    print("文件读取成功，没有异常")
finally:
    print("这一句话永远都会打印，不管成功还是失败")
