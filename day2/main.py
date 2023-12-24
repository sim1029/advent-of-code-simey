with open("input.txt", "r") as file:
    ret = 0
    for line in file:
        line = line.strip()
        game_head = line.split(":")
        game_id = int(game_head[0].split(" ")[1])
        game_body = line.split(":")[1]
        pulls = game_body.split(";")
        keys = {"red": 0, "blue": 0, "green": 0}
        for pull in pulls:
            items = pull.split(",")
            for item in items:
                item = item.strip()
                curr = item.split(" ")
                val, color = int(curr[0]), curr[1]
                if val > keys[color]:
                    keys[color] = val
        power = 1
        for key, val in keys.items():
            power *= val
        ret += power
    print(ret)
