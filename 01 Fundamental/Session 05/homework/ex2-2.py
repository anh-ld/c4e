numbers = [1, 6, 8, 1, 2, 1, 5, 6]

input_number = int(input("Enter a number: "))
occurs = 0
for i in numbers:
    if input_number == i:
        occurs += 1
print("{} appears {} time(s) in my list.".format(input_number,occurs))
