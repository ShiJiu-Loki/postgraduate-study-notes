# 执行非查询性质SQL

from pymysql import Connection
# 获取到MySQL数据库的链接对象
conn = Connection(
    host='localhost',   # 主机名（或IP地址）
    port=3306,          # 端口，默认3306
    user='root',        # 用户名
    password='123456'   # 密码
)
# 获取游标对象
cursor = conn.cursor()
conn.select_db("test")  # 选择数据库
# 使用游标对象，执行sql语句
cursor.execute("CREATE TABLE test_pymysql(id INT, info VARCHAR(255))")
# 关闭到数据库的链接
conn.close()
