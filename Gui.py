#! /usr/bin/python3.4
__author__ = 'proute_k'

from random import randint
import define
import sdl2
import sdl2.ext


class gui():
    def __init__(self, wx, wy):
        sdl2.ext.init()
        self.R = sdl2.ext.Resources(__file__, "sprite")
        self.x = wx * define.size_case
        self.y = wy * define.size_case

        self.win = sdl2.ext.Window(define.win_name, size=(self.x, self.y))
        self.sprite = None

        self.render = sdl2.ext.Renderer(self.win)
        self.factory = sdl2.ext.SpriteFactory(sdl2.ext.TEXTURE, renderer=self.render)
        self.s_render = self.factory.create_sprite_render_system(self.win)

    def get_event(self):
        pass

    def draw(self, map):
        mx = int(self.x/define.size_case)
        my = int(self.y/define.size_case)
        for y in range(my):
            for x in range(mx):
                self.drawSquar(x * define.size_case,
                               y * define.size_case,
                               define.color[define.relem[map[y][x]]])

    def drawSquar(self, px, py, c):
        ws = self.win.get_surface()
        sdl2.ext.fill(ws, c, (px, py, px + define.size_case, py + define.size_case))

    def aff(self, map):
        self.draw(map)
        self.win.refresh()
        self.win.show()

    def deb(self, map):
        for x in range(int(self.x/define.size_case)):
            for y in range(int(self.y/define.size_case)):
                pass
                print('{} '.format(map[x][y]), end="")
            print()
