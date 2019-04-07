from turtle import *

color("red")
speed(-1)

# a 1st shape
penup()
goto(-200,0)
pendown()

setheading(-30)
for i in range(4):
    forward(50)
    left(60)
    forward(50)
    left(120)
    forward(50)
    left(60)
    forward(50)
    right(150)

# a 2nd shape
penup()
goto(50,-80)
pendown()

setheading(0)
for i in range(1,5):
    if i % 2 != 0:
        color("blue")
    else:
        color("red")
    for j in range(i + 2):
        forward(100)
        left(360/(i + 2))

mainloop()
