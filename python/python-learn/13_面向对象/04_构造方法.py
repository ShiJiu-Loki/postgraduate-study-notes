# 构造方法__init__()
class Student:
    # name = None   # 可以省略
    # age = None    # 可以省略
    # tel = None    # 可以省略

    def __init__(self, name, age, tel):
        self.name = name
        self.age = age
        self.tel = tel


stu = Student("周杰轮", 31, '18500006666')
print(stu.name)
print(stu.age)
print(stu.tel)
