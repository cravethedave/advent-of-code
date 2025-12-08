import time
import numpy as np
from scipy import signal

file_root = "25/day_7/star_2"

with open(f"{file_root}/input.txt") as f:
    data = [iter.rstrip() for iter in f.readlines()]
current_paths = np.array([1 if iter == 'S' else 0 for iter in data[0]])
data = np.array([[1 if c == '^' else 0 for c in data[i]] for i in range(1, len(data)) if i % 2 == 0])

start = time.time()

kernel = np.array([
    [1,0,1]
])

for splitters in data:
    # Hits is the paths that hit a splitter
    hits = current_paths * splitters
    # Inverse hits is all paths that pass without hitting a splitter
    inverse_hits = current_paths * (np.ones(current_paths.shape, dtype=np.int64) - splitters)
    
    # Add the split hits to the pass through (inverse_hits)
    current_paths = signal.convolve2d(np.array([hits]), kernel, mode='same', boundary='wrap')[0]
    current_paths += inverse_hits

total_paths = sum(current_paths)

duration = time.time() - start

print(total_paths, f"In {duration} seconds")
