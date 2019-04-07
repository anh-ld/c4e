from turtle import *

title("This is a title :D")
color("green")
fillcolor("yellow")
speed(-1)

begin_fill()

penup()
goto(-200,0)
pendown()

for i in range(4):
    forward(100)
    left(90)

penup()
goto(0,0)
pendown()

for i in range(3):
    forward(100)
    left(120)

penup()
goto(-150,-150)
pendown()

circle(50)

penup()
goto(50,50)
pendown()

end_fill()

penup()
goto(50,-100)
pendown()

for i in range(6):
    circle(25)
    left(60)

penup()
goto(50,-220)
pendown()

for i in range(30):
    circle(25)
    left(12)

mainloop()
