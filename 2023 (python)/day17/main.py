import heapq
from collections import defaultdict

with open("input.txt", "r") as file:
    grid = []
    for line in file:
        line = line.strip()
        curr = []
        for c in line:
            curr.append(int(c))
        grid.append(curr)

    h = []
    heapq.heappush(h, (0, 0, 0, 0, "X"))
    heur = defaultdict(lambda: float("inf"))
    heur[(0, 0, "X")] = 0

    while len(h) > 0:
        curr = heapq.heappop(h)
        old_man, cost, i, j, direction = curr
        if old_man > heur[(i, j, direction)]:
            continue
        if i == len(grid) - 1 and j == len(grid[0]) - 1:
            print(cost)
            break

        moves = [["V", -1, 0], ["H", 0, 1], ["V", 1, 0], ["H", 0, -1]]

        for d, row_off, col_off in moves:
            if direction == d:
                continue

            cum_score = 0
            for size in range(1, 11):
                r, c = i + size * row_off, j + size * col_off
                if (r < 0 or r >= len(grid)) or (c < 0 or c >= len(grid[0])):
                    break

                cum_score += grid[r][c]
                new_cost = cost + cum_score
                man = abs(len(grid) - 1 - r) + abs(len(grid[0]) - 1 - c)
                key = (r, c, "V" if col_off == 0 else "H")
                new_heur = man + new_cost
                t = (new_heur, new_cost) + key
                if size >= 4 and new_heur < heur[key]:
                    heur[key] = new_heur
                    heapq.heappush(h, t)
