import operator

ops = {">": operator.gt, "<": operator.lt}
map = {}
var_trans = {"x": 0, "m": 1, "a": 2, "s": 3}
ret = 0

with open("input.txt", "r") as file:
    for line in file:
        line = line.strip()
        if line == "":
            continue
        if line[0] != "{":
            key, value = line.split("{")
            value = value[:-1]
            stmts = value.split(",")
            conds = []
            base = stmts[-1]
            for i, stmt in enumerate(stmts):
                if i < len(stmts) - 1:
                    if ">" in stmt:
                        halves = stmt.split(">")
                        op = ">"
                    elif "<" in stmt:
                        halves = stmt.split("<")
                        op = "<"
                    else:
                        print("ERROR - OP Not Supported")
                    var = var_trans[halves[0]]
                    const, dest = halves[1].split(":")
                    conds.append([var, op, int(const), dest])
            map[key] = [conds, base]

    def calc_ranges(ranges, loc):
        if loc == "A":
            ret = 1
            for l, r in ranges:
                ret *= r - l + 1
            return ret
        elif loc == "R":
            return 0

        total = 0
        for var, op, const, dest in map[loc][0]:
            if op == ">":
                if ranges[var][1] > const:
                    ranges_copy = ranges.copy()
                    ranges_copy[var] = [const + 1, ranges[var][1]]
                    ranges[var] = [ranges[var][0], const]
                    total += calc_ranges(ranges_copy, dest)
            elif op == "<":
                if ranges[var][0] < const:
                    ranges_copy = ranges.copy()
                    ranges_copy[var] = [ranges[var][0], const - 1]
                    ranges[var] = [const, ranges[var][1]]
                    total += calc_ranges(ranges_copy, dest)

        return total + calc_ranges(ranges, map[loc][1])

    possible_ranges = calc_ranges([[1, 4000] for _ in range(4)], "in")
    print(possible_ranges)
