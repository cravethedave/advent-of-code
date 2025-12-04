import time
import numpy as np
from scipy import signal

file_root = "25/day_4/star_1"

with open(f"{file_root}/input.txt") as f:
    shelves = f.readlines()

# Transforms problem into a matrix where 1 is a roll and 0 is no roll
shelves = np.array([[1 if roll == '@' else 0 for roll in iter.rstrip()] for iter in shelves])

start = time.time()

kernel = np.array([
    [1,1,1],
    [1,0,1],
    [1,1,1]
])
# Creates a matrix where each element is the number of neighboring rolls
neighbors = signal.convolve2d(shelves, kernel, boundary='fill', mode='same')
# Applies a mask to only consider positions with a roll in them
masked_neighbors = np.multiply(neighbors,shelves)
# Counts the number of positions with less than 4
result = np.sum(shelves[masked_neighbors < 4])

duration = time.time() - start

print(result, f"In {duration} seconds")
