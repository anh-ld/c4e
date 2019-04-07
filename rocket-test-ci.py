# initialize variables
map_rocket = {
    "x" : 4,
    "y" : 4
}
enemies = [
    {"x" : 0, "y" : 1},
    {"x" : 2, "y" : 3}
]

hit_object = []
missed_object = []

rockets = 5
enemies_left = 2

# print first map
print(" ", end=" ")
for a in range(4):
    print(a, end=" ")
print()
for y in range(map_rocket["y"]):
    print(y, end=" ")
    for x in range(map_rocket["x"]):
        print("-", end=" ")
    print()

# loop
while True:
    print()
    target = input("Your target? ").split()
    target_x = int(target[1])
    target_y = int(target[0])
    rockets -= 1

    if target_x not in range(4) or target_y not in range(4):
        print("Wrong move. -1 rocket.")
        continue

    wrong = False

    for obj in hit_object:
        if target_x == obj["x"] and target_y == obj["y"]:
            wrong = True
    for obj in missed_object:
        if target_x == obj["x"] and target_y == obj["y"]:
            wrong = True

    if wrong == True:
        print("Wrong move. -1 rocket.")
        continue

    check = 0
    enemies_around = 0

    for enemy in enemies:
        if enemy["x"] == target_x and enemy["y"] == target_y:
            check = 1

    if check == 1:
        enemies_left -= 1
        hit_object.append({"x" : target_x, "y" : target_y})
    else:
        missed_object.append({"x" : target_x, "y" : target_y})

    print()

    print(" ", end=" ")
    for a in range(4):
        print(a, end=" ")
    print()
    for y in range(map_rocket["y"]):
        print(y, end=" ")
        for x in range(map_rocket["x"]):
            hit = False
            missed = False

            if len(hit_object) > 0:
                for obj in hit_object:
                    if obj["x"] == x and obj["y"] == y:
                        hit = True

            if len(missed_object) > 0:
                for obj in missed_object:
                    if obj["x"] == x and obj["y"] == y:
                        missed = True
            if hit:
                print("o", end=" ")
            elif missed:
                print("x", end=" ")
            else:
                print("-", end=" ")
        print()

    if check == 1:
        print("You hit")
    else:
        print("You missed")

    for y in range(target_y - 1, target_y + 2):
        for x in range(target_x - 1, target_x + 2):
            for enemy in enemies:
                if enemy["x"] == x and enemy["y"] == y:
                    enemies_around += 1
    if check == 1:
        enemies_around -= 1

    print(enemies_around, "enemy(s) around")
    print(rockets, "rocket(s) left")
    print(enemies_left, "enemy(s) left")

    if enemies_left == 0:
        print("You won!!!")
        print()
        break

    if rockets == 0:
        print("You lose!!!")
        print()
        break
