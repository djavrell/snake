#! /usr/bin/python3.4
__author__ = 'proute_k'

from Body import *
from random import randint


class board():
    def __init__(self, mx, my):
        self.map = [[define.elem["case"]] * my for _ in range(mx)]
        self.mx = mx
        self.my = my
        self.p = [mx / 2, my / 2]
        self.head = [mx / 2, my / 2]
        self.cherry = [0, 0]
        self.apple = [0, 0]
        self.b = body()
        self.b.init_body(self.head)

    def initBoard(self):
        self.setApple()
        self.setCherry()
        for x in range(self.mx):
            for y in range(self.my):
                self.map[x][y] = define.elem["head"] if [x, y] == self.head \
                    else define.elem["body"] if (x, y) in self.b.body \
                    else define.elem["apple"] if [x, y] == self.apple \
                    else define.elem["cherry"] if [x, y] == self.cherry \
                    else define.elem["case"]

    def updateBoard(self):
        for x in range(self.mx):
            for y in range(self.my):
                self.map[x][y] = define.elem["head"] if [x, y] == self.head \
                    else define.elem["body"] if (x, y) in self.b.body \
                    else define.elem["apple"] if [x, y] == self.apple \
                    else define.elem["cherry"] if [x, y] == self.cherry \
                    else define.elem["case"]

    def getp(self):
        return self.p

    def get_head(self):
        return self.head

    def getmap(self):
        return self.map

    def setp(self, x, y):
        self.p = [x, y]

    def set_head(self, x, y):
        self.head = [x, y]

    def setApple(self):
        x, y = 0, 0
        while 1:
            x = randint(0, self.mx - 1)
            y = randint(0, self.my - 1)
            if x < self.mx and y < self.my and self.map[x][y] == define.elem["case"]:
                self.apple = [x, y]
                break

    def setCherry(self):
        x, y = 0, 0
        while 1:
            x = randint(0, self.mx - 1)
            y = randint(0, self.my - 1)
            if x <= self.mx and y <= self.my and self.map[x][y] == define.elem["case"]:
                self.cherry = [x, y]
                break

    def isApple(self, p):
        if p[0] == self.apple[0] and p[1] == self.apple[1]:
            return True
        return False

    def isCherry(self, p):
        if p[0] == self.cherry[0] and p[1] == self.cherry[1]:
            return True
        return False

    def deb(self):
        for x in range(self.mx):
            for y in range(self.my):
                print('{} '.format(self.map[x][y]), end="")
            print()