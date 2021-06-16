from socket import *
import sys
import pygame
from pynput import keyboard

from time import ctime


keyp = '0'
i = 0
sig = "0"

def key_monitor(s):
    def on_press(key):
        try:
        
            print("按下字母键{0}".format(key.char))
            
        except Exception:

            print("按下特殊(非字母)的按键{0}".format(key))
            sig = "1"
            s.sendall(sig.encode())

    def on_release(key):
       
        print("按键{0}被松开".format(key))
        if key == keyboard.Key.esc:
            return False

    print("线程1")
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
if __name__ == '__main__':
    
    address = ('192.168.209.1', 8888)  # 服务端地址和端口
    s = socket(AF_INET, SOCK_STREAM)
    pygame.init()
    try:
        print("dodo")
        s.connect(address)  # 尝试连接服务端
    except Exception:
        print('[!] Server not found ot not open')
        sys.exit()
                                                   
    finally:        
        key_monitor(s)
        s.close()           