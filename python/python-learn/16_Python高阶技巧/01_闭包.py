# 通过全局变量account_amount来记录余额
account_amount = 0      # 账户余额
def atm(num, deposit=True):
    global account_amount
    if deposit:
        account_amount += num
        print(f"存款：+{num}，账户余额：{account_amount}")
    else:
        account_amount -= num
        print(f"取款：-{num}，账户余额：{account_amount}")

atm(300)
atm(300)
atm(100, False)
print("===========================================================")


# 闭包
def account_create(initial_amount=0):
    def atm(num, deposit=True):
        nonlocal initial_amount     #需要使用nonlocal关键字修饰外部函数的变量才可在内部函数中修改它

        if deposit:
            initial_amount += num
            print(f"存款：+{num}，账户余额：{initial_amount}")
        else:
            initial_amount -= num
            print(f"取款：-{num}，账户余额：{initial_amount}")
    return atm

ac = account_create()
ac(300)
ac(300)
ac(100, False)
