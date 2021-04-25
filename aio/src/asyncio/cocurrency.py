import asyncio
import threading

@asyncio.coroutine
def hello():
    print("hello world from %s" % threading.currentThread())
    # sleep()可以看为耗时一秒的io操作
    r = yield from asyncio.sleep(1)
    print("hello again from %s" % threading.currentThread())

# 获取eventloop:
loop = asyncio.get_event_loop()
tasks = [hello(),hello()]
# 执行coroutine
loop.run_until_complete(asyncio.wait(tasks))
loop.close()