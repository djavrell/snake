#! /usr/bin/python3.4
__author__ = 'proute_k'

import sdl2
import sdl2.ext
from Board import *
from Gui import *


class Game:
    def __init__(self, mx=10, my=10):
        self.board = Board(mx, my)
        self.gui = Gui(mx, my)
        self.last = sdl2.SDLK_UP
        self.dir = {
            sdl2.SDLK_UP: [-1, 0],
            sdl2.SDLK_DOWN: [1, 0],
            sdl2.SDLK_LEFT: [0, -1],
            sdl2.SDLK_RIGHT: [0, 1],
            }

    def start(self):
        run = True
        self.board.init_board()
        while run:
            for e in sdl2.ext.get_events():
                if e.type == sdl2.SDL_QUIT:
                    exit()
                if e.type == sdl2.SDL_KEYDOWN:
                    k = e.key.keysym.sym
                    if k in self.dir.keys() and self.last != k:
                        self.last = self.check_key(k)
                    if k == sdl2.SDLK_ESCAPE:
                        self.quit()
            run = self.move(self.dir[self.last])
            self.gui.aff(self.board.get_map())
            sdl2.SDL_Delay(200)
        sdl2.ext.quit()
        return 0

    def check_key(self, k):
        l = self.dir[self.last]
        n = self.dir[k]
        return self.last if n[0] == l[0] or n[1] == l[1] else k

    def move(self, d):
        h = self.board.get_head()
        n = (h[0] + d[0], h[1] + d[1])
        self.board.set_head(n[0], n[1])
        if self.board.body.is_body(n):
            return False
        if self.board.apple.is_apple(n):
            self.board.body.rise(d)
            self.board.apple.set_apple(self.board.get_map())
        elif self.board.cherry.is_cherry(self.board.get_map(), n):
            self.board.body.rise(d)
            self.board.cherry.set_cherry(self.board.get_map())
        else:
            self.board.body.move(d)
        self.board.update_board()
        ret = self.board.is_wall(n)
        return ret

    def aff(self):
        self.gui.draw(self.board)

    def quit(self):
        exit()
