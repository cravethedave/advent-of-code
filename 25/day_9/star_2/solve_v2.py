"""
We modify the previous solution by replacing the regex fill method with a BFS flood.
The idea was to avoid string conversion AND regex pattern search in a string which is heavy.
By finding any cell that we are sure is in the shape, we can use it as a starting point for
a BFS flood.
Once the flood is complete, we continue with no changes to the code.

I never fully ran this method as I found a better method before it finished running.
"""

import time
import queue
import numpy as np
from math import prod

file_root = "25/day_9/star_2"

with open(f"{file_root}/input.txt") as f:
    corners = [np.array([int(iter) for iter in line.rstrip().split(',')]) for line in f.readlines()]

start = time.time()

# Initialize the smallest matrix possible, adjust corners to be in new referential
lowest_x, lowest_y = np.min(corners, axis=0)
highest_x, highest_y = np.max(corners, axis=0) + 1
corners -= np.array([lowest_x,lowest_y])
matrix = np.zeros((highest_x-lowest_x, highest_y-lowest_y), dtype=np.int8)

# Initialize the edge of the matrix, mark corners as special
for i, current in enumerate(corners):
    x1,y1 = corners[i-1]
    x2,y2 = current
    
    if y1 == y2:
        for j in range(min(x1,x2), max(x1,x2) + 1):
            matrix[j,y1] = 1
    else:
        for j in range(min(y1,y2), max(y1,y2) + 1):
            matrix[x1,j] = 1
    
    matrix[x1,y1] = 2
    matrix[x2,y2] = 2
print(f"Initialized the sides of the matrix after {time.time() - start}s")

# Find any cell inside the shape
found = False
start_coords = (0,0)
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        # This has to be a top left corner
        if matrix[i,j] == 2:
            if matrix[i+1,j] == 1 and matrix[i,j+1] == 1:
                start_coords = (i+1,j+1)
                found = True
            # Skips the whole line if we crossed a single corner
            break
        # Any edge
        if matrix[i,j] == 1:
            if matrix[i+1,j] == 0:
                start_coords = (i+1,j)
                found = True
            break
    if found:
        break
print(f"Found the starting cell after {time.time() - start}s")

# BFS through the shape, turning 0 to 1
matrix[start_coords] = 1
neighbors = queue.Queue()
neighbors.put(start_coords)
while not neighbors.empty():
    x,y = neighbors.get()
    if x > 0 and matrix[x-1,y] == 0:
        matrix[x-1,y] = 1
        neighbors.put((x-1,y))
    if x+1 < len(matrix) and matrix[x+1,y] == 0:
        matrix[x+1,y] = 1
        neighbors.put((x+1,y))
    if y > 0 and matrix[x,y-1] == 0:
        matrix[x,y-1] = 1
        neighbors.put((x,y-1))
    if y+1 < len(matrix[0]) and matrix[x,y+1] == 0:
        matrix[x,y+1] = 1
        neighbors.put((x,y+1))
print(f"Filled the matrix after {time.time() - start}s")

# Change all corners back to ones for simple validation
for x,y in corners:
    matrix[x,y] = 1
print(f"Replaced corners in matrix after {time.time() - start}s")

# Iterate over corner pairs and use matrix to find the biggest valid rectangle
biggest_rectangle = 0
for i, v1 in enumerate(corners):
    for v2 in corners[i+1:]:
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
