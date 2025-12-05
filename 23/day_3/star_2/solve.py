import time
import re

file_root = "23/day_3/star_2"
with open(f"{file_root}/input.txt", 'r') as f:
    data = f.readlines()
data = [line.rstrip() for line in data]

start = time.time()

# Find all gears and their place on the line
gears: list[dict[int,list[int]]] = []
for line in data:
    line_gears: dict[int,list[int]] = {}
    for m in re.finditer(r"\*", line):
        line_gears[m.start()] = []
    gears.append(line_gears)

# Associates numbers to their respective gears
for i, line in enumerate(data):
    for m in re.finditer(r"\d+", line):
        left_bound = m.start() - 1
        right_bound = m.end()
        value = m.group()
        for j in range(max(0,i-1), min(i+2,len(data))):
            for key in gears[j].keys():
                if left_bound <= key <= right_bound:
                    gears[j][key].append(int(value))

gear_ratio_sum = 0
for line in gears:
    for associated_ratios in line.values():
        if len(associated_ratios) != 2:
            continue
        gear_ratio_sum += associated_ratios[0] * associated_ratios[1]

duration = time.time() - start

print(gear_ratio_sum, f"In {duration} seconds")