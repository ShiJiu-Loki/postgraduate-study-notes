# 执行查询性质SQL

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
cursor.execute("SELECT * FROM team")
# 获取查询结果
results: tuple = cursor.fetchall()
for res in results:
    print(res)
# 关闭到数据库的链接
conn.close()
