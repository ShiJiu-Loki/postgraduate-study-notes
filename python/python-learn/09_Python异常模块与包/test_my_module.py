# import my_module1
# import my_module2

# my_module1.test(10, 20)
# my_module2.test(10, 20)


from my_module1 import test
from my_module2 import test

test(10, 20)    # 执行的是my_module2中的test方法
