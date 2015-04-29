#! /usr/bin/python3.4
__author__ = 'proute_k'

import define
import sdl2
import sdl2.ext

class gui():
    def __init__(self, wx, wy):
        self.R = None
        self.win = None
        self.render = None
        self.s_render = None
        self.factory = None
        self.sprite = None
        self.x = wx
        self.y = wy

    def init(self):
        self.R = sdl2.ext.Resources(__file__, "sprite")
        sdl2.ext.init()
        self.win = sdl2.ext.Window(define.win_name, size=(self.x, self.y))
        self.render = sdl2.ext.Renderer(self.win)
        self.factory = sdl2.ext.SpriteFactory(sdl2.ext.TEXTURE, renderer=self.render)
        self.win.show()
        self.sprite = None
        self.s_render = self.factory.create_sprite_render_system(self.win)

    def get_event(self):
        pass

    def draw(self, board):
        pass