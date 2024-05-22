# 案例（发工资）
import random
account = 10000
for i in range(1, 21):
    num = random.randint(1, 10)
    if num < 5:
        print("员工%d，绩效分%d，低于5，不发工资，下一位" % (i,num))
    else:
        account -= 1000
        print("向员工%d发放工资1000元，账户余额还剩余%d元" % (i,account))
        print(f"向员工{i}发放工资1000元，账户余额还剩余{account}元")
    if account <= 0:
        print("工资发完了，下个月领取吧。")
        break
