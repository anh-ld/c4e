from turtle import *

def draw_square(length, colour):
    speed(-1)
    color(colour)
    for i in range(4):
        forward(length)
        left(90)

draw_square(100, "blue")
mainloop() # if you wanna keep the turtle window in a screen
