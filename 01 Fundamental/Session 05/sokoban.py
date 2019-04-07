map_sokoban = {
    "x" : 5,
    "y" : 5
}

player = {
    "x" : 0,
    "y" : 4
}

boxes = [
    {"x" : 1, "y" : 1},
    {"x" : 2, "y" : 2},
    {"x" : 3, "y" : 3}
]

destinations = [
    {"x" : 2, "y" : 1},
    {"x" : 3, "y" : 2},
    {"x" : 4, "y" : 3}
]
while True:
    for y in range(map_sokoban["y"]):
        for x in range(map_sokoban["x"]):
            box_is_here = False
            des_is_here = False
            player_is_here = False

            for box in boxes:
                if box["x"] == x and box["y"] == y:
                    box_is_here = True

            for des in destinations:
                if des["x"] == x and des["y"] == y:
                    des_is_here = True

            if x == player["x"] and y == player["y"]:
                player_is_here = True

            if box_is_here:
                print("B",end=" ")
            elif des_is_here:
                print("D",end=" ")
            elif player_is_here:
                print("P",end=" ")
            else:
                print("-",end=" ")
        print()
    is_win = True
    for box in boxes:
        if box not in destinations:
            is_win = False
    if is_win:
        print("WIN")
        break

    move = input("Your move? ").upper()

    dx = 0
    dy = 0
    if move == "W":
        dy = -1
    elif move == "S":
        dy = 1
    elif move == "A":
        dx = -1
    elif move == "D":
        dx = 1

    if (player["x"] + dx) in range(0,map_sokoban["x"]) and \
    (player["y"] + dy) in range(0,map_sokoban["y"]):
        player["x"] += dx
        player["y"] += dy

    for box in boxes:
        if box["x"] == player["x"] and box["y"] == player["y"]:
            box["x"] += dx
            box["y"] += dy
