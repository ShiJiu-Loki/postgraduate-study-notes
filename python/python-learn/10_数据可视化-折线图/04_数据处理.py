import json

# 处理数据
f_us = open("折线图数据/美国.txt", 'r', encoding='utf-8')
us_data = f_us.read()
# 去掉不合JSON规范的开头
us_data = us_data.replace("jsonp_1629344292311_69436(", "")
# 去掉不合JSON规范的结尾
us_data = us_data[:-2]    # 等价于us_data[0:-2:1]，从第一开始取到倒数第二个(不包含倒数第二个)
# JSON转Python字典
us_dict = json.loads(us_data)
print(type(us_dict))    # 确认转换后的数据类型是否为字典(dict)
print(us_dict)  # 打印数据
# 获取trend key
trend_data = us_dict['data'][0]['trend']
print(trend_data)    # 打印数据
# 获取日期数据，用于x轴，取2020年（到314下标结束）
x_data = trend_data['updateDate'][:314]
print(x_data)
# 获取确认数据，用于y轴，取2020年（到314下标结束）
y_data = trend_data['list'][0]['data'][:314]
print(y_data)
# 生成图表
