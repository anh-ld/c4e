from random import choice
#
# x = 3
# y = 7
# op = choice(["+","-","x","/"])
#
# if (op == "+"):
#     result = x + y
# elif (op == "-"):
#     result = x - y
# elif (op == "x"):
#     result = x * y
# else:
#     result = x / y
#
# print(result)


def calc(x,y,op):
    # op = choice(["+","-","x","/"])
    if (op == "+"):
        result = x + y
    elif (op == "-"):
        result = x - y
    elif (op == "x"):
        result = x * y
    else:
        result = x / y
    return result

# argument, parameter
# op = choice(["+","-","x","/"])
# calc(1,2,op)

# res = calc(1,3,"+")
# print(res)
#
# r = calc(1,2,"-")
# print(r)
