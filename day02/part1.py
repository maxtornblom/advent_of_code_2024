file = open("day02/input.in", "r").read().strip().split("\n")

valid_numbers = []
number_valid = 0
for line in file:
    numbers = list(map(int, line.split()))
    is_increasing = all(i < j for i, j in zip(numbers, numbers[1:]))
    is_decreasing = all(i > j for i, j in zip(numbers, numbers[1:]))
    if is_increasing or is_decreasing:
        valid_numbers.append(numbers)

for numbers in valid_numbers:
    report = [abs(numbers[i] - numbers[i + 1]) for i in range(len(numbers) - 1)]
    if all(diff <= 3 for diff in report):
        number_valid += 1
print(number_valid)
