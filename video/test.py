import time, threading
import cv2
cap = cv2.VideoCapture("http://192.168.4.2:81/stream")


def foo1():
  while True:
    if( cap.isOpened() ) :
      ret,img = cap.read()
      cv2.imshow("image",img)
      cv2.waitKey(10)

t1 = threading.Thread(target=foo1)

t1.start()

