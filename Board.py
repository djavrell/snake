#! /usr/bin/python3.4
__author__ = 'proute_k'

from Apple import *
from Cherry import *
from Body import *


class board():
    def __init__(self, mx, my):
        self.map = [[define.elem["case"]] * my for _ in range(mx)]
        self.mx = mx
        self.my = my
        self.head = [self.mx / 2, self.my / 2]
        self.b = body()
        self.apple = Apple(self.mx, self.my)
        self.cherry = Cherry(self.mx, self.my)

    def initBoard(self):
        self.b.init_body(self.head)
        self.apple.setApple(self.map)
        self.cherry.setCherry(self.map)
        print(self.cherry.cherry)
        for x in range(self.mx):
            for y in range(self.my):
                self.map[x][y] = define.elem["head"] if [x, y] == self.head \
                    else define.elem["body"] if (x, y) in self.b.body \
                    else define.elem["apple"] if self.apple.isApple([x, y]) \
                    else define.elem["cherry"] if self.cherry.isCherryConst([x, y]) \
                    else define.elem["case"]

    def updateBoard(self):
        for x in range(self.mx):
            for y in range(self.my):
                self.map[x][y] = define.elem["head"] if [x, y] == self.head \
                    else define.elem["body"] if (x, y) in self.b.body \
                    else define.elem["apple"] if self.apple.isApple([x, y]) \
                    else define.elem["cherry"] if self.cherry.isCherryConst([x, y]) \
                    else define.elem["case"]

    def getmap(self):
        return self.map

    def get_head(self):
        return self.head

    def set_head(self, x, y):
        self.head = [x, y]

    def isWall(self, p):
        if p[0] < 0 or p[0] > self.mx or p[1] < 0 or p[1] > self.my:
            return False
        return True

    def deb(self):
        for x in range(self.mx):
            for y in range(self.my):
                print('{} '.format(self.map[x][y]), end="")
            print()