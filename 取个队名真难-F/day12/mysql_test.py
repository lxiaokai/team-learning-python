# @time 2018/10/26 16:50
# @Author lhf

import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",  # 数据库主机地址
    user="root",  # 数据库用户名
    password='123456',  # 数据库密码
    database='my_app' # 数据库名称
)

if __name__ == "__main__":
    conn = mysql.connector.connect(user='root', password='123456',database='my_app')
    # conn=mydb.connect()
    cursor = conn.cursor()
    # 插入一行记录，注意MySQL的占位符是%s:
    # cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
    cursor.execute('select * from user ')  #查询所有用户数据
    values = cursor.fetchall()
    print(type(values))
    print(values)

    username='xiaoqing'
    password='aaadddd'

    cursor.execute("select * from user where username = '%s' " % (username))
    values = cursor.fetchall()
    print(values)
    if not len(values):  #没有username用户数据
        cursor.execute("insert into user(username,password) values('%s', '%s')" % (username,password)) #插入一条数据
        conn.commit()

    cursor.execute('select * from user ')  # 查询所有用户数据
    values = cursor.fetchall()
    print(values)

    cursor.execute("update user set password = '%s' where username = '%s'" % ("abc123",username))  # 修改密码
    conn.commit()

    cursor.execute('select * from user ')  # 查询所有用户数据
    values = cursor.fetchall()
    print(values)

    cursor.execute("delete from user where username='%s'"%(username)) # 删除xiaoqing
    conn.commit()

    cursor.execute('select * from user ')  # 查询所有用户数据
    values = cursor.fetchall()
    print(values)

    cursor.close()
