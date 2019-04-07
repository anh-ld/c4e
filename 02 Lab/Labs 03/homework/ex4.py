from turtle import *

def draw_square(length, colour):
    speed(-1)
    color(colour)
    for i in range(4):
        forward(length)
        left(90)

for i in range(30):
    draw_square(i * 5, "red")
    left(17)
    penup()
    forward(i * 2)
    pendown()

mainloop() # if you wanna keep the turtle window in a screen
