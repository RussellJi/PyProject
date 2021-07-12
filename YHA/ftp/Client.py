from ftplib import FTP


def ftpconnect():
    ftp_server = '192.168.3.80'
    username = 'user'
    password = 'root'
    ftp = FTP ()
    ftp.connect (ftp_server, 21)  # 连接
    ftp.login (username, password)  # 登录，如果匿名登录则用空串代替即可
    return ftp


def downloadfile():
    # remotepath = "c.txt";
    # ftp = ftpconnect()
    # print(ftp.getwelcome())  # 显示ftp服务器欢迎信息
    # bufsize = 1024  # 设置缓冲块大小
    # localpath = 'f:'+remotepath
    print (localpath)
    fp = open (localpath, 'wb')  # 以写模式在本地打开文件
    ftp.retrbinary ('RETR ' + remotepath, fp.write, bufsize)  # 接收服务器上文件并写入本地文件
    fp.close ()


def uploadfile():
    print (remotepath)
    fp = open (localpath, 'rb')
    ftp.storbinary ('STOR ' + remotepath, fp, bufsize)  # 上传文件
    fp.close ()  # 关闭文件


if __name__ == '__main__':

    # downloadfile()
    ftp = ftpconnect ()

    bufsize = 1024  # 设置缓冲块大小

    while True:
        print ("ftp>>")
        cmds = input ()
        cmd = str.split (cmds)  # 使用空格分隔用户输入的内容，返回一个列表

        if str.lower (cmd[0]) == 'quit':  # 如果用户只输入了一个quit
            ftp.quit ()
            break

        elif str.lower (cmd[0]) == 'dir':
            ftp.dir ()  # 查询文件路径

        elif str.lower (cmd[0]) == 'get':
            fileName = str.lower (cmd[1])
            remotepath = "\\" + fileName
            localpath = 'f:\\' + fileName
            downloadfile ()

        elif str.lower (cmd[0]) == 'put':
            fileName = str.lower (cmd[1])
            remotepath = "\\" + fileName
            localpath = 'f:\\' + fileName
            uploadfile ()
        else:
            print("请重新输入指令")
