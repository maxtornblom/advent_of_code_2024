file = open("day02/input.in", "r").read().strip().split("\n")

safe = 0
for line in file:
    numbers = list(map(int, line.split()))

    is_increasing = all(i < j for i, j in zip(numbers, numbers[1:]))
    is_decreasing = all(i > j for i, j in zip(numbers, numbers[1:]))

    if is_increasing or is_decreasing:
        report = [abs(numbers[i] - numbers[i + 1]) for i in range(len(numbers) - 1)]
        if all(diff <= 3 for diff in report):
            safe += 1
            continue

    for i in range(len(numbers)):
        modified_numbers = numbers[:i] + numbers[i + 1 :]
        report = [abs(modified_numbers[j] - modified_numbers[j + 1]) for j in range(len(modified_numbers) - 1)]
        
        if all(diff <= 3 for diff in report):
            safe += 1
            break

print(safe)
