# 形参注解
def add(x: int, y: int):
    return x + y


def func(data: list):
    data.append()


add()   # 在括号内Ctrl+P
func()  # 在括号内Ctrl+P


# 返回值注解
def add(x: int, y: int) -> int:
    return x + y


def func(data: list[int]) -> list[int]:
    pass


res = add(1, 2)     # 鼠标悬停在方法上
func([1, 2, 3])         # 鼠标悬停在方法上
