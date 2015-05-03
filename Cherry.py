#! /usr/bin/python3.4
__author__ = 'proute_k'

import define
from random import randint


class Cherry():
    def __init__(self, mx, my):
        self.mx = mx
        self.my = my
        self.cherry = []
        self.life = 0
        self.current = 0

    def set_cherry(self, map):
        self.life = define.life_cherry
        self.current = self.life
        x, y = 0, 0
        if randint(0, 10) in define.list_rand:
            while 1:
                x = randint(0, self.mx - 1)
                y = randint(0, self.my - 1)
                if x < self.mx and y < self.my and map[x][y] == define.elem["case"]:
                    self.cherry = [x, y]
                    break
        else:
            self.cherry = [-1, -1]

    def is_cherry_const(self, p):
        if p[0] == self.cherry[0] and p[1] == self.cherry[1]:
            return True
        return False

    def is_cherry(self, map, p):
        if p[0] == self.cherry[0] and p[1] == self.cherry[1]:
            return True
        self.set_life(map)
        return False

    def set_life(self, map):
        self.current -= 1
        if self.current == 0:
            self.set_cherry(map)
