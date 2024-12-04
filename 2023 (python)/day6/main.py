with open("input.txt", "r") as file:
    time_line = file.readline().strip()
    distance_line = file.readline().strip()

    time_vals = time_line.split(":")[1].strip()
    distance_vals = distance_line.split(":")[1].strip()

    time_arr_split = time_vals.split(" ")
    dist_arr_split = distance_vals.split(" ")

    time_str, dist_str = "", ""

    for time in time_arr_split:
        if time != "":
            time_str += time

    for dist in dist_arr_split:
        if dist != "":
            dist_str += dist

    ret = 0

    length, goal = int(time_str), int(dist_str)

    def calc_speed(hold):
        time = length - hold
        dist = hold * time
        return dist > goal

    def lower_bound(point):
        return not calc_speed(point) and calc_speed(point + 1)

    def upper_bound(point):
        return not calc_speed(point) and calc_speed(point - 1)

    left, right = 0, length
    mid = (right + left) // 2
    while not lower_bound(mid):
        if calc_speed(mid):
            right = mid - 1
        else:
            left = mid + 1
        mid = (right + left) // 2
    lower = mid + 1
    upper = length - lower
    print(upper - lower + 1)
