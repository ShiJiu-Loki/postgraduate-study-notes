def test_func(compute):
    result = compute(1, 2)
    print(result)


def compute1(x, y):
    return x + y


def compute2(x, y):
    return x - y


def compute3(x, y):
    return x * y


def compute4(x, y):
    return x / y


test_func(compute1)  # 结果：3
test_func(compute2)  # 结果：-1
test_func(compute3)  # 结果：2
test_func(compute4)  # 结果：0.5


# 匿名函数
def test_func(compute):
    result = compute(1, 2)
    print(result)


def compute(x, y):
    return x + y


test_func(compute)  # 结果：3


def test_func(compute):
    result = compute(1, 2)
    print(result)


test_func(lambda x, y: x + y)   # 结果：3