import sys

# Increase the recursion limit
sys.setrecursionlimit(1000000)

with open("input.txt", "r") as file:
    connections = []
    for line in file:
        line = line.strip()
        row = []
        for c in line:
            row.append([c, float("inf")])
        connections.append(row)

    s_i, s_j = 0, 0
    for i, row in enumerate(connections):
        for j, col in enumerate(row):
            if col[0] == "S":
                s_i = i
                s_j = j

    connections[s_i][s_j][1] = 0

    def make_connections(last, i, j, depth):
        if (i < 0 or i >= len(connections)) or (j < 0 or j >= len(connections[i])):
            return

        if i == s_i and j == s_j:
            return

        connections[i][j][1] = min(depth, connections[i][j][1])
        curr = connections[i][j][0]

        if curr in ["|", "L", "J"] and last != 3:
            make_connections(1, i - 1, j, depth + 1)

        if curr in ["L", "F", "-"] and last != 4:
            make_connections(2, i, j + 1, depth + 1)

        if curr in ["|", "7", "F"] and last != 1:
            make_connections(3, i + 1, j, depth + 1)

        if curr in ["-", "J", "7"] and last != 2:
            make_connections(4, i, j - 1, depth + 1)

    moves = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    for r, c in moves:
        if (r + s_i < 0 or r + s_i >= len(connections)) or (
            c + s_j < 0 or c + s_j >= len(connections[s_i + r])
        ):
            continue
        letter = connections[s_i + r][s_j + c][0]
        n_r, n_c = s_i + r, s_j + c
        if r == -1 and letter in ["|", "F", "7"]:
            make_connections(1, n_r, n_c, 1)
        if c == 1 and letter in ["-", "7", "J"]:
            make_connections(2, n_r, n_c, 1)
        if r == 1 and letter in ["|", "L", "J"]:
            make_connections(3, n_r, n_c, 1)
        if c == -1 and letter in ["-", "L", "F"]:
            make_connections(4, n_r, n_c, 1)

    ret = 0
    for row in connections:
        for col in row:
            if col[1] != float("inf"):
                ret = max(ret, col[1])
    print(ret)

    new_connections = []
    new_connections.append(
        [["#", float("inf")] for _ in range(len(connections[0]) * 2 + 2)]
    )
    for row in connections:
        new_row = []
        between_row = []
        between_row.append(["#", float("inf")])
        new_row.append(["#", float("inf")])
        for col in row:
            if col[1] != float("inf"):
                new_row.append(col)
                if col[0] not in ["J", "|", "7"]:
                    new_row.append(["-", col[1]])
                else:
                    new_row.append(["#", float("inf")])
                if col[0] not in ["-", "L", "J"]:
                    between_row.append(["|", col[1]])
                else:
                    between_row.append(["#", float("inf")])
            else:
                new_row.append([".", float("inf")])
                new_row.append(["#", float("inf")])
                between_row.append(["#", float("inf")])
            between_row.append(["#", float("inf")])
        between_row.append(["#", float("inf")])
        new_row.append(["#", float("inf")])
        new_connections.append(new_row)
        new_connections.append(between_row)
    new_connections.append(
        [["#", float("inf")] for _ in range(len(connections[0]) * 2 + 2)]
    )

    con = new_connections

    seen = set()

    def bfs(i, j):
        if ((i, j)) in seen:
            return

        if con[i][j][0] not in ["#", "."]:
            return

        seen.add((i, j))
        con[i][j][0] = "#"

        moves = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        for r, c in moves:
            if (i + r < 0 or i + r >= len(con)) or (j + c < 0 or j + c >= len(con[i])):
                continue

            bfs(i + r, j + c)

    bfs(0, 0)

    for row in con:
        for col in row:
            print(col[0], end="")
        print()

    ret = 0
    for row in con:
        for col in row:
            if col[0] == ".":
                ret += 1
    print(ret)
