import sqlite3

def insert(name,passwd):
    # 连接到数据库
    conn = sqlite3.connect("test.db")

    # 创建一个cursor
    cursor = conn.cursor()

    # 执行一条sql语句，创建user表
    cursor.execute("insert into users(username,password) values(?,?)",(name,passwd)) 
    signal = cursor.rowcount
    print(signal)
    # 关闭cursor
    cursor.close()
    # 提交事务
    conn.commit()
    # 关闭连接
    conn.close()
    return signal
