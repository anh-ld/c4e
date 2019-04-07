items = ['T-Shirt','Sweater']
print("*** Note: If you want to quit this program, simply type 'quit' or 'QUIT'.")
print("*" * 20) 

while True:
    action = (input("Welcome to our shop, what do you want (C, R, U, D)? ")).upper()
    if action == "R":
        print("Our items: ", end='')
        print(*items,sep=', ')
    elif action == "C":
        new_item = input("Enter new item: ")
        items.append(new_item)
        print("Our items: ", end='')
        print(*items,sep=', ')
    elif action == "U":
        update_pos = int(input("Update position? ")) - 1
        if update_pos in range(0,len(items)):
            update_item = input("New item? ")
            items[update_pos] = update_item
            print("Our items: ", end='')
            print(*items,sep=', ')
        else:
            print("Not found.")
    elif action == "D":
        delete_pos = int(input("Delete position? ")) - 1
        if delete_pos in range(0,len(items)):
            items.pop(delete_pos)
            print("Our items: ", end='')
            print(*items,sep=', ')
        else:
            print("Not found.")
    elif action == "QUIT":
        break
    else:
        print("Wrong command. Type again please!")
