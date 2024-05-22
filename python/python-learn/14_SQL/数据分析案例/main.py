"""
 面向对象，数据分析案例，主业务逻辑代码
 实现步骤：
  1.设计一个类，可以完成数据的封装
  2.设计一个抽象类，定义文件读取的相关功能，并使用子类实现具体功能
  3.读取文件，生产数据对象
  4.进行数据需求的逻辑计算（计算每一天的销售额）
  5.通过PyEcharts进行图形绘制
"""
from file_define import FileReader, TextFileReader, JsonFileReader
from data_define import Record
from pyecharts.charts import Bar
from pyecharts.options import *
from pyecharts.globals import ThemeType
from pymysql import Connection

text_file_reader = TextFileReader("2011年1月销售数据.txt")
json_file_reader = JsonFileReader("2011年2月销售数据JSON.txt")
jan_data: list[Record] = text_file_reader.read_data()
feb_data: list[Record] = json_file_reader.read_data()
# 将两个月份的数据合并为1个list存储
all_data: list[Record] = jan_data + feb_data
# print(len(all_data))    # 1987条数据，插入完成后可跟表的数据数量进行对照

# 构建MySQL链接对象
conn = Connection(
    host='localhost',  # 主机名（或IP地址）
    port=3306,  # 端口，默认3306
    user='root',  # 用户名
    password='123456'  # 密码
)
# 获得游标对象
cursor = conn.cursor()
# 选择数据库
conn.select_db("py_sql")
# 组织SQL语句
for record in all_data:
    sql = (f"INSERT INTO orders (order_date, order_id, money, province) "
           f"VALUES('{record.date}', '{record.order_id}', {record.money}, '{record.province}')")
    # print(sql)        # 打印SQL语句，检查语法
    cursor.execute(sql)
# 执行SQL语句
conn.commit()
# 关闭链接对象
conn.close()
