from random import shuffle
from random import choice

wordlist = ['friends','actor','chef','waitress','caterer','copywriter','manager']
word = choice(wordlist)
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
