#! /usr/bin/python3.4
__author__ = 'proute_k'

import Body


class board():
    def __init__(self, x, y):
        self.map = []
        self.px = 0
        self.py = 0
        self.head = [x/2, y/2]
        self.b = Body.body()
        self.b.init_body(x, y, self.head)

    def setx(self, x):
        self.px = x

    def sety(self, y):
        self.py = y

    def set_head(self, x, y):
        self.head[0] = x
        self.head[1] = y

    def getx(self):
        return self.px

    def gety(self):
        return self.py

    def get_head(self):
        return self.head

    def get_board(self):
        return self.map