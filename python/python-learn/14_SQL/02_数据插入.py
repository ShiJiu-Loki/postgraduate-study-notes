# commit提交

from pymysql import Connection
# 获取到MySQL数据库的链接对象
conn = Connection(
    host='localhost',    # 主机名（或IP地址）
    port=3306,           # 端口，默认3306
    user='root',         # 用户名
    password='123456'    # 密码
    # autocommit=True     # 设置自动提交
)
# 获取游标对象
cursor = conn.cursor()
# 选择数据库
conn.select_db("test")
# 使用游标对象，执行sql语句
cursor.execute("insert into team values(8, 'AS仙阁')")
# 通过链接对象的commit()方法进行提交，否则不会插入数据
conn.commit()
# 关闭到数据库的链接
conn.close()
