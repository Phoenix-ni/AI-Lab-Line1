# Task09 异常捕获 try-except
## 任务目标
学习Python异常捕获机制，掌握 try、except、else、finally、raise 的用法；区分不同异常类型，实现程序出错时友好提示、不直接崩溃。

## 文件说明
- demo_file_try.py：文件读取示例，捕获 FileNotFoundError（文件不存在异常）
- demo_calc_try.py：除法运算，分别捕获 ValueError（输入不是数字）、ZeroDivisionError（除零）
- demo_all_except.py：使用 Exception 通用捕获异常，查看错误详情
- demo_raise.py：使用 raise 主动抛出异常，限制非法输入

## 核心知识点
1. `try`：存放**有可能报错**的代码；一旦里面出错，立刻跳出try块
2. `except 指定错误类型`：捕获对应类型的异常，自定义错误提示（推荐写具体异常，不滥用万能捕获）
3. `else`：只有 try 里面代码**没有任何报错**的时候，才会执行
4. `finally`：无论代码成功还是报错，这一段代码一定会执行，常用于资源清理
5. `raise`：手动主动抛出异常，用来拦截不符合规则的数据

## 运行截图
![task09_1_file](task09_1_file.png)
![task09_2_calc_raise](task09_2_calc_raise.png)

## 踩坑记录
1. try 块不要塞过多无关代码，只放容易出错的片段
2. 空 `except:` 不推荐，无法定位错误类型，作业优先使用指定异常捕获
3. raise 抛出的异常如果没有写except接住，程序依然会终止并打印报错信息

## 总结
异常捕获可以提升程序鲁棒性，避免用户非法输入、文件缺失等情况直接让程序崩溃；raise 用于主动校验数据，把不符合业务规则的情况变成异常。