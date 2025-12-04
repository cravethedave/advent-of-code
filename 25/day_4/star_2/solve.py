import time
import numpy as np
from scipy import signal

file_root = "25/day_4/star_2"

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
total_rolls = 0

# Necessary evil to enter the while loop
result = 1
while result > 0:
    # Creates a matrix where each element is the number of neighboring rolls
    neighbors = signal.convolve2d(shelves, kernel, boundary='fill', mode='same')
    
    # Applies a mask to only consider positions with a roll in them
    masked_neighbors = np.multiply(neighbors,shelves)
    
    # Creates a matrix where 1 indicates that we can reach this roll
    reachable_rolls = np.multiply(shelves,masked_neighbors < 4)
    
    # Counts the number of rolls removed this iteration
    result = np.sum(reachable_rolls)
    
    # Updates the shelves, removing rolls
    shelves -= reachable_rolls
    total_rolls += result

duration = time.time() - start

print(total_rolls, f"In {duration} seconds")
