with open("input.txt", "r") as file:
    smudge = False

    def row_match(game, l, r):
        global smudge
        for j in range(len(game[l])):
            if game[l][j] != game[r][j]:
                if smudge:
                    return False
                else:
                    smudge = True
        return True

    def col_match(game, l, r):
        global smudge
        for i in range(len(game)):
            if game[i][l] != game[i][r]:
                if smudge:
                    return False
                else:
                    smudge = True
        return True

    def find_fold(game):
        global smudge
        # for row in game:
        #     for col in row:
        #         print(col, end="")
        #     print()
        l = 0
        while l < len(game) - 1:
            r = l + 1
            c_l = l
            smudge = False
            while l >= 0 and r < len(game) and row_match(game, l, r):
                l -= 1
                r += 1
            if (l < 0 or r >= len(game)) and smudge:
                return (c_l + 1) * 100
            l = c_l + 1
        l = 0
        while l < len(game[0]) - 1:
            r = l + 1
            c_l = l
            smudge = False
            while l >= 0 and r < len(game[0]) and col_match(game, l, r):
                l -= 1
                r += 1
            if (l < 0 or r >= len(game[0])) and smudge:
                return c_l + 1
            l = c_l + 1
        print("ERROR - NO FOLD!")
        return -1

    game = []
    ret = 0
    for line in file:
        line = line.strip()
        if line == "":
            ret += find_fold(game)
            game = []
        else:
            curr_row = []
            for c in line:
                curr_row.append(c)
            game.append(curr_row)
    ret += find_fold(game)
    print(ret)
