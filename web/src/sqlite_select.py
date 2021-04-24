import sqlite3

def select(name):
    # 连接到数据库
    conn = sqlite3.connect("test.db")

    # 创建一个cursor
    cursor = conn.cursor()

    # 执行一条sql语句，创建user表
    cursor.execute("select password from users where username=:name",{"name":name}) 
    signal = cursor.fetchone()
    # print(signal)
    # 关闭cursor
    cursor.close()
    # 提交事务
    conn.commit()
    # 关闭连接
    conn.close()
    return signal
signal = select("zsm")
# print(type(signal))
# print(signal[0])
# 如果没有用户名，返回None，
if signal is None:
    print("用户名不存在")
elif signal[0]=="123456":
    print("登录成功")
else:
    print("用户名或密码错误")

