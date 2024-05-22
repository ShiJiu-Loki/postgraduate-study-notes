# __str__字符串方法
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


student = Student("周杰轮", 11)
print(student)
print(str(student))
print(type(student))
print(type(str(student)))
print("=======================================================")


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Student类对象，name={self.name}, age={self.age}"


student = Student("周杰轮", 11)
print(student)
print(str(student))
