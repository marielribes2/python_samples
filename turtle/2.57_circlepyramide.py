import turtle
from turtle import *


speed(10)

penup()
setposition(-100,-200)
pendown()

for i in range(3):
    circle(50)
    penup()
    forward(100)
    pendown()
    
    
penup()
setposition(-200, -100)
forward(150)

for i in range(2):
    pendown()
    circle(50)
    penup()
    forward(100)
    pendown()
 
penup()   
setposition (0,0) 

pendown()
circle(50)