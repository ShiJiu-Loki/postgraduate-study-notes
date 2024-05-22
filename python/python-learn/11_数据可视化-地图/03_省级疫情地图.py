"""
省级疫情地图
以河北省为例，将河北省疫情信息展示出来
"""
import json
from pyecharts.charts import Map
from pyecharts.options import *

# 打开疫情文件读取数据，关闭文件
with open("地图数据\\疫情.txt", 'r', encoding='UTF-8') as f:
    data = f.read()
# 将疫情数据转化为python对象
data = json.loads(data)
# json数据处理,取出每个省份数据
data = data['areaTree'][0]['children']
# 取出河北省疫情数据(也可以通过索引下标的方式进行获取，例如河北省的数据索引下标为32)
for province_data in data:
    if province_data['name'] == '河北':
        data = province_data
# print(data)
# 河北省各市级数据列表
city_list = list()
# 遍历各地级市，将地级市名称和确诊人数组装成元组，添加到列表中
for city_data in data['children']:
    city_name = city_data['name']+'市'
    city_confirm = city_data['total']['confirm']
    city_list.append((city_name, city_confirm))
print(city_list)

# 创建地图对象
map = Map()
# 添加数据
map.add("河北省疫情数据", city_list, "河北")
# 设置全局配置，定制分段的视觉映射
map.set_global_opts(
    title_opts=TitleOpts(title="河北省疫情地图"),
    visualmap_opts=VisualMapOpts(
        is_show=True,       # 是否显示
        is_piecewise=True,  # 是否分段
        pieces=[
            {"min": 1, "max": 9, "label": "1~9人", "color": "#CCFFFF"},
            {"min": 10, "max": 99, "label": "10~99人", "color": "#FFFF99"},
            {"min": 100, "max": 499, "label": "100~499", "color": "#FF9966"},
            {"min": 500, "max": 999, "label": "500~999人", "color": "#FF6666"},
            {"min": 1000, "max": 9999, "label": "1000~9999人", "color": "#CC3333"},
            {"min": 10000, "label": "10000人+", "color": "#990033"},
        ]
    )
)
# 绘图
map.render("河北省疫情地图.html")
