"""
国内疫情地图
将各省级疫情信息展示出来
"""
import json
from pyecharts.charts import Map
from pyecharts.options import *
from my_utils.province_name_deal import name_deal

# 打开疫情文件读取数据，关闭文件
with open("地图数据\\疫情.txt", 'r', encoding='UTF-8') as f:
    data = f.read()
# 将疫情数据转化为python对象
data = json.loads(data)
# json数据处理,取出每个省份和对应的确诊人数
nation_data = data['areaTree'][0]['children']
# 准备国内各省份数据列表
data_list = list()
# 遍历各省份，将省份名称和确诊人数组装成元组，添加到列表中
for province_data in nation_data:
    province_name = province_data['name']                   # 省份名称
    province_confirm = province_data['total']['confirm']    # 确诊人数
    # 省份名称不够规范，需要处理成完整的省份名称(name_deal()方法为自定义处理方法)
    data_list.append((name_deal(province_name), province_confirm))
# print(data_list)

# 创建地图对象
map = Map()
# 添加数据
map.add("国内疫情地图", data_list, "china")
# 设置全局配置，定制分段的视觉映射
map.set_global_opts(
    title_opts=TitleOpts(title="全国疫情地图"),
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
map.render("全国疫情地图.html")
