# 设计类(class)
class Student:
    name = None             # 记录学生姓名
    gender = None           # 记录学生性别
    nationality = None      # 记录学生国籍
    native_place = None     # 记录学生籍贯
    age = None              # 记录学生年龄


# 创建对象
stu_1 = Student()
stu_2 = Student()
# 对象属性赋值
stu_1.name = "周杰轮"
stu_2.name = "林军杰"

print(stu_1)
print(stu_2)
print(type(stu_1))
print(type(stu_2))
print(stu_1.name)
print(stu_2.name)
