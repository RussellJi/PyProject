from pygame import *
import pygame
import time
from numpy import *
import cv2
import os
cap = cv2.VideoCapture(0)
pygame.init()
os.environ['SDL_VIDEO_CENTERED'] = '1'
screen = pygame.display.set_mode((600, 400), NOFRAME)
pygame.display.set_caption("pySSVEP")
done = False
clock = pygame.time.Clock()
n = 1
t1 = time.time()

while not done:
    for event in pygame.event.get():
        if (event.type == pygame.KEYUP) or (event.type == pygame.KEYDOWN):
            if event.key == pygame.K_ESCAPE:
                done = True
        if event.type == pygame.QUIT:
            done = True

    n = n + 1
    if n % 2 == 0:
        ret, frame = cap.read()
        try:
            frame = rot90(frame, k=-1)
        except:
            continue
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = pygame.surfarray.make_surface(frame)
        frame = pygame.transform.scale(frame, (600, 400))
        frame = pygame.transform.flip(frame, False, True)

        screen.blit(frame, (0, 0))

    if n == 60:
        n = 1
        t2 = time.time()
        print("t:", t2 - t1)
        t1 = t2
    clock.tick(60)  # 16 ms between frames ~ 60FPS
    pygame.display.flip()


pygame.quit()