from random import randint

number = randint(0,100)
count = 0

while True:
    number2 = int(input("Guess my number (1 - 100)? "))
    if number2 < number:
        print("Too small")
    elif number2 > number:
        print("Too large")
    else:
        print("Bingo")
        break
    count += 1
    if count == 7:
        print("You lose.")
        break
