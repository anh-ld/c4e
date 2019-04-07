from turtle import *

colors = ['red', 'blue', 'brown', 'yellow', 'grey']
speed(-1)

penup()
goto(-200,0)
pendown()

for i in range(5):
    color(colors[i])
    for j in range(i + 3):
        forward(100)
        left(360/(i + 3))

penup()
goto(0,200)
pendown()

for i in range(5):
    fillcolor(colors[i])
    color(colors[i])
    begin_fill()
    for j in range(2):
        forward(55)
        right(90)
        forward(100)
        right(90)
    forward(55)
    end_fill()

mainloop()
