#! /usr/bin/python3.4
__author__ = 'proute_k'

from Apple import *
from Cherry import *
from Body import *


class Board():
    def __init__(self, mx, my):
        self.map = [[define.elem["case"]] * my for _ in range(mx)]
        self.mx = mx
        self.my = my
        self.head = [self.mx / 2, self.my / 2]
        self.body = Body()
        self.apple = Apple(self.mx, self.my)
        self.cherry = Cherry(self.mx, self.my)

    def init_board(self):
        self.body.init_body(self.head)
        self.apple.set_apple(self.map)
        self.cherry.set_cherry(self.map)
        self.update_board()

    def update_board(self):
        for x in range(self.mx):
            for y in range(self.my):
                self.map[x][y] = define.elem["head"] if [x, y] == self.head \
                    else define.elem["body"] if self.body.is_body([x, y]) \
                    else define.elem["apple"] if self.apple.is_apple([x, y]) \
                    else define.elem["cherry"] if self.cherry.is_cherry_const([x, y]) \
                    else define.elem["case"]

    def get_map(self):
        return self.map

    def get_head(self):
        return self.head

    def set_head(self, x, y):
        self.head = [x, y]

    def is_wall(self, p):
        return p[0] < 0 or p[0] > self.mx or p[1] < 0 or p[1] > self.my

    def deb(self):
        for x in range(self.mx):
            for y in range(self.my):
                print('{} '.format(self.map[x][y]), end="")
            print()