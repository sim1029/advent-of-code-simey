with open("input.txt", "r") as file:
    line = file.readline().strip()
    moves = ""
    while line != "":
        moves += line
        line = file.readline().strip()

    move_arr = []
    for char in moves:
        if char == "L":
            move_arr.append(0)
        else:
            move_arr.append(1)

    map = {}
    for line in file:
        line = line.strip()
        split_str = line.split("=")
        state = split_str[0].strip()
        decisions = split_str[1].strip()
        decisions = decisions[1:-1]
        left, right = decisions.split(",")
        left = left.strip()
        right = right.strip()
        map[state] = [left, right]

    move = 0
    states = []
    goal = []
    for key in map.keys():
        if key[-1] == "A":
            states.append(key)
        elif key[-1] == "Z":
            goal.append(key)

    def end_states(states):
        for state in states:
            if state[-1] != "Z":
                return False
        return True

    path = {}
    for state in states:
        move = 0
        curr = state
        while state[-1] != "Z":
            idx = move_arr[move % len(move_arr)]
            state = map[state][idx]
            move += 1
        path[curr] = move

    import math

    def lcm(arr):
        lcm_value = arr[0]
        for i in range(1, len(arr)):
            lcm_value = abs(lcm_value * arr[i]) // math.gcd(lcm_value, arr[i])
        return lcm_value

    print(lcm(list(path.values())))
