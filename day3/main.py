from collections import defaultdict

with open("input.txt", "r") as file:
    ret = 0
    digits = set(["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"])
    arr = []
    for line in file:
        line = line.strip()
        line_arr = [c for c in line]
        arr.append(line_arr)

    gears = defaultdict(list)

    def check_if_part(row, start, end, num):
        directions = [
            (-1, 0),
            (-1, 1),
            (0, 1),
            (1, 1),
            (1, 0),
            (1, -1),
            (0, -1),
            (-1, -1),
        ]
        is_part = False
        is_gear = False
        for col in range(start, end):
            for direction in directions:
                i, j = direction
                if (row + i < len(arr) and row + i >= 0) and (
                    col + j < len(arr[row + i]) and col + j >= 0
                ):
                    if (
                        arr[row + i][col + j] != "."
                        and arr[row + i][col + j] not in digits
                    ):
                        is_part = True
                    if not is_gear and arr[row + i][col + j] == "*":
                        gears[f"{row+i}:{col+j}"].append(num)
                        is_gear = True
        return is_part

    is_digit = False
    digit_start, digit_end = 0, 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if not is_digit and arr[i][j] in digits:
                is_digit = True
                digit_start = j
            elif is_digit and (arr[i][j] not in digits or j == len(arr[i]) - 1):
                is_digit = False
                digit_end = j
                if j == len(arr[i]) - 1 and arr[i][j] in digits:
                    digit_end += 1
                digit_val = int("".join(arr[i][digit_start:digit_end]))
                check_if_part(i, digit_start, digit_end, digit_val)
    for key, val in gears.items():
        if len(val) == 2:
            ret += val[0] * val[1]
    print(ret)
