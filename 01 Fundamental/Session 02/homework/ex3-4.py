# d
print("Section D")
for i in range(10):
    for j in range(10):
        if (i + j) % 2 == 0:
            print("1",end='  ')
        else:
            print("0",end='  ')
    print()
number4 = int(input("Enter a number: "))
for i in range(number4):
    for j in range(number4):
        if (i + j) % 2 == 0:
            print("1",end='  ')
        else:
            print("0",end='  ')
    print()
