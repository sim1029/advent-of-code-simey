from collections import defaultdict

with open("input.txt", "r") as file:
    ret = 0
    wins = {}
    copies = defaultdict(lambda: 1)
    for line_num, line in enumerate(file):
        line = line.strip()
        card = line.split(":")[1]
        win_num, my_num = card.split("|")[0].strip(), card.split("|")[1].strip()
        win_set = set()
        matches = 0
        for num_str in win_num.split(" "):
            num_str = num_str.strip()
            win_set.add(num_str)
        for num_str in my_num.split(" "):
            if num_str != "" and num_str in win_set:
                matches += 1
        wins[line_num + 1] = matches

    def calc_wins(card):
        for i in range(1, wins[card] + 1):
            copies[card + i] += 1
            calc_wins(card + i)

    for i in range(1, len(wins) + 1):
        calc_wins(i)
        ret += copies[i]
    print(ret)
