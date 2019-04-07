prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

for item in prices:
    print(item)
    print("price:",prices[item])
    print("stock:",stock[item])
    print()

total = 0
for item in prices:
    value = prices[item] * stock[item]
    print("Value of {}: {}".format(item,value))
    total += value
print("Total: {}".format(total))
