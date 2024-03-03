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


def polyflippyty(a, n, m):
    for i in range(0, n):
        flippyty(m, a)
        right(360/n)


polyflippyty(400, 9, 8)

# Autrement, la fenêtre se ferme immédiatement sur Mac
time.sleep(10)
