print("Guess your number game")
print("""Think of a number from 0 - 100
All you have to do is to answer to my guess
'c' if my guess is 'C'orrect
's' if my guess is 'S'maller than your number
'l' if my guess is 'L'arger than your number """)
low = 0
high = 101

while True:
    mid = (low + high) // 2
    answer = input("Is {0} your number? ".format(mid)).lower()
    if answer == "s":
        low = mid
    elif answer == "l":
        high = mid
    elif answer == "c":
        print("I knew it")
        break
    else:
        print("Wrong commmand")
