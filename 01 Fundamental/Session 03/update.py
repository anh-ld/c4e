favor = ['deathnote','netflix','teaching']
print("Hi there, here are your favorite things so far")

for index, item in enumerate(favor):
    print(index + 1,'. ',item,sep='')

pos = int(input("Position you want to update ? ")) - 1
newf = input("Your replacing favorite? ")
favor[pos] = newf

for index, item in enumerate(favor):
    print(index + 1,'. ',item,sep='')
