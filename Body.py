#! /usr/bin/python3.4
__author__ = 'proute_k'

import define


class body():
    def __init__(self):
        """
            [(x,y), (x,y), ...] => morceau du corps
        """
        self.body = []

    def init_body(self, head):
        i = 0
        while i <= define.len_body:
            self.body.append((head[0] + i, head[1]))
            i += 1

    def isBody(self, d):
        if d in self.body:
            return True
        return False

    def rise(self, d):
        t = self.body[0]
        n = (t[0] + d[0], t[1] + d[1])
        self.body.insert(0, n)

    def move(self, d):
        t = self.body[0]
        self.body.pop()
        n = (t[0] + d[0], t[1] + d[1])
        self.body.insert(0, n)
