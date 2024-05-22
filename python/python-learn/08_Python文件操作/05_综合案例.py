# encoding参数省略时默认为GBK
old = open('bill.txt', 'r', encoding='UTF-8')
new = open('bill.txt.bak', 'w', encoding='UTF-8')
for line in old:
    # print(line)
    # 是测试则继续读取下一行
    if line.count('测试') > 0:
        continue
    # 不是测试则 写 到 new对象的文件中
    new.write(line)
# 内容刷新，可省略，close()方法具有flush()功能
# new.flush()
new.close()
old.close()
