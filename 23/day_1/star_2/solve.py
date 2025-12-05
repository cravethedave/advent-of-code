import time
import re

file_root = "23/day_1/star_2"
with open(f"{file_root}/input.txt", 'r') as f:
    lines = f.readlines()
lines = [iter.rstrip() for iter in lines]

alpha_to_num = {
    'one':      1,
    'two':      2,
    'three':    3,
    'four':     4,
    'five':     5,
    'six':      6,
    'seven':    7,
    'eight':    8,
    'nine':     9,
}

start = time.time()

total_calibration = 0
for line in lines:
    matches = []
    # Finds all substrings that are numbers OR numbers spelled out
    for m in re.finditer(r"(?=(" + r'|'.join(alpha_to_num.keys()) + r"|\d))", line):
        # Convert the string to a number and keep it in memory
        found_str = str(m.group(1))
        if not found_str.isdigit():
            value = alpha_to_num[found_str]
        else:
            value = int(found_str)
        matches.append(value)
    # Sum the first and last, add to total, next line
    value = matches[0] * 10 + matches[-1]
    total_calibration += value

duration = time.time() - start

print(total_calibration, f"In {duration} seconds")
