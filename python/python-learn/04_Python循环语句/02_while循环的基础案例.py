# 猜数字案例：设置一个范围1-100的随机整数变量，通过while循环，配合input语句，判断输入的数字是否等于随机数
# 随机函数
import random
num = random.randint(1, 100)    # 随机生成一个1-100的数字
print(f'-----{num}-----')   # 把数字打印出来，方便测试
i = 0   # 记录猜了几次
flag = True
while flag:
    guess = int(input("请输入数字："))
    i += 1
    if guess == num:
        print("猜对了，猜了%d次" % i)
        flag = False
    elif guess > num:
        print("大了")
    else:
        print("小了")
