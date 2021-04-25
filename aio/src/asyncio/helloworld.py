import asyncio

# @asyncio.coroutine
# def hello():
#     print("hello world")
#     r = yield from asyncio.sleep(1)
#     print("hello again")

async def hello():
    print("hellp world")
    await asyncio.sleep(1)
    print("hello again")


# 获取eventloop:
loop = asyncio.get_event_loop()
# 执行coroutine
loop.run_until_complete(hello())
loop.close()