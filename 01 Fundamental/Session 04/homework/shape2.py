from turtle import *

hideturtle()
color("blue")
speed(-1)

length = 110
setheading(-140)
while length > 0:
    for j in range(4):
        forward(length)
        right(90)
    right(10)
    length -= 2

mainloop()
