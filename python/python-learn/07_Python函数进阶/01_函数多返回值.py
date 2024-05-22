# 多返回值
def test_return():
    return 1, 2


x, y = test_return()
print(x)    # 结果1
print(y)    # 结果2
