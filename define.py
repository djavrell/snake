#! /usr/bin/python3.4
__author__ = 'proute_k'

from sdl2.ext import Color

len_body = 3
win_name = "Snake V2 python"
size_case = 20

# number of turn for the life of the cherry
life_cherry = 30
list_rand = [0, 3, 5, 8]

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
