import time
import numpy as np
from math import prod

file_root = "25/day_9/star_1"

with open(f"{file_root}/input.txt") as f:
    data = [np.array([int(iter) for iter in line.rstrip().split(',')]) for line in f.readlines()]

start = time.time()

biggest_rectangle = 0
for i, v1 in enumerate(data):
    for v2 in data[i+1:]:
        step1 = v2 - v1
        step2 = np.abs(step1) + np.array([1,1])
        current_area = prod(step2)
        biggest_rectangle = max(biggest_rectangle, current_area)

duration = time.time() - start

print(biggest_rectangle, f"In {duration} seconds")
