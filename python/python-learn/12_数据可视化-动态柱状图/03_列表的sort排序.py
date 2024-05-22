# 如下嵌套列表，要求对外层列表进行排序，排序的依据是内层列表的第二个元素数字
# 以前学习的sorted函数就无法适用了。可以使用列表的sort方法

# 定义排序方法
# element是将列表的每一个元素传入，函数体再决定由元素中的哪一个元素进行排序
def choose_sort_key(element):
    return element[1]


# 带名函数形式
my_list = [['a', 33], ['b', 55], ['c', 11]]
my_list.sort(key=choose_sort_key, reverse=True)
print(my_list)

# lambda匿名函数
my_list = [['a', 33], ['b', 55], ['c', 11]]
my_list.sort(key=lambda element: element[1], reverse=True)
print(my_list)
