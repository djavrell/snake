#! /usr/bin/python3.4
__author__ = 'proute_k'

import sdl2
import Game
from sdl2.ext import Color

len_body = 3
win_name = "Snake V2 python"
size_case = 20

# elem
case = ' '
head = '1'
body = '2'
apple = '3'
cherry = '4'

elem = {
    "case": case,
    "body": body,
    "head": head,
    "apple": apple,
    "cherry": cherry,
    }

relem = {
    case: "case",
    body: "body",
    head: "head",
    apple: "apple",
    cherry: "cherry",
}

# couleur
color = {
    "case": Color(118, 112, 112),
    "body": Color(255, 255, 255),
    "head": Color(0, 0, 0),
    "apple": Color(119, 255, 0),
    "cherry": Color(192, 22, 22),
    }

# event
# call = {
#     sdl2.SDLK_UP: Game.game.moveUp(),
#     sdl2.SDLK_DOWN: Game.game.moveDown(),
#     sdl2.SDLK_LEFT: Game.game.moveLeft(),
#     sdl2.SDLK_RIGHT: Game.game.moveRight(),
#     sdl2.SDLK_ESCAPE: Game.game.Quit(),
# }