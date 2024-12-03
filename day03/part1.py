import re

file = open("day03/input.in", "r").read().strip()

pattern = r"mul\((-?\d+),\s*(-?\d+)\)"

matches = re.findall(pattern, file)

final_product = 0
for factor1, factor2 in matches:
    final_product += int(factor1) * int(factor2)

print(final_product)
