# 序列切片
my_list = [1, 2, 3, 4, 5]
new_list = my_list[1:4]
print(new_list)     # [2, 3, 4]

my_tuple = (1, 2, 3, 4, 5)
new_tuple = my_tuple[:]
print(new_tuple)    # (1, 2, 3, 4, 5)

my_list = [1, 2, 3, 4, 5]
new_list = my_list[::2]
print(new_list)     # [1, 3, 5]

my_str = "12345"
new_str = my_str[:4:2]
print(new_str)      # "13"

my_str = "12345"
new_str = my_str[::-1]
print(new_str)      # "54321"

my_list = [1, 2, 3, 4, 5]
new_list = my_list[3:1:-1]      # [4, 3]
print(new_list)

my_tuple = (1, 2, 3, 4, 5)
new_tuple = my_tuple[:1:-2]     # (5, 3)
print(new_tuple)


# 有字符串："万过薪月，员序程马黑来，nohtyP学"
# - 请使用学过的任何方式，得到"黑马程序员"

# 可用方式参考：
# - 倒序字符串，切片取出或切片取出，然后倒序
print("--------------------------------------------")
test_str_0 = "万过薪月，员序程马黑来，nohtyP学"
test_str_1 = test_str_0[::-1]
print(test_str_1)
test_str_2 = test_str_1[9:14:]
print(test_str_2)
# - split分隔"，" replace替换"来"为空，倒序字符串
print("--------------------------------------------")
test1 = test_str_0.split("，")[1]
print(test1)
test2 = test1.replace("来","")
print(test2)
test3 = test2[::-1]
print(test3)
