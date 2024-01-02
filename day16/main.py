import sys

sys.setrecursionlimit(1000000)

with open("input.txt", "r") as file:
    grid = []
    for line in file:
        line = line.strip()
        curr = []
        for c in line:
            curr.append([c, False])
        grid.append(curr)

    def print_grid():
        # for row in grid:
        #     for col in row:
        #         print(col[0], end="")
        #     print()

        # print()

        for row in grid:
            for col in row:
                if col[1]:
                    print("#", end="")
                else:
                    print(".", end="")
            print()
        print()

    seen = set()

    def beam(i, j, row_off=0, col_off=0):
        if (
            (i < 0 or i >= len(grid))
            or (j < 0 or j >= len(grid[0]))
            or ((i, j, grid[i][j][0], row_off, col_off) in seen)
        ):
            return

        grid[i][j][1] = True
        seen.add((i, j, grid[i][j][0], row_off, col_off))

        piece = grid[i][j][0]

        if piece == ".":
            beam(i + row_off, j + col_off, row_off=row_off, col_off=col_off)
        elif piece in ["/", "\\"]:
            if (piece == "/" and col_off == -1) or (piece == "\\" and col_off == 1):
                beam(i + 1, j, row_off=1)
            elif (piece == "/" and col_off == 1) or (piece == "\\" and col_off == -1):
                beam(i - 1, j, row_off=-1)
            elif (piece == "/" and row_off == 1) or (piece == "\\" and row_off == -1):
                beam(i, j - 1, col_off=-1)
            elif (piece == "/" and row_off == -1) or (piece == "\\" and row_off == 1):
                beam(i, j + 1, col_off=1)
            else:
                print("ERROR - Conditional not supported")
        elif piece in ["|", "-"]:
            if piece == "|" and col_off != 0:
                beam(i - 1, j, row_off=-1)
                beam(i + 1, j, row_off=1)
            elif piece == "-" and row_off != 0:
                beam(i, j - 1, col_off=-1)
                beam(i, j + 1, col_off=1)
            else:
                beam(i + row_off, j + col_off, row_off=row_off, col_off=col_off)
        else:
            print("ERROR - Piece not supported")

    ret = 0

    def calc_max():
        global ret
        curr = 0
        for row in grid:
            for col in row:
                if col[1]:
                    col[1] = False
                    curr += 1
        ret = max(curr, ret)

    for j in range(len(grid[0])):
        seen = set()
        beam(0, j, row_off=1)
        calc_max()
    for i in range(len(grid)):
        seen = set()
        beam(i, len(grid[0]) - 1, col_off=-1)
        calc_max()
    for j in range(len(grid[0]) - 1, -1, -1):
        seen = set()
        beam(len(grid) - 1, j, row_off=-1)
        calc_max()
    for i in range(len(grid) - 1, -1, -1):
        seen = set()
        beam(i, 0, col_off=1)
        calc_max()
    print(ret)
