#! /usr/bin/python3.4
__author__ = 'proute_k'

import define
from random import randint


class Apple():
    def __init__(self, mx, my):
        self.mx = mx
        self.my = my
        self.apple = []

    def set_apple(self, map):
        x, y = 0, 0
        while 1:
            x = randint(0, self.mx - 1)
            y = randint(0, self.my - 1)
            if x < self.mx and y < self.my and map[x][y] == define.elem["case"]:
                self.apple = [x, y]
                break

    def is_apple(self, p):
        if p[0] == self.apple[0] and p[1] == self.apple[1]:
            return True
        return False
