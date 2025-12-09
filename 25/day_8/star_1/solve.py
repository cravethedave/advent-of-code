import time
import numpy as np
from math import prod

file_root = "25/day_8/star_1"

with open(f"{file_root}/input.txt") as f:
    data = [[int(iter) for iter in line.rstrip().split(',')] for line in f.readlines()]
data = [(line[0],line[1],line[2]) for line in data]

start = time.time()

distances = {}
for i, v1 in enumerate(data):
    for v2 in data[i+1:]:
        distances[(v1,v2)] = sum(np.square(np.array(v1) - np.array(v2)))

keys_sorted = sorted(distances.keys(), key=lambda x: distances[x])[:1000]

current_circuits: list[set[list[int]]] = []
for v1, v2 in keys_sorted:
    index1 = index2 = -1
    for i, circuit in enumerate(current_circuits):
        if v1 in circuit:
            index1 = i
        if v2 in circuit:
            index2 = i

    # The two boxes are already connected and the process should be skipped
    if index1 == index2 and index1 != -1:
        continue

    # Both boxes were not in any existing circuit, create a new circuit
    if index1 == index2 == -1:
        current_circuits.append(set([v1,v2]))
        continue

    # Both boxes are in an existing circuit, combine circuits
    if index1 != -1 and index2 != -1:
        current_circuits[index1] = current_circuits[index1].union(current_circuits[index2])
        # Switch the circuit to remove with the last to avoid long operations
        temp = current_circuits[-1]
        current_circuits[-1] = current_circuits[index2]
        current_circuits[index2] = temp
        current_circuits.pop()
        continue
    
    # One of the boxes is connected and the other isn't, add the orphaned box
    if index1 == -1:
        current_circuits[index2].add(v1)
    else:
        current_circuits[index1].add(v2)

three_largest_circuits = sorted([len(iter) for iter in current_circuits], reverse=True)[:3]
product_of_circuits = prod(three_largest_circuits)

duration = time.time() - start

print(product_of_circuits, f"In {duration} seconds")
