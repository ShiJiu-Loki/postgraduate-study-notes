"""
 演示第三个图表：GDP动态柱状图开发
"""
from pyecharts.charts import Bar, Timeline
from pyecharts.options import *
from pyecharts.globals import ThemeType

# 读取数据，删除第一行(标题)
f = open('动态柱状图数据/1960-2019全球GDP数据.csv', 'r')
lines = f.readlines()
lines.pop(0)
f.close()
# 将数据转换为字典存储
# 构建字典数据，格式为
# { 1960:[["美国", 123], ["中国", 123], ......], 1961: [[], [], ......] }
"""
格式结构如下：
{
   年份:[
        [国家, gdp],
        [国家, gdp],
        ...
   ],
   年份:[
        [国家, gdp],
        [国家, gdp],
        ...
   ],
   ......
}
"""
data_dict = {}
for line in lines:
    year = int(line.split(',')[0])          # 年份
    country = line.split(',')[1]            # 国家
    gdp = float(line.split(',')[2])         # GDP
    # 将每一年每一个国家的GDP数据添加到字典中
    # 如何判断字典里面有没有指定的key
    try:
        data_dict[year].append((country, gdp))
    except KeyError:
        data_dict[year] = []
        data_dict[year].append((country, gdp))
# print(data_dict)

# 创建时间线对象（theme设置主题）
timeline = Timeline({"theme": ThemeType.LIGHT})
# 将年份升序排序（字典无序）
sorted_year_list = sorted(data_dict.keys())
# print(sorted_year_list)
for year in sorted_year_list:
    data_dict[year].sort(key=lambda element: element[1], reverse=True)  # 按GDP数据降序排序
    year_data = data_dict[year][0:8]     # 取出GDP前八的数据
    # print(year_data)
    countrys = []
    gdps = []
    for country_data in year_data:
        countrys.append(country_data[0])                 # 取出国家名
        gdps.append(int(country_data[1] / 100000000))    # 取出GDP，单位：亿
    # print(country)
    # print(gdp)
    bar = Bar()             # 创建柱状图
    countrys.reverse()      # 反转国家，让GDP最高的排在上面
    gdps.reverse()          # 同步反转GDP数据
    # 设置标题
    bar.set_global_opts(title_opts=TitleOpts(title=f"{year}年全球GDP前8国家"))
    bar.add_xaxis(countrys)     # 添加x轴数据
    bar.add_yaxis("GDP(亿)", gdps, label_opts=LabelOpts(position='right'))   # 添加y轴数据
    bar.reversal_axis()     # 反转x和y轴
    timeline.add(bar, str(year))    # timeline对象添加bar柱状图，即时间线添加一个点(对象)
# 设置自动播放
timeline.add_schema(
    play_interval=1000,         # 自动播放的时间间隔，单位毫秒
    is_timeline_show=True,      # 是否在自动播放的时候，显示时间线
    is_auto_play=True,          # 是否自动播放
    is_loop_play=False          # 是否循环自动播放
)
timeline.render("1960-2019全球GDP前8国家.html")  # 通过时间线绘图
