#!/usr/local/bin/python3
from turtle import *
import time


def polygone(n, a):
    for i in range(0, n):
        forward(a)
        left(360/n)


polygone(7, 200)

# Autrement, la fenêtre se ferme immédiatement sur Mac
time.sleep(10)
