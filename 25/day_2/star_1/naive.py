import time
from math import log,ceil

file_root = "25/day_2/star_1"

with open(f"{file_root}/input.txt") as f:
    data = f.readline()

ids = [[int(iter) for iter in values.split('-')] for values in data.split(',')]

start = time.time()
total_of_ids = 0
# Using math
for lower_val,upper_val in ids:
    for value in range(lower_val,upper_val+1):
        # Adding 1 avoids 1000 having a length of 3, 999 still has a length of 3
        value_len = ceil(log(value+1,10))
        if value_len % 2 != 0:
            continue
        half_base = int(10**(value_len/2))
        if value // half_base == value % half_base:
            total_of_ids += value

# Using strings
# for lower_val,upper_val in ids:
#     for value in range(lower_val,upper_val+1):
#         value_str = str(value)
#         if len(value_str) % 2 != 0:
#             continue
#         half_len = len(value_str)//2
#         if value_str[:half_len] == value_str[half_len:]:
#             total_of_ids += value

duration = time.time() - start

print(total_of_ids, f"In {duration} seconds")
