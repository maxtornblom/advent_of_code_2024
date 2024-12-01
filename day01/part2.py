file = (open("day01/input.in", "r")).read().split("\n")


def main():
    left_list = []
    right_list = []
    similarities = 0
    similarity_score = 0

    for line in file:
        parts = line.split()
        left_list.append(int(parts[0]))
        right_list.append(int(parts[1]))

    for number in left_list:
        similarities = right_list.count(number)
        similarity_score += number * similarities

    print(similarity_score)


if __name__ == "__main__":
    main()
