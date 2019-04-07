from turtle import *

def draw_star(x, y, length):
    speed(-1)
    penup()
    goto(x,y)
    pendown()

    for i in range(5):
        forward(length)
        right(144)

draw_star(-100,0,200)
mainloop() # if you wanna keep the turtle window in a screen
