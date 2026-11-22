import mytools

import random

from test_package import multiple

print("调用mytools.add:",mytools.add(6,7))
print("调用mytools.greet:",mytools.greet("Task10"))
print("随机数:",random.randint(1,100))
print("包里面multiple:",multiple(5,6))
