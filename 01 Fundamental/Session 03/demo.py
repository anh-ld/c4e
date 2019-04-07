from random import choice
chars = list("champion")
new_chars = []
while len(new_chars) != len(chars):
    random_char = choice(chars)
    if not(random_char in new_chars):
        new_chars.append(random_char)
