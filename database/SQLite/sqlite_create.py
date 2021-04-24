import sqlite3

# 连接到数据库
conn = sqlite3.connect("test.db")

# 创建一个cursor
cursor = conn.cursor()

# 执行一条sql语句，创建user表
cursor.execute("""create table users
    (
        username varchar(20) primary key, 
        password varchar(128) 
    )
    """
) 
cursor.execute("""insert into users(username,password) 
            values("jhh","123456")"""
)

print(cursor.rowcount)
# 关闭cursor
cursor.close()
# 提交事务
conn.commit()
conn.close