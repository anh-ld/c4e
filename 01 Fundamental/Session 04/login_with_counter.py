print("Hi there, this is a superuser gateaway")
count = 0
while True:
    username = input("Username: ")
    if username == "c4e":
        password = input("Password: ")
        if password == "codethechange":
            print("Welcome, c4e")
            break
        else:
            print("Password is incorrect")
    else:
        print("You are not superuser")
        count += 1
        if count == 3:
            print("You failed to log in 3 times, go away")
            break
