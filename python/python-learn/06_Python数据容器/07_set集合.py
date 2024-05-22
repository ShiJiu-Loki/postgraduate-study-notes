# 有如下列表对象：
# my_list = ['黑马程序员', '传智播客', '黑马程序员', '传智播客', 'itheima', 'itcast', 'itheima', 'itcast', 'best']
# 请：
# •定义一个空集合
my_list = ['黑马程序员', '传智播客', '黑马程序员', '传智播客', 'itheima', 'itcast', 'itheima', 'itcast', 'best']
my_set = set()
# •通过for循环遍历列表
# •在for循环中将列表的元素添加至集合
for ele in my_list:
    print(ele)
    my_set.add(ele)
# •最终得到元素去重后的集合对象，并打印输出
print(my_set)
