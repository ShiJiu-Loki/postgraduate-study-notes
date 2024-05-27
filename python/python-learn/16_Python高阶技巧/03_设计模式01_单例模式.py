from test import str_tool

s1 = str_tool
s2 = str_tool
print(s1)       # s1和s2是同一个对象
print(s2)       # s1和s2是同一个对象


class Tool:
    pass

t1 = Tool()
t2 = Tool()
print(t1)       # t1和t2不是同一个对象
print(t2)       # t1和t2不是同一个对象
