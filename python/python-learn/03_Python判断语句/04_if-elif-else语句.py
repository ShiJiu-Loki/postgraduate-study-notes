print("欢迎来到动物园")
if int(input("请输入你的身高（cm）：")) < 120:
    print("您的身高小于120CM，可以免费游玩。")
elif int(input("请输入你的vip级别(1~5)：")) > 3:
    print("您的vip级别大于3，可以免费游玩。")
elif int(input("请输入今天的日期(1~30)：")) == 1:
    print("今天是1号免费，可以免费游玩。")
else:
    print("不好意思，所有条件都不满足，需要购票10元。")
print("祝您游玩愉快。")
print("==========================================================================")


# 练习案例：猜猜心里数字
# 1. 定义一个变量，数字类型，内容随意。
# 2. 基于input语句输入猜想的数字，通过if和多次elif的组合，判断猜想数字是否和心里数字一致。
import random
num = random.randint(1,10)
print(num)  # 打印出随机生成的数字，便于测试
if int(input("请输入第一次猜想的数字：")) == num:
    print("猜对了")
elif int(input("不对，再猜一次：")) == num:
    print("猜对了")
elif int(input("不对，再猜最后一次：")) == num:
    print("猜对了")
else:
    print("Sorry，全部猜错啦，我想的是%d" % num)
