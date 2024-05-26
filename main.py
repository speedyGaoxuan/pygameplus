from pygameplus import *
from random import *

#
# list = linklist()
# for i in range(10):
#     n = Node(random.randint(-100, 100))
#     list.append(n)
# list.print()
# list.pop()
# list.print()


pygame.init()
DISPLAYSURF = pygame.display.set_mode((800, 450))
pygame.display.set_caption('hello world!')

list = linklist(DISPLAYSURF)
# list.append(Node((10, 20, 30, 40)))
for i in range(100):
    n = Node((randint(0, 800), randint(0, 450), 50, 50),
             (randint(0, 255), randint(0, 255), randint(0, 255)))
    list.append(n)
while True:  # main game lop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        list.show()
        pygame.display.update()
