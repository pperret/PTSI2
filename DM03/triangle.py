#!/usr/local/bin/python3
from turtle import *
import time


def triangle(a):
    forward(a)
    left(120)
    forward(a)
    left(120)
    forward(a)


triangle(200)

# Autrement, la fenêtre se ferme immédiatement sur Mac
time.sleep(10)
