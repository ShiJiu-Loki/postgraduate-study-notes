class Student:
    name = None
    age = None

    def say_hi(self):
        print(f"Hi大家好，我是{self.name}")


stu = Student()
stu.name = '周杰轮'
stu.say_hi()
