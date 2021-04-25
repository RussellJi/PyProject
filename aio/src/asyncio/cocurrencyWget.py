import asyncio
import threading


async def wget(host):
    print("wget %s" % host)
    connect = asyncio.open_connection(host, 80)
    reader,writer = await connect
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode("utf-8"))
    await writer.drain()
    while True:
        line = await reader.readline()
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