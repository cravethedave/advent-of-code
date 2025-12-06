import time

file_root = "25/day_5/star_2"

with open(f"{file_root}/input.txt") as f:
    data = [iter.rstrip() for iter in f.readlines()]

start = time.time()

valid_ranges = {}
for line in data:
    if len(line) == 0:
        break
    split_line = line.split('-')
    lower_bound = int(split_line[0])
    upper_bound = int(split_line[1])
    
    if lower_bound in valid_ranges.keys():
        valid_ranges[lower_bound] = max(valid_ranges[lower_bound],upper_bound)
        continue
    valid_ranges[lower_bound] = upper_bound

ordered_lower_bounds = sorted(valid_ranges.keys())

for i,lower_bound in enumerate(ordered_lower_bounds):
    # This lower bound was already absorbed into another range
    if lower_bound not in valid_ranges.keys():
        continue
    # Check the next lowest ranges to see if they can be merged
    for next_lower_bound in ordered_lower_bounds[i+1:]:
        # The next lowest unmerged bound is not mergeable
        if next_lower_bound > valid_ranges[lower_bound]:
            break
        valid_ranges[lower_bound] = max(valid_ranges[lower_bound],valid_ranges[next_lower_bound])
        valid_ranges.pop(next_lower_bound)

valid_id_count = 0
for lower_bound in valid_ranges.keys():
    valid_id_count += valid_ranges[lower_bound] - lower_bound + 1

duration = time.time() - start

print(valid_id_count, f"In {duration} seconds")
