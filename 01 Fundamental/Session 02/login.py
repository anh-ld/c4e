import getpass
user = input("Username: ")
passw = getpass.getpass("Password: ")

if user == "c4e" and passw == "123":
    print("Welcome")
elif user == "c4e" and passw != "123":
    print("Wrong Password")
else:
    print("Get out")
