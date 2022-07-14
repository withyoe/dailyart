import colorsys
from tkinter import N
from turtle import *

sc_width = 701 
sc_height = 1920
setup(sc_width, sc_height, startx= None, starty= None)
bgcolor('black')
speed(0)

n = 70
h = 0

for i in range(360):
    c = colorsys.hsv_to_rgb(h, 1, 0.8)
    h += 1/n
    color(c)
    left(1)
    fd(1)
    for j in range(2):
        left(2)
        circle(100)
