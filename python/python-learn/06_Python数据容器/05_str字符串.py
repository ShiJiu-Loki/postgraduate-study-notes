my_str = 'itcast and itheima'
# 查找
# print(my_str.index('and'))
# 替换
new_str = my_str.replace('and','kira')
# print(my_str)
# print(new_str)
# 分隔
names = "kira lawliet near mihael"
name = names.split(" ")
# print(name)
# print(type(names))
# print(type(name))
# 去空格
my_str = "  itcast and itheima  "
# print(my_str.strip())
my_str = "12itcast and itheima21"
# print(my_str.strip("12"))
# 统计
# print(my_str.count("it"))
# 长度
# print(len(my_str))


# 练习案例：分割字符串
# 给定一个字符串："itheima itcast boxuegu"
test = "itheima itcast boxuegu"
print(test)
# 统计字符串内有多少个"it"字符
print(test.count("it"))
# 将字符串内的空格，全部替换为字符："|"
new_test = test.replace(" ","|")
# print(test)
print(new_test)
# 并按照"|"进行字符串分割，得到列表
list_test = new_test.split("|")
print(list_test)

