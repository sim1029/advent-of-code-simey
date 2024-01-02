with open("input1.txt", "r") as file:
    grid = []
    for line in file:
        line = line.strip()
        curr = []
        for c in line:
            curr.append(c)
        grid.append(curr)

    def print_grid():
        for row in grid:
            for col in row:
                print(col, end="")
            print()

    print_grid()
