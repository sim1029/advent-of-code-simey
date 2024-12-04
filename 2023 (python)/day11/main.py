from collections import deque

with open("input.txt", "r") as file:
    grid = []
    num = 0
    num_key = {}
    for line in file:
        line = line.strip()
        curr = []
        for c in line:
            if c != ".":
                curr.append(f"{num}")
                num += 1
            else:
                curr.append(c)
        grid.append(curr)

    def print_grid():
        for row in grid:
            for col in row:
                print(col, end="")
            print()

    def get_spaces():
        rows = set()
        cols = set()
        all_rows = set()
        all_cols = set()
        for i, row in enumerate(grid):
            all_rows.add(i)
            for j, col in enumerate(row):
                all_cols.add(j)
                if col != ".":
                    rows.add(i)
                    cols.add(j)
        row_diff = all_rows - rows
        col_diff = all_cols - cols
        r = list(row_diff)
        c = list(col_diff)
        r.sort()
        c.sort()
        return r, c

    def expand_grid(r, c):
        r_off, c_off = 0, 0
        c_offs = [0] * len(grid[0])
        for j, col in enumerate(grid[0]):
            if j in c:
                c_off += 999999
            c_offs[j] = c_off
        for i, row in enumerate(grid):
            if i in r:
                r_off += 999999
            for j, col in enumerate(row):
                if col != ".":
                    num_key[col] = [i + r_off, j + c_offs[j]]

    ret = {}

    def get_distances(curr_dist):
        dists = [i for i in range(curr_dist + 1, num)]
        i, j = num_key[f"{curr_dist}"]
        for dist in dists:
            x, y = num_key[f"{dist}"]
            length = abs(x - i) + abs(y - j)
            ret[(curr_dist, dist)] = length

    r, c = get_spaces()
    expand_grid(r, c)
    for i in range(num):
        get_distances(i)
    total = 0
    for l in ret.values():
        total += l
    print(total)
