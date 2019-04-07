from random import randint, choice
from eval import calc

x = randint(0,10)
y = randint(1,10)
op = choice(["+","-","x","/"])
error = choice([-1,0,0,0,0,1])

result = calc(x,y,op)

result += error

print("*" * 30)
print("{} {} {} = {}".format(x,op,y,result))
print("*" * 30)

yn = input("(Y/N)? ").upper()

if error == 0:
    if yn == "Y":
        print("Yay")
    else:
        print("You're wrong")
else:
    if yn == "Y":
        print("You're wrong")
    else:
        print("Yay")
