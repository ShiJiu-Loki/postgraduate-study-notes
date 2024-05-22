# 定义函数
def add(x, y):
    result = x + y
    print(f"{x} + {y}的结果是:{result}")


# 调用函数
add(5, 6)


# 综合案例：升级版自动查核酸
# 定义一个函数，名称任意，并接受一个参数传入（数字类型，表示体温）
# 在函数内进行体温判断（正常范围：小于等于37.5度）
def detection(temperature):
    print("欢迎来到山河大学！请出示您的健康码以及72小时核酸证明，并配合测量体温！")
    if temperature <= 37.5:
        print(f"体温测量中，您的体温是：{temperature}度，体温正常请进！")
    else:
        print(f"体温测量中，您的体温是：{temperature}度，需要隔离！")


detection(37.5)
detection(38.2)
