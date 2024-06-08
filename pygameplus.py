import os

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "PYGAME_HIDE_SUPPORT_PROMPT"

import pygame
import sys


class none_Node:
    def __init__(self):
        self.pre = None
        self.next = None


class Node(none_Node):
    def __init__(self, container):
        self.container = container
        super().__init__()


class line(Node):
    def __init__(self, con, color, start, end, width=1):
        self.color = color
        self.start = start
        self.end = end
        self.width = width
        super().__init__(con)

    def show(self):
        pygame.draw.line(self.container.surface, self.color, self.start, self.end, self.width)


class rect(Node):
    def __init__(self, con, color, rect):
        self.rect = rect
        self.color = color
        super().__init__(con)

    def show(self):
        pygame.draw.rect(self.container.surface, self.color, self.rect)


class circle(Node):
    def __init__(self, con, color, center, radius):
        self.color = color
        self.center = center
        self.radius = radius
        super().__init__(con)

    def show(self):
        pygame.draw.circle(self.container.surface, self.color, self.center, self.radius)


def connect(a: none_Node, b: none_Node):
    a.next = b
    b.pre = a


class linklist:
    def __init__(self, surface):
        self.head = none_Node()
        self.end = none_Node()
        self.head.next = self.end
        self.end.pre = self.head
        self.surface = surface

    def isempty(self):
        return self.head.next is self.end

    # 尾插
    def append(self, node):
        connect(self.end.pre, node)
        connect(node, self.end)

    def pop(self):
        if not self.isempty():
            n1 = self.end.pre
            connect(self.end.pre.pre, self.end)
            del n1

    def clear(self):
        connect(self.head, self.end)

    def print(self):
        if self.isempty():
            print("empty!!!")
        else:
            node = self.head
            while node.next.next != self.end:
                node = node.next
                print(node.rect, end='->')
            print(node.next.rect)

    def show(self):
        if self.isempty():
            # print("empty!!!")
            pass
        else:
            node = self.head
            while node.next != self.end:
                node = node.next
                node.show()
