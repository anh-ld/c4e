from random import *

def generate_quiz():
    # Hint: Return [x, y, op, result]
    x = randint(0,10)
    y = randint(1,10)
    op = choice(["+","-","x","/"])
    error = choice([-1,0,1])

    result = calc(x, y, op)
    result += error

    return [x, y, op, result]

def check_answer(x, y, op, result, user_choice):
    true_ans = calc(x, y, op)
    check = (true_ans == result)
    return (check == user_choice)

def calc(x,y,op):
    if (op == "+"):
        result = x + y
    elif (op == "-"):
        result = x - y
    elif (op == "x"):
        result = x * y
    else:
        result = x / y
    return result
