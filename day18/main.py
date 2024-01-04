with open("input.txt", "r") as file:
    vertices = []
    x, y = 0, 0
    border = 0
    vertices.append([x, y])
    for line in file:
        line = line.strip()
        curr = line.split(" ")
        direction, length = curr[0], int(curr[1])
        if direction == "U":
            y += length
        elif direction == "R":
            x += length
        elif direction == "D":
            y -= length
        elif direction == "L":
            x -= length
        else:
            print("ERROR - Direction Not Supported")
        vertices.append([x, y])
        border += length

    n = len(vertices) - 1

    area = 0
    for i in range(n):
        area += (vertices[i][0] * vertices[i + 1][1]) - (
            vertices[i + 1][0] * vertices[i][1]
        )

    area = abs(area) / 2.0

    ret = int(abs(area) - 0.5 * border + 1) + border
    print(ret)
