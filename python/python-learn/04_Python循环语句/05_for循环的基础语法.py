# 练习案例：数一数有几个a
# 定义字符串变量name，内容为："itheima is a brand of itcast"
name = "itheima is a brand of itcast"
# for循环处理字符串
i = 0
for x in name:
    if x == 'a':
        i += 1
print(i)    # 字符串中有i个a(4个)
print("==========================================================================")


# 练习案例：有几个偶数
# 定义一个数字变量num，内容随意
# 并使用range()语句，获取从1到num的序列，使用for循环遍历它。
# 在遍历的过程中，统计有多少偶数出现
# num = int(input("请输入数字："))
num = 100
stat = 0
for i in range(1, num):     # 生成从1到num的序列，不包含num本身
    if i % 2 == 0:
        stat += 1
print(stat)
print("==========================================================================")


# 变量作用域
for i in range(5):
    print("%d  " % i, end='')
print("")
print(i)    # 编程规范上来讲不允许这么做，但实际上可以访问到;建议在使用前定义变量i
