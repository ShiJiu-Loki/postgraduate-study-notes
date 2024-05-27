import re

# match匹配
s = "python itheima python itheima python itheima"
result = re.match('python', s)
print(result)               # <re.Match object; span=(0, 6), match='python'>
print(result.span())        # (0, 6)
print(result.group())       # python
s = "1python itheima python itheima python itheima"
result = re.match('python', s)
print(result)               # None
print("===================================================")

# search
s = "1python666itheima666python666"
result = re.search('python', s)
print(result)               # <re.Match object; span=(1, 7), match='python'>
print(result.span())        # (1, 7)
print(result.group())       # python
s = "itheima666"
result = re.search('python', s)
print(result)               # None
print("===================================================")

# findall
s = "1python666itheima666python666"
result = re.findall('python', s)
print(result)               # ['python', 'python']
result = re.findall('itcast', s)
print(result)               # []
