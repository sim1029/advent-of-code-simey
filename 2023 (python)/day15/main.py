from collections import defaultdict

with open("input.txt", "r") as file:

    def my_hash(s):
        h = 0
        for c in s:
            h += ord(c)
            h *= 17
            h %= 256
        return h

    boxes = [[] for _ in range(256)]
    contents = [set() for _ in range(256)]

    ret = 0
    for line in file:
        line = line.strip()
        to_hash = line.split(",")
        for item in to_hash:
            op = item[-1]

            if op == "-":
                label = item[:-1]
                box = my_hash(label)
                if label in contents[box]:
                    contents[box].remove(label)
                    idx = -1
                    for i, item in enumerate(boxes[box]):
                        if item[0] == label:
                            idx = i
                            break
                    boxes[box].pop(i)
            else:
                label, val = item.split("=")
                box = my_hash(label)
                if label in contents[box]:
                    for i, item in enumerate(boxes[box]):
                        if item[0] == label:
                            boxes[box][i] = [label, int(val)]
                            break
                else:
                    boxes[box].append([label, int(val)])
                    contents[box].add(label)
    ret = 0
    for i, box in enumerate(boxes):
        box_num = i + 1
        for j, item in enumerate(box):
            ret += box_num * (j + 1) * item[1]
    print(ret)
