"""
演示可视化需求1：折线图开发
"""
import json
from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LabelOpts

# 处理数据
f_us = open("折线图数据/美国.txt", 'r', encoding='utf-8')
f_jp = open("折线图数据/日本.txt", 'r', encoding='utf-8')
f_in = open("折线图数据/印度.txt", 'r', encoding='utf-8')
us_data = f_us.read()
jp_data = f_jp.read()
in_data = f_in.read()
# 去掉不合JSON规范的开头
us_data = us_data.replace("jsonp_1629344292311_69436(", "")
jp_data = jp_data.replace("jsonp_1629350871167_29498(", "")
in_data = in_data.replace("jsonp_1629350745930_63180(", "")
# 去掉不合JSON规范的结尾
us_data = us_data[:-2]    # 等价于us_data[0:-2:1]，从第一开始取到倒数第二个(不包含倒数第二个)
jp_data = jp_data[:-2]
in_data = in_data[:-2]
# JSON转Python字典
us_dict = json.loads(us_data)
jp_dict = json.loads(jp_data)
in_dict = json.loads(in_data)
# 获取trend key
us_trend_data = us_dict['data'][0]['trend']
jp_trend_data = jp_dict['data'][0]['trend']
in_trend_data = in_dict['data'][0]['trend']
print(us_trend_data)    # 打印数据
print(jp_trend_data)    # 打印数据
print(in_trend_data)    # 打印数据
# 获取日期数据，用于x轴，取2020年（到314下标结束）
us_x_data = us_trend_data['updateDate'][:314]
jp_x_data = jp_trend_data['updateDate'][:314]
in_x_data = in_trend_data['updateDate'][:314]
print(us_x_data)
print(jp_x_data)
print(in_x_data)
# 获取确认数据，用于y轴，取2020年（到314下标结束）
us_y_data = us_trend_data['list'][0]['data'][:314]
jp_y_data = jp_trend_data['list'][0]['data'][:314]
in_y_data = in_trend_data['list'][0]['data'][:314]
print(us_y_data)
print(jp_y_data)
print(in_y_data)

# 生成图表
line = Line()
# 添加x轴数据
line.add_xaxis(us_x_data)   # x轴是公用的，所以使用一个国家的数据即可
# 添加y轴数据
line.add_yaxis("美国确诊人数", us_y_data, label_opts=LabelOpts(is_show=False))     # 添加美国的y轴数据
line.add_yaxis("日本确诊人数", jp_y_data, label_opts=LabelOpts(is_show=False))     # 添加日本的y轴数据
line.add_yaxis("印度确诊人数", in_y_data, label_opts=LabelOpts(is_show=False))     # 添加印度的y轴数据
# 设置全局选项
line.set_global_opts(
    title_opts=TitleOpts(title="2020年美日印三国确诊人数对比折线图", pos_left="center", pos_bottom="1%")
)
# 调用render方法，生成图表
line.render()
# 关闭文件对象
f_us.close()
f_jp.close()
f_in.close()
