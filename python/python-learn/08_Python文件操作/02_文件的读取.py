# open("python.txt", "r", encoding="UTF-8")


# 练习:单词计数
# f = open("E:/python_workspace/python-learn/08_Python文件操作/word.txt", 'r', encoding="UTF-8")
f = open("word.txt", 'r', encoding="UTF-8")
# num = 0
# for line in f:
#     num += line.count('itheima')
# print(num)
print(f.read().count('itheima'))    # 直接读取使用count方法统计即可，不需要像上述一样逐行统计
f.close()
# 不需要手动关闭文件的方式
with open("word.txt", 'r', encoding="UTF-8") as f:
    num = 0
    for line in f:
        num += line.count('itheima')
    print(num)
