file = (open("day01/input.in", "r")).read().split("\n")


def main():
    left_list = []
    right_list = []
    distance = 0
    distance_sum = 0
    n = 0

    for line in file:
        parts = line.split()
        left_list.append(int(parts[0]))
        right_list.append(int(parts[1]))

    left_list = sorted(list(left_list))
    right_list = sorted(list(right_list))

    for number in left_list:
        distance = abs(number - right_list[0 + n])
        distance_sum += distance
        n += 1

    print(distance_sum)


if __name__ == "__main__":
    main()
