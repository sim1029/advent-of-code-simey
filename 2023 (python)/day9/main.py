with open("input.txt", "r") as file:
    ret = 0
    for line in file:
        line = line.strip()
        seq = []
        start_str = line.split(" ")
        start = []
        for s in start_str:
            start.append(int(s))
        zeroes = False
        while not zeroes:
            curr = []
            for i in range(1, len(start)):
                curr.append(start[i] - start[i - 1])
            seq.append(start)
            start = curr
            z = True
            for num in start:
                if num != 0:
                    z = False
                    break
            zeroes = z
        seq.append(start)

        for i in range(len(seq) - 2, -1, -1):
            curr = seq[i]
            prev = seq[i + 1]
            seq[i][0] = curr[0] - prev[0]
        ret += seq[0][0]
        # print(seq[0][0])
    print(ret)
