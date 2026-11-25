import os
base_path=os.path.dirname(os.path.abspath(__file__))
file_path=os.path.join(base_path,"data")

with open(file_path,"a",encoding="utf-8")as f:
    f.write("这是追加的一行\n")
    f.write("又是追加的一行\n")
    print("a模式追加完成")
