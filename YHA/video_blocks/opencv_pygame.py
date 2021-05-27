from pygame import *
import pygame
import time
from numpy import *
import cv2
cap = cv2.VideoCapture(0)
pygame.init()
screen = pygame.display.set_mode([1400, 800])
pygame.display.set_caption("pySSVEP")
done = False
C_black = (0, 0, 0)
C_white = (255, 255, 255)
clock = pygame.time.Clock()
n = 1
t1 = time.time()
# location
r1 = Rect(400, 20, 150, 150)
r2 = Rect(850, 20, 150, 150)
r6 = Rect(400, 630, 150, 150)
r5 = Rect(850, 630, 150, 150)
r8 = Rect(100, 210, 150, 150)
r7 = Rect(100, 440, 150, 150)
r3 = Rect(1150, 210, 150, 150)
r4 = Rect(1150, 440, 150, 150)


# index
def sine(fre, cont, phase):
    s = 0.5*(1+math.sin(2*math.pi*fre*cont/60+phase))
    return s


# draw rect
def color_change(index1, index2, index3, index4, index5, index6, index7, index8):
    if index1 >= 0.5:
        screen.fill(C_white, r1)
    else:
        screen.fill(C_black, r1)
    if index2 >= 0.5:
        screen.fill(C_white, r2)
    else:
        screen.fill(C_black, r2)
    if index3 >= 0.5:
        screen.fill(C_white, r3)
    else:
        screen.fill(C_black, r3)
    if index4 >= 0.5:
        screen.fill(C_white, r4)
    else:
        screen.fill(C_black, r4)
    if index5 >= 0.5:
        screen.fill(C_white, r5)
    else:
        screen.fill(C_black, r5)
    if index6 >= 0.5:
        screen.fill(C_white, r6)
    else:
        screen.fill(C_black, r6)
    if index7 >= 0.5:
        screen.fill(C_white, r7)
    else:
        screen.fill(C_black, r7)
    if index8 >= 0.5:
         screen.fill(C_white, r8)
    else:
         screen.fill(C_black, r8)


while not done:
    for event in pygame.event.get():
        if (event.type == pygame.KEYUP) or (event.type == pygame.KEYDOWN):
            if event.key == pygame.K_ESCAPE:
                done = True
        if event.type == pygame.QUIT:
            done = True

    n = n + 1
    index1 = sine(7.0, n, 0)
    index2 = sine(8.0, n, 0.5 * math.pi)
    index3 = sine(9.0, n, math.pi)
    index4 = sine(10.0, n, 1.5*math.pi)
    index5 = sine(11.0, n, 0)
    index6 = sine(12.0, n, 0.5 * math.pi)
    index7 = sine(13.0, n, math.pi)
    index8 = sine(15.0, n, 1.5*math.pi)
    color_change(index1, index2, index3, index4, index5, index6, index7, index8)
    if n % 3 == 0:
        ret, frame = cap.read()
        try:
            frame = rot90(frame, k=-1)
        except:
            continue
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = pygame.surfarray.make_surface(frame)
        frame = pygame.transform.scale(frame, (800, 400))
        frame = pygame.transform.flip(frame, False, True)

        screen.blit(frame, (300, 200))

    if n == 60:
        n = 1
        t2 = time.time()
        print("t:", t2 - t1)
        t1 = t2
    clock.tick(60)  # 16 ms between frames ~ 60FPS
    pygame.display.flip()


pygame.quit()