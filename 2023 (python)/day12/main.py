with open("input.txt", "r") as file:
    patterns, counts = [], []
    for line in file:
        line = line.strip()
        curr = line.split(" ")
        patterns.append(curr[0])
        nums = []
        for num_str in curr[1].split(","):
            nums.append(int(num_str))
        counts.append(nums)

    mem = {}

    def calc(pat, curr_len, counts):
        counts_str = ""
        for c in counts:
            counts_str += str(c) + "#"
        counts_str += str(curr_len)
        if (pat + "_" + counts_str) in mem:
            return mem[pat + "_" + counts_str]
        if pat == "":
            if curr_len > 0:
                if len(counts) != 1:
                    return 0
                elif curr_len == counts[0]:
                    return 1
                else:
                    return 0
            else:
                if len(counts) == 0:
                    return 1
                else:
                    return 0
        if pat[0] == ".":
            if len(counts) > 0 and curr_len == counts[0]:
                counts = counts[1:]
            elif len(counts) > 0 and curr_len > 0 and curr_len != counts[0]:
                return 0
            elif len(counts) == 0 and curr_len > 0:
                return 0
            ret = calc(pat[1:], 0, counts)
            mem[pat + "_" + counts_str] = ret
            return ret
        elif pat[0] == "#":
            ret = calc(pat[1:], curr_len + 1, counts)
            mem[pat + "_" + counts_str] = ret
            return ret
        else:
            ret = calc("." + pat[1:], curr_len, counts) + calc(
                "#" + pat[1:], curr_len, counts
            )
            mem[pat + "_" + counts_str] = ret
            return ret

    ret = 0
    for i in range(len(patterns)):
        mem = {}
        c = calc(patterns[i] + ("?" + patterns[i]) * 4, 0, counts[i] * 5)
        ret += c
    print(ret)
