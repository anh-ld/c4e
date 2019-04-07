teencode = {
    "hc" : "hoc",
    "ng" : "nguoi",
    "pt" : "phat trien",
    "eny" : "em nguoi yeu",
    "any" : "anh nguoi yeu",
    "ns" : "noi",
    "ngta" : "nguoi ta",
    "lm" : "lam",
    "r" : "roi",
    "stt" : "status"
}

def showcase():
    for i in teencode:
        print(i,end="\t")
    print()

while True:
    showcase()
    code = input("Your code? ")
    if code in teencode:
        print("Translation:",teencode[code])
    else:
        print("Not found.")
        check = input("Do you want to contribute this word? (Y/N)? ").upper()
        if check == "Y":
            new_trans = input("Enter your new translation: ")
            teencode[code] = new_trans
            print("Updated")
        else:
            break
