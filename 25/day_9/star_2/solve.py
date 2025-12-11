"""
Solves the problem but is ridiculously slow, 20h of runtime on my pc
Converts each line in the matrix into a string.
We can then use regex on the string to find which positions are in the shape.
Once the shape is full, we iterate over corner pairs and compare the theoretical area
with the sum in the matrix over that area. The sum will be equivalent to the theoretical
area if and only if every tile in the rectangle is in the shape.
"""

import re
import time
import numpy as np
from math import prod

file_root = "25/day_9/star_2"

with open(f"{file_root}/input.txt") as f:
    data = [np.array([int(iter) for iter in line.rstrip().split(',')]) for line in f.readlines()]

start = time.time()

highest_x = max(x for x,y in data) + 1
highest_y = max(y for x,y in data) + 1

# Initialize the edge of the matrix
matrix = np.zeros((highest_x, highest_y), dtype=np.int8)
for i, current in enumerate(data):
    x1,y1 = data[i-1]
    x2,y2 = current
    
    if y1 == y2:
        for j in range(min(x1,x2), max(x1,x2) + 1):
            matrix[j,y1] = 1
    else:
        for j in range(min(y1,y2), max(y1,y2) + 1):
            matrix[x1,j] = 1
print(f"Initialized the sides of the matrix after {time.time() - start}s")

# Fill the shape in the matrix
matrix_str = [''.join(str(iter) for iter in line) for line in matrix]
print("Converted matrix to string")
for i, line in enumerate(matrix_str):
    in_shape = True
    for m in re.finditer(r'10+1', line):
        if not in_shape:
            in_shape = True
            continue
        in_shape = False
        # Replace the values in the matrix directly
        for j in range(m.start(), m.end()):
            matrix[i,j] = 1
print(f"Filled in the matrix after {time.time() - start}s")

# Iterate over corner pairs and use matrix to find the biggest valid rectangle
biggest_rectangle = 0
for i, v1 in enumerate(data):
    for v2 in data[i+1:]:
        step1 = v2 - v1
        step2 = np.abs(step1) + np.array([1,1])
        theoretical_area = prod(step2)
        real_area = np.sum(matrix[min(v1[0],v2[0]):max(v1[0],v2[0])+1, min(v1[1],v2[1]):max(v1[1],v2[1])+1])
        # The rectangle is disqualified if the matrix is not full of ones (area and sum are not equal)
        if theoretical_area != real_area:
            continue
        biggest_rectangle = max(biggest_rectangle, theoretical_area)

duration = time.time() - start

print(biggest_rectangle, f"In {duration} seconds")
