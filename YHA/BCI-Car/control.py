from socket import *
import sys
import time 
import pygame
from pygame import key
import keyboard

sig = "0" 

# def abc(x):
#     a = keyboard.KeyboardEvent('down', 28, 'space')
#     b = keyboard.KeyboardEvent('up', 28, 'space')
#     #按键事件a为按下enter键，第二个参数如果不知道每个按键的值就随便写，
#     #如果想知道按键的值可以用hook绑定所有事件后，输出x.scan_code即可
#     if x.event_type == 'down' and x.name == a.name:
#         sig="1"
#         # print(sig)                 
#     if x.event_type == 'up' and x.name == b.name:
#         sig="0" 
#     # print(sig)
#     #当监听的事件为space键，且是按下的时候                                      

address = ('127.0.0.1', 8888)  # 服务端地址和端口
s = socket(AF_INET, SOCK_STREAM)
pygame.init()
try:
    print("dodo")
    s.connect(address)  # 尝试连接服务端
except Exception:
    print('[!] Server not found ot not open')
    sys.exit()
while True:

    # keyboard.hook(abc)
    # s.sendall(sig.encode())
    time.sleep(1)      
    key_pressed = pygame.key.get_pressed()
    sig = "0"
    if key.get_pressed[pygame.K_RIGHT]:
        print("停止")
        sig="1"; 
    if sig == "1":
        s.sendall(sig.encode()) 
    if sig == 'q':  # 自定义结束字符串                                                              
        break                                                       
s.close()     