# 字符串三种定义方式
name = '山河大学'
name = "山河大学"
name = """山河大学"""

# 字符串拼接
print("你好" + "Hello World")
print()

# 字符串格式化
class_num = '山河大学2022届'
avg_salary = 16781
message = "计算机科学与技术，%s毕业生，毕业平均工资：%d" % (class_num, avg_salary)
print(message)
print()

# 格式化精度控制
num1 = 11
num2 = 11.345
print("数字11宽度限制5，结果：%5d" % num1)
print("数字11宽度限制1，结果：%1d" % num1)
print("数字11.345宽度限制7，小数精度2，结果：%7.2f" % num2)
print("数字11.345不限制宽度，小数精度2，结果：%.2f" % num2)
print()

# 字符串格式化方式2
name = "lawliet"
birthday_year = 1979
stock_price = 19.99
print(f"我是{name}，我出生于：{birthday_year}年，我的收入是：{stock_price}")
print()

# 对表达式进行格式化
# 示例
print("1 * 1的结果是：%d" % (1 * 1))
print(f"1 * 1的结果是：{1 * 1}")
print("字符串在Python中的类型是：%s" % type('字符串'))
