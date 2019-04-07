favor = ['deathnote','netflix','teaching']
print("Hi there, here are your favorite things so far")
print(*favor, sep=', ')

addf = input("Name one thing you want to add? ")
favor.append(addf)
print(*favor, sep=', ')
