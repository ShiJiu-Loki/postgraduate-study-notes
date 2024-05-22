def fun01():
    print("这是func01的开始")
    num = 1/0
    print("这是func01的结束")


def fun02():
    print("这是func02的开始")
    fun01()
    print("这是func02的结束")


def main():
    try:
        fun02()
    except Exception as e:
        print(e)


# 异常在func01中没有被捕获
# 异常在func02中没有被捕获
# 异常在main中被捕获
main()
