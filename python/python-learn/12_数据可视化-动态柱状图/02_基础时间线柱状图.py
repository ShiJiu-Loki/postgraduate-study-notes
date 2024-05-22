"""
 演示带有时间线的柱状图的开发
"""
from pyecharts.charts import Bar, Timeline
from pyecharts.options import *
from pyecharts.globals import ThemeType

bar1 = Bar()
bar1.add_xaxis(['中国', '美国', '英国'])
bar1.add_yaxis("GDP", [30, 20, 10], label_opts=LabelOpts(position='right'))
bar1.reversal_axis()

bar2 = Bar()
bar2.add_xaxis(['中国', '美国', '英国'])
bar2.add_yaxis("GDP", [50, 30, 20], label_opts=LabelOpts(position='right'))
bar2.reversal_axis()

bar3 = Bar()
bar3.add_xaxis(['中国', '美国', '英国'])
bar3.add_yaxis("GDP", [85, 60, 50], label_opts=LabelOpts(position='right'))
bar3.reversal_axis()

# 创建时间线对象（theme设置主题）
timeline = Timeline({"theme": ThemeType.LIGHT})
# timeline对象添加bar柱状图
timeline.add(bar1, "2021年GDP")
timeline.add(bar2, "2022年GDP")
timeline.add(bar3, "2023年GDP")
# 设置自动播放
timeline.add_schema(
    play_interval=1000,         # 自动播放的时间间隔，单位毫秒
    is_timeline_show=True,      # 是否在自动播放的时候，显示时间线
    is_auto_play=True,          # 是否自动播放
    is_loop_play=True           # 是否循环自动播放
)
# 通过时间线绘图
timeline.render("基础时间线柱状图.html")
