favor = ['deathnote','netflix','teaching']
print("Hi there, here are your favorite things so far")

for index, item in enumerate(favor):
    print(index + 1,'. ',item,sep='')

# pos = int(input("Position you want to get rid of? ")) - 1
# favor.pop(pos)
fav_name_to_delete = input("Name to delete: ")
if fav_name_to_delete in favor:
    favor.remove(fav_name_to_delete)
else:
    print("Not found")
for index, item in enumerate(favor):
    print(index + 1,'. ',item,sep='')
