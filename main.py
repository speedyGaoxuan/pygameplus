import os
import random

from pygameplus import *
from random import *
import time
import threading


# closing = False


# def fun():
#     global list
#     while True:
#         for i in range(100):
#             n = rect((randint(0, 255), randint(0, 255), randint(0, 255)),
#                      (randint(0, 800), randint(0, 450), 50, 50),)
#             list.append(n)
#             time.sleep(0.01)
#             # print("im still here")
#         while not list.isempty():
#             list.pop()
#             time.sleep(0.01)


# def fun():
#     global list
#     while True:
#         for i in range(200):
#             n = circle(color=(randint(0, 255), randint(0, 255), randint(0, 255)),
#                        center=(randint(25, 800), randint(25, 450)), radius=30)
#             list.append(n)
#             time.sleep(0.01)
#             # print("im still here")
#         while not list.isempty():
#             list.pop()
#             time.sleep(0.01)

def fun():
    global list
    while True:
        for i in range(200):
            if getrandbits(1)==1:
                n = circle(color=(randint(0, 255), randint(0, 255), randint(0, 255)),
                           center=(randint(25, 800), randint(25, 450)), radius=30)
            else:
                n = rect((randint(0, 255), randint(0, 255), randint(0, 255)),
                         (randint(0, 800), randint(0, 450), 50, 50),)
            list.append(n)
            time.sleep(0.01)
            # print("im still here")
        while not list.isempty():
            list.pop()
            time.sleep(0.01)


def test():
    while True:
        for i in range(100):
            print(i)
            time.sleep(0.05)


pygame.init()
DISPLAYSURF = pygame.display.set_mode((800, 450))
pygame.display.set_caption('hello world!')
FPS = 120
fpsClock = pygame.time.Clock()

list = linklist(DISPLAYSURF)
# list.append(Node((10, 20, 30, 40)))


t1 = threading.Thread(target=fun, daemon=True)
# t2 = threading.Thread(target=test, daemon=True)
t1.start()
# t2.start()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    DISPLAYSURF.fill((255, 255, 255))
    list.show()
    pygame.display.update()
    fpsClock.tick(FPS)
