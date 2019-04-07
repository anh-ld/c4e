numbers = [1, 6, 8, 1, 2, 1, 5, 6]

input_number = int(input("Enter a number: "))
occurs = numbers.count(input_number)
print("{} appears {} time(s) in my list.".format(input_number,occurs))
