string = input("String: ").lower().strip().split()
string = "".join(string)

char_list = sorted(list(set(string)))
for i in char_list:
    print(i,string.count(i))
