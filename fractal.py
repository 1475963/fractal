#!/usr/bin/python

from __future__ import print_function

import sys
import tk_draw
import math
import consts

def main():
    instance = tk_draw.getInstance()
    window = tk_draw.getWindow(instance)
    points = [[(100, 700), (700, 700), (400, 700 - math.sqrt(270000))]]
    tk_draw.resetBackground(window, consts.TK_COLOR_BLACK)
    tk_draw.attachUpdater(instance, window, points)
    tk_draw.attachMainloop(instance)

if __name__ == '__main__':
    main()