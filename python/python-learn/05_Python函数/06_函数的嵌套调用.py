# 函数的嵌套调用
def func_b():
    print("---2---")


def func_a():
    print("---1---")
    func_b()
    print("---3---")


# 调用函数func_a，在函数func_a中又调用了函数fun_b
func_a()
