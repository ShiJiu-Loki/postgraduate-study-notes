# 原生使用类创建对象方式
class Person:
    pass
class Worker(Person):
    pass
class Student(Person):
    pass
class Teacher(Person):
    pass

worker = Worker()
stu = Student()
teacher = Teacher()


# 工厂模式
class Person:
    pass
class Worker(Person):
    pass
class Student(Person):
    pass
class Teacher(Person):
    pass

class Factory:
    def get_person(self, p_type):
        if p_type == 'w':
            return Worker()
        elif p_type == 's':
            return Student()
        else:
            return Teacher()

factory = Factory()
worker = factory.get_person('w')
stu = factory.get_person('s')
teacher = factory.get_person('t')
