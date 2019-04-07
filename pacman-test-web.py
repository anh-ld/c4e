from random import randint

size = 4
player = [1, 1]
foods = [[0, 0], [0, 1], [1, 0]]
ghosts = [[0, 3], [3, 3]]
food_count = 0
is_win = False
is_lose = False

while(True):


    dx = 0
    dy = 0
    for i in range(size):
        for j in range(size):
            player_is_here = False
            food_is_here = False
            ghost_is_here = False

            if (i == player[0] and j == player[1]):
                player_is_here = True
            for food in foods:
                if (i == food[0] and j == food[1]):
                    food_is_here = True
            for ghost in ghosts:
                if (i == ghost[0] and j == ghost[1]):
                    ghost_is_here = True

            if (ghost_is_here):
                print("G", end=" ")
            elif (player_is_here):
                print("P", end=" ")
            elif (food_is_here):
                print("F", end=" ")
            else:
                print("-", end=" ")
        print()

    if (is_win):
        print("You Won!!!")
        break

    if (is_lose):
        print("You Lost!!!")
        break

    move = str(input("\nYour next move? ")).upper()

    if (move == "A"):
        dy = -1
    elif (move == "D"):
        dy = 1
    elif (move == "W"):
        dx = -1
    elif (move == "S"):
        dx = 1
    else:
        print("Use only A S W D to move your player!!!")
        continue

    if ((player[0] + dx in range(size)) and (player[1] + dy in range(size))):
        player[0] += dx
        player[1] += dy

    for ghost in ghosts:
        g_dx = 0
        g_dy = 0
        while ((g_dx == 0 and g_dy == 0) or (g_dx != 0 and g_dy != 0)):
            g_dx = randint(-1, 1)
            g_dy = randint(-1, 1)
        # print("G: ", g_dx, " ", g_dy)
        if ((ghost[0] + g_dx in range(size)) and (ghost[1] + g_dy in range(size))):
            ghost[0] += g_dx
            ghost[1] += g_dy

    for food in foods:
        if (food[0] == player[0] and food[1] == player[1]):
            food[0] = -1
            food[1] = -1
            food_count += 1

    if (food_count == len(foods)):
        is_win = True

    for ghost in ghosts:
        if (ghost[0] == player[0] and ghost[1] == player[1]):
            is_lose = True
