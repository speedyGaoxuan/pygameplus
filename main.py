from pygameplus import *
from random import *
import time
import threading


# def random_choose(l):
#     r = randint(0, len(l) - 1)
#     return l[r]()


def random_color():
    return randint(0, 255), randint(0, 255), randint(0, 255)


def draw_circle():
    return circle(DISPLAYSURF, color=random_color(), center=(randint(25, 800), randint(25, 450)), radius=30)


def draw_square():
    return rect(DISPLAYSURF, random_color(), (randint(0, 800), randint(0, 450), 50, 50), )


def draw_line():
    return line(DISPLAYSURF, random_color(), (randint(0, 800), randint(0, 450)), (randint(0, 800), randint(0, 450)),
                randint(1, 20))


fun_list = [draw_line, draw_square, draw_circle]


def fun():
    global list
    while True:
        for i in range(200):
            n = choice(fun_list)()
            # print(n)
            list.append(n)
            time.sleep(0.01)
            # print("im still here")
        while not list.isempty():
            list.pop()
            time.sleep(0.01)


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
            print("exit with 0:window close operate")
            sys.exit()
    DISPLAYSURF.fill((255, 255, 255))
    list.show()
    pygame.display.update()
    fpsClock.tick(FPS)
