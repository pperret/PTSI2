#!/usr/local/bin/python3
from turtle import *
import time


def flippyty(n, a):
    if n == 0:
        forward(a)
    else:
        n1 = n-1
        a3 = a/3
        flippyty(n1, a3)
        left(60)
        flippyty(n1, a3)
        right(120)
        flippyty(n1, a3)
        left(60)
        flippyty(n1, a3)


flippyty(4, 200)

# Autrement, la fenêtre se ferme immédiatement sur Mac
time.sleep(10)
