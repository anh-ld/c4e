from random import shuffle

word = "friends"
chars = list(word)

while True:
    shuffle(chars)
    print(*chars,sep=' ')
    answer = input("Your answer: ")
    if word == answer:
        print("Hura")
        break
    else:
        print(":(")
