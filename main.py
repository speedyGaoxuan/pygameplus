import os

from pygameplus import *
from random import *
import time
import threading

closing = False


def fun():
    global list,closing
    time.sleep(1)
    while not closing:
        for i in range(100):
            n = Node((randint(0, 800), randint(0, 450), 50, 50),
                     (randint(0, 255), randint(0, 255), randint(0, 255)))
            list.append(n)
            time.sleep(0.01)
            # print("im still here")
        while not list.isempty():
            list.pop()
            time.sleep(0.01)


pygame.init()
DISPLAYSURF = pygame.display.set_mode((800, 450))
pygame.display.set_caption('hello world!')
FPS = 30
fpsClock = pygame.time.Clock()

list = linklist(DISPLAYSURF)
# list.append(Node((10, 20, 30, 40)))

t1 = threading.Thread(target=fun)
t1.start()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            closing = True
            sys.exit()
    DISPLAYSURF.fill((255, 255, 255))
    list.show()
    # list.print()
    pygame.display.update()
    fpsClock.tick(FPS)
