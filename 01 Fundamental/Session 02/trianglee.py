height = int(input("Height: "))

for i in range(height):
    for j in range(height):
        if j <= i:
            print("*",end='')
        else:
            print(" ",end='')
    print()

for i in range(height):
    for j in range(height):
        if j < height - i - 1:
            print(" ",end='')
        else:
            print("*",end='')
    print()
