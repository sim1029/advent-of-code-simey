with open("input.txt", "r") as file:
    for line in file:
        line = line.strip()
        card = line.split(":")[1]
        print(card)
