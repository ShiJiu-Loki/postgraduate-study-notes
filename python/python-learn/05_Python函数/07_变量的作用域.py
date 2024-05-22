# 变量的作用域
num = 100


def test_a():
    num = 200
    print(num)


def test_b():
    # global 关键字声明num是全局变量
    global num  # 如果不声明global，则num为局部变量，不会影响最外层的num变量的值，此时等同test_a()
    num = 200
    print(num)


test_a()
print(f"全局变量num = {num}")   # 结果：全局变量num = 100
test_b()
print(f"全局变量num = {num}")   # 结果：全局变量num = 200
