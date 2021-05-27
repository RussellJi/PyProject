import time, threading
import cv2
# cap = cv2.VideoCapture("http://192.168.4.3:81/stream")
cap = cv2.VideoCapture("http://www.896.tv/live/1")

def foo1():
  while True:
    if( cap.isOpened() ) :
      ret,img = cap.read()
      cv2.imshow("image",img)
      cv2.waitKey(10)

def foo2():
  i=0
  while i<100:
    print(i)
    time.sleep(1)
    i=i+1

t1 = threading.Thread(target=foo1)

t1.start()
# foo2()
