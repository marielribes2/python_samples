"""
this program will draw a pyramide of 6 circles. 
Each circle has a radio of 50
"""

from turtle import *
speed(10)
penup()
setposition(-200,-200)

#drawing 3 circles
for i in range(3):
    penup()
    forward(100)
    pendown()
    circle(50)
    

penup()
setposition(-150, -100)

#drawing 2 circles
for i in range(2):
    penup()
    forward(100)
    pendown()
    circle(50)

penup()
setposition(0,0)

pendown()
circle(50)