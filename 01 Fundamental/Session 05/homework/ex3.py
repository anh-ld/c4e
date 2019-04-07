bacteria  = int(input("How many B bacteria(s) are there? "))
time = int(input("How much time in minutes will we wait? "))

bacteria = bacteria * (2 ** (time // 2))

print("After {} minutes, we would have {} bacteria(s)".format(time,bacteria))
