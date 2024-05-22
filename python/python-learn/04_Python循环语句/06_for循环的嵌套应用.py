# 案例-for循环打印九九乘法表，并且使用range()语句
for i in range(1, 10):
    for j in range(1, i+1):
        print("%d * %d = %d\t" % (j, i, i*j), end='')
    print()
