import time

file_root = "25/day_5/star_1"

with open(f"{file_root}/input.txt") as f:
    data = [iter.rstrip() for iter in f.readlines()]

start = time.time()

valid_ranges = {}
empty_line_id = 0
for i, line in enumerate(data):
    if len(line) == 0:
        empty_line_id = i
        break
    split_line = line.split('-')
    lower_bound = int(split_line[0])
    upper_bound = int(split_line[1])
    
    if lower_bound in valid_ranges.keys():
        valid_ranges[lower_bound] = max(valid_ranges[lower_bound],upper_bound)
        continue
    valid_ranges[lower_bound] = upper_bound

ordered_lower_bounds = sorted(valid_ranges.keys())

valid_ingredient_count = 0
for line in data[empty_line_id + 1:]:
    value = int(line)
    for lower_bound in ordered_lower_bounds:
        if value < lower_bound or value > valid_ranges[lower_bound]:
            continue
        valid_ingredient_count += 1
        break

duration = time.time() - start

print(valid_ingredient_count, f"In {duration} seconds")
