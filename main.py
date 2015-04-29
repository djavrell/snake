#! /usr/bin/python3.4
__author__ = 'proute_k'

import sys
import Game


def is_nb(nb):
    for i in range(len(nb)):
        if int('0') <= int(i) >= int('9'):
            return False
    return True


def run(av):
    try:
        if is_nb(av[1]) is not True or is_nb(av[2]) is not True:
            raise ValueError
        g = Game.game(int(av[1]), int(av[2]))

        g.move()
        g.aff()

    except ValueError:
        print("x and y must be a number")


if __name__ == '__main__':
    if len(sys.argv) == 3:
        run(sys.argv)
    else:
        print('./main.py x y')