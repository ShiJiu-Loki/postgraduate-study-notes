# 案例 将存款余额默认为5000元，存取款都设置为每次1000元
money = 5000
name = None


def menu():
    """
    主菜单函数
    """
    print("----------------主菜单----------------")
    print("lawliet，您好，欢迎来到秋水银行ATM。请选择操作：")
    print("查询余额\t[输入1]")
    print("存款\t\t[输入2]")
    print("存款\t\t[输入3]")
    print("退出\t\t[输入4]")
    return int(input("请输入您的选择："))


def balance():
    """
    查询余额函数
    """
    print("----------------查询余额----------------")
    print(f"lawliet，您好，您的余额剩余：{money}元")


def deposit(amount):
    """
    存款函数
    :param amount:存款金额
    :return:
    """
    print("----------------存款----------------")
    global money
    money += amount
    print(f"lawliet，您好，您存款{amount}元成功")
    print(f"lawliet，您好，您的余额剩余：{money}")


def withdraw(amount):
    """
    取款函数
    :param amount:取款金额
    :return:
    """
    print("----------------取款----------------")
    global money
    if money >= amount:
        money -= amount
        print(f"lawliet，您好，您取款{amount}元成功")
    else:
        print("您好，余额不足")
    print(f"lawliet，您好，您的余额剩余：{money}")


name = input("请输入您的姓名：")
while True:
    select = menu()
    if select == 1:
        balance()
    elif select == 2:
        deposit(1000)
    elif select == 3:
        withdraw(1000)
    elif select == 4:
        break
