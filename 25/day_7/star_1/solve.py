import time

file_root = "25/day_7/star_1"

with open(f"{file_root}/input.txt") as f:
    data = [iter.rstrip() for iter in f.readlines()]
current = set(i for i,iter in enumerate(data[0]) if iter == 'S')
data = [set(j for j,c in enumerate(data[i]) if c == '^') for i in range(1, len(data)) if i % 2 == 0]

start = time.time()

total_splits = 0
for splitters in data:
    # Get the rays that split and the ones that pass
    hits = current.intersection(splitters)
    leftovers = current.difference(splitters)
    total_splits += len(hits)
    # Reset the current rays to the leftovers and add the splits
    current = leftovers
    for v in list(hits):
        current.add(v - 1)
        current.add(v + 1)

duration = time.time() - start

print(total_splits, f"In {duration} seconds")
