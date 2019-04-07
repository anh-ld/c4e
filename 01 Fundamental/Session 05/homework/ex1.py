inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}
# add a key called 'pocket'
inventory["pocket"] = None
# set the value of 'pocket'
inventory["pocket"] = ["seashell", "strange berry", "lint"]
# remove 'dagger'
inventory["backpack"].remove("dagger")
# add 50 to the value of 'gold' key
inventory["gold"] += 50

for item in inventory:
    print("{} : {}".format(item,inventory[item]))
