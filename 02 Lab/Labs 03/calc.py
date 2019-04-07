x = float(input("x = "))
operation = input("Operation (+,-,x,/): ")
y = float(input("y = "))

result = -9999
if (operation == "+"):
    result = x + y
elif (operation == "-"):
    result = x - y
elif (operation == "x"):
    result = x * y
elif (operation == "/"):
    result = x / y

print("*" * 20)
print("{} {} {} = {}".format(x,operation,y,result))
print("*" * 20)
