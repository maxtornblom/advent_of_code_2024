import re

file = open("day03/input.in", "r").read().strip()

pattern = r"(don't\(\))|(do\(\))|mul\((-?\d+),\s*(-?\d+)\)"
matches = re.findall(pattern, file)

cleaned_matches = [
    (m[0],) if m[0] else (m[1],) if m[1] else (m[2], m[3]) for m in matches
]


multiply = []
mul_enabled = True

for i in range(len(cleaned_matches)):
    if cleaned_matches[i][0] == "do()":
        mul_enabled = True
    elif cleaned_matches[i][0] == "don't()":
        mul_enabled = False
    else:
        if mul_enabled:
            multiply.append(cleaned_matches[i])

final_product = 0
for factor1, factor2 in multiply:
    final_product += int(factor1) * int(factor2)

print(final_product)
