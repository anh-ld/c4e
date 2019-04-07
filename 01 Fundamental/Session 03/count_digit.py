number = int(input("Insert your number: "))

count = 0
if number == 0:
    count = 1
else:
    while number > 0:
        number = number // 10
        count += 1}

print("Number(s) of digit:",count)

# tach chuong trinh thanh 3 khoi: input - process - output
