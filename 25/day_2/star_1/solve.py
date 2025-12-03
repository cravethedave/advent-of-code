import time
from math import log,ceil

file_root = "25/day_2/star_1"

with open(f"{file_root}/input.txt") as f:
    data = f.readline()

ids = [[int(iter) for iter in values.split('-')] for values in data.split(',')]

start = time.time()
total_of_ids = 0
for lower_val,upper_val in ids:
    # Adding 1 avoids 1000 having a length of 3, 999 still has a length of 3
    lower_len = ceil(log(lower_val+1,10))
    upper_len = ceil(log(upper_val+1,10))
    # If both bounds are of odd length, no invalid values
    if lower_len % 2 != 0 and upper_len % 2 != 0:
        continue
    # Lower bound is of odd length
    elif lower_len % 2 != 0:
        lower_prefix = int(10**(upper_len/2 - 1))
        upper_prefix = upper_val // int(10**(upper_len/2))
        prefix_length = upper_len // 2
    # Upper bound is of odd length
    elif upper_len % 2 != 0:
        lower_prefix = lower_val // int(10**(lower_len/2))
        upper_prefix = int(10**(lower_len/2)) - 1
        prefix_length = lower_len // 2
    # Both bounds are of even length, easy case
    else:
        lower_prefix = lower_val // int(10**(lower_len/2))
        upper_prefix = upper_val // int(10**(upper_len/2))
        prefix_length = lower_len // 2
    
    # Create possible invalid vals and check if they are in range
    for prefix in range(lower_prefix,upper_prefix+1):
        value = prefix*10**prefix_length + prefix
        if lower_val <= value <= upper_val:
            total_of_ids += value
duration = time.time() - start

print(total_of_ids, f"In {duration} seconds")
