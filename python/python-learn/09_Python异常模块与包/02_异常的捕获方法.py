

# print(name)
try:
    print(name)
except NameError as e:
    print('name变量名称未定义错误')

try:
    print(1/0)
except (NameError, ZeroDivisionError):
    print('ZeroDivision错误...')

try:
    print(num)
except (NameError, ZeroDivisionError) as e:
    print(e)

try:
    print(name)
except Exception as e:
    print(e)

try:
    print(1)
except Exception as e:
    print(e)
else:
    print('我是else，是没有异常的时候执行的代码')

try:
    f = open('test.txt', 'r')
except Exception as e:
    f = open('test.txt', 'w')
else:
    print('没有异常，真开心')
finally:
    f.close()
