#input
number = int(input("Enter a number: "))
#processing
isprime = True
if number >= 2:
    i = 2
    while i <= (number ** 0.5):
        if number % i == 0:
            isprime = False
            break
        i += 1
else:
    isprime = False
#output
if isprime:
    print(number,"is a prime number")
else:
    print(number,"is not a prime number")
