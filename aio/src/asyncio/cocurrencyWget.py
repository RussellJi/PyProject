import asyncio
import threading

@asyncio.coroutine
def hello():
    print("hello world from %s" % threading.currentThread())
    # sleep()可以看为耗时一秒的io操作
    r = yield from asyncio.sleep(1)
    print("hello again from %s" % threading.currentThread())

@asyncio.coroutine
def wget(host):
    print("wget %s" % host)
    connect = asyncio.open_connection(host, 80)
    reader,writer = yield from connect
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode("utf-8"))
    yield from writer.drain()
    while True:
        line = yield from reader.readline()
        if line == b'\r\n':
            break
        print("%s header > %s" % (host,line.decode('utf-8').rstrip()))
    writer.close()    


# 获取eventloop:
loop = asyncio.get_event_loop()
tasks = [wget(host) for host in["www.baidu.com","www.sina.com","www.163.com"]]
# 执行coroutine
loop.run_until_complete(asyncio.wait(tasks))
loop.close()