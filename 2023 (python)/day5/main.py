with open("input.txt", "r") as file:
    ret = 0
    line = file.readline().strip()
    seed_line = line.split(":")[1].strip()
    seeds = []
    split_line = seed_line.split(" ")
    for i in range(0, len(split_line), 2):
        start, steps = split_line[i], split_line[i + 1]
        seeds.append([int(start), int(steps)])
    line = file.readline().strip()

    map = []

    def translate_seeds():
        global seeds
        seeds.sort(key=lambda x: x[0])
        map.sort(key=lambda x: x[0])
        new_seeds = []
        for seed_range in seeds:
            start, step = seed_range[0], seed_range[1]
            curr = start
            for interval in map:
                src, count, dest = interval[0], interval[1], interval[2]
                if curr < (start + step - 1) and curr < src:
                    new_seeds.append([curr, min(src - curr, step - (curr - start))])
                    curr = min(src, curr + (step - (curr - start)))

                if curr < (start + step - 1) and curr >= src and curr < src + count:
                    diff = dest - src
                    new_seeds.append(
                        [curr + diff, min((src + count) - curr, step - (curr - start))]
                    )
                    curr = src + count

            if curr < (start + step - 1):
                new_seeds.append([curr, step - (curr - start)])

        seeds = new_seeds

    new_map = False
    for line in file:
        line = line.strip()
        if ":" in line:
            print(line)
            new_map = True
        elif line == "":
            new_map = False
        elif new_map:
            nums = line.split(" ")
            dest, src, count = (
                int(nums[0].strip()),
                int(nums[1].strip()),
                int(nums[2].strip()),
            )
            map.append([src, count, dest])

        if not new_map:
            translate_seeds()
            map = []
    translate_seeds()
    seeds.sort(key=lambda x: x[0])
    print(seeds[0])
