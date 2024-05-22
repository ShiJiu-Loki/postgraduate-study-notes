# as定义别名
# 模块别名
import time as tt
tt.sleep(2)
print("hello")

# 功能别名
from time import sleep as sl
sl(2)
# sleep(2)    # 报错
# time.sl(2)    # 报错，只能直接使用方法名的别名进行调用
print("hello")
