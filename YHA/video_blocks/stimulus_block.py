from pygame import *
import pygame
import time, threading
from numpy import *
import cv2

NUM_OF_THREAD = 9
b = threading.Barrier(NUM_OF_THREAD)
# cap = cv2.VideoCapture("http://192.168.4.3:81/stream")
cap = cv2.VideoCapture(0)
t1 = time.time()


def drawText2(points):
    pygame.font.init()
    font = pygame.font.Font("仿宋_GB2312.ttf", 40)
    text_sf = font.render("+", True, (255, 255, 0))

    text_rect = points
    return text_sf, text_rect


def blinking_block(points, frequency, point0, text1):
    COUNT = 1
    CLOCK = pygame.time.Clock()
    ''' FrameRate '''

    FrameRate = 70

    b.wait()  # Synchronize the start of each thread
    while True:  # execution block
        CLOCK.tick(FrameRate)
        tmp = sin(2 * pi * frequency * (COUNT / FrameRate))
        color = 255 * (tmp > 0)
        block = pygame.draw.rect(win, (color, color, color), points, 0)
        pygame.display.update(block)  # can't update in main thread which will introduce delay in different block
        """tex2, p2 = drawText2(point0)
        te2 = win.blit(tex2, p2)
        pygame.display.update(te2)"""
        COUNT += 1
        if COUNT == FrameRate:
            COUNT = 0

        print(CLOCK.get_time())  # check the time between each frame (144HZ=7ms; 60HZ=16.67ms)


def video():
    COUNT = 1
    CLOCK = pygame.time.Clock()
    ''' FrameRate '''
    FrameRate = 60
    b.wait()
    while True:
        CLOCK.tick(FrameRate)
        COUNT = COUNT + 1
        if COUNT % 4.5 == 0 and cap.isOpened():
            ret, frame = cap.read()
            try:
                frame = rot90(frame, k=-1)
            except:
                continue
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = pygame.surfarray.make_surface(frame)
            frame = pygame.transform.scale(frame, (400, 200))
            frame = pygame.transform.flip(frame, False, True)
            picture = win.blit(frame, (800, 400))
            pygame.display.update(picture)
            if COUNT == FrameRate:
                COUNT = 0
            print(CLOCK.get_time())









if __name__ == '__main__':
    pygame.init()
    pygame.TIMER_RESOLUTION = 1  # set time resolutions
    win = pygame.display.set_mode((1920, 1080), FULLSCREEN)

    # background canvas
    bg = pygame.Surface(win.get_size())
    bg = bg.convert()
    bg.fill((0, 0, 0))  # black background
    # display
    win.blit(bg, (0, 0))
    pygame.display.update()
    pygame.display.set_caption("Blinking")

    ''' frequency '''
    frequency = [8, 9, 10, 11, 12, 13, 14, 15]  # frequency bank
    ''' POINTS '''
    """POINTS1 = [[(1175, 0), (1070, 210), (1280, 210)],  
              [(1175, 640), (1070, 430), (1280, 430)],  
              [(425, 0), (530, 210), (320, 210)],  
              [(425, 640), (530, 430), (320, 430)],  
              [(0, 320), (210, 425), (210, 215)],  
              [(850, 320), (640, 425), (640, 215)]]  
              """
    """POINTS2 = [(100, 100, 100, 100),
               (600, 100, 100, 100),
               (1200, 100, 100, 100),
               (100, 400, 100, 100),
               (600, 400, 100, 100),
               (1200, 400, 100, 100),
               (100, 700, 100, 100),
               (600, 700, 100, 100)]"""
    """POINTS3 = [(40, 40, 100, 100),
               (650, 40, 100, 100),
               (1260, 40, 100, 100),
               (40, 660, 100, 100),
               (650, 660, 100, 100),
               (1260, 660, 100, 100),
               (200, 350, 100, 100),
               (1100, 350, 100, 100)]"""
    POINTS4 = [(200, 50, 120, 120),
               (900, 50, 120, 120),
               (1600, 50, 120, 120),
               (1400, 480, 120, 120),
               (1600, 910, 120, 120),
               (900, 910, 120, 120),
               (200, 910, 120, 120),
               (400, 480, 120, 120)]
    POINTS0 = [(250, 90),
               (950, 90),
               (1650, 90),
               (1450, 520),
               (1650, 950),
               (950, 950),
               (250, 950),
               (450, 520)]
    text = ["A", "B", "C", "D", "E", "F", "G", "H"]

    threads = []
    for i in range(8):
        threads.append(threading.Thread(target=blinking_block, args=(POINTS4[i], frequency[i], POINTS0[i], text[i])))
        threads[i].setDaemon(True)
        threads[i].start()
    Video = threading.Thread(target=video)
    Video.setDaemon(True)
    Video.start()
    RUN = True
    while RUN:
        for event in pygame.event.get():
            if (event.type == pygame.KEYUP) or (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_ESCAPE):
                    RUN = False
            if event.type == pygame.QUIT:
                RUN = False
        pygame.time.delay(100)
    pygame.quit()


