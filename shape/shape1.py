from turtle import *
import time

for steps in range(100):
    for c in ("red", "green", "blue"):
        fillcolor(c)
        forward(steps*10)
        left(30)
