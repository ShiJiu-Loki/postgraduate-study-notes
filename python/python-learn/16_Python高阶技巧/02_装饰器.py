# 装饰器的一般写法（闭包写法）
# 定义一个闭包函数，在闭包函数内部：执行目标函数;并完成功能的添加
def outer(func):
    def inner():
        print("我要睡觉了")
        func()
        print("我起床了")
    return inner

def sleep():
    import random
    import time
    print("睡眠中......")
    time.sleep(random.randint(1, 5))

fn = outer(sleep)
fn()
print("==================================================")


# 装饰器的语法糖写法
# 使用@outer定义在目标函数sleep之上
def outer(func):
    def inner():
        print("我要睡觉了")
        func()
        print("我起床了")
    return inner

@outer
def sleep():
    import random
    import time
    print("睡眠中......")
    time.sleep(random.randint(1, 5))

sleep()
