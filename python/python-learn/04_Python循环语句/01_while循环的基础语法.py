# 案例,计算1~100的累加，注意累加完后i的值
sum = 0
i = 1
while i <= 100:
    sum += i    # 等同于 sum = sum + i
    i += 1      # 等同于 i = i + 1
print("sum=%d" % sum)
print("i=%d" % i)
