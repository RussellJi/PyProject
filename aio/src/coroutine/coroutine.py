# 消费者通过yield读取发送消息
def consumer():
    r = ''
    while True:
        n = yield r
        # 如果n为0，返回
        if not n:
            return
        print("[CONSUMER] Consuming %d..." % n)
        r = '200 OK'

# 生产者
def producer(c):
    c.send(None)
    n = 0
    while n<5:
        n+=1
        print("[PRODUCER] Producing %d..." % n)
        r = c.send(n)
        print("[PRODUCER] Consumer return %s" % r)
    c.close()

c = consumer()
producer(c)


