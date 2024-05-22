# 函数说明文档
def add(x, y):
    """
    函数说明
    :param x: 参数x的说明
    :param y: 参数y的说明
    :return:  返回值的说明
    """
    add_res = x + y
    return add_res


# 鼠标悬停在方法名上可以看到函数的说明文档
result = add(1, 2)
print(f"result={result}")
