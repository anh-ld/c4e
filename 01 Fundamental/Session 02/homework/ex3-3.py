# c
print("Section C")
for i in range(1,10):
    for j in range(1,10):
        print('{:2}'.format(str(i * j)),end=' ')
    print()
number3 = int(input("Enter a number: "))
for i in range(1,number3 + 1):
    for j in range(1,number3 + 1):
        print('{:3}'.format(str(i * j)),end=' ')
    print()
