# 练习案例：成年人判断
# 结合前面学习的input输入语句，完成如下案例：
#   1. 通过input语句，获取键盘输入，为变量age赋值。（注意转换成数字类型）
#   2. 通过if判断是否是成年人，满足条件则输出提示信息
print("欢迎来到儿童游乐场，儿童免费，成人收费。")
age = int(input("请输入你的年龄："))
if age >= 18:
    print("您已成年，游玩需要补票10元。")
print("祝您游玩愉快。")
