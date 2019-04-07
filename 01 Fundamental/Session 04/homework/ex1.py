fullname = input("Your full name: ").lower()
fullname = fullname.strip().split()

s_name = [i[0].upper() + i[1:] for i in fullname]

s_fullname = " ".join(s_name)
print("Updated:",s_fullname)
