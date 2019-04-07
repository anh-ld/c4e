h = 5
print("*" * h)
for i in range(1,h):
    for j in range(h):
        if j == h - i:
            print("*",end='')
        else:
            print(" ",end='')
    print()
print("*" * h)
