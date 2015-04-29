#! /usr/bin/python3.4
__author__ = 'proute_k'

import sdl2
import sdl2.ext
import Board
import Gui


class game:
    def __init__(self, x=10, y=10):
        self.x = x
        self.y = y
        self.b = Board.board(x, y)
        self.gui = Gui.gui()

    def start(self):
        run = True
        while run:
            run = self.move(self.gui.get_event())
            self.gui.draw(self.b.get_board())
            sdl2.SDL_Delay(1)
        sdl2.ext.quit()
        return 0

    def move(self, e):
        return True

    def aff(self):
        self.gui.draw(self.b.get_board())