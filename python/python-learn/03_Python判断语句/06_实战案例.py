# 综合案例：通过逻辑判断语句，完成猜数字的案例代码编写
# 案例需求：定义一个数字（1~10，随机产生），通过3次判断来猜出来数字
# 案例要求：
#   1. 数字随机产生，范围1-10
#   2. 有3次机会猜测数字，通过3层嵌套判断实现
#   3. 每次猜不中，会提示大了或小了
import random
num = random.randint(1, 10)
print(num)  # 打印出随机生成的数字，便于测试

guess = int(input("请输入你要猜测的数字："))
if guess == num:
    print("第一次猜对了")
else:
    if guess > num:
        print("大了")
    else:
        print("小了")

    guess = int(input("请输入你要猜测的数字："))
    if guess == num:
        print("第二次猜对了")
    else:
        if guess > num:
            print("大了")
        else:
            print("小了")

        guess = int(input("请输入你要猜测的数字："))
        if guess == num:
            print("第三次猜对了")
        else:
            print("三次机会用完了，没有猜中")
