#! /usr/bin/python3.4
__author__ = 'proute_k'

import sdl2
import sdl2.ext
from Board import *
from Gui import *


class game:
    def __init__(self, mx = 10, my = 10):
        self.b = board(mx, my)
        self.gui = gui(mx, my)
        self.last = sdl2.SDLK_UP
        self.dir = {
            sdl2.SDLK_UP: [-1, 0],
            sdl2.SDLK_DOWN: [1, 0],
            sdl2.SDLK_LEFT: [0, -1],
            sdl2.SDLK_RIGHT: [0, 1],
            }

    def start(self):
        run = True
        self.b.initBoard()
        while run:
            for e in sdl2.ext.get_events():
                if e.type == sdl2.SDL_QUIT:
                    exit()
                if e.type == sdl2.SDL_KEYDOWN:
                    k = e.key.keysym.sym
                    if k in self.dir.keys() and self.last != k:
                        self.last = self.checkKey(k)
                    if k == sdl2.SDLK_ESCAPE:
                        self.Quit()
            run = self.move(self.dir[self.last])
            self.gui.aff(self.b.getmap())
            sdl2.SDL_Delay(200)
        sdl2.ext.quit()
        return 0

    def checkKey(self, k):
        l = self.dir[self.last]
        n = self.dir[k]
        return self.last if n[0] == l[0] or n[1] == l[1] else k

    def move(self, d):
        h = self.b.get_head()
        n = (h[0] + d[0], h[1] + d[1])
        self.b.set_head(n[0], n[1])
        if self.b.b.isBody(n):
            return False
        if self.b.apple.isApple(n):
            self.b.b.rise(d)
            self.b.apple.setApple(self.b.getmap())
        elif self.b.cherry.isCherry(self.b.getmap(), n):
            self.b.b.rise(d)
            self.b.cherry.setCherry(self.b.getmap())
        else:
            self.b.b.move(d)
        self.b.updateBoard()
        ret = self.b.isWall(n)
        return ret

    def Quit(self):
        exit()

    def aff(self):
        self.gui.draw(self.b)
