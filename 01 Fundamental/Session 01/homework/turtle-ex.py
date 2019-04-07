from turtle import *

socanh = input("Nhap so canh: ")

shape('turtle')
speed(1)
fillcolor('red')
# 3 60 4 90 5 120
#n-2 . 180/n
begin_fill()
for i in range(int(socanh)):
    forward(100)
    left(360/int(socanh))
end_fill()

mainloop()
