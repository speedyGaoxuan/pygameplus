import pygame
import sys


class none_Node:
    def __init__(self):
        self.pre = None
        self.next = None


class Node(none_Node):
    def __init__(self, rect, color):
        # self.data = data
        self.rect = rect
        self.color = color
        super().__init__()


def connect(a: none_Node, b: none_Node):
    a.next = b
    b.pre = a


class linklist():
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
        n1 = self.end.pre
        connect(self.end.pre.pre, self.end)
        del n1

    def print(self):
        node = self.head
        while node.next.next != self.end:
            node = node.next
            print(node.data, end='->')
        print(node.next.data)

    def show(self):
        node = self.head
        while node.next != self.end:
            node = node.next
            pygame.draw.rect(self.surface, node.color, node.rect)
