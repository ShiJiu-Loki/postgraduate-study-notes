# __lt__小于符号比较方法
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


stu1 = Student("周杰轮", 11)
stu2 = Student("林军杰", 13)
# print(stu1 < stu2)    # 报错，不能进行比较
print("=======================================================")


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __lt__(self, other):
        return self.age < other.age


stu1 = Student("周杰轮", 11)
stu2 = Student("林军杰", 13)
print(stu1 < stu2)      # 结果：True
print(stu1 > stu2)      # 结果：False
