with open("input.txt", "r") as file:
    grid = []
    for line in file:
        line = line.strip()
        row = []
        for c in line:
            row.append(c)
        grid.append(row)

    mem = {}

    def print_grid():
        for row in grid:
            for col in row:
                print(col, end="")
            print()

    def north():
        for i, row in enumerate(grid):
            for j, col in enumerate(row):
                if grid[i][j] == "O":
                    s_i = i - 1
                    while s_i >= 0 and grid[s_i][j] == ".":
                        grid[s_i + 1][j] = "."
                        grid[s_i][j] = "O"
                        s_i -= 1

    def west():
        for j in range(len(grid[0])):
            for i in range(len(grid)):
                if grid[i][j] == "O":
                    s_j = j - 1
                    while s_j >= 0 and grid[i][s_j] == ".":
                        grid[i][s_j + 1] = "."
                        grid[i][s_j] = "O"
                        s_j -= 1

    def south():
        for i in range(len(grid) - 1, -1, -1):
            for j in range(len(grid[0])):
                if grid[i][j] == "O":
                    s_i = i + 1
                    while s_i < len(grid) and grid[s_i][j] == ".":
                        grid[s_i - 1][j] = "."
                        grid[s_i][j] = "O"
                        s_i += 1

    def east():
        for j in range(len(grid[0]) - 1, -1, -1):
            for i in range(len(grid)):
                if grid[i][j] == "O":
                    s_j = j + 1
                    while s_j < len(grid[0]) and grid[i][s_j] == ".":
                        grid[i][s_j - 1] = "."
                        grid[i][s_j] = "O"
                        s_j += 1

    def cycle():
        north()
        west()
        south()
        east()
        r = 0
        for i, row in enumerate(grid):
            for col in row:
                if col == "O":
                    r += len(grid) - i
        return r

    def run_cycles(cycles):
        global mem
        c = 0
        mem = {}
        for i in range(cycles):
            cycle_load = cycle()
            key = "".join(["".join(row) for row in grid])
            if key in mem:
                found, load = mem[key]
                off = (cycles - c - 1) % (c - found)
                for key, val in mem.items():
                    if val[0] == (found + off) % len(mem):
                        return val[1]
            else:
                mem[key] = [c, cycle_load]
            c += 1

    print(run_cycles(1000000000))
