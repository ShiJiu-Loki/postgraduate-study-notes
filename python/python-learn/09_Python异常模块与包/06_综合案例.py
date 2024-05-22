from my_utils import str_util
from my_utils import file_util

s = "您好，我叫lawliet"
print("字符串反转：", end='')
print(str_util.str_reverse(s))
print("姓名：", end='')
print(str_util.substr(s, 5, 12))
print("---------------------------------------------------")

file_name = "my_utils\\poem.txt"
data = ("滕王高阁临江渚，佩玉鸣鸾罢歌舞。\n"
        "画栋朝飞南浦云，珠帘暮卷西山雨。\n"
        "闲云潭影日悠悠，物换星移几度秋。\n"
        "阁中帝子今何在？槛外长江空自流。\n"
        "——（唐）王勃《滕王阁诗》")
file_util.print_file_info(file_name)
file_util.append_to_file(file_name, data)
# 追加完可以再输出一遍
print("---------------------------------------------------")
file_util.print_file_info(file_name)
