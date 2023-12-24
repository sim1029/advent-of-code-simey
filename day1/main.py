with open("input.txt", "r") as file:
    ret = 0
    words = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    nums = {"1", "2", "3", "4", "5", "6", "7", "8", "9"}
    for line in file:
        line = line.strip()
        curr = ""
        first_val, last_val = None, None
        for char in line:
            curr += char
            if char in nums:
                first_val = char
                break
            else:
                found = False
                for word in words.keys():
                    if curr.find(word) != -1:
                        first_val = words[word]
                        found = True
                        break
                if found:
                    break

        curr = ""
        for i in range(len(line) - 1, -1, -1):
            curr = line[i] + curr
            if line[i] in nums:
                last_val = line[i]
                break
            else:
                found = False
                for word in words.keys():
                    if curr.find(word) != -1:
                        last_val = words[word]
                        found = True
                        break
                if found:
                    break
        ret += int(first_val + last_val)
    print(ret)
