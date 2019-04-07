def rabbit(month):
    if month <= 1:
        return month + 1
    else:
        return rabbit(month - 1) + rabbit(month - 2)

for i in range(5):
    print("Month {}: {} pair(s) of rabbit".format(i,rabbit(i)))
